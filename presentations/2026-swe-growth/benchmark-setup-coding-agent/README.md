# Benchmarking My Coding Agent Setup: One Engineer, Many Agents

> **Status**: The v2 deck is built. 60 slides, lint clean. Speaker notes are in `sources/outlines/presenter.md`.
> **Event**: SWE Growth community, online on Zoom. Organizer: Mas Zikrul. Date to be confirmed.
> **Duration**: 90 minutes. 71 minutes of talking, 19 for Q&A and slack.
> **Speaker**: Zahid
> **Language**: English slides

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails.

## Run of show

71 minutes of talking, then Q&A and slack from 71:00 to about 90:00. The deck has 60 numbered slides, and dividers are numbered slides.

| Clock | Section | Slides | Organizer topics |
|---|---|---|---|
| 0-5 | Opening. The 9:29 phone screenshot, PR #804 with QA at 08:52 and 09:57 WIB, the claim, and Can Bölük's quote. | 1 to 5 | none |
| 5-12 | My journey. Tools and why each switch, what a harness is, why omp, from one chat to many agents. The live demo starts at slide 10. | 6 to 10 | 1 |
| 12-26 | Part 1. Choosing models and paying for them. Principle: Measure it on your own work. | 11 to 21 | 2, 3, 11 |
| 26-37 | Part 2. Teaching the agent. Principle: Do it twice, make it a skill. | 22 to 31 | 5, 7, 8 |
| 37-48 | Part 3. Many agents at once. Principle: One writer per branch. | 32 to 39 | 4 |
| 48-57 | Part 4. Trusting the result. Principle: Show proof, not "done". The demo check is slide 45. | 40 to 46 | 9 |
| 57-64 | Part 5. Running it safely. Principle: Make it safe to walk away. | 47 to 54 | 6, 10 |
| 64-68 | What's still hard. A screen a clip cannot judge, worktree setup time, RAM. | 55 to 57 | 12 |
| 68-71 | Close. The five principles, links, questions. | 58 to 60 | none |

The live demo starts at slide 10 (clock 10:30) and is checked at slide 45 (clock 54:30). A recorded backup exists and is never named on a slide.

## How the deck is made

`deck/content.py` holds the slide data. `sources/outlines/presenter.md` holds the speaker notes, one section per slide with `Say:` and `Evidence:`. Slides speak only to the audience, and all sources, dates and caveats live in the notes.

- `deck/build.py --render` builds the slides, runs the lint and renders pages to `/tmp/deck-render/`. Run it from `/home/zahid/work/talks` with `uv run python3 presentations/2026-swe-growth/benchmark-setup-coding-agent/deck/build.py --render`.
- `deck/publish.py` updates the same Google Slides file. Edits made directly in Slides are lost on the next publish, so change `content.py` or `presenter.md` and rebuild.
- `prompts/` and `sources/outlines/detailed.md` are kept for a NotebookLM comparison test. They follow the same v2 rules as the deck, but the deck does not use them.

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
│   │   └── detailed.md     # Self-reading v2 outline, for the NotebookLM comparison test
│   └── references/
│       ├── referensi-benchmark-lab.md
│       ├── referensi-evolusi-biaya-plugin.md
│       ├── referensi-setup-dan-infra.md
│       ├── referensi-skills-prompt-dan-config.md
│       ├── referensi-mesh-koordinator-mobile.md
│       ├── referensi-pr-proof-security-prod.md
│       └── screenshot-omp-mobile-0929.png
└── prompts/                # NotebookLM prompts, v2 rules, for the comparison test
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
- **Rehearsal.** Run the talk end to end against the 71-minute plan.

## Sources

Research digests in `sources/references/`:

- `referensi-benchmark-lab.md` covers Part 1, the core of the talk. The value formula, the October 2026 bench, effort versus steps, handoff arms, the Terminal-Bench caveat, the subscription portfolio (September 2026 versus now), prewalk (Can Bölük's own numbers with his models, and Zahid's own bench and timeline), and the harness-only quote.
- `referensi-evolusi-biaya-plugin.md` covers the tool journey, harness, plugins, terminal journey, model roles, cost, memory and beads.
- `referensi-setup-dan-infra.md` covers the agent setup, devkit idea, and machine map.
- `referensi-skills-prompt-dan-config.md` covers how instructions are organized, poteto-mode, area skills, and memory and autolearn config.
- `referensi-mesh-koordinator-mobile.md` covers the mesh, the coordinator session, and the PR #804 phone story.
- `referensi-pr-proof-security-prod.md` covers the PR standard and proof ladder, guardrails, secrets, and production dry runs.
- `screenshot-omp-mobile-0929.png` is the phone screenshot for the opening.

Settled decisions and usage numbers come from the speaker's answers and from `omp stats` re-aggregated on 2026-11-05.
