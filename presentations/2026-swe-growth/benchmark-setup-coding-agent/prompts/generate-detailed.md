# Prompt for the detailed deck

## Instructions for NotebookLM

Create a **Detailed Slides** deck for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

### Settings
- **Format**: Detailed Slides (self-reading, more text per slide, usable without the speaker).
- **Language**: English.
- **Length**: Long.

---

## Content direction

### Title and opening
- Title: "Benchmarking My Coding Agent Setup: One Engineer, Many Agents".
- Speaker: Zahid.
- Context: SWE Growth community, online on Zoom, 90 minutes, mixed Indonesian developers.

### The claim
"The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

### Structure to follow

1. **Cold open.** The 9:29 phone screenshot and PR #804. QA warning at 08:52, QA pass at 09:57 WIB. Fixed from the Tern Android app while already on board the plane, before takeoff. The claim.
2. **The journey.** Tool by tool with dates and Zahid's reasons: Claude Code, OMO on OpenCode, Amp, a short Antigravity side trip, omp. m5 then x1. What a harness is. Why omp: extensible, his own plugins, with the plugin list and what each one does.
3. **Pillar 1, the benchmark lab.** The core of the talk. Model roles with model and effort, the effort rule and speed. The value formula. His October 2026 bench (method, solo arms, every arm passed so speed and cost separate, effort versus turns, handoff arms, the Terminal-Bench caveat). Prewalk explained in plain words from the omp docs and Can Bölük's post, then his own prewalk bench (Claude 5.5 only) and timeline, and why it is off. Can Bölük's numbers only labelled as his, with his models. Cost per month. The subscription journey (own versus office plans, September 2026 versus now) ending in all in on Claude 5.5.
4. **Pillar 2, knowledge.** Skills as reusable knowledge. Area skills and the lint. Memory as cross-project, and the memory journey (Mnemopi, Hindsight, Cognee). Autolearn and why it went from automatic to manual. Context and compaction. Specs. Why beads was dropped. His skill rule.
5. **Pillar 3, the crew.** Worktrees. Mesh (his own plugin). The SHIP coordinator and its ledger. Base-branch coordination, solved by mesh plus one coordinator agent. Review gates, independent review, frozen verdicts. The PR body standard and proof. The demo PR.
6. **Infra and guardrails.** The machine map. The terminal journey (OpenChamber, Ghostty, herdr, Paseo, Tern). Per-worktree setup. Secrets. Damage-control rules. Production read-only by default and the dry-run runbook.
7. **Open problems.** Agent UI, environment seeding per worktree, shared RAM.
8. **Close.** The claim, his skill rule as the one action, a short set of quotes, Q&A.

### Proportions
- Cold open: 8%.
- Journey and harness: 8%.
- Pillar 1, the benchmark lab: 27%.
- Pillar 2, knowledge: 14%.
- Pillar 3, the crew: 24%.
- Infra and guardrails: 11%.
- Open problems and close: 8%.

### Facts that must appear
- Tool journey dates: m5 `~/.gemini` 2025-07-29, Claude Code 2025-10-19, OpenCode 2025-10-20 (215 sessions on m5), Amp 2025-12-22 to 2026-03-16, omp on m5 2026-02-23, omp on x1-dev main since 2026-03-07.
- A slide with the line: "I forgot why I left Amp, but omp is better because..." and the reasons.
- Model roles as a table: default Opus 5.5 low, plan Opus 5.5 high, reviewer Opus 5.5 medium, task Sonnet 5.5 medium, scout and sonic Haiku 5.5 fast.
- The speed table with requests, average duration, time to first token and output tokens per second.
- The per-month table: requests, tokens, API-equivalent price, price without cache, cache-read share, subagent share, project or worktree folders. All-time figures: 11,842 sessions, 833,553 requests, 138B tokens, $25.9k API-equivalent, $158.7k without prompt caching.
- The providers tried, by request count.
- The PR #804 timeline table and the sequence diagram.
- His skill rule, word for word: "when you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- His memory line, word for word: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project."
- The value formula, four lines: Value Multiplier = quota $ / subscription cost. Effective $/1M = blended $/1M / multiplier. Value Score = benchmark / effective $/1M. Speed-adjusted QSPD = (benchmark x tok/s) / (effective $/1M x 1000).
- The October 2026 bench: the solo arms table, the effort-versus-turns table, the handoff arms, "every arm passed 126 of 126 checks, so speed and cost separate the models", and the Terminal-Bench 4.0 caveat (Haiku 5.5 39.2%, Sonnet 5.5 70.6%).
- Prewalk defined from the omp docs, Can Bölük's lines "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale.", his SWE-Bench Pro test (his models, not Zahid's), and Zahid's own bench and timeline (off now).
- The subscription journey. September 2026: GLM Max his own (one-year plan, cheap launch price), Codex Pro from the office, Devin Pro and OpenCode Go his own. Then all in on Claude 5.5, "Claude 5.5 series quality is GOAT". Now 2x Claude Max plus OpenCode Go.
- The harness quote on the claim slide. Can Bölük: "I improved 15 LLMs at coding in one afternoon. Only the harness changed."
- Base-branch coordination is solved (mesh plugin plus one coordinator agent). Open problems are only the agent UI, env and seeding per worktree, and RAM on the shared box.

### Style
- Detailed: each slide has a short heading, one main idea, and the evidence under it (a table, a quote, a number, a file path or a command). Someone who was not there can read it.
- One idea per slide. If a slide needs two ideas, split it.
- Real numbers from the sources. Quotes verbatim, typos kept.
- Plain, calm, practical. No hype, no marketing words.
- Short sentences. No long dashes. Sentence-case headings.
- Explain a technical term the first time it appears.

### Slide count
- About 37 slides. Follow the slide-by-slide outline, which gives the exact count.

### Boundaries
- No customer company names. Write "a food-manufacturing customer" or "a pilot customer".
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers.
- Every dollar figure from the stats is an **API-equivalent price** (the list price of the tokens), **not** spend. Label it on every slide that shows it. State real spend separately: usually about $100 per month, about $200 now (2x Claude Max plus OpenCode Go).
- Subscription history. GLM Max was his own. Codex Pro came from the office. Devin Pro and OpenCode Go were his own. Do not call GLM an office subscription. Do not state account counts of other people or quota percentages.
- Teammates: first names only where a source already uses them from public PRs. Otherwise write "QA".
- Do not state an item marked `[UNVERIFIED]` or `[INFERENCE]` in a source as fact. Leave it out or word it as open.
- No command called "poteto validate" exists. Proof is the "Prove It Works" principle, the PR body shape and the repo verify script that fails on master and passes on the branch.

---

## Source priority
1. `sources/context/brief.md`: context, audience, goal.
2. `sources/context/structure.md`: narrative structure.
3. `sources/outlines/detailed.md`: slide-by-slide breakdown (detailed).
4. `sources/references/referensi-benchmark-lab.md`: **highest priority for Pillar 1.** Value formula, October 2026 bench, effort versus turns, handoff arms, subscription journey, prewalk, harness quote.
5. `sources/references/referensi-evolusi-biaya-plugin.md`: tool journey, harness, plugins, terminal journey, model roles, cost, memory, beads.
6. `sources/references/referensi-mesh-koordinator-mobile.md`: mesh, coordinator, PR #804.
7. `sources/references/referensi-skills-prompt-dan-config.md`: instructions, poteto principles, area skills, lint, memory config.
8. `sources/references/referensi-pr-proof-security-prod.md`: PR standard, proof, secrets, production.
9. `sources/references/referensi-setup-dan-infra.md`: setup, worktrees, devkit, remote servers.
10. `sources/references/screenshot-omp-mobile-0929.png`: the phone screenshot.

---

## Special notes
- The talk has a live demo from the phone (Tern Android app), shared by screen mirror on Zoom, with a recorded backup. Include a demo kickoff slide and a demo check slide.
- Zahid was already on board the plane, before takeoff, when the PR #804 fix ran.
- Security: omp has secret obfuscation on by default. Present it with damage-control rules, Infisical for machines, Bitwarden for people, and production dry-run discipline. Say plainly that obfuscation is not secret management.
- Mesh is his own plugin (`omp-agent-mesh`). The poteto skill set is ported to omp by him. `principle-check-every-layer` is his own principle.
- Close with the claim, his skill rule as the one action, and a short set of quotes from the sources.
