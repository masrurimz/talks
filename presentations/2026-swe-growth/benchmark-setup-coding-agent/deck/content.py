"""Deck content as typed data. One dataclass per layout, DECK in talk order.

Slides carry no number here. SLIDES numbers them 1..N in talk order, and build.py reads the
speaker notes, timing and clock from sources/outlines/presenter.md by that number.
Every string on a slide face is spoken to the audience. Sources, dates, caveats, timing
and chat cues live in presenter.md.

Any slide can take a screenshot by setting `shot`. The renderer then swaps the
slide body for headline, screenshot and one direct label. Assets live in deck/assets/.
`crop` and `cut` shape the real artifact in memory, so the file on disk stays untouched.
`stack` re-wraps text that is too wide to read: each rectangle becomes one row, left aligned, and a
rectangle wider than `stack_w` is scaled down to it. Source pixels are never redrawn.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

REFS = "sources/references/"
ASSETS = "deck/assets/"


@dataclass(frozen=True, kw_only=True)
class Blur:
    """Gaussian blur of `box` (x1, y1, x2, y2 in the final cropped or stacked picture), or all of it when `box` is None."""

    radius: int
    box: tuple[int, int, int, int] | None = None


@dataclass(frozen=True, kw_only=True)
class Shot:
    path: str
    label: str
    box: tuple[float, float, float, float] = (0.0, 0.0, 1.0, 1.0)
    crop: tuple[int, int, int, int] | None = None
    cut: tuple[tuple[int, int], ...] = ()
    stack: tuple[tuple[int, int, int, int], ...] = ()
    stack_w: int | None = None
    blur: tuple[Blur, ...] = ()


@dataclass(frozen=True, kw_only=True)
class Slide:
    title: str
    n: int | None = None
    shot: Shot | None = None
    demo: bool = False


@dataclass(frozen=True, kw_only=True)
class Title(Slide):
    subtitle: str = ""


@dataclass(frozen=True, kw_only=True)
class Divider(Slide):
    part: int = 0
    question: str = ""


@dataclass(frozen=True, kw_only=True)
class Principle(Slide):
    number: int = 0
    line: str = ""


@dataclass(frozen=True, kw_only=True)
class TryThis(Slide):
    pass


@dataclass(frozen=True, kw_only=True)
class BeforeAfter(Slide):
    """Two frames of one action, side by side."""

    before: Shot
    after: Shot


@dataclass(frozen=True, kw_only=True)
class Statement(Slide):
    support: str = ""
    extra: str = ""


@dataclass(frozen=True, kw_only=True)
class Stat:
    value: str
    label: str
    muted: bool = False


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
    text: str = ""
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
    caption: str = ""


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


DECK: tuple[Slide, ...] = (
    # Opening, 0:00 to 5:00
    Title(
        title="Benchmarking My Coding Agent Setup: One Engineer, Many Agents",
        subtitle="SWE Growth community, online. Zahid.",
    ),
    Image(
        title="My agent reproduced a bug from my phone at 9:29, before takeoff.",
        path=REFS + "screenshot-omp-mobile-0929.png",
        crops=(
            Crop(box=(20, 20, 420, 110), label="9:29 WIB"),
            Crop(box=(60, 2238, 1030, 2372), label="voice prompt"),
        ),
        circles=((55, 38, 165, 94), (888, 2252, 992, 2352)),
    ),
    Timeline(
        title="QA flagged the bug at 08:52 and passed my fix at 09:57.",
        events=(
            Event(when="08:52", label="QA flags a bug", at=0),
            Event(when="09:26", label="I paste it in from my phone", at=34),
            Event(when="09:29", label="The agent records the bug", at=37),
            Event(when="09:57", label="QA passes", at=65),
        ),
        highlight=3,
    ),
    Hub(
        title="The model is a swappable part. The setup does the work.",
        center="Model",
        spokes=(
            Spoke(label="Skills"),
            Spoke(label="Proof"),
            Spoke(label="Coordination"),
            Spoke(label="Guardrails"),
        ),
        neutral_center=True,
        accent_spokes=True,
    ),
    Quote(
        title="Only the harness changed, and 15 models got better.",
        lines=("\"I improved 15 LLMs at coding in one afternoon. Only the harness changed.\"",),
        attribution="Can Bölük, omp author, on X",
        shot=Shot(
            path=ASSETS + "x-can1357-post.png",
            label="Can Bölük, omp author",
            box=(0.1, 0.63, 0.9, 0.79),
            crop=(0, 0, 745, 640),
        ),
    ),
    # My journey, 5:00 to 12:00
    Gantt(
        title="Each switch had a reason, and omp is the one that stayed.",
        bars=(
            GanttBar(label="Gemini tooling", start="2025-07-01", end="2025-10-19"),
            GanttBar(label="Claude Code", start="2025-10-19", end="2025-10-20", reason="quality"),
            GanttBar(label="OpenCode", start="2025-10-20", end="2025-12-22", reason="bans"),
            GanttBar(label="Amp", start="2025-12-22", end="2026-03-16", reason="forgot why"),
            GanttBar(label="omp", start="2026-02-23", end="2026-11-05", reason="extensible", highlight=True),
        ),
        ticks=(("2025-07-01", "Jul 2025"), ("2026-01-01", "Jan 2026"), ("2026-07-01", "Jul 2026")),
        caption="Each bar ends with the reason I left.",
    ),
    Hub(
        title="A harness is everything around the model.",
        center="Model",
        spokes=(
            Spoke(label="Tools"),
            Spoke(label="Context"),
            Spoke(label="Memory"),
            Spoke(label="Rules"),
        ),
        caption="Claude Code, Cursor and omp are harnesses.",
    ),
    Compare(
        title="I can extend omp, so I fix my own problems.",
        cards=(
            Card(heading="Plugins", body="I write my own"),
            Card(heading="Autolearn", body="Writes skills after a session"),
            Card(heading="Memory", body="Hindsight"),
            Card(heading="Logins", body="Several subscriptions"),
            Card(heading="Compaction", body="Shortens long chats"),
        ),
        cols=3,
        highlight=0,
        fill=True,
    ),
    BarChart(
        title="From one chat at a time to many agents at once.",
        bars=Bars(
            rows=(
                BarRow(label="May", values=(2.2,), texts=("2.2k",)),
                BarRow(label="Jun", values=(23,), texts=("23k",)),
                BarRow(label="Jul", values=(46,), texts=("46k",)),
                BarRow(label="Aug", values=(174,), texts=("174k",)),
                BarRow(label="Sep", values=(235,), texts=("235k",)),
                BarRow(label="Oct", values=(270,), texts=("270k",)),
            ),
            highlight=5,
            vertical=True,
        ),
        caption="Requests to my agents each month.",
    ),
    Code(
        title="I send one prompt from my phone, and the agent keeps working.",
        lines=(
            "create new worktree, trace the impacted flow,",
            "fix, open a pr with proof in the body,",
            "coordinate with SHIP poteto",
        ),
        caption="We open the result later in the talk.",
        demo=True,
    ),
    # Part 1. Measure it on your own work, 12:00 to 26:00
    Divider(
        part=1,
        title="Choosing models and paying for them",
        question="Per token or per subscription? Tell us in chat.",
    ),
    BarChart(
        title="The fastest model on paper was the slowest in my hands.",
        bars=Bars(
            rows=(
                BarRow(label="Opus 5.5 low", values=(92,), texts=("92 s",)),
                BarRow(label="Sonnet 5.5 medium", values=(94,), texts=("94 s",)),
                BarRow(label="Haiku 5.5 medium", values=(170,), texts=("170 s",)),
                BarRow(label="DeepSeek flash low", values=(476,), texts=("476 s",)),
            ),
            highlight=3,
        ),
        caption="On paper, DeepSeek runs at 118 tokens/s.",
    ),
    Principle(
        number=1,
        title="Measure it on your own work",
        line="A benchmark on paper is a guess. Your own task is the test.",
    ),
    Compare(
        title="Each job gets its own model.",
        cards=(
            Card(heading="Chat with me", body="Opus, low"),
            Card(heading="Plan", body="Opus, high"),
            Card(heading="Review", body="Opus, medium"),
            Card(heading="Helper agents", body="Sonnet, medium"),
            Card(heading="Quick searches", body="Haiku"),
        ),
        cols=3,
        fill=True,
        caption="Low to do, medium to review, high to plan, max almost never.",
    ),
    Scatter(
        title="Every model passed. Speed and price decided.",
        points=(
            ScatterPoint(label="Opus", x=92, y_low=0.22, y_high=0.39),
            ScatterPoint(label="Sonnet", x=94, y_low=0.17, y_high=0.24),
            ScatterPoint(label="Spark", x=103, y_low=0.08, y_high=0.15),
            ScatterPoint(label="Wonder", x=136, y_low=0.39, y_high=0.41),
            ScatterPoint(label="Haiku", x=170, y_low=0.02, y_high=0.03),
            ScatterPoint(label="DeepSeek", x=476, y_low=0.04, y_high=0.07, side="l"),
        ),
        highlight=0,
        x_max=500,
        y_max=0.45,
        x_ticks=((250, "250 s"), (500, "500 s")),
        y_ticks=((0.2, "$0.20"), (0.4, "$0.40")),
        note="Left is faster. Lower is cheaper.",
        caption="126 of 126 checks passed. Cost if I paid per token.",
    ),
    BarChart(
        title="Thinking harder made the agent take more steps.",
        bars=Bars(
            rows=(
                BarRow(label="Haiku", values=(12, 16), texts=("12 steps", "16 steps")),
                BarRow(label="Spark", values=(9, 23), texts=("9 steps", "23 steps")),
                BarRow(label="Sonnet", values=(7, 10), texts=("7 steps", "10 steps")),
                BarRow(label="DeepSeek", values=(28, 40), texts=("28 steps", "40 steps")),
            ),
            highlight=1,
        ),
        caption="Blue bar: higher effort.",
    ),
    Flow(
        title="Plan with the big model, let a small one type.",
        steps=(
            "Opus 5.5 reads and plans",
            "At the first edit, omp switches",
            "A cheaper model makes the edits",
        ),
        highlight=1,
        caption="Reading costs money. Editing is cheap.",
    ),
    BarChart(
        title="On my tasks it was never cheaper.",
        bars=Bars(
            rows=(
                BarRow(label="Opus low", values=(0.39, 0.48), texts=("$0.39 alone", "$0.48 with prewalk")),
                BarRow(label="Sonnet medium", values=(0.24, 0.36), texts=("$0.24 alone", "$0.36 with prewalk")),
            ),
            highlight=1,
        ),
        caption="UI task. Cost if I paid per token.",
    ),
    BigNumbers(
        title="$7,300 worth of tokens. I paid about $200.",
        items=(
            Stat(value="$7,300", label="worth of tokens in October"),
            Stat(value="about $200", label="what I paid"),
        ),
        highlight=1,
    ),
    Compare(
        title="When Claude 5.5 quality moved, I moved.",
        cards=(
            Card(heading="September", body="GLM Max, Codex Pro, Devin Pro, OpenCode Go."),
            Card(heading="Now", body="2x Claude Max, OpenCode Go."),
        ),
        cols=2,
        highlight=1,
        fill=True,
    ),
    TryThis(title="Time one real task of yours on two different models."),
    # Part 2. Do it twice, make it a skill, 26:00 to 37:00
    Divider(
        part=2,
        title="Teaching the agent",
        question="Which task do you repeat with your agent more than twice? Tell us in chat.",
    ),
    Flow(
        title="Autolearn made too many skills, so I merged them.",
        steps=(
            "Autolearn writes many small skills",
            "I merge them into 14 area skills",
            "Now I run autolearn by hand",
        ),
        highlight=2,
    ),
    Code(
        title="A lint script checks my 14 skills and found 0 errors.",
        shot=Shot(
            path=ASSETS + "skills-lint.png",
            label="14 skills, 0 errors",
            box=(0.0, 0.5, 0.88, 0.86),
            crop=(24, 40, 640, 206),
            cut=((84, 160),),
        ),
    ),
    Principle(
        number=2,
        title="Do it twice, make it a skill",
        line="Doing the same work more than twice makes it a candidate for a skill.",
    ),
    Compare(
        title="Skills hold how to do a thing, memory holds what I decided.",
        cards=(
            Card(heading="Skills", body="Steps to follow and facts to look up"),
            Card(heading="Memory", body="What I did, across projects"),
        ),
        cols=2,
        fill=True,
    ),
    Timeline(
        title="I tried three memory tools and kept Hindsight.",
        events=(
            Event(when="First", label="Mnemopi"),
            Event(when="Then", label="Hindsight, kept"),
            Event(when="Tried", label="Cognee, removed"),
        ),
        highlight=1,
    ),
    Stacks(
        title="My prompts are loose, because the files hold the structure.",
        stacks=(
            Stack(
                heading="Instruction layers",
                rows=(
                    Row(label="Global file", detail="Short, hard rules"),
                    Row(label="Rule files", detail="Small, loaded when they match"),
                    Row(label="Repo instructions", detail="The nearest file wins"),
                ),
            ),
        ),
        code=("Brief for subagents", "", "Target", "Change", "Contract"),
    ),
    Compare(
        title="My agent follows 25 principles, and one of them is mine.",
        cards=(
            Card(heading="poteto-mode", body="25 principles and 23 playbooks, ported to omp"),
            Card(heading="Check every layer", body="Product and the human walk, structure, data and flow"),
        ),
        cols=2,
        highlight=1,
        fill=True,
    ),
    Compare(
        title="I dropped beads because agents now keep context.",
        cards=(
            Card(heading="Beads, a task tracker", body="Hard for humans to read", muted=True),
            Card(heading="Now", body="GitHub issues and coordinator logs"),
        ),
        cols=2,
        highlight=1,
        fill=True,
    ),
    TryThis(title="Write the skill the third time you repeat a task."),
    # Part 3. One writer per branch, 37:00 to 48:00
    Divider(
        part=3,
        title="Many agents at once",
        question="How many agents do you run at once? Tell us in chat.",
    ),
    Flow(
        title="Idle agents never saw the messages sent to them.",
        steps=(
            "The coordinator sends a message to every agent",
            "Agents that went idle never wake up to read it",
            "Now each branch gets one owner agent that is running",
        ),
        highlight=2,
    ),
    Principle(
        number=3,
        title="One writer per branch",
        line="Many agents, many branches, and exactly one writer on each.",
    ),
    Hub(
        title="Every agent task gets its own copy of the repo.",
        center="One repo",
        spokes=(
            Spoke(label="Own folder, own branch"),
            Spoke(label="Own folder, own branch"),
            Spoke(label="Own folder, own branch"),
        ),
        caption="Tern makes each copy as a tab, and offers to remove it when the tab closes.",
    ),
    Compare(
        title="Mesh lets agents see what the others are holding.",
        cards=(
            Card(heading="ADDR agent", body="PR #580 passed review, waits for my go"),
            Card(heading="SEARCH agent", body="PR #579 merged, holds nothing"),
            Card(heading="SHIP coordinator", body="Staging green, production release waits for my go"),
        ),
        cols=3,
        highlight=2,
        fill=True,
        caption="19 agents online.",
    ),
    Compare(
        title="I wrote the mesh plugin myself, and it is running.",
        shot=Shot(
            path=ASSETS + "plugins.png",
            label="My mesh plugin, enabled",
            box=(0.0, 0.34, 0.98, 0.64),
            crop=(40, 84, 660, 185),
        ),
    ),
    Hub(
        title="One coordinator merges, after an independent review.",
        center="Coordinator",
        spokes=(
            Spoke(label="Worker, branch A"),
            Spoke(label="Worker, branch B"),
            Spoke(label="Worker, branch C"),
            Spoke(label="Worker, branch D"),
        ),
        caption="One writer per branch, merged one at a time.",
    ),
    TryThis(title="When you run two agents, give each its own worktree."),
    # Part 4. Show proof, not "done", 48:00 to 57:00
    Divider(
        part=4,
        title="Trusting the result",
        question="Which part of your agent's work do you still check by hand? Tell us in chat.",
    ),
    BeforeAfter(
        title="Remember the plane? This is the proof that came with that fix.",
        before=Shot(
            path=ASSETS + "pr804-draft-click-before.png",
            label="Before: click opens the edit modal",
            crop=(60, 65, 1000, 900),
            blur=(Blur(radius=14),),
        ),
        after=Shot(
            path=ASSETS + "pr804-draft-click-after.png",
            label="After: click only selects",
            crop=(60, 65, 1000, 900),
            blur=(Blur(radius=14),),
        ),
    ),
    BigNumbers(
        title="The test failed on the old code and passed with the fix.",
        items=(
            Stat(value="3 failed", label="on the old code", muted=True),
            Stat(value="3 passed", label="with the fix"),
        ),
        highlight=1,
        support="It used the same data that broke staging.",
    ),
    Principle(
        number=4,
        title="Show proof, not \"done\"",
        line="A PR is ready when it shows evidence, not when the agent says so.",
    ),
    Stacks(
        title="A second agent checks the work and freezes its verdict.",
        stacks=(
            Stack(
                heading="PASS with notes, frozen at one commit",
                rows=(
                    Row(label="Fails on main, passes on the PR"),
                    Row(label="Merges cleanly"),
                    Row(label="Types check"),
                    Row(label="Lint clean"),
                ),
            ),
        ),
        caption="A new commit gets a new review round.",
    ),
    Compare(
        title="The demo PR should carry its proof in the body.",
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
            blur=(Blur(radius=9, box=(0, 135, 1300, 10_000)),),
        ),
        demo=True,
    ),
    TryThis(title="Ask for a before and after clip in your next PR."),
    # Part 5. Make it safe to walk away, 57:00 to 64:00
    Divider(
        part=5,
        title="Running it safely",
        question="Where do your agents run: laptop, server or cloud? Tell us in chat.",
    ),
    Flow(
        title="Every production change goes dry run, backup, apply, then verify.",
        steps=("Dry run first", "Backup", "Apply, counts checked", "Verify the result"),
        highlight=0,
        caption="\"dry run first then show me what will be changed\"",
    ),
    Principle(
        number=5,
        title="Make it safe to walk away",
        line="A human can repeat every step, and secrets stay hidden.",
    ),
    Compare(
        title="Three layers protect my secrets.",
        cards=(
            Card(heading="Hidden values", body="The model sees placeholders"),
            Card(heading="Blocked commands", body="rm -rf, force push, DROP TABLE"),
            Card(heading="Secret managers", body="Infisical for machines, Bitwarden for humans"),
        ),
        cols=3,
        fill=True,
    ),
    Hub(
        title="Proof runs away from my workstation, and production is read-only.",
        center="Workstation",
        spokes=(
            Spoke(label="Mac, for review"),
            Spoke(label="Shared dev box"),
            Spoke(label="Batch box"),
            Spoke(label="Office staging"),
            Spoke(label="Production, read-only", dashed=True),
        ),
    ),
    Code(
        title="One command takes a fresh worktree to a running stack.",
        lines=("bun run bootstrap",),
        caption="Ports and database come from the branch name.",
    ),
    Timeline(
        title="Each terminal step removed one chore, and now I use Tern.",
        events=(
            Event(when="OpenChamber", label="Web UI for OpenCode"),
            Event(when="Ghostty", label="Windows and tabs"),
            Event(when="herdr", label="Worktrees and sessions"),
            Event(when="Paseo", label="Tried it, stopped it"),
            Event(when="Tern", label="With an Android app"),
        ),
        highlight=4,
    ),
    TryThis(title="Make every production change start with a dry run."),
    # What's still hard, 64:00 to 68:00
    Compare(
        title="A proof clip shows a button works, not that it looks right.",
        cards=(
            Card(heading="Clips prove", body="A button works"),
            Card(heading="I check by hand", body="Visual feel and UX"),
        ),
        cols=2,
        highlight=1,
        fill=True,
    ),
    BarChart(
        title="Setting up a worktree dropped from 652 s to 171 s.",
        bars=Bars(
            rows=(
                BarRow(label="Before the fix", values=(652,), texts=("652 s",)),
                BarRow(label="After the fix", values=(171,), texts=("171 s",)),
            ),
            highlight=1,
        ),
        caption="Every new worktree still pays 171 s.",
    ),
    BigNumbers(
        title="One test run used 38 GB, so a rule now caps memory.",
        items=(
            Stat(value="38 GB", label="peak of one uncapped test run"),
            Stat(value="15 GiB", label="free RAM needed before checks run"),
        ),
        highlight=0,
    ),
    # Close, 68:00 to 71:00
    Stacks(
        title="The model is a swappable part. The setup does the work.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="Measure it on your own work"),
                    Row(label="Do it twice, make it a skill"),
                    Row(label="One writer per branch"),
                    Row(label="Show proof, not \"done\""),
                    Row(label="Make it safe to walk away"),
                ),
            ),
        ),
    ),
    Stacks(
        title="Links for anyone who wants to dig deeper.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="omp", detail="github.com/can1357/oh-my-pi"),
                    Row(label="Prewalk article", detail="stencil.so/blog/prewalk"),
                    Row(label="Can Bölük on X", detail="x.com/_can1357/status/2021828033640911196"),
                    Row(label="My mesh plugin", detail="github.com/masrurimz/omp-agent-mesh"),
                    Row(label="My account router plugin", detail="github.com/masrurimz/omp-org-account-router"),
                ),
            ),
        ),
    ),
    Statement(
        title="Questions are welcome, in chat or out loud.",
        support="@masrurimz",
        extra="Thank you, SWE Growth. The slides link is in the chat.",
    ),
)

SLIDES: tuple[Slide, ...] = tuple(replace(s, n=i) for i, s in enumerate(DECK, 1))
