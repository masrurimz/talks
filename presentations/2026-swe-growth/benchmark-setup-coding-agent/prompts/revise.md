# Prompt for revising a deck

## Instructions for NotebookLM

Revise the deck that was already generated for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

Make a light revision, not a rewrite. Keep the structure and the slide order. Fix only what the checks below find. Keep the language English.

### Revision checks

#### 1. Claim
- The claim appears near the start and again at the close, word for word: "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

#### 2. Structure and timing
- The sections run in this order: cold open (0-5), the journey (5-15), pillar 1 the benchmark lab (15-30), pillar 2 knowledge (30-45), pillar 3 the crew (45-65), infra and guardrails (65-75), open problems (75-82), close (82-90).
- The deck rehearses to about 72 minutes. Presenter deck: about 47 slides. Detailed deck: about 37 slides.

#### 3. Tool journey
- Order and dates: m5 `~/.gemini` 2025-07-29, Claude Code 2025-10-19, OpenCode 2025-10-20, Amp 2025-12-22 to 2026-03-16, omp on m5 2026-02-23, omp on x1-dev main since 2026-03-07.
- The slide line "I forgot why I left Amp, but omp is better because..." is present, with the reasons after it.
- Antigravity is a short side trip, not a main step.

#### 4. Numbers
- Every number matches the sources. All time: 11,842 sessions, 833,553 requests, 138B tokens, $25.9k API-equivalent, $158.7k without caching.
- October 2026: 270k requests, 41B tokens, $7.3k API-equivalent, about $200 paid, 97% cache reads.
- Every dollar figure from the stats is labeled "API-equivalent" and is never called spend, cost paid or savings.
- Real spend is stated separately: usually about $100 per month, about $200 now.
- GLM Max is described as his own plan. Codex Pro is described as coming from the office. Neither is described the other way round.
- The speed table matches the source. Effort level is not described as measured per request.

#### 5. Effort rule and roles
- Low for execution, high for plans and hard debugging, medium for review, max almost never.
- Roles: default Opus 5.5 low, plan Opus 5.5 high, reviewer Opus 5.5 medium, task Sonnet 5.5 medium, scout and sonic Haiku 5.5 fast.

#### 5a. Pillar 1, the benchmark lab
- The value formula has its four lines. The rules are present (one benchmark only, count accounts, API-equivalent, GLM is verbose).
- The October 2026 bench says two easy tasks, three runs, hidden-check graders, and that every arm passed 126 of 126 checks, so speed and cost separate the models.
- Effort versus turns says raising effort raised the turn count in every pair. The cause is worded as likely, not proven.
- The Terminal-Bench caveat is present. Haiku 5.5 39.2% and Sonnet 5.5 70.6% on Terminal-Bench 4.0.
- Prewalk is explained in plain words as a handoff from the active model to a cheaper one at the first edit, after a todo list exists. Can Bölük's numbers are labeled as his own, with his models. Zahid's own bench (Claude 5.5 only) and his 24 to 25 October timeline are the evidence that it is off now.
- The subscription journey reads GLM Max (his own), Codex Pro (office), Devin Pro and OpenCode Go (his own), then all in on Claude 5.5 because "Claude 5.5 series quality is GOAT".
- The harness quote by Can Bölük appears on the claim slide.

#### 6. Phone story
- The phone app is the Tern Android app.
- Zahid was already on board the plane, before takeoff.
- PR #804 timeline: QA warning 08:52, QA pass 09:57 WIB, 65 minutes. The 9:29 screenshot is the before and after step.

#### 7. Memory, skills, autolearn, beads
- The memory journey: Mnemopi, then Hindsight, with Cognee tried and destroyed.
- Skills and memory line is verbatim: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project."
- Autolearn: automatic minted too many skills, they were consolidated into 14 domain skills plus a lint, and it is now triggered manually.
- Beads was dropped because agents got smarter, beads is not human-readable, and compaction plus memory keep context. Replaced by GitHub issues and coordinator ledgers.
- His skill rule is verbatim: "when you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."

#### 8. Plugins and terminal
- Mesh is `omp-agent-mesh`, his own plugin. The deck does not call it built into omp.
- The plugin list matches the references: `omp-agent-mesh`, `omp-org-account-router`, `tern-worktrees`, `paseo-omp`, `opencode-go-multi-auth`, plus the poteto-mode extension.
- Terminal journey order: OpenChamber, Ghostty, herdr, Paseo, Tern.
- Base-branch coordination appears in pillar 3 as solved by the mesh plugin plus one coordinator agent. It is not listed under open problems. Open problems are three, the agent UI, env and seeding per worktree, and RAM on the shared box.

#### 9. Security
- omp secret obfuscation is described as on by default.
- Obfuscation is not called secret management. Infisical for machines and Bitwarden for people are named.
- Production is read-only by default. Writes follow dry run, backup, guarded apply, verify.

#### 10. Boundaries
- No customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers.
- Teammates appear as first names only where a source uses them from public PRs. Otherwise "QA".
- No claim from a `[UNVERIFIED]` or `[INFERENCE]` marker is stated as fact.
- No command called "poteto validate".

#### 11. Style
- One idea per slide. Split a slide that is too dense.
- Add substance to a slide that is too thin, using only the sources.
- Quotes are verbatim, typos kept.
- Plain, calm tone. No hype or marketing words.
- Short sentences. No long dashes. Sentence-case headings.
- A technical term is explained the first time it appears.

---

## Source priority for the revision
1. `sources/context/brief.md`: audience and style.
2. `sources/context/structure.md`: structure and timing.
3. `sources/outlines/presenter.md` or `sources/outlines/detailed.md`: slide-by-slide check.
4. `sources/references/referensi-benchmark-lab.md`: pillar 1, the value formula, bench, prewalk, subscriptions.
5. `sources/references/referensi-evolusi-biaya-plugin.md`: journey, plugins, models, cost, memory.
6. `sources/references/referensi-mesh-koordinator-mobile.md`: mesh, coordinator, PR #804.
7. `sources/references/referensi-skills-prompt-dan-config.md`: skills, principles, prompting.
8. `sources/references/referensi-pr-proof-security-prod.md`: PR standard, secrets, production.
9. `sources/references/referensi-setup-dan-infra.md`: setup, worktrees, servers.

---

## Revision request template

Copy this block, fill the brackets, and paste it after the checks above when you want a targeted change.

```
Revise slide [number or title] of the [presenter or detailed] deck.

Problem: [what is wrong, in one sentence].
Change: [what the slide should say or show instead].
Source: [the file and section that backs it].
Keep: [what must stay the same].
Do not: [anything to avoid].
```

Example.

```
Revise slide 18 of the presenter deck.

Problem: the cost slide shows $7.3k without saying it is API-equivalent.
Change: label the figure "API-equivalent, not spend" and add "paid about $200".
Source: sources/references/referensi-evolusi-biaya-plugin.md, section 7.
Keep: the monthly table.
Do not: add new numbers.
```

---

## Special notes
- Light revision only. Do not change the claim, the section order or the timings.
- If a check cannot be satisfied from the sources, leave the slide as it is and say which source is missing.
