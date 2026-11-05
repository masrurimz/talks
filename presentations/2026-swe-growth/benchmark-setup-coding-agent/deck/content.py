"""Deck content as typed data. One dataclass per layout, SLIDES in talk order.

Key points, speaker notes, timing and labels are not repeated here. build.py reads
them from sources/outlines/presenter.md by the outline slide number `n`. A slide added
after the outline has no `n` and carries its own `notes`.
"""

from __future__ import annotations

from dataclasses import dataclass, field

REFS = "sources/references/"


@dataclass(frozen=True, kw_only=True)
class Slide:
    title: str
    n: int | None = None
    source: str = ""
    notes: str = ""


@dataclass(frozen=True, kw_only=True)
class Title(Slide):
    subtitle: str = ""


@dataclass(frozen=True, kw_only=True)
class Divider(Slide):
    section: int = 0
    minute: int = 0
    ask_chat: str = ""


@dataclass(frozen=True, kw_only=True)
class Statement(Slide):
    support: str = ""


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
class Code(Slide):
    lines: tuple[str, ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class Image(Slide):
    path: str = ""
    caption: str = ""
    circles: tuple[tuple[int, int, int, int], ...] = ()


@dataclass(frozen=True, kw_only=True)
class Event:
    when: str
    label: str


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


@dataclass(frozen=True, kw_only=True)
class Spoke:
    label: str
    dashed: bool = False


@dataclass(frozen=True, kw_only=True)
class Hub(Slide):
    center: str = ""
    spokes: tuple[Spoke, ...] = ()
    strip: tuple[str, ...] = ()
    caption: str = ""


@dataclass(frozen=True, kw_only=True)
class Quote(Slide):
    lines: tuple[str, ...] = ()
    attribution: str = ""
    code: tuple[str, ...] = ()
    strip: tuple[str, ...] = ()


SLIDES: tuple[Slide, ...] = (
    # Section 1. Cold open
    Title(
        n=1,
        title="Benchmarking My Coding Agent Setup: One Engineer, Many Agents",
        subtitle="SWE Growth community, online. Zahid.",
    ),
    Image(
        n=2,
        title="An agent was reproducing a bug on a real stack from my phone at 9:29, before takeoff.",
        path=REFS + "screenshot-omp-mobile-0929.png",
        caption="Tuesday, 27 October 2026, WIB.",
        circles=((55, 38, 165, 94), (888, 2252, 992, 2352)),
        source="My phone, Tern Android app, 27 October 2026, 9:29 WIB. Serial numbers blurred.",
    ),
    Timeline(
        n=3,
        title="QA warned about PR #804 at 08:52 and passed it 65 minutes later, at 09:57.",
        events=(
            Event(when="08:52", label="QA warns on an approved PR"),
            Event(when="09:26", label="I paste the finding from my phone"),
            Event(when="09:29", label="Agent records the before clip"),
            Event(when="09:31", label="PR body updated"),
            Event(when="09:57", label="QA passes"),
        ),
        highlight=4,
        source="GinaV2 PR #804 timeline, 26 to 27 October 2026",
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
        strip=("Pillar 1, the engine, minute 15", "Pillar 2, knowledge, minute 30", "Pillar 3, the crew, minute 45"),
        source="Zahid, the claim of this talk",
    ),
    Quote(
        title="An outside engineer changed only the harness and improved 15 LLMs at coding in one afternoon.",
        lines=("\"I improved 15 LLMs at coding in one afternoon. Only the harness changed.\"",),
        attribution="Can Bölük, omp author, on X",
        source="x.com/_can1357/status/2021828033640911196",
        notes=(
            "Outside evidence for the claim on the previous slide.\n\n"
            "Say: This is the author of omp, not me. He changed only the harness and moved 15 models. "
            "That is the claim of this talk, from someone with no reason to flatter my setup.\n\n"
            "Before the talk: open the link once to confirm the wording. The digest did not re-fetch the post.\n\n"
            "Timing: 0.5 min. [Wajib]"
        ),
    ),
    # Section 2. The journey
    Divider(
        section=2,
        minute=5,
        title="Every tool switch had a reason, and omp stayed because I can extend it.",
        ask_chat="Which coding agent do you use today?",
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
    Timeline(
        n=6,
        title="Amp was my longest stay, and omp has been my main tool since March 2026.",
        events=(
            Event(when="July 2025", label="Gemini tooling on m5"),
            Event(when="2025-10-19", label="Claude Code"),
            Event(when="2025-10-20", label="OpenCode with oh-my-opencode, 215 sessions on m5"),
            Event(when="2025-12-22", label="Amp, until 2026-03-16"),
            Event(when="2026-02-23", label="omp on m5"),
            Event(when="2026-03-07", label="omp on x1, main since"),
        ),
        highlight=5,
        source="omp stats (~/.omp/stats.db) and session folders on my two machines, first session per tool",
    ),
    Table(
        n=7,
        title="Each switch had a reason about my workload and timing, not a verdict on the tool.",
        header=("Tool", "What I liked", "Why I left"),
        rows=(
            ("Antigravity", "Free usage, plan annotations, session artifacts", "Heavy, quality and limits, account ban"),
            ("Claude Code", "Where I started", "Some tasks not good enough, wanted more efficiency"),
            ("oh-my-opencode on OpenCode", "Pure CLI, then the OpenChamber web UI", "Many issues, subscription bans"),
            ("Amp", "Mature, cross-agent messages, spawn agents", "\"I forgot why I left Amp\""),
        ),
        highlight=3,
        widths=(0.27, 0.37, 0.36),
        source="My own account of each switch, 2026-11-05",
    ),
    Compare(
        n=8,
        title="I chose omp because I can extend it, and the later slides are plugins I wrote.",
        cards=(
            Card(heading="Plugins", body="I write my own"),
            Card(heading="Autolearn", body="Mints skills"),
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
        title="The benchmark lab: I pick models with a bench I built, not a feeling.",
        ask_chat="Do you pay per token or per subscription?",
    ),
    Code(
        n=9,
        title="I send one prompt from my phone, and the agent works while I keep talking.",
        lines=(
            "create new worktree, trace the impacted flow,",
            "fix, open a pr with proof in the body,",
            "coordinate with SHIP poteto",
        ),
        caption="Goal: a PR with proof in the body, checked at about minute 60.",
        source="Live demo from the Tern Android app, recorded backup ready",
    ),
    Table(
        n=10,
        title="I pick a model and an effort level once per role, not once per prompt.",
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
        n=11,
        title="A price per million tokens lies, because a subscription changes what a token costs.",
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
    Table(
        n=12,
        title="Every arm passed 126 of 126 checks, so only speed and cost separated the models.",
        header=("Setup", "UI", "Slot finder", "Cost per task, API-equivalent"),
        rows=(
            ("Opus 5.5 low", "92 s", "54 s", "$0.22 to $0.39"),
            ("Sonnet 5.5 medium", "94 s", "84 s", "$0.17 to $0.24"),
            ("Spark 1.3 low", "103 s", "71 s", "$0.08 to $0.15"),
            ("Haiku 5.5 medium", "170 s", "120 s", "$0.02 to $0.03"),
            ("Wonder 1.0 low", "136 s", "252 s", "$0.39 to $0.41"),
            ("DeepSeek v4.1 flash low", "476 s", "275 s", "$0.04 to $0.07"),
        ),
        highlight=0,
        widths=(0.34, 0.14, 0.2, 0.32),
        caption="Two easy tasks, three runs each, medians. Not a quality ranking.",
        source="My October 2026 bench, 2 tasks x 3 runs, medians",
    ),
    BarChart(
        n=13,
        title="Raising effort raised the turn count in every head-to-head pair I measured.",
        bars=Bars(
            rows=(
                BarRow(label="Haiku, slot finder", values=(12, 16), texts=("12 turns, lower effort", "16 turns, higher effort")),
                BarRow(label="Spark, slot finder", values=(9, 23), texts=("9", "23")),
                BarRow(label="Sonnet, UI", values=(7, 10), texts=("7", "10")),
                BarRow(label="DeepSeek, UI", values=(28, 40), texts=("28", "40")),
            ),
            highlight=1,
        ),
        caption="Low for execution, high for plans and hard debugging, medium for review, max almost never.",
        source="My October 2026 bench, 2 tasks x 3 runs, medians",
    ),
    Table(
        n=14,
        title="A handoff costs extra on short tasks and pays off on long sessions, where reading is the cost.",
        header=("Setup", "Short bench tasks", "Long sessions, estimate"),
        rows=(
            ("Sonnet medium alone", "$0.17 to $0.24", "$2.58"),
            ("Sonnet medium to Haiku medium", "$0.17 to $0.36", "$1.63"),
            ("Opus low alone", "$0.22 to $0.39", "n/a"),
            ("Opus low to Sonnet medium", "$0.35 to $0.48", "n/a"),
        ),
        highlight=1,
        widths=(0.42, 0.29, 0.29),
        caption="Costs are API-equivalent. Long sessions are log estimates, not graded.",
        source="My October 2026 bench, handoff arms, plus estimates from session logs",
    ),
    Compare(
        n=15,
        title="Prewalk hands off to a cheaper model after planning, and I turned it off.",
        cards=(
            Card(
                heading="Can Bölük, omp author",
                body="\"Opus reading things costs money.\" \"Hand off a trajectory, not a fairytale.\"",
            ),
            Card(
                heading="His SWE-Bench Pro receipts",
                body=(
                    "Sol prewalk into Luna: 85%, $1.04, 300 s. Sol alone: 88%, $1.71, 372 s. "
                    "Opus 4.8 prewalk into Flash: 78%, $1.46. Opus alone: 85%, $2.78."
                ),
            ),
            Card(
                heading="Zahid, prewalk, off now",
                body="It took extra time on some tasks. Haiku was too expensive as the target. DeepSeek was too slow.",
            ),
        ),
        cols=3,
        highlight=2,
        source="stencil.so/blog/prewalk (Can Bölük); omp docs; my own use of prewalk",
    ),
    BigNumbers(
        n=16,
        title="I paid about $200 for October work that prices at $7.3k API-equivalent.",
        items=(
            Stat(value="$7.3k", label="API-equivalent list price, October 2026"),
            Stat(value="about $200", label="what I paid"),
            Stat(value="36x", label="roughly less than the API-equivalent"),
        ),
        highlight=1,
        bars=Bars(
            rows=(
                BarRow(label="Mar", values=(36,), texts=("36k",)),
                BarRow(label="Apr", values=(0.8,), texts=("0.8k",)),
                BarRow(label="May", values=(2.2,), texts=("2.2k",)),
                BarRow(label="Jun", values=(23,), texts=("23k",)),
                BarRow(label="Jul", values=(46,), texts=("46k",)),
                BarRow(label="Aug", values=(174,), texts=("174k",)),
                BarRow(label="Sep", values=(235,), texts=("235k",)),
                BarRow(label="Oct", values=(270,), texts=("270k",)),
                BarRow(label="Nov 1 to 5", values=(47,), texts=("47k",)),
            ),
            highlight=7,
            vertical=True,
        ),
        support="Requests per month.",
        source="omp stats (~/.omp/stats.db), re-aggregated 2026-11-05, API-equivalent",
    ),
    Compare(
        n=17,
        title="When Claude 5.5 arrived I went all in, and my plan list changed.",
        cards=(
            Card(
                heading="September 2026",
                body=(
                    "GLM Max, own. Codex Pro, office. Devin Pro, own. OpenCode Go, own. "
                    "Default model GLM-5.3."
                ),
            ),
            Card(heading="Now", body="2x Claude Max and OpenCode Go. \"Claude 5.5 series quality is GOAT.\""),
        ),
        cols=2,
        highlight=1,
        source="My subscription portfolio, verified 2026-09-14; omp stats by provider, 2026-11-05",
    ),
    # Section 4. Pillar 2
    Divider(
        section=4,
        minute=30,
        title="Knowledge: skills hold how to do a thing, and memory holds what I decided.",
        ask_chat="Which task do you repeat with your agent more than twice?",
    ),
    Compare(
        n=18,
        title="Skills hold how to do a thing, and memory holds what I did and decided.",
        cards=(
            Card(heading="Skills and references", body="Today I learned, and reusable knowledge"),
            Card(heading="Memory", body="What you do cross-project"),
        ),
        cols=2,
        lead="\"Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project.\"",
        source="Zahid, 2026-11-05",
    ),
    Quote(
        n=19,
        title="Doing the same work more than twice makes it a candidate for a skill.",
        lines=("\"When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you.\"",),
        attribution="Zahid, the one action to take home",
        code=("SKILL.md", "playbooks/", "references/"),
        source="Zahid, 2026-11-05",
    ),
    Code(
        n=20,
        title="I keep 14 area skills, one folder per domain, and a lint script checks the layout.",
        lines=(
            "managed-skills/",
            "  infra-ops/",
            "    SKILL.md        router only",
            "    playbooks/      step lists to follow",
            "    references/     facts to look up",
            "  groundup-ops/  alkhidmah-ops/  git-pr-workflow/  omp-ops/ ...",
        ),
        caption="A pre-commit hook runs the lint and it exits 1 on errors.",
        source="My managed skills folder (~/.omp/agent/managed-skills), 14 area skills and a lint script",
    ),
    Flow(
        n=21,
        title="Autolearn minted too many skills, so I consolidated them and now trigger it by hand.",
        steps=("Autolearn on: many small skills", "14 domain skills plus a lint", "Manual trigger after a session that taught something"),
        highlight=2,
        code=("autolearn: { enabled: true, autoContinue: false }",),
        source="~/.omp/agent/config.yml (autolearn); my own account, 2026-11-05",
    ),
    Timeline(
        n=22,
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
        n=23,
        title="Compaction tries three methods in order, so I do not watch the context window.",
        steps=("snapcompact", "remote", "soft"),
        highlight=0,
        caption="It starts at 70% of the context window, and compacts when idle after 60 seconds.",
        source="~/.omp/agent/config.yml (compaction)",
    ),
    Stacks(
        n=24,
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
        n=25,
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
        minute=45,
        title="The crew: parallel agents stay safe because of worktrees, mesh and one coordinator.",
        ask_chat="How many agents do you run at once?",
    ),
    Code(
        n=26,
        title="Every task gets its own worktree, and one CLI is the only way to make it.",
        lines=(
            "tern-wt list --all",
            "",
            "one JSON object, stable error codes",
            "example: dirty_worktree",
        ),
        caption="Rule: use tern-wt, not git worktree.",
        source="tern-worktrees plugin and its skill, ~/work/labs/tern-worktrees",
    ),
    Compare(
        n=27,
        title="When something hurts I write a plugin, and mesh is the biggest one.",
        cards=(
            Card(heading="omp-agent-mesh", body="My Effect-based engine. Parallel agents see each other."),
            Card(heading="omp-org-account-router", body="Office account for office repos, personal for personal"),
            Card(heading="tern-worktrees", body="Branch picker, CLI and a skill"),
            Card(heading="poteto-mode", body="Autoloads the skill once per context"),
            Card(heading="paseo-omp", body="237 commits, September to October 2026"),
            Card(heading="opencode-go-multi-auth", body="Multi-account auth"),
            Card(heading="herdr state hooks", body="Hooks into herdr"),
            Card(heading="muse-sub", body="Retired 2026-10-10", muted=True),
        ),
        cols=3,
        highlight=0,
        source="omp plugin lockfile (~/.omp/plugins/omp-plugins.lock.json) and my plugin repos",
    ),
    Code(
        n=28,
        title="Mesh stops two agents from running the same heavy job or editing the same file.",
        lines=(
            "Other omp agents may be running in other sessions.",
            "Run the mesh tool with action peers before work",
            "that touches shared resources.",
            "",
            "actions: peers, note, send, broadcast, claim, release",
        ),
        caption="The shared event log had 10,083 lines on 2026-11-05. 101 session files used the tool.",
        source="~/.omp/agent/AGENTS.md (mesh rule); mesh event log, 2026-11-05",
    ),
    Quote(
        n=29,
        title="Idle sessions never see a mesh message, so each branch needs exactly one writer.",
        lines=(
            "started fresh owners for #488 ... because their sessions had ended and never saw the broadcast",
            "idle sessions don't wake on mesh messages; each branch needs one writer",
        ),
        attribution="SHIP ledger, 2026-11-02",
        source="SHIP coordinator ledger, 2026-11-02",
    ),
    Compare(
        n=30,
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
        n=31,
        title="Check-every-layer forces the agent to look at the layers it would otherwise skip.",
        stacks=(
            Stack(
                heading="",
                rows=(
                    Row(label="Product and the human walk", detail="Findings, or one line on why it does not apply"),
                    Row(label="Structure", detail="Findings, or one line on why it does not apply"),
                    Row(label="Data and flow", detail="Findings, or one line on why it does not apply"),
                ),
            ),
        ),
        source="principle-check-every-layer, my own principle added to poteto-mode",
    ),
    Flow(
        n=32,
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
        caption="Ledger columns: ts, phase, decision, why, evidence, result.",
        source="SHIP coordinator ledger, 276 lines, 2026-11-03",
    ),
    Hub(
        n=33,
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
        n=34,
        title="The reviewer freezes a verdict at one commit and proves it through gates.",
        header=("Gate", "What it checks"),
        rows=(
            ("verify.ts", "PROVEN: red on master, green on head, desktop 1280 and mobile 390"),
            ("merge-tree", "Clean"),
            ("check-types, architecture lint", "Run as gates"),
            ("Unit and e2e", "On a throwaway database, removed after"),
        ),
        highlight=0,
        widths=(0.36, 0.64),
        caption="Frozen verdict: PASS+NOTES at head 592b92ae9.",
        source="Coordinator review report for PR #580, 2026-11-05",
    ),
    Compare(
        n=35,
        title="The PR from my phone should show Why, proof and an honest Not verified.",
        cards=(
            Card(heading="Why", body="Does the body say why?"),
            Card(heading="Proof", body="The recording or screenshots the agent attached"),
            Card(heading="Not verified", body="An honest list, or none"),
        ),
        cols=3,
        source="Live PR from the demo, recorded backup ready",
    ),
    Stacks(
        n=36,
        title="A PR body is a briefing, and each claim gets the first proof rung that shows it.",
        stacks=(
            Stack(
                heading="PR body sections",
                rows=(
                    Row(label="Why"),
                    Row(label="How"),
                    Row(label="What changed"),
                    Row(label="Scope"),
                    Row(label="Tradeoffs"),
                    Row(label="Blast Radius"),
                    Row(label="Verification"),
                ),
                highlight=6,
            ),
            Stack(
                heading="Proof ladder",
                rows=(
                    Row(label="Recording", detail="Visible behavior, before and after for a bug"),
                    Row(label="Command and real output", detail="API or CLI"),
                    Row(label="Run link", detail="CI"),
                    Row(label="Test command and result", detail="Nothing visible"),
                ),
            ),
        ),
        source="My PR body template (pr-body-shape, git-pr-workflow skill)",
    ),
    # Section 6. Infra and guardrails
    Divider(
        section=6,
        minute=65,
        title="Infra and guardrails: proof runs away from the workstation, and production stays read-only.",
    ),
    Hub(
        n=37,
        title="Agents run on one workstation, and proof runs on other machines.",
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
        n=38,
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
        n=39,
        title="One command takes a fresh worktree to a running stack.",
        lines=("From a fresh clone (or a fresh worktree):", "bun run bootstrap"),
        caption="Ports and database tier come from arithmetic on the branch slug.",
        source="alkhidmah devkit README, bun run bootstrap",
    ),
    Compare(
        n=40,
        title="Three layers protect secrets: hidden values, blocked commands and managed storage.",
        cards=(
            Card(heading="Obfuscation", body="The model sees placeholders, not values"),
            Card(
                heading="Damage control",
                body="Blocks rm -rf, git reset --hard, force push, DROP TABLE. ~/.ssh/ is zero access. .env is read-only.",
            ),
            Card(heading="Secret managers", body="Infisical for machines, Bitwarden for humans. Never print them."),
        ),
        cols=3,
        source="~/dotfiles/omp/agent/damage-control-rules.yaml; ~/.omp/agent/config.yml (secrets)",
    ),
    Flow(
        n=41,
        title="Every production write goes dry run, backup, guarded apply, then verify.",
        steps=("Dry run, real update rolled back", "Backup", "Apply with expected counts", "Verify the running version"),
        highlight=0,
        caption="\"dry run first then show me what will be changed\"",
        source="My groundup-ops dry-run runbook; my prompt of 2026-11-05",
    ),
    # Section 7. Open problems
    Divider(
        section=7,
        minute=75,
        title="Open problems: agent UI, per-worktree seeding and shared RAM are still unsolved.",
        ask_chat="Which part of your agent's work do you still check by hand?",
    ),
    Compare(
        n=42,
        title="Proof clips show that a button works, but not that the screen looks right.",
        cards=(
            Card(heading="Proof clips show", body="A button works"),
            Card(heading="I still check by hand", body="UI and visual feel, and UX"),
        ),
        cols=2,
        highlight=1,
        source="Zahid, what I still check by hand",
    ),
    BarChart(
        n=43,
        title="One fix cut the per-worktree seed from 652 s to 171 s, and 171 s is still too slow.",
        bars=Bars(
            rows=(
                BarRow(label="Before the fix", values=(652,), texts=("652 s",)),
                BarRow(label="After the fix", values=(171,), texts=("171 s",)),
            ),
            highlight=1,
        ),
        caption="Still 171 s per worktree.",
        source="My own timing of the per-worktree seed, before and after one fix",
    ),
    BigNumbers(
        n=44,
        title="An uncapped test run reached 38 GB, so a rule now caps memory when test commands appear.",
        items=(
            Stat(value="38 GB", label="reached by one uncapped test run"),
            Stat(value="15 GiB", label="free RAM the verify script requires"),
        ),
        highlight=0,
        support="A rule fires on the command and tells the agent to cap memory first.",
        source="Memory-cap rule in ~/.omp/agent/rules; verify script threshold; my shared workstation",
    ),
    # Section 8. Close and Q&A
    Divider(
        section=8,
        minute=82,
        title="Close: the model is swappable, and the setup around it is what ships.",
    ),
    Quote(
        n=45,
        title="Skills, proof, coordination and guardrails are the setup around a swappable model.",
        lines=("\"When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you.\"",),
        attribution="One action for Monday",
        strip=("Skills", "Proof", "Coordination", "Guardrails"),
        source="Zahid, 2026-11-05",
    ),
    Compare(
        n=46,
        title="Four lines from this talk carry the whole setup.",
        cards=(
            Card(heading="On knowledge", body="\"Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project.\""),
            Card(heading="The 9:29 prompt", body="\"Fix those own changes proof and update pr.\""),
            Card(heading="On mesh", body="\"idle sessions don't wake on mesh messages; each branch needs one writer.\""),
            Card(heading="On deploys", body="\"A deploy is done only when the running version is verified, not when the job is green.\""),
        ),
        cols=2,
        source="Zahid; SHIP coordinator ledger, 2026-11-02; infra-ops hard rules; PR #804 prompt, 2026-10-27",
    ),
    Statement(
        n=47,
        title="Questions are welcome in chat or aloud, and one small skill is a good place to start.",
        support="Thank you, SWE Growth.",
    ),
)
