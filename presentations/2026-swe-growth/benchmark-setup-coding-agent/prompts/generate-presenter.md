# Prompt for the presenter deck

## Instructions for NotebookLM

Create a **Presenter Slides** deck for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

### Settings
- **Format**: Presenter Slides.
- **Language**: English. Every slide, every label, every speaker note.
- **Length**: Long.

---

## Content direction

### Title and opening
- Title: "Benchmarking My Coding Agent Setup: One Engineer, Many Agents".
- Speaker: Zahid.
- Context: SWE Growth community, online on Zoom, 90 minutes, mixed Indonesian developers. Some use Claude Code or Cursor. Few know omp.

### The claim (state it near the start and again at the close)
"The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

### Structure to follow (rehearse to about 72 minutes of material)

| Time | Section | What it covers |
|---|---|---|
| 0-5 | Cold open | The 9:29 phone screenshot. PR #804. QA warning at 08:52, QA pass at 09:57 WIB. Done from the Tern Android app while already on board the plane, before takeoff. State the claim. |
| 5-15 | The journey | Tools and why each switch (Claude Code, OMO on OpenCode, Amp, a short Antigravity side trip, omp). m5 then x1. What a harness is, in one slide. Why omp: extensible, his own plugins. |
| 15-30 | Pillar 1, the benchmark lab | The core of the talk. Short routing per role and the effort rule. The value formula. His October 2026 bench (method, solo arms, effort versus turns, every arm passed so speed and cost separate, the Terminal-Bench caveat). Prewalk, explained in plain words (slide 16), then his own prewalk bench and timeline and why it is off (slide 17). Cost in October. The subscription journey ending in all in on Claude 5.5. The phone demo starts here. |
| 30-45 | Pillar 2, knowledge | Skills as reusable knowledge (TIL). Memory as cross-project. The autolearn story. Context and compaction. Specs. Why beads was dropped. |
| 45-65 | Pillar 3, the crew | Worktrees. Mesh, his own plugin. The SHIP coordinator, run with the poteto skill set ported to omp. Long runs. Base-branch coordination, solved by his mesh plugin plus one coordinator agent. Review gates and proof. Check the demo PR. |
| 65-75 | Infra and guardrails | Remote servers. The terminal journey. Secrets (omp obfuscates by default). Per-worktree setup. Dry run in production. |
| 75-82 | Open problems | Honest limits. Three only. Agent UI quality, env and seeding per worktree, RAM on the shared box. |
| 82-90 | Close | Restate the claim. Quotes. Q&A. |

### Facts that must appear
- The data order of the tool journey: m5 `~/.gemini` 2025-07-29, Claude Code 2025-10-19, OpenCode 2025-10-20, Amp 2025-12-22 to 2026-03-16, omp on m5 2026-02-23, omp on x1-dev main since 2026-03-07.
- A slide with the exact line: "I forgot why I left Amp, but omp is better because..." followed by the reasons.
- The effort rule: low for execution, high for plans and hard debugging, medium for review, max almost never.
- The speed numbers for Haiku 5.5, Sonnet 5.5 and Opus 5.5 from the stats source, on the routing slide.
- The value formula, four lines: Value Multiplier = quota $ / subscription cost. Effective $/1M = blended $/1M / multiplier. Value Score = benchmark / effective $/1M. Speed-adjusted QSPD = (benchmark x tok/s) / (effective $/1M x 1000).
- The October 2026 bench: two easy tasks, three runs, hidden-check graders, every arm 126 of 126, so speed and cost separate the models. The solo arms table, the effort-versus-turns table (raising effort raised turns in every pair), the handoff arms, and the Terminal-Bench 4.0 caveat (Haiku 5.5 39.2%, Sonnet 5.5 70.6%).
- Prewalk, defined from the omp docs, with Can Bölük's lines "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale.", his own SWE-Bench Pro numbers only when labelled as his with his models, and Zahid's own bench and timeline (off now).
- The subscription journey. September 2026: GLM Max his own (one-year plan, cheap launch price), Codex Pro from the office, Devin Pro and OpenCode Go his own. Then all in on Claude 5.5, "Claude 5.5 series quality is GOAT". Now 2x Claude Max plus OpenCode Go.
- The harness quote on the claim slide. Can Bölük: "I improved 15 LLMs at coding in one afternoon. Only the harness changed."
- October 2026 as the cost headline: 270k requests, 41B tokens, $7.3k API-equivalent, about $200 paid, 97% of tokens from cache reads.
- The memory journey: Mnemopi, then Hindsight, with Cognee tried and destroyed.
- His skill rule, as a closing action: "when you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- Base-branch coordination is solved (mesh plugin plus one coordinator agent). The open problems are only three: the agent UI is still fat and ugly, per-worktree environment seeding is slow and heavy, and RAM on the shared box is a limit.

### Style
- One idea per slide.
- Use real numbers from the sources. Never round into a claim the source does not make.
- Quotes verbatim. Prompts keep their typos.
- Plain, calm, practical. No hype, no marketing words, no "revolutionary".
- Short sentences. No long dashes. Sentence-case headings.
- Explain a technical term the first time it appears (harness, worktree, mesh, compaction, API-equivalent).
- Tables for the model roles, the speed table, the cost per month and the PR #804 timeline.
- A timeline for the tool journey and for the terminal journey.
- Diagrams only where a source file gives one (the PR #804 loop, the coordinator loop, the machine map).

### Slide count
- About 47 slides, to match a 72-minute rehearsal. Follow the slide-by-slide outline, which gives the exact count.

### Boundaries
- No customer company names. Write "a food-manufacturing customer" or "a pilot customer" if a customer must be mentioned.
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers, even partial ones.
- Every dollar figure from the stats is an **API-equivalent price** (the list price of the tokens). It is **not** what Zahid paid. Label it as such on every slide that shows it. State the real spend separately: usually about $100 per month, about $200 now (2x Claude Max plus OpenCode Go).
- Subscription history. GLM Max was his own. Codex Pro came from the office. Devin Pro and OpenCode Go were his own. Do not call GLM an office subscription. Do not state account counts of other people or quota percentages.
- Teammates: first names only where a source already uses them from public PRs. Otherwise write "QA".
- Do not state an item marked `[UNVERIFIED]` or `[INFERENCE]` in a source as fact. Leave it out or word it as open.
- Do not invent commands. There is no command named "poteto validate". Proof means the poteto-mode "Prove It Works" principle plus the PR body shape and the repo verify script that fails on master and passes on the branch.

---

## Source priority
1. `sources/context/brief.md`: context, audience, goal.
2. `sources/context/structure.md`: narrative structure and slide order.
3. `sources/outlines/presenter.md`: slide-by-slide breakdown.
4. `sources/references/referensi-benchmark-lab.md`: **highest priority for Pillar 1.** Value formula, October 2026 bench, effort versus turns, handoff arms, subscription journey, prewalk, harness quote.
5. `sources/references/referensi-evolusi-biaya-plugin.md`: tool journey, harness, plugins, terminal journey, model roles, cost, memory, beads.
6. `sources/references/referensi-mesh-koordinator-mobile.md`: mesh, coordinator, PR #804 from the phone.
7. `sources/references/referensi-skills-prompt-dan-config.md`: instructions, prompting, poteto principles, area skills, lint, memory config.
8. `sources/references/referensi-pr-proof-security-prod.md`: PR standard, proof, secrets, production discipline.
9. `sources/references/referensi-setup-dan-infra.md`: setup, worktrees, devkit, remote servers.
10. `sources/references/screenshot-omp-mobile-0929.png`: the phone screenshot for the cold open and the demo slides.

---

## Special notes
- The live demo is driven from the phone (Tern Android app) on a small real issue from the alkhidmah backlog, ending in a PR with proof. It is shared by screen mirror next to the laptop on Zoom. A recorded backup exists. Add a demo kickoff slide in the 15-30 section and a demo check slide in the 45-65 section.
- The phone story: Zahid was already on board the plane, before takeoff.
- Security: omp has secret obfuscation on by default. Present it with damage-control rules, Infisical for machines, Bitwarden for people, and production dry-run discipline. Obfuscation is not secret management, and the slides should say so.
- Mesh is his own plugin (`omp-agent-mesh`). The poteto skill set is ported to omp by him. `principle-check-every-layer` is his own principle added to poteto.
- The close has two parts: the claim, and his skill rule as the one action for the audience. Then a short set of quotes taken from the sources.
