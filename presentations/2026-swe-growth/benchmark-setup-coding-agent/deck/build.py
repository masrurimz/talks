"""Build the talk deck from content.py, lint it, and optionally render contact sheets.

    uv run python3 presentations/2026-swe-growth/benchmark-setup-coding-agent/deck/build.py [--render]
"""

from __future__ import annotations

import dataclasses
import io
import math
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Callable

from PIL import Image as PILImage
from PIL import ImageDraw, ImageFilter, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

sys.path.insert(0, str(Path(__file__).parent))
import content as C  # noqa: E402

TALK = Path(__file__).resolve().parent.parent
OUTPUT = TALK / "output" / "benchmark-setup-coding-agent.pptx"
OUTLINE_PATH = TALK / "sources" / "outlines" / "presenter.md"
RENDER_DIR = Path("/tmp/deck-render")

# ---------------------------------------------------------------- theme tokens

BG, INK, MUTED, RULE = "F4F6FA", "121A2B", "4E586B", "C9D0DC"
ACC, TBL_HEAD, WHITE = "1F4FE0", "E6EAF2", "FFFFFF"
PANEL, PANEL_TXT = "121A2B", "E8ECF4"
ACC_TINT = "A9BCF7"
BAR = "7D879B"
PALETTE = frozenset({BG, INK, MUTED, RULE, ACC, TBL_HEAD, WHITE, PANEL, PANEL_TXT, ACC_TINT, BAR})
SANS, MONO = "Source Sans 3", "Source Code Pro"

SLIDE_W, SLIDE_H = 13.333, 7.5
X0 = 0.8
CW = SLIDE_W - 2 * X0
TOP = 2.0
BOTTOM = 6.8

SIZE_HEADLINE, SIZE_PROSE, SIZE_EVIDENCE, SIZE_MIN = 36, 28, 20, 14
SIZE_DIVIDER = 48
MAX_HEADLINE_WORDS = 12
MAX_FACE_WORDS = 30
FACE_LIMITS: dict[type, int] = {C.Map: 70, C.Timeline: 36}
CHART_FACE_WORDS = 45
MAX_LABEL_WORDS = 8
MIN_GRAPHIC_CONTRAST = 3.0
TALK_MINUTES = 86.0
FALLBACK_SENTENCE = "The live run is slow today, so here is the recording from this morning."
DEMO_TIME_BOX = "90 s"

FONT_DIR = Path("/usr/share/fonts/truetype")
FONT_FILES = {
    ("sans", False): "SourceSans3-Regular.otf",
    ("sans", True): "SourceSans3-Bold.otf",
    ("mono", False): "SourceCodePro-Regular.otf",
    ("mono", True): "SourceCodePro-Bold.otf",
}


# ---------------------------------------------------------------- measuring

@lru_cache(maxsize=None)
def _font(mono: bool, bold: bool) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / FONT_FILES[("mono" if mono else "sans", bold)]), 1000)


def text_width_pt(s: str, size: float, mono: bool = False, bold: bool = False) -> float:
    return _font(mono, bold).getlength(s) * size / 1000


def line_height_pt(size: float, mono: bool = False, bold: bool = False) -> float:
    ascent, descent = _font(mono, bold).getmetrics()
    return (ascent + descent) * size / 1000


def wrap(s: str, size: float, width_in: float, mono: bool = False, bold: bool = False) -> list[str]:
    limit = width_in * 72
    lines: list[str] = []
    for hard in s.split("\n"):
        cur = ""
        for word in hard.split(" "):
            trial = word if not cur else cur + " " + word
            if cur and text_width_pt(trial, size, mono, bold) > limit:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
    return lines


def block_height_in(paras: list[tuple[str, bool]], size: float, width_in: float, mono: bool = False) -> float:
    total = 0.0
    for text, bold in paras:
        total += len(wrap(text, size, width_in, mono, bold)) * line_height_pt(size, mono, bold)
    return total / 72


# ---------------------------------------------------------------- contrast

def _lin(c: int) -> float:
    v = c / 255
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def luminance(hexcol: str) -> float:
    r, g, b = (int(hexcol[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg: str, bg: str) -> float:
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


# ---------------------------------------------------------------- canvas

@dataclass
class TextRecord:
    slide: int
    kind: str
    size: float
    fg: str
    bg: str
    words: int
    snippet: str
    text: str
    need_h: float
    box_h: float
    widest_word_pt: float
    box_w_pt: float


@dataclass
class GraphicRecord:
    slide: int
    fill: str
    bg: str
    what: str


@dataclass
class Lint:
    violations: list[str] = field(default_factory=list)

    def fail(self, slide: int, msg: str) -> None:
        self.violations.append(f"slide {slide}: {msg}")


def emu(x: float) -> Emu:
    return Emu(int(round(x * 914400)))


def rgb(h: str) -> RGBColor:
    return RGBColor.from_string(h)


class Canvas:
    def __init__(self, slide, index: int, bg: str, lint: Lint, records: list[TextRecord], graphics: list[GraphicRecord]):
        self.slide, self.index, self.bg, self.lint, self.records, self.graphics = slide, index, bg, lint, records, graphics
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = rgb(bg)

    def _strip_style(self, shape) -> None:
        style = shape._element.find(qn("p:style"))
        if style is not None:
            shape._element.remove(style)

    def rect(self, x, y, w, h, fill: str | None, line: str | None = None, line_w: float = 1.0, shape=MSO_SHAPE.RECTANGLE):
        for col in (fill, line):
            if col is not None and col not in PALETTE:
                raise ValueError(f"color {col} is outside the palette")
        r = self.slide.shapes.add_shape(shape, emu(x), emu(y), emu(w), emu(h))
        self._strip_style(r)
        if fill is None:
            r.fill.background()
        else:
            r.fill.solid()
            r.fill.fore_color.rgb = rgb(fill)
        if line is None:
            r.line.fill.background()
        else:
            r.line.color.rgb = rgb(line)
            r.line.width = Pt(line_w)
        return r

    def gfx(self, x, y, w, h, fill: str, what: str = "chart mark") -> None:
        """A filled mark that carries data. Linted for 3:1 non-text contrast (WCAG 1.4.11)."""
        self.graphics.append(GraphicRecord(self.index, fill, self.bg, what))
        self.rect(x, y, w, h, fill)

    def line(self, x1, y1, x2, y2, color: str = MUTED, width: float = 2.0, dashed: bool = False) -> None:
        cn = self.slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, emu(x1), emu(y1), emu(x2), emu(y2))
        self._strip_style(cn)
        cn.line.color.rgb = rgb(color)
        cn.line.width = Pt(width)
        if dashed:
            cn.line.dash_style = MSO_LINE.DASH

    def text(
        self,
        x,
        y,
        w,
        h,
        paras,
        size: float,
        color: str,
        bg: str | None = None,
        kind: str = "evidence",
        bold: bool = False,
        mono: bool = False,
        align=PP_ALIGN.LEFT,
        anchor=MSO_ANCHOR.TOP,
    ) -> float:
        """Draw text, record it for lint, return the needed height in inches."""
        if color not in PALETTE:
            raise ValueError(f"color {color} is outside the palette")
        bg = bg or self.bg
        items = [(p, bold) if isinstance(p, str) else p for p in (paras if isinstance(paras, list) else [paras])]
        tb = self.slide.shapes.add_textbox(emu(x), emu(y), emu(w), emu(h))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.auto_size = MSO_AUTO_SIZE.NONE
        tf.vertical_anchor = anchor
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        for i, (t, b) in enumerate(items):
            para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            para.alignment = align
            para.font.size = Pt(size)
            run = para.add_run()
            run.text = t
            run.font.size = Pt(size)
            run.font.bold = b
            run.font.name = MONO if mono else SANS
            run.font.color.rgb = rgb(color)
        need = block_height_in(items, size, w, mono)
        widest = max(
            (text_width_pt(word, size, mono, b) for t, b in items for word in t.split(" ")),
            default=0,
        )
        self.records.append(
            TextRecord(
                slide=self.index,
                kind=kind,
                size=size,
                fg=color,
                bg=bg,
                words=sum(len(t.split()) for t, _ in items),
                snippet=items[0][0][:40],
                text=" ".join(t for t, _ in items),
                need_h=need,
                box_h=h,
                widest_word_pt=widest,
                box_w_pt=w * 72,
            )
        )
        return need

    def headline(self, title: str, width: float = CW, h: float = 1.4, color: str = INK, bg: str | None = None) -> None:
        self.text(X0, 0.45, width, h, title, SIZE_HEADLINE, color, bg, kind="headline", bold=True)

    def prose(self, x, y, w, s: str, color: str = INK, bg: str | None = None, max_bottom: float = BOTTOM) -> float:
        need = self.text(x, y, w, block_height_in([(s, False)], SIZE_PROSE, w), s, SIZE_PROSE, color, bg, kind="prose")
        if y + need > max_bottom + 0.01:
            self.lint.fail(self.index, f"prose runs below {max_bottom}in: {s[:40]!r}")
        return need

    def check_bottom(self, y: float, what: str, limit: float = BOTTOM) -> None:
        if y > limit + 0.01:
            self.lint.fail(self.index, f"{what} ends at {y:.2f}in, below {limit}in")


def fit_mono(lines, width_in: float, max_h_in: float, sizes=(28, 26, 24, 22, 20)) -> float | None:
    for size in sizes:
        if all(text_width_pt(l, size, mono=True) <= width_in * 72 for l in lines):
            h = len(lines) * line_height_pt(size, mono=True) / 72
            if h <= max_h_in:
                return size
    return None


def code_panel(c: Canvas, x, y, w, lines, max_h: float = 3.6, sizes=(28, 26, 24, 22, 20), pad: float = 0.35) -> float:
    size = fit_mono(lines, w - 2 * pad, max_h - 2 * pad, sizes)
    if size is None:
        c.lint.fail(c.index, f"code panel does not fit at 20pt: {lines[0][:30]!r}")
        size = 20
    text_h = len(lines) * line_height_pt(size, mono=True) / 72
    h = text_h + 2 * pad
    c.rect(x, y, w, h, PANEL)
    c.text(x + pad, y + pad, w - 2 * pad, text_h, [(l if l else " ", False) for l in lines], size, PANEL_TXT, PANEL, mono=True)
    return h


# ---------------------------------------------------------------- renderers

def render_title(c: Canvas, s: C.Title) -> None:
    c.rect(X0, 1.6, 0.12, 3.8, ACC)
    c.text(X0 + 0.5, 1.6, 10.9, 3.1, s.title, 54, WHITE, kind="title", bold=True)
    c.text(X0 + 0.5, 4.9, 10.5, 0.5, s.subtitle, 28, PANEL_TXT, kind="display")


PART_COUNT = 5
STRIP_SEG_GAP = 0.15


def render_divider(c: Canvas, s: C.Divider) -> None:
    kicker = f"Part {s.segment}" if 1 <= s.segment <= PART_COUNT else C.MAP[s.segment].covers
    c.text(X0, 0.8, 6, 0.5, kicker, 28, WHITE, kind="display", bold=True)
    c.text(X0, 1.6, CW, 2.8, s.title, SIZE_DIVIDER, WHITE, kind="divider-headline", bold=True)
    c.rect(X0, 4.75, CW, 0.03, WHITE)
    c.text(X0, 5.0, CW, 1.1, s.question, 28, WHITE, kind="display")
    n = len(C.MAP)
    seg_w = (CW - (n - 1) * STRIP_SEG_GAP) / n
    for i in range(n):
        x = X0 + i * (seg_w + STRIP_SEG_GAP)
        here = i == s.segment
        c.gfx(x, 6.2 if here else 6.26, seg_w, 0.2 if here else 0.08, WHITE if here else ACC_TINT, "map strip")
        if here:
            right = i == n - 1
            c.text(x - (1.5 - seg_w if right else 0), 6.5, max(seg_w, 1.5), 0.35, "You are here", 18, WHITE, kind="display", bold=True, align=PP_ALIGN.RIGHT if right else PP_ALIGN.LEFT)


MAP_ROW_GAP = 0.07
MAP_NUM_W, MAP_NAME_W = 0.65, 5.6


def render_map(c: Canvas, s: C.Map) -> None:
    c.headline(s.title)
    n = len(C.MAP)
    rh = (BOTTOM - TOP - MAP_ROW_GAP * (n - 1)) / n
    for i, row in enumerate(C.MAP):
        y = TOP + i * (rh + MAP_ROW_GAP)
        c.rect(X0, y, CW, rh, WHITE, RULE)
        if 1 <= i <= PART_COUNT:
            c.text(X0 + 0.2, y, 0.4, rh, str(i), 22, ACC, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        c.text(X0 + MAP_NUM_W, y, MAP_NAME_W, rh, row.name, 22, INK, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        cx = X0 + MAP_NUM_W + MAP_NAME_W + 0.2
        c.text(cx, y, X0 + CW - 0.2 - cx, rh, row.covers, 22, MUTED, anchor=MSO_ANCHOR.MIDDLE)


def render_principle(c: Canvas, s: C.Principle) -> None:
    w = CW - 0.5
    h = block_height_in([(s.title, True)], 60, w)
    c.text(X0, 0.9, 6, 0.5, f"Principle {s.number}", 28, ACC_TINT, kind="display", bold=True)
    c.rect(X0, 1.7, 0.12, h, ACC)
    c.text(X0 + 0.5, 1.7, w, h + 0.02, s.title, 60, WHITE, kind="title", bold=True)
    if s.line:
        c.text(X0 + 0.5, 1.7 + h + 0.5, w, block_height_in([(s.line, False)], 32, w) + 0.02, s.line, 32, PANEL_TXT, kind="display")


def render_trythis(c: Canvas, s: C.TryThis) -> None:
    w = CW - 0.5
    h = block_height_in([(s.title, True)], 44, w)
    c.text(X0, 0.9, 6, 0.5, "Try this week", 28, ACC, kind="display", bold=True)
    c.rect(X0, 1.9, 0.12, h, ACC)
    c.text(X0 + 0.5, 1.9, w, h + 0.02, s.title, 44, INK, kind="title", bold=True)


def render_statement(c: Canvas, s: C.Statement) -> None:
    c.headline(s.title)
    c.text(X0, 3.0, CW, 1.2, s.support, 54, ACC, kind="display", bold=True)
    if s.extra:
        c.prose(X0, 4.4, CW, s.extra)


VBAR_FRACTION = 0.55


def vbar_left(bars: C.Bars) -> float:
    col_w = CW / len(bars.rows)
    return X0 + col_w * (1 - VBAR_FRACTION) / 2


def draw_bars(c: Canvas, bars: C.Bars, y0: float, y1: float) -> float:
    rows = bars.rows
    paired = len(rows[0].values) == 2
    vmax = max(v for r in rows for v in r.values)
    if bars.vertical:
        col_w = CW / len(rows)
        val_h, lab_h = 0.4, 0.45
        plot_h = y1 - y0 - val_h - lab_h - 0.1
        for i, r in enumerate(rows):
            bw = col_w * VBAR_FRACTION
            bx = X0 + i * col_w + (col_w - bw) / 2
            bh = max(0.04, r.values[0] / vmax * plot_h)
            base = y1 - lab_h
            c.gfx(bx, base - bh, bw, bh, ACC if i == bars.highlight else BAR, "bar")
            c.text(X0 + i * col_w, base - bh - val_h - 0.03, col_w, val_h, r.texts[0], SIZE_EVIDENCE, INK, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM)
            c.text(X0 + i * col_w, base + 0.05, col_w, lab_h - 0.05, r.label, SIZE_EVIDENCE, MUTED, align=PP_ALIGN.CENTER)
        return y1
    label_w, bar_x, max_w = 3.4, X0 + 3.6, 5.2
    row_h = min(1.0, (y1 - y0) / len(rows))
    thick = 0.36 if paired else 0.55
    for i, r in enumerate(rows):
        top = y0 + i * row_h
        n = len(r.values)
        group_h = n * thick + (n - 1) * 0.08
        gy = top + (row_h - group_h) / 2
        c.text(X0, gy, label_w, group_h, r.label, SIZE_EVIDENCE, INK, anchor=MSO_ANCHOR.MIDDLE)
        for k, v in enumerate(r.values):
            by = gy + k * (thick + 0.08)
            bw = max(0.04, v / vmax * max_w)
            hi = (k == bars.highlight) if paired else (i == bars.highlight)
            c.gfx(bar_x, by, bw, thick, ACC if hi else BAR, "bar")
            c.text(bar_x + bw + 0.12, by, CW + X0 - (bar_x + bw + 0.12), thick, r.texts[k], SIZE_EVIDENCE, INK, anchor=MSO_ANCHOR.MIDDLE)
    return y0 + row_h * len(rows)


def render_barchart(c: Canvas, s: C.BarChart) -> None:
    c.headline(s.title)
    cap_h = block_height_in([(s.caption, False)], SIZE_PROSE, CW) if s.caption else 0
    y_end = BOTTOM - (cap_h + 0.25 if s.caption else 0)
    end = draw_bars(c, s.bars, TOP, y_end)
    if s.caption:
        c.prose(X0, end + 0.25, CW, s.caption)


def render_scatter(c: Canvas, s: C.Scatter) -> None:
    c.headline(s.title)
    px0, px1 = X0 + 0.9, X0 + CW - 0.2
    py0, py1 = TOP, 5.65
    px = lambda v: px0 + v / s.x_max * (px1 - px0)
    py = lambda v: py1 - v / s.y_max * (py1 - py0)
    c.gfx(px0, py1, px1 - px0, 0.03, MUTED, "axis")
    c.gfx(px0 - 0.03, py0, 0.03, py1 - py0, MUTED, "axis")
    for v, lab in s.y_ticks:
        c.text(X0, py(v) - 0.2, px0 - X0 - 0.15, 0.4, lab, SIZE_EVIDENCE, MUTED, align=PP_ALIGN.RIGHT)
    for v, lab in s.x_ticks:
        c.text(px(v) - 0.6, py1 + 0.08, 1.2, 0.4, lab, SIZE_EVIDENCE, MUTED, align=PP_ALIGN.CENTER)
    order = [i for i in range(len(s.points)) if i != s.highlight] + [s.highlight]
    mark_w, label_h = 0.2, 2 * line_height_pt(SIZE_EVIDENCE) / 72
    for i in order:
        p = s.points[i]
        top, bottom = py(p.y_high), py(p.y_low)
        mid = (top + bottom) / 2
        h = max(0.2, bottom - top)
        hi = i == s.highlight
        c.gfx(px(p.x) - mark_w / 2, mid - h / 2, mark_w, h, ACC if hi else BAR, "scatter mark")
        if p.inline or not p.text:
            paras = [(f"{p.label}, {p.text}" if p.text else p.label, False)]
            w = text_width_pt(paras[0][0], SIZE_EVIDENCE) / 72 + 0.1
            lh = line_height_pt(SIZE_EVIDENCE) / 72
        else:
            paras = [(p.label, True), (p.text, False)]
            w = max(text_width_pt(p.label, SIZE_EVIDENCE, bold=True), text_width_pt(p.text, SIZE_EVIDENCE)) / 72 + 0.1
            lh = label_h
        if p.side == "r":
            lx, align = px(p.x) + mark_w / 2 + 0.12, PP_ALIGN.LEFT
            ly = mid - lh / 2
        elif p.side == "l":
            lx, align = px(p.x) - mark_w / 2 - 0.12 - w, PP_ALIGN.RIGHT
            ly = mid - lh / 2
        else:
            lx, align = px(p.x) + mark_w / 2 - w, PP_ALIGN.RIGHT
            ly = top - 0.08 - lh
        ly = min(max(ly, py0), py1 - lh - 0.03)
        c.text(lx, ly, w, lh + 0.02, paras, SIZE_EVIDENCE, ACC if hi else INK, align=align)
    if s.note:
        nw = 5.0
        c.text(px1 - nw, py0 + 0.05, nw, block_height_in([(s.note, False)], SIZE_EVIDENCE, nw) + 0.02, s.note, SIZE_EVIDENCE, MUTED)
    if s.caption:
        c.prose(X0, 6.15, CW, s.caption)


def render_bignumbers(c: Canvas, s: C.BigNumbers) -> None:
    c.headline(s.title)
    n = len(s.items)
    col_w = CW / n
    compact = s.bars is not None
    size = 72 if not compact else 54
    while size > 28 and max(text_width_pt(i.value, size, bold=True) for i in s.items) > (col_w - 0.3) * 72:
        size -= 2
    vy = TOP + (0.0 if compact else 0.5)
    vh = size * 1.4 / 72
    label_need = []
    for i, it in enumerate(s.items):
        x = X0 + i * col_w
        c.text(x, vy, col_w - 0.3, vh, it.value, size, ACC if i == s.highlight else (MUTED if it.muted else INK), kind="display", bold=True)
        label_size = SIZE_EVIDENCE if compact else 28
        label_h = max(0.8 if compact else 1.2, block_height_in([(it.label, False)], label_size, col_w - 0.3))
        label_need.append(c.text(x, vy + vh + 0.05, col_w - 0.3, label_h, it.label, label_size, MUTED))
    if compact:
        stat_bottom = vy + vh + 0.05 + max(label_need)
        bars_y = stat_bottom + 0.3
        if s.support:
            bar_left = vbar_left(s.bars)
            c.text(bar_left, bars_y, X0 + CW - bar_left, 0.4, s.support, SIZE_EVIDENCE, MUTED, bold=True)
            bars_y += 0.45
        draw_bars(c, s.bars, bars_y, BOTTOM)
    elif s.support:
        c.prose(X0, vy + vh + 1.3, CW, s.support)


def _set_cell_border(cell, color: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    ln = tcPr.makeelement(qn("a:lnB"), {"w": "12700", "cap": "flat", "cmpd": "sng", "algn": "ctr"})
    fill = ln.makeelement(qn("a:solidFill"), {})
    clr = fill.makeelement(qn("a:srgbClr"), {"val": color})
    fill.append(clr)
    ln.append(fill)
    tcPr.insert(0, ln)


def render_table(c: Canvas, s: C.Table) -> None:
    c.headline(s.title)
    n_cols = len(s.header)
    widths = [f * CW for f in (s.widths or tuple(1 / n_cols for _ in range(n_cols)))]
    pad_x, pad_y = 0.15, 0.06
    all_rows = [s.header, *s.rows]
    heights = []
    for ri, row in enumerate(all_rows):
        need = 0.0
        for ci, cell in enumerate(row):
            need = max(need, block_height_in([(cell, ri == 0)], SIZE_EVIDENCE, widths[ci] - 2 * pad_x))
        heights.append(max(0.46, need + 2 * pad_y))
    total = sum(heights)
    shape = c.slide.shapes.add_table(len(all_rows), n_cols, emu(X0), emu(TOP), emu(CW), emu(total))
    tbl = shape.table
    tbl._tbl.tblPr.find(qn("a:tableStyleId")).text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"
    tbl.horz_banding = False
    tbl.first_row = False
    for ci, w in enumerate(widths):
        tbl.columns[ci].width = emu(w)
    for ri, row in enumerate(all_rows):
        tbl.rows[ri].height = emu(heights[ri])
        hi = ri - 1 == s.highlight
        fill = TBL_HEAD if ri == 0 else (ACC if hi else WHITE)
        fg = INK if ri == 0 else (WHITE if hi else INK)
        for ci, text in enumerate(row):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = emu(pad_x)
            cell.margin_top = cell.margin_bottom = emu(pad_y)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(fill)
            tf = cell.text_frame
            tf.word_wrap = True
            para = tf.paragraphs[0]
            run = para.add_run()
            run.text = text
            run.font.size = Pt(SIZE_EVIDENCE)
            run.font.name = SANS
            run.font.bold = ri == 0 or hi
            run.font.color.rgb = rgb(fg)
            _set_cell_border(cell, RULE)
            c.records.append(
                TextRecord(
                    slide=c.index, kind="evidence", size=SIZE_EVIDENCE, fg=fg, bg=fill, words=len(text.split()),
                    snippet=text[:40], need_h=heights[ri], box_h=heights[ri],
                    text=text,
                    widest_word_pt=max(text_width_pt(w_, SIZE_EVIDENCE, bold=ri == 0 or hi) for w_ in text.split(" ")),
                    box_w_pt=(widths[ci] - 2 * pad_x) * 72,
                )
            )
    end = TOP + total
    if s.caption:
        end += 0.3
        end += c.prose(X0, end, CW, s.caption)
    c.check_bottom(end, "table block")


def render_code(c: Canvas, s: C.Code) -> None:
    c.headline(s.title)
    cap_need = block_height_in([(s.caption, False)], SIZE_PROSE, CW) + 0.3 if s.caption else 0
    h = code_panel(c, X0, TOP, CW, s.lines, max_h=BOTTOM - TOP - cap_need)
    if s.caption:
        c.prose(X0, TOP + h + 0.3, CW, s.caption)


SERIAL_BLURS = (
    (670, 470, 1025, 518),
    (440, 671, 560, 693),
    (440, 709, 560, 731),
    (780, 592, 832, 608),
    (918, 816, 996, 832),
    (698, 1096, 850, 1136),
)


def _png(img: PILImage.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


@lru_cache(maxsize=None)
def sanitized_image(path: str) -> bytes:
    img = PILImage.open(TALK / path).convert("RGBA")
    if path.endswith("screenshot-omp-mobile-0929.png"):
        for box in SERIAL_BLURS:
            region = img.crop(box).filter(ImageFilter.GaussianBlur(10))
            img.paste(region, box)
    return _png(img)


IMAGE_TOP, IMAGE_BOTTOM = 0.3, 7.2
CROP_W = 5.4
CROP_YS = (2.5, 4.3)


def render_image(c: Canvas, s: C.Image) -> None:
    base = PILImage.open(io.BytesIO(sanitized_image(s.path)))
    ih = IMAGE_BOTTOM - IMAGE_TOP
    iw = ih * base.width / base.height
    ix = SLIDE_W - X0 - iw
    iy = IMAGE_TOP
    text_w = ix - X0 - 0.5
    c.text(X0, 0.45, text_w, 1.4, s.title, SIZE_HEADLINE, INK, kind="headline", bold=True)
    c.slide.shapes.add_picture(io.BytesIO(sanitized_image(s.path)), emu(ix), emu(iy), emu(iw), emu(ih))
    scale = ih / base.height
    for (x1, y1, x2, y2) in s.circles:
        c.rect(ix + x1 * scale, iy + y1 * scale, (x2 - x1) * scale, (y2 - y1) * scale, None, ACC, 4.0, MSO_SHAPE.OVAL)
    for crop, y in zip(s.crops, CROP_YS):
        part = base.crop(crop.box)
        h = CROP_W * part.height / part.width
        c.slide.shapes.add_picture(io.BytesIO(_png(part)), emu(X0), emu(y), emu(CROP_W), emu(h))
        c.rect(X0, y, CROP_W, h, None, ACC, 3.0)
        lw = text_w - CROP_W - 0.25
        c.text(X0 + CROP_W + 0.25, y, lw, h, crop.label, 28, ACC, bold=True, anchor=MSO_ANCHOR.MIDDLE)


SHOT_LABEL_W = 3.3
SHOT_TOP = 1.9
SHOT_LABEL_BELOW_H = 0.68
SHOT_MAX_IN_PER_PX = 0.02
BANNER_FONT = FONT_DIR / FONT_FILES[("sans", True)]


def _stack_rows(img: PILImage.Image, shot: C.Shot) -> PILImage.Image:
    rows = [img.crop(r) for r in shot.stack]
    width = shot.stack_w or max(r.width for r in rows)
    rows = [
        r if r.width <= width else r.resize((width, round(r.height * width / r.width)), PILImage.LANCZOS)
        for r in rows
    ]
    background = max(rows[-1].getcolors(rows[-1].width * rows[-1].height))[1]
    out = PILImage.new("RGB", (width, sum(r.height for r in rows)), background)
    at = 0
    for r in rows:
        out.paste(r, (0, at))
        at += r.height
    return out


def _crop_cut(img: PILImage.Image, shot: C.Shot) -> PILImage.Image:
    if shot.crop:
        x1, y1, x2, y2 = shot.crop
        img = img.crop(shot.crop)
    else:
        x1 = y1 = 0
    if shot.cut:
        keep, y = [], 0
        for c1, c2 in sorted(shot.cut):
            keep.append((y, c1 - y1))
            y = c2 - y1
        keep.append((y, img.height))
        out = PILImage.new("RGB", (img.width, sum(b - a for a, b in keep)))
        at = 0
        for a, b in keep:
            out.paste(img.crop((0, a, img.width, b)), (0, at))
            at += b - a
        img = out
    return img


@lru_cache(maxsize=None)
def shot_image(shot: C.Shot, banner: bool = False) -> PILImage.Image:
    """The real artifact, cropped and cut in memory. `banner` paints the label onto the picture."""
    img = PILImage.open(TALK / shot.path).convert("RGB")
    if shot.stack:
        img = _stack_rows(img, shot)
    else:
        img = _crop_cut(img, shot)
    for b in shot.blur:
        box = b.box or (0, 0, img.width, img.height)
        box = (box[0], box[1], min(box[2], img.width), min(box[3], img.height))
        img.paste(img.crop(box).filter(ImageFilter.GaussianBlur(b.radius)), box[:2])
    if banner:
        size = max(24, round(img.width * 0.06))
        font = ImageFont.truetype(str(BANNER_FONT), size)
        while font.getlength(shot.label) > img.width * 0.94 - 2 * 18 and size > 16:
            size -= 2
            font = ImageFont.truetype(str(BANNER_FONT), size)
        draw = ImageDraw.Draw(img)
        pad = 18
        w = font.getlength(shot.label) + 2 * pad
        draw.rectangle((0, 0, w, size * 1.5), fill="#" + ACC)
        draw.text((pad, size * 0.2), shot.label, font=font, fill="#" + WHITE)
    return img


def shot_scale(img: PILImage.Image, max_w: float, max_h: float) -> float:
    return min(max_w / img.width, max_h / img.height, SHOT_MAX_IN_PER_PX)


def render_shot(c: Canvas, s: C.Slide) -> None:
    """Headline, one artifact, one direct label. Label sits beside or under the picture, whichever lets the picture grow larger."""
    shot = s.shot
    img = shot_image(shot)
    c.headline(s.title)
    area_h = BOTTOM - SHOT_TOP
    side = shot_scale(img, CW - SHOT_LABEL_W - 0.3, area_h)
    below = shot_scale(img, CW, area_h - SHOT_LABEL_BELOW_H)
    beside = side >= below
    scale = side if beside else below
    iw, ih = img.width * scale, img.height * scale
    c.slide.shapes.add_picture(io.BytesIO(_png(img)), emu(X0), emu(SHOT_TOP), emu(iw), emu(ih))
    c.rect(X0, SHOT_TOP, iw, ih, None, RULE, 1.0)
    fx1, fy1, fx2, fy2 = shot.box
    bx, by = X0 + fx1 * iw, SHOT_TOP + fy1 * ih
    bw, bh = (fx2 - fx1) * iw, (fy2 - fy1) * ih
    c.rect(bx, by, bw, bh, None, ACC, 4.0)
    if beside:
        lx = X0 + iw + 0.3
        need = block_height_in([(shot.label, True)], 28, SHOT_LABEL_W)
        ly = min(max(by + bh / 2 - need / 2, SHOT_TOP), BOTTOM - need)
        c.line(bx + bw, by + bh / 2, lx - 0.05, ly + need / 2, ACC, 2.0)
        c.text(lx, ly, SHOT_LABEL_W, need + 0.02, shot.label, 28, ACC, bold=True)
    else:
        lw = X0 + CW - bx
        need = block_height_in([(shot.label, True)], 28, lw)
        ly = SHOT_TOP + ih + 0.1
        c.check_bottom(ly + need, "screenshot label")
        c.text(bx, ly, lw, need + 0.02, shot.label, 28, ACC, bold=True)


def render_before_after(c: Canvas, s: C.BeforeAfter) -> None:
    """Same region of two frames, each labelled on the picture itself."""
    c.headline(s.title)
    gap = 0.3
    frames = [shot_image(sh, banner=True) for sh in (s.before, s.after)]
    scale = min(shot_scale(f, (CW - gap) / 2, BOTTOM - SHOT_TOP) for f in frames)
    x = X0
    for f in frames:
        iw, ih = f.width * scale, f.height * scale
        c.slide.shapes.add_picture(io.BytesIO(_png(f)), emu(x), emu(SHOT_TOP), emu(iw), emu(ih))
        c.rect(x, SHOT_TOP, iw, ih, None, RULE, 1.0)
        x += iw + gap


def render_spec(c: Canvas, s: C.Spec) -> None:
    """Wireframe on the left, the three layers it leads to on the right."""
    c.headline(s.title)
    img = shot_image(s.picture)
    area_h = BOTTOM - SHOT_TOP
    scale = shot_scale(img, 7.0, area_h)
    iw, ih = img.width * scale, img.height * scale
    c.slide.shapes.add_picture(io.BytesIO(_png(img)), emu(X0), emu(SHOT_TOP), emu(iw), emu(ih))
    c.rect(X0, SHOT_TOP, iw, ih, None, RULE, 1.0)
    x = X0 + iw + 0.4
    w = X0 + CW - x
    n = len(s.steps)
    gap = 0.2
    rh = (ih - gap * (n - 1)) / n
    for i, step in enumerate(s.steps):
        y = SHOT_TOP + i * (rh + gap)
        c.rect(x, y, w, rh, WHITE, RULE)
        c.text(x + 0.2, y, 0.5, rh, str(i + 1), 32, ACC, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        c.text(x + 0.8, y, w - 1.0, rh, step, 28, INK, bold=True, anchor=MSO_ANCHOR.MIDDLE)


def render_timeline(c: Canvas, s: C.Timeline) -> None:
    if all(e.at is not None for e in s.events):
        render_timeline_proportional(c, s)
        return
    c.headline(s.title)
    n = len(s.events)
    step = CW / n
    alternate = n >= 5
    line_y = 4.3 if alternate else (2.5 if s.code else 3.3)
    c.gfx(X0, line_y - 0.02, CW, 0.04, MUTED, "timeline axis")
    lw_max = min(3.6, 2 * step - 0.25) if alternate else step - 0.2
    for i, ev in enumerate(s.events):
        cx = X0 + step * (i + 0.5)
        lw = min(lw_max, 2 * (cx - X0), 2 * (X0 + CW - cx))
        hi = i == s.highlight
        c.gfx(cx - 0.14, line_y - 0.14, 0.28, 0.28, ACC if hi else MUTED, "timeline marker")
        above = alternate and i % 2 == 0
        paras = [(ev.when, True), (ev.label, False)]
        h = block_height_in(paras, SIZE_EVIDENCE, lw)
        if above:
            c.rect(cx - 0.01, line_y - 0.55, 0.02, 0.41, RULE)
            by = line_y - 0.6 - h
            anchor = MSO_ANCHOR.BOTTOM
        else:
            c.rect(cx - 0.01, line_y + 0.14, 0.02, 0.41, RULE)
            by = line_y + 0.6
            anchor = MSO_ANCHOR.TOP
        c.check_bottom(by + h, "timeline label")
        if by < TOP - 0.05:
            c.lint.fail(c.index, "timeline label collides with the headline")
        c.text(cx - lw / 2, by, lw, h, [(ev.when, True), (ev.label, False)], SIZE_EVIDENCE, ACC if hi else INK, align=PP_ALIGN.CENTER, anchor=anchor)
    if s.code:
        code_panel(c, X0, 4.25, CW, s.code, max_h=BOTTOM - 4.25, sizes=(24, 22, 20), pad=0.2)


CLUSTER_GAP_IN = 1.3


def render_timeline_proportional(c: Canvas, s: C.Timeline) -> None:
    """Marker spacing is proportional to clock time. Close events share one label under the axis."""
    c.headline(s.title)
    x_left, x_right = X0 + 0.2, X0 + CW - 0.2
    t0 = min(e.at for e in s.events)
    t1 = max(e.at for e in s.events)
    xs = [x_left + (e.at - t0) / (t1 - t0) * (x_right - x_left) for e in s.events]
    line_y = 3.9
    c.gfx(X0, line_y - 0.02, CW, 0.04, MUTED, "timeline axis")
    groups: list[list[int]] = []
    for i in range(len(s.events)):
        if groups and xs[i] - xs[groups[-1][-1]] < CLUSTER_GAP_IN:
            groups[-1].append(i)
        else:
            groups.append([i])
    for i, ev in enumerate(s.events):
        c.gfx(xs[i] - 0.14, line_y - 0.14, 0.28, 0.28, ACC if i == s.highlight else MUTED, "timeline marker")
    for gi, g in enumerate(groups):
        cx = sum(xs[i] for i in g) / len(g)
        hi = s.highlight in g
        if len(g) == 1:
            ev = s.events[g[0]]
            lw = 3.4
            paras = [(ev.when, True), (ev.label, False)]
            h = block_height_in(paras, SIZE_EVIDENCE, lw)
            left = min(max(cx - lw / 2, X0), X0 + CW - lw)
            align = PP_ALIGN.LEFT if left == X0 else (PP_ALIGN.RIGHT if left == X0 + CW - lw else PP_ALIGN.CENTER)
            c.rect(xs[g[0]] - 0.01, line_y - 0.55, 0.02, 0.41, RULE)
            c.text(left, line_y - 0.6 - h, lw, h, paras, SIZE_EVIDENCE, ACC if hi else INK, align=align, anchor=MSO_ANCHOR.BOTTOM)
        else:
            lw = 4.6
            paras = [p for i in g for p in ((s.events[i].when, True), (s.events[i].label, False))]
            h = block_height_in(paras, SIZE_EVIDENCE, lw)
            left = min(max(cx - lw / 2, X0), X0 + CW - lw)
            c.rect(cx - 0.01, line_y + 0.14, 0.02, 0.41, RULE)
            c.check_bottom(line_y + 0.6 + h, "timeline label")
            c.text(left, line_y + 0.6, lw, h, paras, SIZE_EVIDENCE, INK, align=PP_ALIGN.CENTER)
    for a, b in zip(groups, groups[1:]):
        minutes = round(s.events[b[0]].at - s.events[a[-1]].at)
        mid = (xs[a[-1]] + xs[b[0]]) / 2
        c.text(mid - 1.0, line_y + 0.14, 2.0, 0.4, f"{minutes} minutes", SIZE_EVIDENCE, MUTED, align=PP_ALIGN.CENTER)


def render_flow(c: Canvas, s: C.Flow) -> None:
    c.headline(s.title)
    n = len(s.steps)
    gap = 0.55 if n < 5 else 0.42
    bw = (CW - gap * (n - 1)) / n
    pad = 0.18 if n < 5 else 0.1
    def fits(z: int) -> bool:
        wide = all(text_width_pt(w, z) <= (bw - 2 * pad) * 72 for t in s.steps for w in t.split(" "))
        return wide and max(block_height_in([(t, False)], z, bw - 2 * pad) for t in s.steps) + 2 * pad <= 1.9

    size = next((z for z in (28, 24) if fits(z)), SIZE_EVIDENCE)
    need = max(block_height_in([(t, False)], size, bw - 2 * pad) for t in s.steps)
    bh = max(1.3, need + 2 * pad)
    by = TOP + 0.15
    for i, t in enumerate(s.steps):
        x = X0 + i * (bw + gap)
        hi = s.highlight == i
        c.rect(x, by, bw, bh, ACC if hi else WHITE, None if hi else RULE)
        c.text(x + pad, by + pad, bw - 2 * pad, bh - 2 * pad, t, size, WHITE if hi else INK, ACC if hi else WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            c.rect(x + bw + 0.1, by + bh / 2 - 0.17, gap - 0.2, 0.34, MUTED, shape=MSO_SHAPE.RIGHT_ARROW)
    y = by + bh
    if s.loop:
        lp = s.loop
        x_from = X0 + lp.from_step * (bw + gap) + bw / 2
        x_to = X0 + lp.to_step * (bw + gap) + bw / 2
        ly = y + 0.5
        c.rect(x_from - 0.015, y, 0.03, 0.5, MUTED)
        c.rect(min(x_from, x_to) - 0.015, ly - 0.015, abs(x_from - x_to) + 0.03, 0.03, MUTED)
        c.rect(x_to - 0.015, y + 0.12, 0.03, 0.4, MUTED)
        c.rect(x_to - 0.12, y, 0.24, 0.2, MUTED, shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        mid = (x_from + x_to) / 2
        c.text(mid - 3.0, ly + 0.1, 6.0, 0.4, lp.label, SIZE_EVIDENCE, MUTED, align=PP_ALIGN.CENTER)
        y = ly + 0.6
    if s.code:
        h = code_panel(c, X0, y + 0.4, CW, s.code, max_h=1.4, sizes=(24, 22, 20))
        y = y + 0.4 + h
    if s.caption:
        need_c = c.prose(X0, y + 0.4, CW, s.caption)
        y = y + 0.4 + need_c
    c.check_bottom(y, "flow block")


def render_compare(c: Canvas, s: C.Compare) -> None:
    c.headline(s.title)
    y = TOP
    cap_h = block_height_in([(s.caption, False)], SIZE_PROSE, CW) + 0.3 if s.caption else 0.0
    if s.lead:
        y += c.prose(X0, y, CW, s.lead) + 0.3
    n = len(s.cards)
    rows = math.ceil(n / s.cols)
    gap = 0.25 if rows < 3 else 0.15
    cw = (CW - gap * (s.cols - 1)) / s.cols
    pad = 0.25 if rows < 3 else 0.15
    avail = BOTTOM - 0.15 - y - cap_h
    cap = (avail - gap * (rows - 1)) / rows
    if rows == 1:
        cap = min(cap, 4.2)
    size = SIZE_EVIDENCE
    for trial in (32, 28, 24) if s.fill else (28, 24, SIZE_EVIDENCE):
        size = trial
        trial_need = max(block_height_in(cd.paras, trial, cw - 2 * pad) for cd in s.cards)
        widest = max(text_width_pt(w_, trial, bold=b) for cd in s.cards for t, b in cd.paras for w_ in t.split(" "))
        if trial_need + 2 * pad <= cap and widest <= (cw - 2 * pad) * 72:
            break
    need = max(block_height_in(cd.paras, size, cw - 2 * pad) for cd in s.cards)
    ch = cap if s.fill else min(cap, max(2.2 if rows == 1 else 1.5, need + 2 * pad + 0.3))
    if rows == 1 and not s.fill:
        y += (avail - ch) * 0.2
    for i, cd in enumerate(s.cards):
        r, col = divmod(i, s.cols)
        in_row = min(s.cols, n - r * s.cols) if s.fill else s.cols
        card_w = (CW - gap * (in_row - 1)) / in_row
        x = X0 + col * (card_w + gap)
        cy = y + r * (ch + gap)
        hi = s.highlight == i
        fill = ACC if hi else WHITE
        fg = WHITE if hi else (MUTED if cd.muted else INK)
        c.rect(x, cy, card_w, ch, fill, None if hi else RULE)
        c.text(
            x + pad, cy + pad, card_w - 2 * pad, ch - 2 * pad, cd.paras, size, fg, fill,
            anchor=MSO_ANCHOR.MIDDLE if s.fill else MSO_ANCHOR.TOP,
        )
    end = y + rows * ch + (rows - 1) * gap
    if s.caption:
        end += 0.3 + c.prose(X0, end + 0.3, CW, s.caption)
    c.check_bottom(end, "cards")


def render_stacks(c: Canvas, s: C.Stacks) -> None:
    c.headline(s.title)
    n = len(s.stacks)
    gap = 0.4
    avail_w = CW * (0.56 if s.code else 1.0) - (0.2 if s.code else 0)
    sw = (avail_w - gap * (n - 1)) / n
    pad = 0.07
    lowest = TOP
    for si, st in enumerate(s.stacks):
        x = X0 + si * (sw + gap)
        y = TOP
        if st.heading and n == 1:
            c.text(x, y, sw, 0.5, st.heading, SIZE_PROSE, ACC, bold=True)
            y += 0.6
        elif st.heading:
            c.text(x, y, sw, 0.35, st.heading, SIZE_EVIDENCE, MUTED, bold=True)
            y += 0.45
        roomy = not s.code and len(st.rows) <= 3
        big = not s.code and all(not r.detail for r in st.rows)
        size = 28 if big else SIZE_EVIDENCE
        min_h = 0.8 if big else ((1.05 if s.caption else 1.3) if roomy else 0.5)
        for ri, row in enumerate(st.rows):
            paras = [(row.label, True)] + ([(row.detail, False)] if row.detail else [])
            need = block_height_in(paras, size, sw - 2 * pad)
            rh = max(min_h, need + 2 * pad)
            hi = st.highlight == ri
            fill = ACC if hi else WHITE
            c.rect(x, y, sw, rh, fill, None if hi else RULE)
            c.text(x + pad, y, sw - 2 * pad, rh, paras, size, WHITE if hi else INK, fill, anchor=MSO_ANCHOR.MIDDLE)
            y += rh + 0.08
        lowest = max(lowest, y - 0.08)
    if s.code:
        cx = X0 + avail_w + 0.2
        code_panel(c, cx, TOP, X0 + CW - cx, s.code, max_h=BOTTOM - TOP, sizes=(24, 22, 20))
    if s.caption:
        lowest += 0.25 + c.prose(X0, lowest + 0.25, CW, s.caption)
    c.check_bottom(lowest, "stacks")


def render_hub(c: Canvas, s: C.Hub) -> None:
    c.headline(s.title)
    cap_need = block_height_in([(s.caption, False)], SIZE_PROSE, CW) if s.caption else 0
    y_top = TOP
    y_bot = BOTTOM - (cap_need + 0.3 if s.caption else 0)
    cx_c, cy = SLIDE_W / 2, (y_top + y_bot) / 2
    cwid, chei = 3.2, 1.1
    sw, sh = 3.6, 0.85
    left = [sp for i, sp in enumerate(s.spokes) if i % 2 == 0]
    right = [sp for i, sp in enumerate(s.spokes) if i % 2 == 1]
    placed = []
    for col, group in ((0, left), (1, right)):
        k = len(group)
        for j, sp in enumerate(group):
            sy = y_top + (j + 0.5) * (y_bot - y_top) / k - sh / 2
            sx = X0 if col == 0 else SLIDE_W - X0 - sw
            placed.append((sp, sx, sy, col))
    for sp, sx, sy, col in placed:
        ex = sx + sw if col == 0 else sx
        ctr_x = cx_c - cwid / 2 if col == 0 else cx_c + cwid / 2
        c.line(ctr_x, cy, ex, sy + sh / 2, MUTED, 2.5, sp.dashed)
    center_fill, center_fg = (RULE, INK) if s.neutral_center else (ACC, WHITE)
    c.rect(cx_c - cwid / 2, cy - chei / 2, cwid, chei, center_fill)
    c.text(cx_c - cwid / 2 + 0.15, cy - chei / 2, cwid - 0.3, chei, s.center, SIZE_EVIDENCE, center_fg, center_fill, bold=not s.neutral_center, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    spoke_fill, spoke_fg = (ACC, WHITE) if s.accent_spokes else (WHITE, INK)
    for sp, sx, sy, col in placed:
        c.rect(sx, sy, sw, sh, spoke_fill, None if s.accent_spokes else RULE)
        c.text(sx + 0.15, sy, sw - 0.3, sh, sp.label, SIZE_EVIDENCE, spoke_fg, spoke_fill, bold=s.accent_spokes, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        c.check_bottom(sy + sh, "hub spoke", y_bot + 0.05)
    if s.caption:
        c.prose(X0, y_bot + 0.3, CW, s.caption)


def render_quote(c: Canvas, s: C.Quote) -> None:
    c.headline(s.title)
    y = TOP + 0.1
    qw = CW - 0.4
    size = 44 if len(s.lines) == 1 and not s.code else 32
    lines_h = lambda sz: sum(block_height_in([(l, False)], sz, qw) for l in s.lines) + 0.25 * (len(s.lines) - 1)
    reserve = (0.6 if s.attribution else 0) + (2.2 if s.code else 0)
    while size > SIZE_PROSE and lines_h(size) > BOTTOM - y - reserve:
        size -= 2
    qh = lines_h(size)
    c.rect(X0, y, 0.08, qh, ACC)
    yy = y
    for l in s.lines:
        h = block_height_in([(l, False)], size, qw)
        c.text(X0 + 0.4, yy, qw, h, l, size, INK, kind="quote")
        yy += h + 0.25
    yy = y + qh + 0.2
    if s.attribution:
        c.text(X0 + 0.4, yy, qw, 0.35, s.attribution, SIZE_EVIDENCE, MUTED)
        yy += 0.6
    if s.code:
        h = code_panel(c, X0 + 0.4, yy, 4.8, s.code, max_h=2.1, sizes=(22, 20))
        yy += h
    c.check_bottom(yy, "quote block")


RENDERERS: dict[type, Callable] = {
    C.Title: render_title,
    C.Divider: render_divider,
    C.Map: render_map,
    C.Spec: render_spec,
    C.BeforeAfter: render_before_after,
    C.Statement: render_statement,
    C.Principle: render_principle,
    C.TryThis: render_trythis,
    C.BigNumbers: render_bignumbers,
    C.Table: render_table,
    C.BarChart: render_barchart,
    C.Scatter: render_scatter,
    C.Code: render_code,
    C.Image: render_image,
    C.Timeline: render_timeline,
    C.Flow: render_flow,
    C.Compare: render_compare,
    C.Stacks: render_stacks,
    C.Hub: render_hub,
    C.Quote: render_quote,
}
DARK_BG = {C.Title: INK, C.Divider: ACC, C.Principle: INK}

# ---------------------------------------------------------------- outline notes

@dataclass(frozen=True)
class OutlineSlide:
    n: int
    label: str
    timing: str
    minutes: float
    clock: float
    say: str
    evidence: str
    delivery: str
    chat: str


TIMING = re.compile(r"^([\d.]+) min \(clock (\d+):(\d\d)\)")


def _field(block: str, name: str) -> str:
    m = re.search(rf"(?ms)^\*\*{name}:\*\* (.+?)(?=^\*\*[A-Za-z ]+:\*\*|^#|^---|\Z)", block)
    return m.group(1).strip() if m else ""


def parse_outline(path: Path = OUTLINE_PATH) -> dict[int, OutlineSlide]:
    text = path.read_text()
    slides: dict[int, OutlineSlide] = {}
    for block in re.split(r"(?m)^(?=## Slide \d+ )", text):
        m = re.match(r"## Slide (\d+) \[(Wajib|Opsional)\]", block)
        if not m:
            continue
        n, label = int(m.group(1)), m.group(2)
        timing = _field(block, "Timing")
        tm = TIMING.match(timing)
        if not tm:
            raise ValueError(f"slide {n}: timing line does not match '<min> min (clock M:SS)': {timing!r}")
        slides[n] = OutlineSlide(
            n, label, timing, float(tm.group(1)), int(tm.group(2)) + int(tm.group(3)) / 60,
            _field(block, "Say"), _field(block, "Evidence"), _field(block, "Delivery"), _field(block, "Chat"),
        )
    return slides


def notes_for(s: C.Slide, outline: dict[int, OutlineSlide]) -> str:
    o = outline[s.n]
    parts = [f"Delivery: {o.delivery}"] if o.delivery else []
    parts.append(f"Say: {o.say}")
    if o.chat:
        parts.append(f"Chat: {o.chat}")
    if o.evidence:
        parts.append(f"Evidence: {o.evidence}")
    parts.append(f"Timing: {o.timing}. [{o.label}]")
    return "\n\n".join(parts)


# ---------------------------------------------------------------- lint

FACE_RULES = (
    (re.compile(r"\bSource\b"), "'Source'"),
    (re.compile(r"~/"), "a file path"),
    (re.compile(r"\b\w+\.(ya?ml|json|db|md|py|ts|sh)\b"), "a file path"),
    (re.compile(r"\b20\d\d-\d\d-\d\d\b"), "an ISO date"),
    (re.compile(r"\bMinute \d+"), "'Minute N'"),
    (re.compile(r"Ask chat"), "'Ask chat'"),
    (re.compile(r"\barms?\b", re.I), "the jargon 'arm'"),
    (re.compile(r"\bmedians?\b", re.I), "the jargon 'median'"),
    (re.compile(r"API-equivalent", re.I), "the jargon 'API-equivalent'"),
    (re.compile(r"head-to-head", re.I), "the jargon 'head-to-head'"),
    (re.compile(r"\bn/a\b", re.I), "the jargon 'n/a'"),
)
HEADLINE_KINDS = frozenset({"headline", "divider-headline", "title"})
FORBIDDEN = [
    (re.compile("\u2014|\u2013"), "dash character"),
    (re.compile(r"\s·\s"), "middle-dot meta string"),
    (re.compile("→|⇒|->"), "arrow appended to text"),
    (re.compile(r"Unilever|AlMajal|Acciona", re.I), "customer or tenant name"),
    (re.compile(r"poteto validate", re.I), "nonexistent command"),
    (re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"), "IP address"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "email"),
]
BACKSTAGE = re.compile(r"recorded backup|backup ready|backup recording", re.I)


def slide_strings(obj) -> list[str]:
    out: list[str] = []
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, (tuple, list)):
        for o in obj:
            out.extend(slide_strings(o))
    elif dataclasses.is_dataclass(obj):
        for f in dataclasses.fields(obj):
            out.extend(slide_strings(getattr(obj, f.name)))
    return out






def lint_content(slides, outline, lint: Lint) -> None:
    ns = [s.n for s in slides]
    if ns != list(range(1, len(slides) + 1)):
        lint.fail(0, f"slide numbers are not 1..{len(slides)} in order: {ns}")
    extra = sorted(set(outline) - set(ns))
    if extra:
        lint.fail(0, f"presenter.md has blocks for slides that do not exist: {extra}")
    last = len(slides)
    clock, total = 0.0, 0.0
    for i, s in enumerate(slides, 1):
        if type(s) not in RENDERERS:
            lint.fail(i, f"no renderer registered for {type(s).__name__}")
            continue
        t = s.title
        if len(t.split()) > MAX_HEADLINE_WORDS:
            lint.fail(i, f"headline has {len(t.split())} words, limit {MAX_HEADLINE_WORDS}: {t!r}")
        if isinstance(s, C.Divider):
            if len(wrap(t, SIZE_DIVIDER, CW, bold=True)) > 3:
                lint.fail(i, "divider title needs more than 3 lines")
            if not 1 <= s.segment < len(C.MAP):
                lint.fail(i, f"divider segment {s.segment} out of range")
            if not s.question.strip():
                lint.fail(i, "divider has no chat question")
        elif isinstance(s, C.Principle):
            if not 1 <= s.number <= PART_COUNT:
                lint.fail(i, f"principle number {s.number} out of range")
        elif not isinstance(s, C.Title):
            if not t.endswith("."):
                lint.fail(i, f"headline does not end with a period: {t!r}")
            if not isinstance(s, C.Image):
                lines = len(wrap(t, SIZE_HEADLINE, CW, bold=True))
                if lines > 2:
                    lint.fail(i, f"headline needs {lines} lines at {SIZE_HEADLINE}pt, limit 2")
        text = " ".join(slide_strings(s))
        for rx, what in FORBIDDEN:
            if rx.search(text):
                lint.fail(i, f"forbidden {what}")
        if BACKSTAGE.search(text):
            lint.fail(i, "backstage text (recorded backup) is visible on the slide; keep it in notes")
        if re.search(r"\$\d", text) and not re.search(r"paid|list price|per token|would cost", text, re.I):
            lint.fail(i, "dollar figure without 'paid', 'list price', 'per token' or 'would cost' beside it")
        if s.n not in outline:
            lint.fail(i, f"presenter.md has no block for slide {s.n}")
            continue
        o = outline[s.n]
        if abs(o.clock - clock) > 1e-6:
            lint.fail(i, f"presenter.md clock {o.clock:g} min does not match the running clock {clock:g} min")
        clock += o.minutes
        total += o.minutes
        notes = notes_for(s, outline)
        if (isinstance(s, C.Title) or s.demo or s.n == last) and not notes.startswith("Delivery:"):
            lint.fail(i, "notes must start with 'Delivery:'")
        if isinstance(s, C.Divider) and not o.chat:
            lint.fail(i, "divider notes need a Chat: line")
        if s.demo and (FALLBACK_SENTENCE not in notes or DEMO_TIME_BOX not in notes):
            lint.fail(i, f"demo notes need the fallback sentence and the {DEMO_TIME_BOX} time-box")
        if s.n == last and "repeat the question" not in notes.lower():
            lint.fail(i, "Q&A notes need 'repeat the question, answer, link back to the claim'")
        for shot in [x for x in (s.shot, getattr(s, "picture", None), getattr(s, "before", None), getattr(s, "after", None)) if x is not None]:
            if not (TALK / shot.path).is_file():
                lint.fail(i, f"screenshot {shot.path} does not exist")
            if not shot.path.startswith(C.ASSETS):
                lint.fail(i, f"screenshot must live in {C.ASSETS}")
            if len(shot.label.split()) > MAX_LABEL_WORDS:
                lint.fail(i, f"screenshot label has more than {MAX_LABEL_WORDS} words")
            if not all(0 <= v <= 1 for v in shot.box):
                lint.fail(i, "screenshot box must be fractions in 0..1")
        if isinstance(s, C.Image) and not (TALK / s.path).is_file():
            lint.fail(i, f"image {s.path} does not exist")
        if s.shot is None and isinstance(s, (C.Table, C.Timeline, C.BigNumbers)) and not (0 <= s.highlight < len(getattr(s, "rows", getattr(s, "events", getattr(s, "items", ()))))):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Compare) and s.shot is None and s.highlight is not None and not 0 <= s.highlight < len(s.cards):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Flow) and s.highlight is not None and not 0 <= s.highlight < len(s.steps):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Scatter) and not 0 <= s.highlight < len(s.points):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Timeline) and any(e.at is not None for e in s.events) and not all(e.at is not None for e in s.events):
            lint.fail(i, "timeline mixes events with and without a clock position")
        bars = getattr(s, "bars", None)
        if isinstance(bars, C.Bars):
            limit = len(bars.rows[0].values) if len(bars.rows[0].values) == 2 else len(bars.rows)
            if not 0 <= bars.highlight < limit:
                lint.fail(i, "bar highlight index out of range")
    if abs(total - TALK_MINUTES) > 1e-6:
        lint.fail(0, f"slide timings sum to {total:g} min, talk time is {TALK_MINUTES:g} min")
    for s in slides:
        if s.n not in outline:
            continue
        for rx, what in FORBIDDEN[2:]:
            if rx.search(notes_for(s, outline)):
                lint.fail(s.n, f"notes contain forbidden {what}: {rx.pattern}")


def face_limit(s: C.Slide) -> int:
    if isinstance(s, C.BigNumbers) and s.bars is not None:
        return CHART_FACE_WORDS
    return FACE_LIMITS.get(type(s), MAX_FACE_WORDS)


def lint_records(records: list[TextRecord], slides, lint: Lint) -> None:
    for r in records:
        where = f"{r.kind} text {r.snippet!r}"
        if r.size < SIZE_MIN:
            lint.fail(r.slide, f"{where} is {r.size}pt, minimum {SIZE_MIN}")
        if r.kind == "headline" and r.size != SIZE_HEADLINE:
            lint.fail(r.slide, f"{where} is {r.size}pt, headline must be {SIZE_HEADLINE}")
        if r.kind == "evidence" and r.size < SIZE_EVIDENCE:
            lint.fail(r.slide, f"{where} is {r.size}pt, evidence minimum {SIZE_EVIDENCE}")
        for rx, what in FACE_RULES:
            if rx.search(r.text):
                lint.fail(r.slide, f"face text {r.snippet!r} contains {what}")
        ratio = contrast(r.fg, r.bg)
        if ratio < 4.5:
            lint.fail(r.slide, f"{where} contrast {ratio:.2f}:1 on {r.bg}, minimum 4.5")
        if r.need_h > r.box_h + 0.02:
            lint.fail(r.slide, f"{where} needs {r.need_h:.2f}in but its box is {r.box_h:.2f}in")
        if r.widest_word_pt > r.box_w_pt:
            lint.fail(r.slide, f"{where} has a word wider than its box")

    face: dict[int, int] = {}
    for r in records:
        if r.kind not in HEADLINE_KINDS:
            face[r.slide] = face.get(r.slide, 0) + r.words
    for slide, n in face.items():
        limit = face_limit(slides[slide - 1])
        if n > limit:
            lint.fail(slide, f"{n} words on the face besides the headline, limit {limit}")


def lint_notes(records: list[TextRecord], notes: dict[int, str], lint: Lint) -> None:
    for i, text in notes.items():
        if not re.search(r"(?m)^Say: \S", text):
            lint.fail(i, "notes have no Say: line")
        face = " ".join(r.text for r in records if r.slide == i)
        if re.search(r"\d", face) and not re.search(r"(?m)^Evidence: \S", text):
            lint.fail(i, "a digit is on the face but the notes have no Evidence: line")


def lint_graphics(graphics: list[GraphicRecord], lint: Lint) -> None:
    for g in graphics:
        ratio = contrast(g.fill, g.bg)
        if ratio < MIN_GRAPHIC_CONTRAST:
            lint.fail(g.slide, f"{g.what} {g.fill} on {g.bg} is {ratio:.2f}:1, non-text minimum {MIN_GRAPHIC_CONTRAST}")


# ---------------------------------------------------------------- build

def build() -> tuple[Presentation, Lint]:
    outline = parse_outline()
    lint = Lint()
    lint_content(C.SLIDES, outline, lint)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
    blank = prs.slide_layouts[6]
    records: list[TextRecord] = []
    graphics: list[GraphicRecord] = []
    notes: dict[int, str] = {}
    for i, s in enumerate(C.SLIDES, 1):
        slide = prs.slides.add_slide(blank)
        if type(s) not in RENDERERS:
            continue
        canvas = Canvas(slide, i, DARK_BG.get(type(s), BG), lint, records, graphics)
        if s.shot is not None and not isinstance(s, (C.Title, C.Divider)):
            if (TALK / s.shot.path).is_file():
                render_shot(canvas, s)
        else:
            RENDERERS[type(s)](canvas, s)
        notes[i] = notes_for(s, outline)
        slide.notes_slide.notes_text_frame.text = notes[i]
    lint_records(records, C.SLIDES, lint)
    lint_notes(records, notes, lint)
    lint_graphics(graphics, lint)
    return prs, lint


def render() -> None:
    if RENDER_DIR.exists():
        shutil.rmtree(RENDER_DIR)
    RENDER_DIR.mkdir(parents=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(RENDER_DIR), str(OUTPUT)], check=True, capture_output=True)
    pdf = RENDER_DIR / (OUTPUT.stem + ".pdf")
    subprocess.run(["pdftoppm", "-r", "100", "-png", str(pdf), str(RENDER_DIR / "page")], check=True)
    pages = sorted(RENDER_DIR.glob("page-*.png"))
    cell_w, cell_h, cols, rows = 800, 450, 2, 3
    sheets = []
    for start in range(0, len(pages), cols * rows):
        sheet = PILImage.new("RGB", (cell_w * cols, cell_h * rows), "white")
        draw = ImageDraw.Draw(sheet)
        for k, page in enumerate(pages[start : start + cols * rows]):
            im = PILImage.open(page).convert("RGB").resize((cell_w - 6, cell_h - 6))
            x, y = (k % cols) * cell_w, (k // cols) * cell_h
            sheet.paste(im, (x + 3, y + 3))
            draw.rectangle((x, y, x + cell_w - 1, y + cell_h - 1), outline="#888888")
            draw.text((x + 8, y + 6), str(start + k + 1), fill="#ff0000")
        out = RENDER_DIR / f"sheet-{start // (cols * rows) + 1:02d}.png"
        sheet.save(out)
        sheets.append(out)
    print(f"pages: {len(pages)} in {RENDER_DIR}")
    for p in sheets:
        print(p)


def main() -> int:
    prs, lint = build()
    if lint.violations:
        print(f"lint failed with {len(lint.violations)} violations:")
        for v in lint.violations:
            print("  " + v)
        return 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUTPUT)
    print(f"wrote {OUTPUT.relative_to(TALK.parent.parent.parent)} with {len(prs.slides)} slides, lint clean")
    if "--render" in sys.argv:
        render()
    return 0


if __name__ == "__main__":
    sys.exit(main())
