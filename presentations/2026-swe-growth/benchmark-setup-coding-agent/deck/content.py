"""Deck content as typed data. One dataclass per layout, SLIDES in talk order.

Key points, speaker notes, timing and labels are not repeated here. build.py reads
them from sources/outlines/presenter.md by the outline slide number `n`. Dividers
carry their own delivery cue because the outline has no block for them.

Any slide can take a screenshot by setting `shot`. The renderer then swaps the
slide body for headline, screenshot and one direct label. Assets live in deck/assets/.
`crop` and `cut` shape the real artifact in memory, so the file on disk stays untouched.
`stack` re-wraps text that is too wide to read: each rectangle becomes one row, left aligned, and a
rectangle wider than `stack_w` is scaled down to it. Source pixels are never redrawn.
"""

from __future__ import annotations

from dataclasses import dataclass

REFS = "sources/references/"
ASSETS = "deck/assets/"


@dataclass(frozen=True, kw_only=True)
class Shot:
    path: str
    label: str
    box: tuple[float, float, float, float] = (0.0, 0.0, 1.0, 1.0)
    crop: tuple[int, int, int, int] | None = None
    cut: tuple[tuple[int, int], ...] = ()
    stack: tuple[tuple[int, int, int, int], ...] = ()
    stack_w: int | None = None


@dataclass(frozen=True, kw_only=True)
class Slide:
    title: str
    n: int | None = None
    source: str = ""
    shot: Shot | None = None
    demo: bool = False


@dataclass(frozen=True, kw_only=True)
class Title(Slide):
    subtitle: str = ""


@dataclass(frozen=True, kw_only=True)
class Divider(Slide):
    section: int = 0
    minute: int = 0
    ask_chat: str = ""
    delivery: str = ""


@dataclass(frozen=True, kw_only=True)
class BeforeAfter(Slide):
    """Two frames of one action, side by side. Unnumbered: it takes seconds from the slide before it."""

    before: Shot
    after: Shot
    delivery: str
    say: str


@dataclass(frozen=True, kw_only=True)
class Statement(Slide):
    support: str = ""
    extra: str = ""


@dataclass(frozen=True, kw_only=True)
class Stat:
    value: str
    label: str


@dataclass(frozen=True, kw_only=True)
class BarRow:
    label: str
    values: tuple[float, ...]
    texts: tuple[str, ...]


@dataclass(frozen=True, kw_only=True)
class Bars:
    rows: tuple[BarRow, ...]
    highlight: int
    vertical: bool = False


@dataclass(frozen=True, kw_only=True)
class BigNumbers(Slide):
    items: tuple[Stat, ...] = ()
    highlight: int = 0
    support: str = ""
    bars: Bars | None = None


@dataclass(frozen=True, kw_only=True)
class Table(Slide):
    header: tuple[str, ...] = ()
    rows: tuple[tuple[str, ...], ...] = ()
    highlight: int = 0
    widths: tuple[float, ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class BarChart(Slide):
    bars: Bars | None = None
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class ScatterPoint:
    label: str
    x: float
    y_low: float
    y_high: float
    text: str
    side: str = "r"
    inline: bool = False


@dataclass(frozen=True, kw_only=True)
class Scatter(Slide):
    points: tuple[ScatterPoint, ...] = ()
    highlight: int = 0
    x_max: float = 1.0
    y_max: float = 1.0
    x_ticks: tuple[tuple[float, str], ...] = ()
    y_ticks: tuple[tuple[float, str], ...] = ()
    note: str = ""
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class GanttBar:
    label: str
    start: str
    end: str
    reason: str = ""
    highlight: bool = False


@dataclass(frozen=True, kw_only=True)
class Gantt(Slide):
    bars: tuple[GanttBar, ...] = ()
    ticks: tuple[tuple[str, str], ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class Code(Slide):
    lines: tuple[str, ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class Crop:
    box: tuple[int, int, int, int]
    label: str


@dataclass(frozen=True, kw_only=True)
class Image(Slide):
    path: str = ""
    crops: tuple[Crop, ...] = ()
    circles: tuple[tuple[int, int, int, int], ...] = ()


@dataclass(frozen=True, kw_only=True)
class Event:
    when: str
    label: str
    at: float | None = None


@dataclass(frozen=True, kw_only=True)
class Timeline(Slide):
    events: tuple[Event, ...] = ()
    highlight: int = 0
    code: tuple[str, ...] = ()


@dataclass(frozen=True, kw_only=True)
class Loop:
    label: str
    from_step: int
    to_step: int


@dataclass(frozen=True, kw_only=True)
class Flow(Slide):
    steps: tuple[str, ...] = ()
    highlight: int | None = None
    loop: Loop | None = None
    caption: str = ""
    code: tuple[str, ...] = ()


@dataclass(frozen=True, kw_only=True)
class Card:
    heading: str
    body: str
    muted: bool = False


@dataclass(frozen=True, kw_only=True)
class Compare(Slide):
    cards: tuple[Card, ...] = ()
    cols: int = 2
    highlight: int | None = None
    lead: str = ""
    fill: bool = False


@dataclass(frozen=True, kw_only=True)
class Row:
    label: str
    detail: str = ""


@dataclass(frozen=True, kw_only=True)
class Stack:
    heading: str
    rows: tuple[Row, ...]
    highlight: int | None = None


@dataclass(frozen=True, kw_only=True)
class Stacks(Slide):
    stacks: tuple[Stack, ...] = ()
    code: tuple[str, ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class Spoke:
    label: str
    dashed: bool = False


@dataclass(frozen=True, kw_only=True)
class Hub(Slide):
    center: str = ""
    spokes: tuple[Spoke, ...] = ()
    caption: str = ""
    neutral_center: bool = False
    accent_spokes: bool = False


@dataclass(frozen=True, kw_only=True)
class Quote(Slide):
    lines: tuple[str, ...] = ()
    attribution: str = ""
    code: tuple[str, ...] = ()


SKILL_RULE = "\"When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you.\""

SLIDES: tuple[Slide, ...] = (
    # Section 1. Cold open
    Title(
        n=1,
        title="Benchmarking My Coding Agent Setup: One Engineer, Many Agents",
        subtitle="SWE Growth community, online. Zahid.",
    ),
    Image(
        n=2,
        title="My agent reproduced a bug from my phone at 9:29, before takeoff.",
        path=REFS + "screenshot-omp-mobile-0929.png",
        crops=(
            Crop(box=(20, 20, 420, 110), label="9:29 WIB"),
            Crop(box=(60, 2238, 1030, 2372), label="voice prompt"),
        ),
        circles=((55, 38, 165, 94), (888, 2252, 992, 2352)),
        source="My phone, Tern Android app, Tuesday 27 October 2026, 9:29 WIB. Serial numbers blurred.",
    ),
    Timeline(
        n=3,
        title="QA warned about PR #804 at 08:52 and passed it 65 minutes later, at 09:57.",
        events=(
            Event(when="08:52", label="QA warns on an approved PR", at=0),
            Event(when="09:26", label="I paste the finding from my phone", at=34),
            Event(when="09:29", label="Agent records the before clip", at=37),
            Event(when="09:31", label="PR body updated", at=39),
            Event(when="09:57", label="QA passes", at=65),
        ),
        highlight=4,
        source="GinaV2 PR #804 timeline, 26 to 27 October 2026",
    ),
    BeforeAfter(
        title="Before the fix a draft click opens the edit modal, and after it the click only selects.",
        before=Shot(
            path=ASSETS + "pr804-draft-click-before.png",
            label="Before: click opens the edit modal",
            crop=(60, 65, 1000, 900),
        ),
        after=Shot(
            path=ASSETS + "pr804-draft-click-after.png",
            label="After: click only selects",
            crop=(60, 65, 1000, 900),
        ),
        source="GinaV2 PR #804 attached recordings, frame at 14 seconds, serial numbers hidden",
        delivery="Point at the modal on the left, then at the same click on the right. Take 15 seconds from slide 3.",
        say="Same sensor, same click. Before the fix the click opens the edit modal. After it, the click only selects the sensor, and the pencil in Machine Information still opens the modal.",
    ),
    Hub(
        n=4,
        title="The model is a swappable part, and the setup around it is what ships the work.",
        center="Model",
        spokes=(
            Spoke(label="Skills"),
            Spoke(label="Proof"),
            Spoke(label="Coordination"),
            Spoke(label="Guardrails"),
        ),
        neutral_center=True,
        accent_spokes=True,
        source="Zahid, the claim of this talk",
    ),
    Stacks(
        n=5,
        title="A harness is the program around the model: it gives the model tools, context, memory and rules.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="Harness: tools, context, memory, rules", detail="Claude Code, Cursor, OpenCode, Amp, omp"),
                    Row(label="Model", detail="Claude, GPT, GLM"),
                ),
                highlight=0,
            ),
        ),
        source="Zahid, working definition for this talk",
    ),
    Stacks(
        n=6,
        title="Six terms come back in this talk, so here is each one in a line before it appears.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="Harness", detail="program around the model"),
                    Row(label="Worktree", detail="a separate checkout of a repo, per task"),
                    Row(label="Skill", detail="a file the agent loads when needed"),
                ),
            ),
            Stack(
                heading="",
                rows=(
                    Row(label="Mesh", detail="plugin so agents see each other"),
                    Row(label="SHIP", detail="my coordinator agent, it merges"),
                    Row(label="poteto-mode", detail="my agent-style skill"),
                ),
            ),
        ),
        source="Mayer, pre-training principle of multimedia learning: name the key terms before the lesson",
    ),
    Quote(
        n=7,
        title="Can Bölük's article on X says only the harness changed, and 15 LLMs got better.",
        lines=("\"I improved 15 LLMs at coding in one afternoon. Only the harness changed.\"",),
        attribution="Can Bölük, omp author, on X",
        shot=Shot(
            path=ASSETS + "x-can1357-post.png",
            label="Article title, word for word",
            box=(0.1, 0.63, 0.9, 0.79),
            crop=(0, 0, 745, 640),
        ),
        source="x.com/_can1357/status/2021828033640911196, his article on X",
    ),
    # Section 2. The journey
    Divider(
        section=2,
        minute=7,
        title="The journey",
        ask_chat="Which coding agent do you use today?",
        delivery=(
            "Look at the lens. Say the throughline in one sentence: the model is swappable, so the setup is what I kept changing. "
            "Ask the chat question and wait 5 s before you speak."
        ),
    ),
    Gantt(
        n=8,
        title="Every tool switch had a reason, and omp stayed because I can extend it.",
        bars=(
            GanttBar(label="Gemini tooling", start="2025-07-01", end="2025-10-19"),
            GanttBar(label="Claude Code", start="2025-10-19", end="2025-10-20", reason="quality"),
            GanttBar(label="OpenCode", start="2025-10-20", end="2025-12-22", reason="bans"),
            GanttBar(label="Amp", start="2025-12-22", end="2026-03-16", reason="forgot"),
            GanttBar(label="omp", start="2026-02-23", end="2026-11-05", reason="extensible", highlight=True),
        ),
        ticks=(("2025-07-01", "Jul 2025"), ("2026-01-01", "Jan 2026"), ("2026-07-01", "Jul 2026")),
        caption="The word at the end of a bar is why I left. Antigravity is missing because I have no date for it.",
        source="omp stats (~/.omp/stats.db) and session folders, first session per tool. A bar ends at the next tool's first session; Amp's end is dated.",
    ),
    Compare(
        n=9,
        title="Extending omp is how I fix my own problems, and the later slides are plugins I wrote.",
        cards=(
            Card(heading="Plugins", body="I write my own"),
            Card(heading="Autolearn", body="Creates skills"),
            Card(heading="Memory", body="Hindsight"),
            Card(heading="Logins", body="Several subscriptions"),
            Card(heading="Compaction", body="Good"),
        ),
        cols=3,
        highlight=0,
        fill=True,
        source="My reasons for omp, 2026-11-05; ~/.omp/agent/config.yml",
    ),
    # Section 3. Pillar 1
    Divider(
        section=3,
        minute=15,
        title="Pillar 1, the benchmark lab",
        ask_chat="Do you pay per token or per subscription?",
        delivery=(
            "Look at the lens. Throughline: I pick models with a bench I built, not a feeling. "
            "Ask the chat question and wait 5 s. The demo starts on the next slide."
        ),
    ),
    Code(
        n=10,
        title="I send one prompt from my phone, and the agent works while I keep talking.",
        lines=(
            "create new worktree, trace the impacted flow,",
            "fix, open a pr with proof in the body,",
            "coordinate with SHIP poteto",
        ),
        caption="Goal: a PR with proof in the body, checked at about minute 60.",
        source="Live demo from the Tern Android app",
        demo=True,
    ),
    Table(
        n=11,
        title="I pick models with a bench I built, so each role gets one model and one effort level.",
        header=("Role", "Model", "Effort"),
        rows=(
            ("default", "Opus", "low"),
            ("plan, slow", "Opus", "high"),
            ("reviewer", "Opus", "medium"),
            ("advisor, designer", "Sonnet", "high"),
            ("task agents", "Sonnet", "medium"),
            ("scout, sonic, smol", "Haiku", "fast"),
        ),
        highlight=0,
        widths=(0.5, 0.25, 0.25),
        caption="Output speed per request since October: Haiku 130 tokens per second, Sonnet 95, Opus 66.",
        source="~/.omp/agent/config.yml (modelRoles); omp stats (~/.omp/stats.db), speed since 2026-10-01",
    ),
    Code(
        n=12,
        title="A price per million tokens misleads, because a subscription changes what a token costs.",
        lines=(
            "Value Multiplier    = Quota $ / Subscription cost",
            "Effective $/1M      = Blended $/1M / Value Multiplier",
            "Value Score         = Benchmark / Effective $/1M",
            "Speed-adjusted QSPD = (Benchmark x tok/s)",
            "                      / (Effective $/1M x 1000)",
        ),
        caption="September: DeepSeek V4.1-Flash scored 90.6 at about 118 tokens per second. GLM-5.3 scored 88.2 at about 42.",
        source="My subscription value ranking, Terminal-Bench 2.1 scores, 2026-09-14",
    ),
    Scatter(
        n=13,
        title="Every arm passed 126 of 126 checks, so only speed and cost separated the models.",
        points=(
            ScatterPoint(label="Opus 5.5 low", x=92, y_low=0.22, y_high=0.39, text="92 s, $0.22 to $0.39"),
            ScatterPoint(label="Sonnet 5.5 medium", x=94, y_low=0.17, y_high=0.24, text="94 s, $0.17 to $0.24"),
            ScatterPoint(label="Spark 1.3 low", x=103, y_low=0.08, y_high=0.15, text="103 s, $0.08 to $0.15", inline=True),
            ScatterPoint(label="Wonder 1.0 low", x=136, y_low=0.39, y_high=0.41, text="136 s, $0.39 to $0.41"),
            ScatterPoint(label="Haiku 5.5 medium", x=170, y_low=0.02, y_high=0.03, text="170 s, $0.02 to $0.03", inline=True),
            ScatterPoint(label="DeepSeek flash low", x=476, y_low=0.04, y_high=0.07, text="476 s, $0.04 to $0.07", side="a"),
        ),
        highlight=0,
        x_max=500,
        y_max=0.45,
        x_ticks=((0, "0 s"), (250, "250 s"), (500, "500 s")),
        y_ticks=((0, "$0"), (0.2, "$0.20"), (0.4, "$0.40")),
        note="126 of 126 checks on every arm. Not a quality ranking. Cost is API-equivalent.",
        caption="UI task time. Cost spans both tasks. 3 runs, medians.",
        source="My October 2026 bench, 2 tasks x 3 runs, medians (~/.omp/agent/bench/results-2026-10.json)",
    ),
    BarChart(
        n=14,
        title="The formula called DeepSeek fast per token, and my bench made it the slowest per task.",
        bars=Bars(
            rows=(
                BarRow(label="Opus 5.5 low", values=(92,), texts=("92 s, 9 turns",)),
                BarRow(label="Sonnet 5.5 medium", values=(94,), texts=("94 s, 10 turns",)),
                BarRow(label="Haiku 5.5 medium", values=(170,), texts=("170 s, 15 turns",)),
                BarRow(label="DeepSeek flash low", values=(476,), texts=("476 s, 28 turns",)),
            ),
            highlight=3,
        ),
        caption="The September formula rated DeepSeek at about 118 tokens per second, and it never counted turns.",
        source="My October 2026 bench, UI task, 3 runs, medians; September ranking, 2026-09-14",
    ),
    BarChart(
        n=15,
        title="Raising effort raised the turn count in every head-to-head pair I measured.",
        bars=Bars(
            rows=(
                BarRow(label="Haiku, slot finder", values=(12, 16), texts=("12 turns, medium", "16 turns, high")),
                BarRow(label="Spark, slot finder", values=(9, 23), texts=("9 turns, low", "23 turns, medium")),
                BarRow(label="Sonnet, UI", values=(7, 10), texts=("7 turns, low", "10 turns, medium")),
                BarRow(label="DeepSeek, UI", values=(28, 40), texts=("28 turns, low", "40 turns, high")),
            ),
            highlight=1,
        ),
        caption="Low for execution, high for plans and hard debugging, medium for review, max almost never.",
        source="My October 2026 bench, 2 tasks x 3 runs, medians",
    ),
    Flow(
        n=16,
        title="Prewalk lets the expensive model plan, then hands the typing to a cheaper one.",
        steps=(
            "Opus 5.5 reads the code and writes a todo list",
            "At the first file edit, omp switches models",
            "A cheaper model makes the edits",
        ),
        highlight=1,
        caption="Reading costs money. Editing is cheap. So the strong model reads and the cheap one types.",
        source="omp docs; stencil.so/blog/prewalk (Can Bölük)",
    ),
    BarChart(
        n=17,
        title="On my short tasks prewalk cost the same or more, so I turned it off.",
        bars=Bars(
            rows=(
                BarRow(label="Slot finder, Opus low into Sonnet low", values=(0.22, 0.35), texts=("$0.22 alone", "$0.35 with prewalk")),
                BarRow(label="UI, Opus low into Sonnet low", values=(0.39, 0.48), texts=("$0.39 alone", "$0.48 with prewalk")),
                BarRow(label="Slot finder, Sonnet medium into Haiku medium", values=(0.17, 0.17), texts=("$0.17 alone", "$0.17 with prewalk")),
                BarRow(label="UI, Sonnet medium into Haiku medium", values=(0.24, 0.36), texts=("$0.24 alone", "$0.36 with prewalk")),
            ),
            highlight=1,
        ),
        caption="On into Haiku 24 Oct. Moved to DeepSeek 25 Oct to save money, too slow, so off the same day.",
        source="My October 2026 bench, Claude 5.5, 2 tasks x 3 runs, medians, API-equivalent",
    ),
    BigNumbers(
        n=18,
        title="I paid about $200 for October work that prices at $7.3k API-equivalent.",
        items=(
            Stat(value="$7.3k", label="API-equivalent list price of 41B tokens, October 2026"),
            Stat(value="about $200", label="what I paid"),
            Stat(value="36x", label="less, because 97% of the tokens were cache reads"),
        ),
        highlight=1,
        bars=Bars(
            rows=(
                BarRow(label="May", values=(2.2,), texts=("2.2k",)),
                BarRow(label="Jun", values=(23,), texts=("23k",)),
                BarRow(label="Jul", values=(46,), texts=("46k",)),
                BarRow(label="Aug", values=(174,), texts=("174k",)),
                BarRow(label="Sep", values=(235,), texts=("235k",)),
                BarRow(label="Oct", values=(270,), texts=("270k",)),
                BarRow(label="Nov 1 to 5", values=(47,), texts=("47k",)),
            ),
            highlight=5,
            vertical=True,
        ),
        support="Requests per month. June to August is the move from one chat to many agents.",
        source="omp stats (~/.omp/stats.db), re-aggregated 2026-11-05, API-equivalent",
    ),
    Compare(
        n=19,
        title="When Claude 5.5 quality moved, I moved, and my plan list changed with it.",
        cards=(
            Card(
                heading="September",
                body="GLM Max, Codex Pro, Devin Pro, OpenCode Go.",
            ),
            Card(
                heading="Now",
                body="2x Claude Max, OpenCode Go. \"Claude 5.5 series quality is GOAT\" (greatest of all time).",
            ),
        ),
        cols=2,
        highlight=1,
        source="My subscription portfolio, verified 2026-09-14; omp stats by provider, 2026-11-05",
    ),
    # Section 4. Pillar 2
    Divider(
        section=4,
        minute=32,
        title="Pillar 2, knowledge",
        ask_chat="Which task do you repeat with your agent more than twice?",
        delivery=(
            "Look at the lens. Throughline: the model is swappable, and what stays is what the agent knows. "
            "Ask the chat question and wait 5 s."
        ),
    ),
    Compare(
        n=20,
        title="Skills hold how to do a thing, and memory holds what I did and decided.",
        cards=(
            Card(heading="Skills and references", body="Today I learned, and reusable knowledge"),
            Card(heading="Memory", body="What you do cross-project"),
        ),
        cols=2,
        source="Zahid, 2026-11-05",
    ),
    Quote(
        n=21,
        title="Doing the same work more than twice makes it a candidate for a skill.",
        lines=(SKILL_RULE,),
        attribution="Zahid, the one action to take home",
        code=("SKILL.md", "playbooks/", "references/"),
        source="Zahid, 2026-11-05",
    ),
    Code(
        n=22,
        title="A lint script checks my 14 area skills, and the last run found 0 errors.",
        shot=Shot(
            path=ASSETS + "skills-lint.png",
            label="14 skills, 0 errors",
            box=(0.0, 0.5, 0.88, 0.86),
            crop=(24, 40, 640, 206),
            cut=((84, 160),),
        ),
        source="omp-skills repo, scripts/skills_lint.py, run 2026-11-05",
    ),
    Flow(
        n=23,
        title="Autolearn created too many skills, so I consolidated them and now trigger it by hand.",
        steps=("Autolearn on: many small skills", "14 domain skills plus a lint", "Manual trigger after a session that taught something"),
        highlight=2,
        code=("autolearn: { enabled: true, autoContinue: false }",),
        source="~/.omp/agent/config.yml (autolearn); my own account, 2026-11-05",
    ),
    Timeline(
        n=24,
        title="I tried three memory tools and kept Hindsight because it fits cross-project facts.",
        events=(
            Event(when="Before 2026-06-28", label="Mnemopi"),
            Event(when="2026-06-28", label="Hindsight, kept"),
            Event(when="September 2026", label="Cognee tried, destroyed on 2026-10-19"),
        ),
        highlight=1,
        code=(
            "memory:",
            "  backend: hindsight",
            "hindsight:",
            "  retainMode: last-turn",
            "  retainEveryNTurns: 10",
            "  retainOverlapTurns: 2",
        ),
        source="~/.omp/agent/config.yml (memory); Hindsight migration notes, 2026-06-28",
    ),
    Flow(
        n=25,
        title="Compaction tries three methods in order, so I do not watch the context window.",
        steps=("snapcompact", "remote", "soft"),
        highlight=0,
        caption="It starts at 70% of the context window, and compacts when idle after 60 seconds.",
        source="~/.omp/agent/config.yml (compaction)",
    ),
    Stacks(
        n=26,
        title="My prompts are loose on purpose, because the structure lives in layered files.",
        stacks=(
            Stack(
                heading="Instruction layers",
                rows=(
                    Row(label="Global file", detail="Short, hard rules"),
                    Row(label="Rule files", detail="Small, always or on a regex"),
                    Row(label="Repo AGENTS.md", detail="Nearest file wins"),
                    Row(label="Nested AGENTS.md", detail="Size budget checked"),
                ),
            ),
        ),
        code=("Brief for subagents", "", "Target", "Change", "Contract"),
        source="~/.omp/agent/AGENTS.md, rule files in ~/.omp/agent/rules, repo AGENTS.md files",
    ),
    Compare(
        n=27,
        title="I ported poteto-mode to omp, and it brings 25 principles and 23 playbooks.",
        cards=(
            Card(heading="25 principles", body="11 core, 6 architecture, 5 verification, 2 delegation, 1 meta"),
            Card(heading="23 playbooks", body="Bug fix, babysit, shipping, orchestrate and more"),
        ),
        cols=2,
        highlight=0,
        source="poteto-mode skill (pstack plugin by poteto, MIT license)",
    ),
    Stacks(
        n=28,
        title="Check-every-layer forces the agent to look at the layers it would otherwise skip.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="Product and the human walk"),
                    Row(label="Structure"),
                    Row(label="Data and flow"),
                ),
            ),
        ),
        caption="Each layer gets findings, or one line on why it does not apply.",
        source="principle-check-every-layer, my own principle added to poteto-mode",
    ),
    Compare(
        n=29,
        title="I dropped beads because agents got smarter and keep context without a tracker.",
        cards=(
            Card(heading="Beads, dropped", body="Not really human-readable", muted=True),
            Card(heading="Now", body="GitHub issues plus coordinator ledgers"),
        ),
        cols=2,
        highlight=1,
        source="My own account, 2026-11-05; SHIP coordinator ledger",
    ),
    # Section 5. Pillar 3
    Divider(
        section=5,
        minute=47,
        title="Pillar 3, the crew",
        ask_chat="How many agents do you run at once?",
        delivery=(
            "Look at the lens. Throughline: the model is swappable, and parallel agents stay safe because of the setup around them. "
            "Ask the chat question and wait 5 s."
        ),
    ),
    Code(
        n=30,
        title="Every agent task gets its own worktree, and tern-wt list shows who owns each one.",
        shot=Shot(
            path=ASSETS + "tern-wt-list.png",
            label="Dirty, 83 changes, owned by tern",
            box=(0.01, 0.175, 0.36, 0.656),
            crop=(120, 588, 870, 800),
        ),
        source="tern-wt list --all, 1 of 101 worktrees, tern-worktrees plugin",
    ),
    Compare(
        n=31,
        title="I run my own omp plugins, and the mesh plugin is enabled.",
        shot=Shot(
            path=ASSETS + "plugins.png",
            label="My mesh plugin, enabled",
            box=(0.0, 0.34, 0.98, 0.64),
            crop=(40, 84, 660, 185),
        ),
        source="omp plugin lockfile (~/.omp/plugins/omp-plugins.lock.json)",
    ),
    Code(
        n=32,
        title="Mesh lets every agent see what the others hold before it touches a shared resource.",
        shot=Shot(
            path=ASSETS + "mesh-peers.png",
            label="SHIP holds prod for the operator",
            box=(0.0, 0.6, 1.0, 0.9),
            stack=(
                (45, 236, 712, 267),
                (714, 236, 1517, 267),
                (98, 267, 920, 298),
                (45, 391, 712, 422),
                (714, 391, 1438, 422),
                (98, 422, 420, 453),
                (45, 453, 650, 484),
                (652, 453, 1465, 484),
                (98, 484, 945, 515),
                (45, 577, 410, 608),
            ),
        ),
        source="mesh tool, action peers, 2026-11-05, lines re-wrapped; 3 of 8 peers shown, 11 more in 6 other repos",
    ),
    Quote(
        n=33,
        title="Idle sessions never see a mesh message, so each branch needs exactly one writer.",
        lines=(
            "started fresh owners for #488 ... because their sessions had ended and never saw the broadcast",
            "idle sessions don't wake on mesh messages; each branch needs one writer",
        ),
        attribution="SHIP ledger, 2026-11-02",
        source="SHIP coordinator ledger, 2026-11-02",
    ),
    Divider(
        section=5,
        minute=55,
        title="Pillar 3, one coordinator",
        ask_chat="Who decides when an agent's PR is ready to merge?",
        delivery=(
            "Look at the lens. Restate the throughline in one sentence: one coordinator, not me, decides when work merges. "
            "Ask the chat question and wait 5 s."
        ),
    ),
    Flow(
        n=34,
        title="I watch one coordinator, and it merges only after an independent review.",
        steps=(
            "Worker opens a PR with proof in the body",
            "Worker sends MERGE-READY #pr and sha",
            "Coordinator freezes the head",
            "Independent reviewer writes a verdict file",
            "PASS: squash merge and clean up",
        ),
        highlight=3,
        loop=Loop(label="FAIL: findings go back, one fix round", from_step=3, to_step=0),
        source="SHIP coordinator ledger, 276 lines, 2026-11-03",
    ),
    Hub(
        n=35,
        title="One coordinator plus mesh solves base branch coordination, with one writer per branch.",
        center="Coordinator",
        spokes=(
            Spoke(label="Worker, branch A"),
            Spoke(label="Worker, branch B"),
            Spoke(label="Worker, branch C"),
            Spoke(label="Worker, branch D", dashed=True),
        ),
        caption="One writer per branch, merge in sequence. Dotted: the session-file fallback.",
        source="SHIP and merge-queue coordinator ledgers, 2026-10-29 to 2026-11-05",
    ),
    Table(
        n=36,
        title="The reviewer freezes a verdict at one commit and proves it through gates.",
        shot=Shot(
            path=ASSETS + "review-580-gates.png",
            label="Verdict frozen at one commit",
            box=(0.0, 0.0, 1.0, 0.25),
            stack=(
                (45, 173, 1045, 204),
                (1048, 173, 1535, 204),
                (70, 205, 460, 236),
                (45, 359, 280, 390),
                (45, 421, 710, 452),
                (722, 421, 1240, 452),
                (100, 453, 858, 484),
                (862, 453, 1505, 484),
                (98, 483, 700, 514),
                (45, 545, 865, 576),
                (45, 576, 800, 607),
                (45, 607, 825, 638),
            ),
        ),
        source="Coordinator review report for PR #580, 2026-11-05, lines re-wrapped, gate rows trimmed",
    ),
    Compare(
        n=37,
        title="The demo PR should carry its proof in the body, the way PR #804 does.",
        shot=Shot(
            path=ASSETS + "pr804-verification.png",
            label="Draft click: before and after",
            box=(0.0, 0.0, 0.73, 0.19),
            stack=(
                (189, 568, 1135, 598),
                (1136, 568, 1814, 598),
                (189, 606, 420, 645),
                (96, 672, 1622, 1100),
            ),
            stack_w=1300,
        ),
        source="GinaV2 PR #804 body, lines re-wrapped, nothing redrawn",
        demo=True,
    ),
    Stacks(
        n=38,
        title="PR #804 proves its fix with a red run on old code and a green run with the fix.",
        shot=Shot(
            path=ASSETS + "pr804-verification.png",
            label="3 failed on old code, 3 pass",
            box=(0.0, 0.0, 1.0, 0.51),
            stack=(
                (150, 213, 770, 245),
                (781, 213, 1792, 245),
                (144, 249, 324, 278),
                (144, 331, 774, 363),
                (778, 331, 1782, 363),
                (144, 369, 300, 394),
            ),
        ),
        source="GinaV2 PR #804 body, lines re-wrapped, nothing redrawn",
    ),
    # Section 6. Infra and guardrails
    Divider(
        section=6,
        minute=65,
        title="Infra and guardrails",
        ask_chat="Where do your agents run: laptop, server or cloud?",
        delivery=(
            "Look at the lens. Throughline: the model is swappable, and the machines and rules around it are the setup. "
            "Ask the chat question and wait 5 s."
        ),
    ),
    Hub(
        n=39,
        title="Proof runs away from the workstation, and production stays read-only.",
        center="x1 workstation, runs the agents",
        spokes=(
            Spoke(label="m5 Mac, review and browser"),
            Spoke(label="Shared dev box, one stack per user"),
            Spoke(label="Batch box, jobs and the NAS"),
            Spoke(label="Office box, staging"),
            Spoke(label="Cloud production, IAP tunnels, read-only", dashed=True),
        ),
        caption="Dotted: read-only by default.",
        source="My machine map, snapshot 2026-11-05",
    ),
    Timeline(
        n=40,
        title="Each terminal step removed one chore, and now I just use Tern.",
        events=(
            Event(when="OpenChamber", label="Web UI for OpenCode"),
            Event(when="Ghostty", label="Windows and tabs, because of omp"),
            Event(when="herdr, 2026-06-27", label="Worktrees and sessions"),
            Event(when="Paseo", label="Evaluated 2026-06-23, daemon stopped 2026-10-16"),
            Event(when="Tern", label="From Stencil, with an Android app"),
        ),
        highlight=4,
        source="My terminal history: herdr migration 2026-06-27, Paseo daemon stopped 2026-10-16",
    ),
    Code(
        n=41,
        title="One command takes a fresh worktree to a running stack.",
        lines=("From a fresh clone (or a fresh worktree):", "bun run bootstrap"),
        caption="Ports and database tier come from arithmetic on the branch slug.",
        source="alkhidmah devkit README, bun run bootstrap",
    ),
    Compare(
        n=42,
        title="Three layers protect secrets: hidden values, blocked commands and managed storage.",
        cards=(
            Card(heading="Obfuscation", body="The model sees placeholders"),
            Card(heading="Damage control", body="Blocks rm -rf, force push and DROP TABLE"),
            Card(heading="Secret managers", body="Infisical for machines, Bitwarden for humans"),
        ),
        cols=3,
        source="~/dotfiles/omp/agent/damage-control-rules.yaml; ~/.omp/agent/config.yml (secrets)",
    ),
    Flow(
        n=43,
        title="Every production write goes dry run, backup, guarded apply, then verify.",
        steps=("Dry run, real update rolled back", "Backup", "Apply with expected counts", "Verify the running version"),
        highlight=0,
        caption="\"dry run first then show me what will be changed\"",
        source="My groundup-ops dry-run runbook; my prompt of 2026-11-05",
    ),
    # Section 7. Open problems
    Divider(
        section=7,
        minute=74,
        title="Open problems",
        ask_chat="Which part of your agent's work do you still check by hand?",
        delivery=(
            "Look at the lens. Throughline: the setup works, and here is where it still breaks. "
            "Ask the chat question and wait 5 s."
        ),
    ),
    Compare(
        n=44,
        title="Three problems are open, and the first is that a proof clip cannot judge how a screen looks.",
        cards=(
            Card(heading="Proof clips show", body="A button works"),
            Card(heading="I still check by hand", body="UI and visual feel, and UX"),
        ),
        cols=2,
        highlight=1,
        source="Zahid, what I still check by hand",
    ),
    BarChart(
        n=45,
        title="One fix cut the per-worktree seed from 652 s to 171 s, and 171 s is still too slow.",
        bars=Bars(
            rows=(
                BarRow(label="Before the fix", values=(652,), texts=("652 s",)),
                BarRow(label="After the fix", values=(171,), texts=("171 s",)),
            ),
            highlight=1,
        ),
        caption="Every new worktree pays 171 s, and agents create many.",
        source="My own timing of the per-worktree seed, before and after one fix",
    ),
    BigNumbers(
        n=46,
        title="An uncapped test run reached 38 GB, so a rule now caps memory when test commands appear.",
        items=(
            Stat(value="38 GB", label="peak memory of one uncapped test run"),
            Stat(value="15 GiB", label="free RAM the verify script needs before it will run"),
        ),
        highlight=0,
        support="A rule fires on the command and tells the agent to cap memory first.",
        source="Memory-cap rule in ~/.omp/agent/rules; verify script threshold; my shared workstation",
    ),
    # Section 8. Close and Q&A
    Quote(
        n=47,
        title="Skills, proof, coordination and guardrails are the setup around a swappable model.",
        lines=(SKILL_RULE,),
        attribution="Monday: one skill, proof in every PR, dry run before production.",
        source="Zahid, 2026-11-05",
    ),
    Statement(
        n=48,
        title="Questions are welcome in chat or aloud, and one small skill is a good place to start.",
        support="@masrurimz",
        extra="Thank you, SWE Growth. Slides link in the chat.",
    ),
)
