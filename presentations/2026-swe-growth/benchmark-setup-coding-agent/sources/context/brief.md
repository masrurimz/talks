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
- A rough effort rule for choosing thinking levels, backed by a small bench that showed higher effort took more turns, and a way to think about cost per task rather than per token.
- A list of things to try on Monday, such as writing the first skill, asking for proof in every PR, and dry-running anything that touches production.
- A realistic view of what is still hard.

## Tone

- Casual community talk, like "ngobrol santai". Speak as one engineer to peers.
- Honest about limits. Say "I forgot why I left Amp" when it is true. Say "this part is still ugly" when it is.
- Show real numbers and real mistakes, not polished claims.
- No hype words. Do not claim the setup is the best. Claim only that it works for one person with this kind of workload.
- Dollar figures are fine to show. State clearly that API-equivalent price is list price of the tokens, not money paid.

## The organizer's 12 questions, mapped to sections

| # | Organizer question | Section in the talk |
|---|---|---|
| 1 | Tool evolution: from Antigravity to OpenCode to Amp to omp, and why each switch | Section 2, the journey (5-15 min) |
| 2 | Model routing per role: plan, execute, review and debug, UI, explore | Section 3, pillar 1 the benchmark lab (15-30 min) |
| 3 | Effort and thinking level: when to use medium, high, max, and the effect on speed | Section 3, pillar 1 the benchmark lab |
| 4 | Orchestration and parallel agents: worktrees, handoff, one coordinator with many workers. Base-branch coordination is solved by the mesh plugin plus one coordinator agent | Section 5, pillar 3 the crew (45-65 min) |
| 5 | Task and spec management: beads, hooks, how to write specs so agents do not get lost | Section 4, pillar 2 knowledge (30-45 min) |
| 6 | Long-horizon runs: guardrails so agents run for hours or days and stay correct | Section 5, pillar 3 the crew |
| 7 | Memory and context: Hindsight and Cognee, managing context so it is not wasteful | Section 4, pillar 2 knowledge |
| 8 | Own skills: one or two favorites and what is inside | Section 4, pillar 2 knowledge |
| 9 | Review and quality gate: multi-reviewer, rules, LSP, linter, what is still checked by hand | Section 5, pillar 3 the crew |
| 10 | Supporting infra: remote dev server, terminal and multiplexer, secrets, setup per worktree | Section 6, infra and guardrails (65-75 min) |
| 11 | Cost and subscription strategy: money-saving tips for a solo dev | Section 3, pillar 1 the benchmark lab (value formula, bench, prewalk, subscription journey) |
| 12 | Open problems: UI, base branch coordination, env and seeding | Section 7, open problems (75-82 min), with UI, env and seeding, and RAM on the shared box. Base-branch coordination is answered in section 5 as solved |

Question 9 is also where "PR standard" lives. No command called "poteto validate" exists. Proof comes from the poteto-mode "Prove It Works" principle, a PR body shape with a Verification section, and Alkhidmah's `verify.ts`, which must fail on master and pass on the branch.

## Hard boundaries

- No secret values, tokens, IPs, emails, or phone numbers on slides.
- No customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- No mention of any secret-handling incident. Present secrets only as practice: obfuscation on by default, damage-control rules, Infisical and Bitwarden, and the dry-run habit.
- Teammates appear as first names only where already public in PRs, otherwise "QA".

## Key source files

Pillar 1 is built on `sources/references/referensi-benchmark-lab.md`. It holds the value formula, the October 2026 bench, effort versus turns, handoff arms, the Terminal-Bench caveat, the subscription portfolio (September 2026 versus now), prewalk (omp docs plus Can Bölük's post, with receipts and quotes), and the harness-only quote. The other references cover the setup, skills and config, mesh and coordinator, and PR proof, secrets and production.
