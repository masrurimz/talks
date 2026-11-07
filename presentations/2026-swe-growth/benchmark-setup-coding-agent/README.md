# Benchmarking My Coding Agent Setup: One Engineer, Many Agents

> **Status**: The v4 deck is built. 73 slides, lint clean. Speaker notes are in `sources/outlines/presenter.md`. All 12 organizer questions are answered on slides.
> **Event**: SWE Growth community, online on Zoom. Organizer: Mas Zikrul. Date to be confirmed.
> **Duration**: 90 minutes. 86 minutes of talking, 4 for Q&A.
> **Speaker**: Zahid
> **Language**: English slides

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails.

## Run of show

86 minutes of talking, then Q&A from 86:00 to about 90:00. The deck has 73 numbered slides, and dividers are numbered slides.

| Clock | Section | Slides | Organizer topics |
|---|---|---|---|
| 0-6 | Opening. The 9:29 phone screenshot, PR #804 with QA at 08:52 and 09:57 WIB, the claim, Can Bölük's quote, and the map of the talk. | 1 to 6 | none |
| 6-15 | My journey. A six-event timeline (Copilot in VS Code, Claude Code in VS Code, Gemini, OpenCode, Ghostty with Neovim and Amp, omp), why parallel agents moved me from the editor to the terminal, Antigravity, what a harness is, why omp, from one chat to many agents. The live demo starts at slide 13. | 7 to 13 | 1 |
| 15-30 | Part 1. Choosing models and paying for them. Principle: Measure it on your own work. Ends with three money tips. | 14 to 25 | 2, 3, 11 |
| 30-45 | Part 2. Teaching the agent. Principle: Do it twice, make it a skill. Includes the PARA skills slide, the rules that step in on risky commands (slide 34) and the wireframe-first spec flow. | 26 to 38 | 5, 7, 8 |
| 45-57 | Part 3. Many agents at once. Principle: One writer per branch. Slide 40 is the busy hour, 4 to 9 agents at once. | 39 to 47 | 4, 6 |
| 57-67.5 | Part 4. Trusting the result. Principle: Show proof, not "done". The five checks are slide 52 and the demo check is slide 54. | 48 to 55 | 9 |
| 67.5-76 | Part 5. Running it safely. Principle: Make it safe to walk away. Includes three accidents and their guardrails. | 56 to 64 | 6, 10 |
| 76-83 | What is still hard. A divider, then a screen a clip cannot judge, CI as the queue, worktree env and seed setup time, a full disk, and a pause and wake plan. | 65 to 70 | 12 |
| 83-86 | Close. The five principles, links, questions. | 71 to 73 | none |

The live demo starts at slide 13 (clock 13:30) and is checked at slide 54 (clock 65:00). A recorded backup exists and is never named on a slide. Slide 6 is a seven-row map of the talk. The same list draws a small strip at the bottom of every divider.

## How the deck is made

`deck/content.py` holds the slide data. `sources/outlines/presenter.md` holds the speaker notes, one section per slide with `Say:` and `Evidence:`. Slides speak only to the audience, and all sources, dates and caveats live in the notes.

- `deck/build.py --render` builds the slides, runs the lint and renders pages to `/tmp/deck-render/`. Run it from `/home/zahid/work/talks` with `uv run python3 presentations/2026-swe-growth/benchmark-setup-coding-agent/deck/build.py --render`.
- `deck/publish.py` updates the same Google Slides file. Edits made directly in Slides are lost on the next publish, so change `content.py` or `presenter.md` and rebuild.
- `prompts/` and `sources/outlines/detailed.md` are kept for a NotebookLM comparison test. They follow the same v4 story and rules as the deck, but the deck does not use them. The presenter prompts follow the 73-slide outline and the detailed outline has 47 slides.

## Folder structure

```
.
├── README.md
├── speaker-guide.md        # Delivery plan: scripts, rehearsal, Zoom, demo, Q&A
├── deck/
│   ├── content.py          # Slide data
│   ├── build.py            # Build, lint, render
│   ├── publish.py          # Updates the Google Slides file
│   └── assets/             # Screenshots and captures used on slides
├── sources/
│   ├── context/
│   │   ├── brief.md        # Event, speaker, audience, claim, goals, 12 questions mapped
│   │   └── structure.md    # Arc, principles, timings, content boundaries, demo checkpoints, Q&A prep
│   ├── outlines/
│   │   ├── presenter.md    # Speaker notes by slide number
│   │   └── detailed.md     # Self-reading v4 outline, 47 slides, for the NotebookLM comparison test
│   └── references/
│       ├── referensi-benchmark-lab.md
│       ├── referensi-evolusi-biaya-plugin.md
│       ├── referensi-setup-dan-infra.md
│       ├── referensi-skills-prompt-dan-config.md
│       ├── referensi-mesh-koordinator-mobile.md
│       ├── referensi-pr-proof-security-prod.md
│       └── screenshot-omp-mobile-0929.png
└── prompts/                # NotebookLM prompts, v4 rules, for the comparison test
```

## NotebookLM workflow

1. Upload every file in `sources/` to NotebookLM.
2. Paste one prompt from `prompts/`, either `generate-presenter.md` or `generate-detailed.md`.
3. Save the generated slides to `output/`.
4. For changes, paste `prompts/revise.md`.

The AI assistant prepares the materials. Zahid runs NotebookLM.

## Open items

- **Event date.** Ask Mas Zikrul for the date and the exact Zoom time slot.
- **Demo issue.** Pick one small real issue from the Alkhidmah backlog before the talk, with its worktree and stack ready.
- **Phone screen on Zoom.** Test screen mirroring of the Tern Android app next to the laptop, since the audience is online.
- **Recorded backup.** Record a full demo run to play if the live one fails.
- **Rehearsal.** Run the talk end to end against the 86-minute plan, with Q&A held to 4 minutes.

## Sources

Research digests in `sources/references/`:

- `referensi-benchmark-lab.md` covers Part 1, the core of the talk. The value formula, the October 2026 bench, effort versus steps, handoff arms, the Terminal-Bench caveat, the subscription portfolio (September 2026 versus now), prewalk (Can Bölük's own numbers with his models, and Zahid's own bench and timeline), and the harness-only quote.
- `referensi-evolusi-biaya-plugin.md` covers the tool journey in the order Zahid gave (Copilot, Claude Code in VS Code, Gemini, OpenCode, Ghostty with Neovim and Amp, omp), the parallel-agents reason for leaving the editor, the busy-hour agent count, plus harness, plugins, terminal journey, model roles, cost, memory and beads.
- `referensi-setup-dan-infra.md` covers the agent setup, devkit idea, machine map, and the open infra problems (CI queue, disk, pause and wake plan).
- `referensi-skills-prompt-dan-config.md` covers how instructions are organized, rules and TTSR, poteto-mode, area skills, and memory and autolearn config.
- `referensi-mesh-koordinator-mobile.md` covers the mesh, the coordinator session, and the PR #804 phone story.
- `referensi-pr-proof-security-prod.md` covers the PR standard and proof ladder, guardrails, secrets, and production dry runs.
- `screenshot-omp-mobile-0929.png` is the phone screenshot for the opening.

Settled decisions and usage numbers come from the speaker's answers and from `omp stats` re-aggregated on 2026-11-05.
