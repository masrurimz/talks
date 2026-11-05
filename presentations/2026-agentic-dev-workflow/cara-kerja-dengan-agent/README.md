# One engineer, many agents: how I ship with omp

> **Status**: Proposal (brainstorm phase)
> **Duration**: 90 minutes
> **Speaker**: Zahid
> **Event, audience, language**: open, see "Open decisions"

## Promise to the audience

By the end, people have seen one real bug go from a QA report to a proven PR from a phone in 65 minutes. They also see the setup, the habits, and the guardrails that make that repeatable, and they leave with five practices they can copy on Monday.

## Run of show

| # | Time | Segment | Your items | What is on screen |
|---|---|---|---|---|
| 0 | 0:00–0:05 | Cold open. The 9:29 screenshot | 8 (teaser) | Phone screenshot, then the PR #804 QA thread: warning at 08:52, pass at 09:57 |
| 1 | 0:05–0:17 | My setup, the map | 1, 11 | Machine map (x1-dev, m5, groundup-dev, groundup-alif, office staging, GCP), Tern with the tern-worktrees plugin, omp model roles, usage numbers |
| 2 | 0:17–0:22 | Start the live demo and leave it running | 5 | Pick a real small issue, `tern-wt create`, one raw prompt ending in "poteto" |
| 3 | 0:22–0:40 | How I organize and prompt | 2, 3 | Instruction layers, rules that fire on a regex, poteto principles, the 14 area skills, skills lint, memory and autolearn config |
| 4 | 0:40–0:48 | Making repos easy for agents | 10 | `bun run bootstrap`, `alkhidmah worktrees`, GinaV2 `develop.sh` and the shared env model |
| 5 | 0:48–1:03 | Many agents at once | 4, 7 | `mesh peers` live, the SHIP ledger, one review report with a frozen verdict |
| 6 | 1:03–1:08 | On the go | 8 | The full PR #804 story with the timeline |
| 7 | 1:08–1:15 | Back to the demo: the PR and its proof | 5, 9 | The demo PR body next to `pr-body-shape`, the proof ladder, #804 as the reference PR |
| 8 | 1:15–1:22 | Guardrails: secrets and production | 6, 12 | damage-control rules, obfuscation vs secret management, the 7-step dry-run runbook |
| 9 | 1:22–1:30 | Five takeaways, Q&A | | A starter kit slide |

## Why this order

- The phone story opens the talk because it is the payoff, and it makes everyone ask "how". The rest of the talk answers that.
- The demo starts at minute 17 and gets checked at minute 68. While it runs you talk about everything else, which is exactly how you work. Seeing an agent finish while you were talking proves more than any slide.
- Items 9 (PR standard) and 5 (demo) share segment 7, so the PR standard is shown on a fresh PR instead of described.
- Guardrails come late but get a teaser in segment 1. Engineers will ask about safety early, so answer "it is coming" and show the damage-control file once.

## Segment notes

**0. Cold open.** Show the screenshot. Read the two commit lines on it. Then show the QA comments on PR #804: warning at 08:52 WIB, pass at 09:57 WIB. Say the flight was booked for 09:00 that morning. Stop there, the details come in segment 6.

**1. Setup.** One diagram of the machines and what runs where. omp as the agent, Tern as the terminal, the tern-worktrees plugin you wrote (`cmd+shift+w` opens a worktree as a tab), herdr for GinaV2 panes. Model roles from `config.yml` (default, plan, reviewer, task, fast) and the usage-aware fallback. Numbers: 9,817 sessions, 682k model requests, about 116B tokens since March 2026. The $19.9k figure is API-equivalent price, not spend, so say that or skip it. The date-tagged `config.yml.bak-*` files tell how the setup changed month by month.

**2. Demo kickoff.** Have the issue and the stack ready before the talk. Type the prompt the way you normally do, typos and all. Do not explain yet.

**3. Organize and prompt.** Four layers of instructions: global `AGENTS.md` hard rules, `~/.omp/agent/rules` (always-on and regex-triggered; the pytest cap fired during this research), repo `AGENTS.md` where the nearest file wins and size budgets are checked, and skills. Real prompts on a slide: "dry run first then show me what will be changed", "go stack and ship all include proof also in pr". Then the principles: poteto-mode (forked from poteto's pstack, MIT) with your own `principle-check-every-layer`. Then why skills are split per domain: one router per area, playbooks are steps, references are facts, the lint enforces it. Config: memory on (Hindsight backend), autolearn on, auto-injected skills off.

**4. Repos made for agents.** The rule is one command from a fresh worktree to a running, seeded stack, with ports and databases isolated per worktree. Show the alkhidmah devkit tiers and `alkhidmah worktrees`. Show the GinaV2 shared `.env` symlink and `${USER}-ginav2` compose projects on groundup-dev.

**5. Many agents.** Why mesh exists: many sessions share one machine, its ports, Docker and checkouts. Show `mesh peers` live. Then the coordinator: a normal omp session that owns merging. Workers send `MERGE-READY #<pr> <sha>`, freeze the head, and get one fix round. An independent reviewer writes a report. Show one row of `coord/2026-11-03-ship.tsv` and the gates table in `coord/2026-11-05-review-580.md`.

**6. On the go.** The full timeline of PR #804: the QA report pasted from WhatsApp, the fix reproduced on groundup-dev, before and after recordings, the PR body updated, QA told to `gh pr checkout 804` instead of waiting for staging, QA pass. All of it ran on the dev servers, and the phone only sent the prompts and voice input.

**7. PR and proof.** Open the demo PR. Walk the sections: Why, How, What changed, Scope, Tradeoffs, Blast Radius, Verification ending with "Not verified:". The proof ladder: a recording for UI, the command output for an API or CLI, the run link for CI, the test command when nothing is visible. Alkhidmah goes one step further: `verify.ts` must fail on master and pass on the branch.

**8. Guardrails.** damage-control blocks `rm -rf`, `git reset --hard`, force push, `DROP`, and reads of `~/.ssh`. Secret obfuscation replaces values with placeholders, but it does not manage secrets, so machines use Infisical and people use Bitwarden. Production is read-only by default. Every write script runs as a dry run first, then a backup, then `--apply` with expected counts, then a verify step. The dry-run output becomes the runbook a human can follow.

**9. Takeaways.**
1. Make the repo bootable by an agent in one command.
2. Put each lesson in a skill for its domain, and lint the skills.
3. Ask for proof, not "done". Red before, green after.
4. One coordinator, one writer per branch, independent review.
5. Dry-run anything that touches production, and keep the output as a runbook.

## Open decisions

- Event and audience: internal GroundUp engineers, the Alkhidmah dev team, or a public meetup? This decides the depth and whether customer names can stay on the slides.
- Language: the repo default is Indonesian. Slides in Indonesian with English terms, or fully English?
- Which phone app is in the screenshot (Tern web, Paseo, or another)? It is not visible in the image.
- The flight was booked for 09:00 and the fix ran 09:27–09:31. Was the flight delayed, or were you at the gate?
- "poteto validate": no command by that name exists on disk. Proof comes from poteto-mode's "Prove It Works" principle plus `pr-body-shape`. Confirm that is what you meant.
- Live demo or recorded? A live demo has a recorded backup either way.

## Before the talk

- Rotate the client secret that was pasted into a prompt on 2026-11-05. Local prompt history keeps it in plain text.
- Move the Hindsight token out of the git-tracked `~/dotfiles/omp/agent/config.yml`.
- Run `skills_lint.py` once and capture clean output for the slide.

## Sources

Research digests in `sources/references/`:

- `referensi-setup-dan-infra.md`: items 1, 10, 11
- `referensi-skills-prompt-dan-config.md`: items 2, 3
- `referensi-mesh-koordinator-mobile.md`: items 4, 7, 8
- `referensi-pr-proof-security-prod.md`: items 6, 9, 12
- `screenshot-omp-mobile-0929.png`: the phone screenshot for the cold open and segment 6

`brief.md`, `structure.md`, the outlines, and the NotebookLM prompts come next, once the open decisions are answered.
