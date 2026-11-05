# Benchmarking My Coding Agent Setup: One Engineer, Many Agents

> **Status**: Sources in progress. Context, references, outlines, and prompts are being written. No slides generated yet.
> **Event**: SWE Growth community, online on Zoom. Organizer: Mas Zikrul. Date to be confirmed.
> **Duration**: 90 minutes. Rehearse to about 72 minutes of material.
> **Speaker**: Zahid
> **Language**: English slides

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails.

## Run of show

| Time | Section | Organizer questions |
|---|---|---|
| 0-5 | Cold open. The 9:29 phone screenshot, PR #804, QA warning at 08:52 and pass at 09:57 WIB. State the claim. | none |
| 5-15 | The journey. Tools and why each switch. What a harness is. Why omp. | 1 |
| 15-30 | Pillar 1, the benchmark lab. Value formula, my October 2026 bench, effort versus turns, prewalk, cost, subscription journey. Start the phone demo. | 2, 3, 11 |
| 30-45 | Pillar 2, knowledge. Skills, memory, autolearn, context, specs. | 5, 7, 8 |
| 45-65 | Pillar 3, the crew. Worktrees, mesh, SHIP coordinator, base-branch coordination (solved), review gates, proof. Check the demo PR. | 4, 6, 9 |
| 65-75 | Infra and guardrails. Remote servers, terminals, secrets, per-worktree setup, production dry run. | 10 |
| 75-82 | Open problems. UI, env and seeding, RAM on the shared box. | 12 |
| 82-90 | Close. Restate the claim, one action, quotes, Q&A. | none |

The live demo starts at about minute 15 and is checked at about minute 60. A recorded backup exists.

## Folder structure

```
.
├── README.md
├── sources/
│   ├── context/
│   │   ├── brief.md        # Event, speaker, audience, claim, goals, 12 questions mapped
│   │   └── structure.md    # Narrative arc, timings, boundaries, demo checkpoints, Q&A prep
│   ├── outlines/
│   │   ├── presenter.md    # Slide outline, presenter style
│   │   └── detailed.md     # Slide outline, detailed style
│   └── references/
│       ├── referensi-benchmark-lab.md
│       ├── referensi-evolusi-biaya-plugin.md
│       ├── referensi-setup-dan-infra.md
│       ├── referensi-skills-prompt-dan-config.md
│       ├── referensi-mesh-koordinator-mobile.md
│       ├── referensi-pr-proof-security-prod.md
│       └── screenshot-omp-mobile-0929.png
└── prompts/
    ├── generate-presenter.md
    ├── generate-detailed.md
    └── revise.md
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
- **Rehearsal.** Run the talk end to end and trim to about 72 minutes of material.
- **Clean output for slides.** Run the skills lint once and capture a clean result for the slide.

## Sources

Research digests in `sources/references/`:

- `referensi-benchmark-lab.md` covers Pillar 1, the core of the talk. The value formula, the October 2026 bench, effort versus turns, handoff arms, the Terminal-Bench caveat, the subscription portfolio (September 2026 versus now), prewalk with Can Bölük's receipts, and the harness-only quote. Prioritize it for Pillar 1.
- `referensi-evolusi-biaya-plugin.md` covers the tool journey, harness, plugins, terminal journey, model roles, cost, memory and beads.
- `referensi-setup-dan-infra.md` covers the agent setup, devkit idea, and machine map.
- `referensi-skills-prompt-dan-config.md` covers how instructions are organized, poteto-mode, area skills, and memory and autolearn config.
- `referensi-mesh-koordinator-mobile.md` covers the mesh, the coordinator session, and the PR #804 phone story.
- `referensi-pr-proof-security-prod.md` covers the PR standard and proof ladder, guardrails, secrets, and production dry runs.
- `screenshot-omp-mobile-0929.png` is the phone screenshot for the cold open.

Settled decisions and usage numbers come from the speaker's answers and from `omp stats` re-aggregated on 2026-11-05.
