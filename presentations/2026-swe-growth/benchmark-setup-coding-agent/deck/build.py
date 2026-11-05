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
ACC_TINT = "6F8EF0"
PALETTE = frozenset({BG, INK, MUTED, RULE, ACC, TBL_HEAD, WHITE, PANEL, PANEL_TXT, ACC_TINT})
SANS, MONO = "Source Sans 3", "Source Code Pro"

SLIDE_W, SLIDE_H = 13.333, 7.5
X0 = 0.8
CW = SLIDE_W - 2 * X0
TOP = 2.0
BOTTOM = 6.8
FOOTER_Y = 6.95

SIZE_HEADLINE, SIZE_PROSE, SIZE_EVIDENCE, SIZE_FOOTER = 36, 28, 20, 14
SIZE_DIVIDER = 48
MAX_HEADLINE_CHARS = 95
MAX_PROSE_WORDS = 25
TOTAL_OUTLINE_SLIDES = 47
THIRD_PARTY_COSTS = {15}

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
    need_h: float
    box_h: float
    widest_word_pt: float
    box_w_pt: float


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
    def __init__(self, slide, index: int, bg: str, lint: Lint, records: list[TextRecord]):
        self.slide, self.index, self.bg, self.lint, self.records = slide, index, bg, lint, records
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

    def footer(self, source: str, width: float = CW) -> None:
        if source:
            self.text(X0, FOOTER_Y, width, 0.3, "Source: " + source, SIZE_FOOTER, MUTED, kind="footer")

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
    c.text(X0 + 0.5, 1.6, 10.9, 3.1, s.title, 54, WHITE, kind="display", bold=True)
    c.text(X0 + 0.5, 4.9, 10.5, 0.5, s.subtitle, 28, PANEL_TXT, kind="display")


SECTION_COUNT = 8


def render_divider(c: Canvas, s: C.Divider) -> None:
    c.text(X0, 0.8, 6, 0.5, f"Minute {s.minute}", 28, WHITE, kind="display", bold=True)
    c.text(X0, 1.6, CW, 2.8, s.title, SIZE_DIVIDER, WHITE, kind="divider-headline", bold=True)
    if s.ask_chat:
        c.rect(X0, 4.75, CW, 0.03, WHITE)
        c.text(X0, 5.0, CW, 0.9, f"Ask chat: {s.ask_chat}", 28, WHITE, kind="display")
    gap, seg_w = 0.15, (CW - 7 * 0.15) / SECTION_COUNT
    for i in range(SECTION_COUNT):
        c.rect(X0 + i * (seg_w + gap), 6.6, seg_w, 0.1, WHITE if i < s.section else ACC_TINT)


def render_statement(c: Canvas, s: C.Statement) -> None:
    c.headline(s.title)
    c.text(X0, 3.0, CW, 1.2, s.support, 54, ACC, kind="display", bold=True)
    c.footer(s.source)


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
            c.rect(bx, base - bh, bw, bh, ACC if i == bars.highlight else RULE)
            c.text(X0 + i * col_w, base - bh - val_h - 0.03, col_w, val_h, r.texts[0], SIZE_EVIDENCE, INK, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM)
            c.text(X0 + i * col_w, base + 0.05, col_w, lab_h - 0.05, r.label, SIZE_EVIDENCE, MUTED, align=PP_ALIGN.CENTER)
        return y1
    label_w, bar_x, max_w = 3.2, X0 + 3.4, 6.2
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
            c.rect(bar_x, by, bw, thick, ACC if hi else RULE)
            c.text(bar_x + bw + 0.12, by, CW + X0 - (bar_x + bw + 0.12), thick, r.texts[k], SIZE_EVIDENCE, INK, anchor=MSO_ANCHOR.MIDDLE)
    return y0 + row_h * len(rows)


def render_barchart(c: Canvas, s: C.BarChart) -> None:
    c.headline(s.title)
    cap_h = block_height_in([(s.caption, False)], SIZE_PROSE, CW) if s.caption else 0
    y_end = BOTTOM - (cap_h + 0.25 if s.caption else 0)
    end = draw_bars(c, s.bars, TOP, y_end)
    if s.caption:
        c.prose(X0, end + 0.25, CW, s.caption)
    c.footer(s.source)


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
        c.text(x, vy, col_w - 0.3, vh, it.value, size, ACC if i == s.highlight else INK, kind="display", bold=True)
        label_need.append(c.text(x, vy + vh + 0.05, col_w - 0.3, 0.8, it.label, SIZE_EVIDENCE, MUTED))
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
    c.footer(s.source)


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
                    widest_word_pt=max(text_width_pt(w_, SIZE_EVIDENCE, bold=ri == 0 or hi) for w_ in text.split(" ")),
                    box_w_pt=(widths[ci] - 2 * pad_x) * 72,
                )
            )
    end = TOP + total
    if s.caption:
        end += 0.3
        end += c.prose(X0, end, CW, s.caption)
    c.check_bottom(end, "table block")
    c.footer(s.source)


def render_code(c: Canvas, s: C.Code) -> None:
    c.headline(s.title)
    cap_need = block_height_in([(s.caption, False)], SIZE_PROSE, CW) + 0.3 if s.caption else 0
    h = code_panel(c, X0, TOP, CW, s.lines, max_h=BOTTOM - TOP - cap_need)
    if s.caption:
        c.prose(X0, TOP + h + 0.3, CW, s.caption)
    c.footer(s.source)


SERIAL_BLURS = (
    (670, 470, 1025, 518),
    (440, 671, 560, 693),
    (440, 709, 560, 731),
    (780, 592, 832, 608),
    (918, 816, 996, 832),
    (698, 1096, 850, 1136),
)


@lru_cache(maxsize=None)
def sanitized_image(path: str) -> bytes:
    img = PILImage.open(TALK / path).convert("RGBA")
    if path.endswith("screenshot-omp-mobile-0929.png"):
        for box in SERIAL_BLURS:
            region = img.crop(box).filter(ImageFilter.GaussianBlur(10))
            img.paste(region, box)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


IMAGE_TOP, IMAGE_BOTTOM = 0.3, 7.2


def render_image(c: Canvas, s: C.Image) -> None:
    img = PILImage.open(TALK / s.path)
    ih = IMAGE_BOTTOM - IMAGE_TOP
    iw = ih * img.width / img.height
    ix = SLIDE_W - X0 - iw
    iy = IMAGE_TOP
    text_w = ix - X0 - 0.5
    c.text(X0, 0.45, text_w, 3.0, s.title, SIZE_HEADLINE, INK, kind="headline", bold=True)
    c.slide.shapes.add_picture(io.BytesIO(sanitized_image(s.path)), emu(ix), emu(iy), emu(iw), emu(ih))
    scale = ih / img.height
    for (x1, y1, x2, y2) in s.circles:
        c.rect(ix + x1 * scale, iy + y1 * scale, (x2 - x1) * scale, (y2 - y1) * scale, None, ACC, 4.0, MSO_SHAPE.OVAL)
    c.prose(X0, 3.2, text_w, s.caption)
    c.footer(s.source, width=ix - X0 - 0.3)


def render_timeline(c: Canvas, s: C.Timeline) -> None:
    c.headline(s.title)
    n = len(s.events)
    step = CW / n
    alternate = n >= 5
    line_y = 4.3 if alternate else (2.5 if s.code else 3.3)
    c.rect(X0, line_y - 0.02, CW, 0.04, MUTED)
    lw_max = min(3.6, 2 * step - 0.25) if alternate else step - 0.2
    for i, ev in enumerate(s.events):
        cx = X0 + step * (i + 0.5)
        lw = min(lw_max, 2 * (cx - X0), 2 * (X0 + CW - cx))
        hi = i == s.highlight
        c.rect(cx - 0.14, line_y - 0.14, 0.28, 0.28, ACC if hi else MUTED)
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
    c.footer(s.source)


def render_flow(c: Canvas, s: C.Flow) -> None:
    c.headline(s.title)
    n = len(s.steps)
    gap = 0.55 if n < 5 else 0.42
    bw = (CW - gap * (n - 1)) / n
    pad = 0.18 if n < 5 else 0.1
    need = max(block_height_in([(t, False)], SIZE_EVIDENCE, bw - 2 * pad) for t in s.steps)
    bh = max(1.3, need + 2 * pad)
    by = TOP + 0.15
    for i, t in enumerate(s.steps):
        x = X0 + i * (bw + gap)
        hi = s.highlight == i
        c.rect(x, by, bw, bh, ACC if hi else WHITE, None if hi else RULE)
        c.text(x + pad, by + pad, bw - 2 * pad, bh - 2 * pad, t, SIZE_EVIDENCE, WHITE if hi else INK, ACC if hi else WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
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
    c.footer(s.source)


def render_compare(c: Canvas, s: C.Compare) -> None:
    c.headline(s.title)
    y = TOP
    if s.lead:
        y += c.prose(X0, y, CW, s.lead) + 0.3
    n = len(s.cards)
    rows = math.ceil(n / s.cols)
    gap = 0.25 if rows < 3 else 0.15
    cw = (CW - gap * (s.cols - 1)) / s.cols
    pad = 0.25 if rows < 3 else 0.15
    avail = BOTTOM - 0.15 - y
    cap = (avail - gap * (rows - 1)) / rows
    if rows == 1:
        cap = min(cap, 4.2)
    size = SIZE_EVIDENCE
    for trial in (32, 28, 24) if s.fill else (28, 24, SIZE_EVIDENCE):
        size = trial
        trial_need = max(block_height_in([(cd.heading, True), (cd.body, False)], trial, cw - 2 * pad) for cd in s.cards)
        widest = max(text_width_pt(w_, trial, bold=b) for cd in s.cards for t, b in ((cd.heading, True), (cd.body, False)) for w_ in t.split(" "))
        if trial_need + 2 * pad <= cap and widest <= (cw - 2 * pad) * 72:
            break
    need = max(block_height_in([(cd.heading, True), (cd.body, False)], size, cw - 2 * pad) for cd in s.cards)
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
            x + pad, cy + pad, card_w - 2 * pad, ch - 2 * pad, [(cd.heading, True), (cd.body, False)], size, fg, fill,
            anchor=MSO_ANCHOR.MIDDLE if s.fill else MSO_ANCHOR.TOP,
        )
    c.check_bottom(y + rows * ch + (rows - 1) * gap, "cards")
    c.footer(s.source)


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
        if st.heading:
            c.text(x, y, sw, 0.35, st.heading, SIZE_EVIDENCE, MUTED, bold=True)
            y += 0.45
        min_h = 1.3 if (n == 1 and not s.code and len(st.rows) <= 3) else 0.5
        for ri, row in enumerate(st.rows):
            paras = [(row.label, True)] + ([(row.detail, False)] if row.detail else [])
            need = block_height_in(paras, SIZE_EVIDENCE, sw - 2 * pad)
            rh = max(min_h, need + 2 * pad)
            hi = st.highlight == ri
            fill = ACC if hi else WHITE
            c.rect(x, y, sw, rh, fill, None if hi else RULE)
            c.text(x + pad, y, sw - 2 * pad, rh, paras, SIZE_EVIDENCE, WHITE if hi else INK, fill, anchor=MSO_ANCHOR.MIDDLE)
            y += rh + 0.08
        lowest = max(lowest, y - 0.08)
    if s.code:
        cx = X0 + avail_w + 0.2
        code_panel(c, cx, TOP, X0 + CW - cx, s.code, max_h=BOTTOM - TOP, sizes=(24, 22, 20))
    c.check_bottom(lowest, "stacks")
    c.footer(s.source)


def render_hub(c: Canvas, s: C.Hub) -> None:
    c.headline(s.title)
    cap_need = block_height_in([(s.caption, False)], SIZE_PROSE, CW) if s.caption else 0
    strip_h = 0.8 if s.strip else 0
    y_top = TOP
    y_bot = BOTTOM - (cap_need + 0.3 if s.caption else 0) - (strip_h + 0.3 if s.strip else 0)
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
    c.rect(cx_c - cwid / 2, cy - chei / 2, cwid, chei, ACC)
    c.text(cx_c - cwid / 2 + 0.15, cy - chei / 2, cwid - 0.3, chei, s.center, SIZE_EVIDENCE, WHITE, ACC, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    for sp, sx, sy, col in placed:
        c.rect(sx, sy, sw, sh, WHITE, RULE)
        c.text(sx + 0.15, sy, sw - 0.3, sh, sp.label, SIZE_EVIDENCE, INK, WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        c.check_bottom(sy + sh, "hub spoke", y_bot + 0.05)
    y = y_bot + 0.3
    if s.strip:
        n = len(s.strip)
        gap = 0.25
        w = (CW - gap * (n - 1)) / n
        for i, t in enumerate(s.strip):
            x = X0 + i * (w + gap)
            c.rect(x, y, w, strip_h, None, MUTED)
            c.text(x + 0.1, y, w - 0.2, strip_h, t, SIZE_EVIDENCE, INK, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        y += strip_h + 0.3
    if s.caption:
        c.prose(X0, y, CW, s.caption)
    c.footer(s.source)


def render_quote(c: Canvas, s: C.Quote) -> None:
    c.headline(s.title)
    y = TOP + 0.1
    qw = CW - 0.4
    size = 44 if len(s.lines) == 1 and not (s.code or s.strip) else 32
    lines_h = lambda sz: sum(block_height_in([(l, False)], sz, qw) for l in s.lines) + 0.25 * (len(s.lines) - 1)
    reserve = (0.6 if s.attribution else 0) + (2.2 if s.code else 0) + (1.1 if s.strip else 0)
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
    if s.strip:
        n = len(s.strip)
        gap = 0.25
        w = (CW - gap * (n - 1)) / n
        for i, t in enumerate(s.strip):
            x = X0 + i * (w + gap)
            c.rect(x, yy + 0.2, w, 0.8, WHITE, RULE)
            c.text(x + 0.1, yy + 0.2, w - 0.2, 0.8, t, SIZE_EVIDENCE, INK, WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        yy += 1.0
    c.check_bottom(yy, "quote block")
    c.footer(s.source)


RENDERERS: dict[type, Callable] = {
    C.Title: render_title,
    C.Divider: render_divider,
    C.Statement: render_statement,
    C.BigNumbers: render_bignumbers,
    C.Table: render_table,
    C.BarChart: render_barchart,
    C.Code: render_code,
    C.Image: render_image,
    C.Timeline: render_timeline,
    C.Flow: render_flow,
    C.Compare: render_compare,
    C.Stacks: render_stacks,
    C.Hub: render_hub,
    C.Quote: render_quote,
}
DARK_BG = {C.Title: INK, C.Divider: ACC}

# ---------------------------------------------------------------- outline notes

@dataclass(frozen=True)
class OutlineSlide:
    n: int
    label: str
    timing: str
    key_points: tuple[str, ...]
    say: str


def parse_outline(path: Path = OUTLINE_PATH) -> dict[int, OutlineSlide]:
    text = path.read_text()
    slides: dict[int, OutlineSlide] = {}
    for block in re.split(r"(?m)^(?=## Slide \d+ )", text):
        m = re.match(r"## Slide (\d+) \[(Wajib|Opsional)\]", block)
        if not m:
            continue
        n, label = int(m.group(1)), m.group(2)
        timing = re.search(r"\*\*Timing:\*\* (.+)", block).group(1).strip()
        kp_block = re.search(r"\*\*Key points\*\*\n((?:- .+\n?)+)", block).group(1)
        points = tuple(l[2:].strip() for l in kp_block.strip().split("\n"))
        say = re.search(r"\*\*Speaker note:\*\* (.+)", block).group(1).strip()
        slides[n] = OutlineSlide(n, label, timing, points, say)
    return slides


def notes_for(s: C.Slide, outline: dict[int, OutlineSlide]) -> str:
    if s.n is None and not isinstance(s, C.Divider):
        return s.notes
    if isinstance(s, C.Divider):
        parts = [f"Section {s.section} of {SECTION_COUNT}, minute {s.minute}. Section divider, an attention reset."]
        if s.ask_chat:
            parts.append(f"Ask chat: {s.ask_chat}")
        return "\n\n".join(parts)
    o = outline[s.n]
    kp = "\n".join(f"- {p}" for p in o.key_points)
    return f"Key points:\n{kp}\n\nSay: {o.say}\n\nTiming: {o.timing}. [{o.label}]"


# ---------------------------------------------------------------- lint

VERB = re.compile(
    r"\b(\w+ed|\w+s|is|are|was|were|be|has|have|had|do|does|did|can|will|see|run|pay|hold|go|get|keep|write|take|make|show|give|cut|reach|stop|fix|check|load|work|look|ship|cost|pick|send|need|bring|prove|solve|watch|use|tell)\b",
    re.I,
)
FORBIDDEN = [
    (re.compile("\u2014|\u2013"), "dash character"),
    (re.compile(r"\s·\s"), "middle-dot meta string"),
    (re.compile("→|⇒|->"), "arrow appended to text"),
    (re.compile(r"Unilever|AlMajal|Acciona", re.I), "customer or tenant name"),
    (re.compile(r"poteto validate", re.I), "nonexistent command"),
    (re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"), "IP address"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "email"),
]


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
    ns = [s.n for s in slides if s.n is not None]
    if ns != list(range(1, TOTAL_OUTLINE_SLIDES + 1)):
        lint.fail(0, f"outline slide numbers are not 1..{TOTAL_OUTLINE_SLIDES} in order: {ns}")
    for i, s in enumerate(slides, 1):
        if type(s) not in RENDERERS:
            lint.fail(i, f"no renderer registered for {type(s).__name__}")
            continue
        if not isinstance(s, C.Title):
            t = s.title
            if not t.endswith("."):
                lint.fail(i, f"headline does not end with a period: {t!r}")
            if len(t) > MAX_HEADLINE_CHARS:
                lint.fail(i, f"headline is {len(t)} chars, limit {MAX_HEADLINE_CHARS}")
            if not VERB.search(t) or len(t.split()) < 5:
                lint.fail(i, f"headline does not read as a full-sentence assertion: {t!r}")
            size = SIZE_DIVIDER if isinstance(s, C.Divider) else SIZE_HEADLINE
            limit = 3 if isinstance(s, C.Divider) else 2
            lines = len(wrap(t, size, CW, bold=True))
            if lines > limit:
                lint.fail(i, f"headline needs {lines} lines at {size}pt, limit {limit}")
            if not isinstance(s, (C.Divider, C.Statement)) and not s.source:
                lint.fail(i, "evidence slide has no Source footer")
            if re.search(r"sources/|referensi|presenter\.md", s.source):
                lint.fail(i, f"footer cites this talk repo instead of the evidence: {s.source!r}")
            if s.n is None and not s.notes and not isinstance(s, C.Divider):
                lint.fail(i, "slide without an outline number has no notes")
        text = " ".join(slide_strings(s))
        for rx, what in FORBIDDEN:
            if rx.search(text):
                lint.fail(i, f"forbidden {what}")
        if re.search(r"\$\d", text) and "API-equivalent" not in text and s.n not in THIRD_PARTY_COSTS:
            lint.fail(i, "dollar figure without an API-equivalent label")
        if s.n is not None and s.n not in outline:
            lint.fail(i, f"outline slide {s.n} not found")
        if isinstance(s, (C.Table, C.Timeline, C.BigNumbers)) and not (0 <= s.highlight < len(getattr(s, "rows", getattr(s, "events", getattr(s, "items", ()))))):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Compare) and s.highlight is not None and not 0 <= s.highlight < len(s.cards):
            lint.fail(i, "highlight index out of range")
        if isinstance(s, C.Flow) and s.highlight is not None and not 0 <= s.highlight < len(s.steps):
            lint.fail(i, "highlight index out of range")
        for bars in (getattr(s, "bars", None),):
            if bars is not None:
                limit = len(bars.rows[0].values) if len(bars.rows[0].values) == 2 else len(bars.rows)
                if not 0 <= bars.highlight < limit:
                    lint.fail(i, "bar highlight index out of range")
    for text in (notes_for(s, outline) for s in slides if s.n in outline or isinstance(s, C.Divider) or s.notes):
        for rx, what in FORBIDDEN[2:]:
            if rx.search(text):
                lint.fail(0, f"notes contain forbidden {what}: {rx.pattern}")


def lint_records(records: list[TextRecord], lint: Lint) -> None:
    for r in records:
        where = f"{r.kind} text {r.snippet!r}"
        if r.size < SIZE_FOOTER:
            lint.fail(r.slide, f"{where} is {r.size}pt, minimum {SIZE_FOOTER}")
        if r.kind == "headline" and r.size != SIZE_HEADLINE:
            lint.fail(r.slide, f"{where} is {r.size}pt, headline must be {SIZE_HEADLINE}")
        if r.kind == "prose":
            if r.size != SIZE_PROSE:
                lint.fail(r.slide, f"{where} is {r.size}pt, prose must be {SIZE_PROSE}")
            if r.words > MAX_PROSE_WORDS:
                lint.fail(r.slide, f"{where} has {r.words} words, limit {MAX_PROSE_WORDS}")
        if r.kind == "evidence" and r.size < SIZE_EVIDENCE:
            lint.fail(r.slide, f"{where} is {r.size}pt, evidence minimum {SIZE_EVIDENCE}")
        if r.kind == "footer" and r.size != SIZE_FOOTER:
            lint.fail(r.slide, f"{where} is {r.size}pt, footer must be {SIZE_FOOTER}")
        ratio = contrast(r.fg, r.bg)
        if ratio < 4.5:
            lint.fail(r.slide, f"{where} contrast {ratio:.2f}:1 on {r.bg}, minimum 4.5")
        if r.need_h > r.box_h + 0.02:
            lint.fail(r.slide, f"{where} needs {r.need_h:.2f}in but its box is {r.box_h:.2f}in")
        if r.widest_word_pt > r.box_w_pt:
            lint.fail(r.slide, f"{where} has a word wider than its box")


# ---------------------------------------------------------------- build

def build() -> tuple[Presentation, Lint]:
    outline = parse_outline()
    lint = Lint()
    lint_content(C.SLIDES, outline, lint)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
    blank = prs.slide_layouts[6]
    records: list[TextRecord] = []
    for i, s in enumerate(C.SLIDES, 1):
        slide = prs.slides.add_slide(blank)
        if type(s) not in RENDERERS:
            continue
        canvas = Canvas(slide, i, DARK_BG.get(type(s), BG), lint, records)
        RENDERERS[type(s)](canvas, s)
        slide.notes_slide.notes_text_frame.text = notes_for(s, outline)
    lint_records(records, lint)
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
