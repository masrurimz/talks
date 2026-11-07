# Brief: Benchmarking My Coding Agent Setup

## Event

- **Community**: SWE Growth (swegrowth.id).
- **Organizer**: Mas Zikrul.
- **Format**: online on Zoom, 90 minutes, casual community talk. The community's usual slot is an evening session in WIB.
- **Date**: to be confirmed.
- **Slides**: all English.
- **Organizer's working title**: "benchmark setup coding agent".
- **Final title**: **Benchmarking My Coding Agent Setup: One Engineer, Many Agents**.

## Speaker

Zahid is an engineer at GroundUp, where he works on an industrial IoT platform (GinaV2). He is also the tech lead for the Alkhidmah digital platform. He works mostly solo across many repositories, so he has spent the last year building a setup that lets one person cover the work of a small team.

Position the speaker as a practitioner who measured his own habits, not as a vendor or a guru. He has tried a dozen model providers and several agent tools, kept notes, built a value formula and a small bench of his own, and has usage data from about 11,800 sessions to back the story. He also says plainly what still does not work.

## The claim

> The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails.

Every section of the talk either supports this claim or shows its limit.

## Audience

- Mixed Indonesian developers, from juniors to seniors, joining from home.
- Many already use Claude Code or Cursor. Few know omp, the harness Zahid uses.
- They are curious about speed and cost, and some are skeptical about letting agents run for hours.
- Explain what a harness is in one or two sentences before using the word again. A harness is the program around the model that gives it tools, context, memory, and rules.
- Slides are in English. Spoken delivery can be relaxed and mixed with Indonesian, so keep slide text short and plain for non-native readers.

## Goals

1. Make the audience believe one engineer can ship a proven fix from a phone, using the real PR #804 story as evidence.
2. Show that the setup matters more than the model, with real usage numbers and a real tool history.
3. Give the audience a small set of habits they can copy without buying anything new.
4. Be honest about open problems, so the talk does not read as a sales pitch.

## What the audience leaves with

- One action. Zahid's rule: "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- A mental model with four parts around any model: skills, proof, coordination, guardrails.
- A rough effort rule for choosing thinking levels, backed by a small bench that showed higher effort took more steps, and a way to think about cost per task rather than per token.
- Five principles, each told through a story: measure it on your own work, do it twice and make it a skill, one writer per branch, show proof and not "done", make it safe to walk away. A list of things to try this week, such as writing the first skill, asking for proof in every PR, and dry-running anything that touches production.
- A realistic view of what is still hard.

## Tone

- Casual community talk, like "ngobrol santai". Speak as one engineer to peers.
- Honest about limits. Say "I forgot why I left Amp" when it is true. Say "this part is still ugly" when it is.
- Show real numbers and real mistakes, not polished claims.
- No hype words. Do not claim the setup is the best. Claim only that it works for one person with this kind of workload.
- Dollar figures are fine to show. On a slide, write "if I paid per token", because the list price of the tokens is not money paid. The full explanation goes in the speaker notes.

## The organizer's 12 questions, mapped to parts

All 12 are answered on slides in the v4 deck (73 slides). Slide numbers follow `sources/outlines/presenter.md`.

| # | Organizer question | Part in the talk |
|---|---|---|
| 1 | Tool evolution: from Copilot and Claude Code to Gemini, OpenCode, Amp and omp, and why each switch | My journey (slides 7 to 11). Slide 7 is the six-event timeline, slide 8 is why parallel agents moved me from the editor to the terminal, slide 9 is Antigravity |
| 2 | Model routing per role: plan, execute, review and debug, UI, explore | Part 1, measure it on your own work (slides 17, 18) |
| 3 | Effort and thinking level: when to use medium, high, max, and the effect on speed | Part 1 (slides 17, 19) |
| 4 | Orchestration and parallel agents: worktrees, handoff, one coordinator with many workers. Base-branch coordination is solved by the mesh plugin plus one coordinator agent | Part 3, one writer per branch (slides 40, 41, 43, 44, 45, 46). Slide 40 is the busy hour, 4 to 9 agents at once |
| 5 | Task and spec management: beads, hooks, how to write specs so agents do not get lost | Part 2, do it twice, make it a skill (slides 33, 36, 37). Slide 36 is the spec flow, slide 37 is beads and no task hooks |
| 6 | Long-horizon runs: guardrails so agents run for hours or days and stay correct | Parts 3 and 5 (slides 41, 46, 57, 59). Slide 59 is the three accidents and their guardrails |
| 7 | Memory and context: Hindsight and Cognee, managing context so it is not wasteful | Part 2 (slides 31, 32) |
| 8 | Own skills: one or two favorites and what is inside | Part 2 (slides 27, 28, 29, 30, 35, 36). Slide 29 is PARA, slide 35 is poteto-mode, slide 36 is show-me. Slide 34 is the rule that steps in on a risky command |
| 9 | Review and quality gate: multi-reviewer, rules, LSP, linter, what is still checked by hand | Part 4, show proof, not "done" (slides 49, 50, 52, 53, 66). Slide 52 is the five checks |
| 10 | Supporting infra: remote dev server, terminal and multiplexer, secrets, setup per worktree | Part 5, make it safe to walk away (slides 60, 61, 62, 63) |
| 11 | Cost and subscription strategy: money-saving tips for a solo dev | Part 1 (slides 15, 18, 20, 21, 22, 23, 24). Slide 24 is the three money tips |
| 12 | Open problems: UI, CI, env and seeding, disk, and what is next | What is still hard (slides 65 to 70). Slide 66 is UI, slide 67 is CI as the queue, slide 68 is env and seeding, slide 69 is the full disk, slide 70 is the pause and wake plan. Base-branch coordination is answered in Part 3 as solved, and slide 65 says so |

Question 9 is also where "PR standard" lives. No command called "poteto validate" exists. Proof comes from the poteto-mode "Prove It Works" principle, a PR body shape with a Verification section, and Alkhidmah's `verify.ts`, which must fail on master and pass on the branch.

## Hard boundaries

- No secret values, tokens, IPs, emails, or phone numbers on slides.
- No customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- No mention of any secret-handling incident. Present secrets only as practice: obfuscation on by default, damage-control rules, Infisical and Bitwarden, and the dry-run habit.
- Teammates appear as first names only where already public in PRs, otherwise "QA".

## Key source files

Part 1 is built on `sources/references/referensi-benchmark-lab.md`. It holds the value formula, the October 2026 bench, effort versus steps, handoff arms, the Terminal-Bench caveat, the subscription portfolio (September 2026 versus now), prewalk (omp docs plus Can Bölük's post, with receipts and quotes), and the harness-only quote. The other references cover the setup, skills and config, mesh and coordinator, and PR proof, secrets and production. The slide-by-slide speaker notes are in `sources/outlines/presenter.md`.
