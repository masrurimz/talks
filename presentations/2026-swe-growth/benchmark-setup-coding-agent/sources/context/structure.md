# Structure: Benchmarking My Coding Agent Setup

Total slot is 90 minutes. Rehearse to about 72 minutes of material. The rest is buffer for the demo, Zoom lag, and Q&A. The talk has a cold open, three pillars, an infra section, an honest-limits section, and a close.

## Narrative arc

The arc moves from proof, to how it got built, to three pillars around the model, to limits.

| Time | Section | Organizer questions |
|---|---|---|
| 0-7 | 1. Cold open | none |
| 7-15 | 2. The journey | 1 |
| 15-32 | 3. Pillar 1, the benchmark lab | 2, 3, 11 |
| 32-47 | 4. Pillar 2, knowledge | 5, 7, 8 |
| 47-65 | 5. Pillar 3, the crew | 4, 6, 9 |
| 65-74 | 6. Infra and guardrails | 10 |
| 74-79 | 7. Open problems | 12 |
| 79-90 | 8. Close and Q&A | none |

## Section details

### 1. Cold open (0-7 min)

**Key theme.** The payoff first. A real bug, fixed and proven from a phone, so the audience asks "how".

**Stories.**
- The 9:29 phone screenshot. Read the two commit lines on it.
- PR #804. QA posted a warning at 08:52 WIB, and a pass at 09:57 WIB. That is about 65 minutes from finding to QA pass.
- It was done while Zahid was already on board the plane, before takeoff, from the Tern Android app.

**Ends with.** The claim, said out loud once: "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails." The claim slide shows the model in grey and the four parts with equal weight.

**Then the words.** What a harness is, in plain words, before any quote that uses the word. Then one pre-training slide that names six terms the audience will hear (harness, worktree, skill, mesh, SHIP, poteto-mode), one short gloss each.

**Outside evidence for the claim.** Can Bölük, the author of omp (Stencil), on X: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." It gets its own short slide after the harness definition, with the link, https://x.com/_can1357/status/2021828033640911196

**Transition.** "To explain how that was possible, I need to show how I got here, and it was not a straight line."

### 2. The journey (7-15 min)

**Key theme.** Every tool switch had a concrete reason, and the reasons point to the same needs: extensibility, usage limits, and quality.

**Stories, in data order.**
- Early Gemini use on the first machine (m5), July 2025.
- Claude Code, October 2025. Some tasks were not good enough, and Zahid wanted more efficiency.
- OMO (oh-my-opencode on OpenCode), from October 2025. First pure CLI, then OpenChamber as a web UI. Many issues and limits because it is an extension of OpenCode. Quality was not as good, and Claude and OpenAI subscriptions were getting banned on OpenCode.
- Amp, December 2025 to March 2026. More mature. Mostly used through a proxy for very large usage. The longest stay, with cross-agent communication and the ability to spawn other agents. Slide line: "I forgot why I left Amp, but omp is better because..."
- Antigravity, briefly. Good free usage and features like plan annotations and session artifacts. Left because it is heavy, quality and limits were uneven, and the Google account got banned.
- omp, first on m5 in February 2026, then on the main dev machine (x1) since March 2026.
- Why omp: extensible with own plugins, autolearn, Hindsight memory, multi-provider subscription logins, good compaction.
- The tool journey is also a terminal journey. OpenChamber, then Ghostty tabs because of omp, then herdr for worktrees and sessions, then Paseo for more managed worktrees, and now Tern. Show it in one slide, with one line each.

**Boundaries.** Dormant tools appear only as history, one line each. Do not teach how to use them.

**Transition.** "Whatever tool I used, the question was always the same. Which model does which job, and what does it cost?"

### 3. Pillar 1, the benchmark lab (15-32 min)

**Key theme.** This is the part that matches the title. Zahid measures before he chooses. He has a value formula, a bench of his own, a finding about effort, a handoff trick he tested and turned off, and a subscription journey that ended with "all in on Claude 5.5". All the facts and evidence paths are in `references/referensi-benchmark-lab.md`. Prioritize that file for this section.

**Stories, in slide order.**
- **Demo starts here (about minute 15).** Pick a small real issue from the Alkhidmah backlog, create a worktree, send one prompt from the phone, and leave it running.
- Model routing per role. Live config: default is Opus at low effort, plan is Opus at high, reviewer is Opus at medium, task is Sonnet at medium, and scout and sonic use fast Haiku. Effort rule of thumb. Low for execution, high for plans and hard debugging, medium for review, max almost never. Speeds since October 2026 (Anthropic, average per request). Haiku subagent 130 tokens per second, Sonnet subagent 95, Opus main 66. Effort is not recorded per request, which is why the bench exists.
- The value formula. Value Multiplier = quota $ / subscription cost. Effective $/1M = blended $/1M / multiplier. Value Score = benchmark / effective $/1M. Speed-adjusted QSPD multiplies the benchmark by tokens per second. It catches the "$25 per 1M versus $2 per 1M at the same performance" trap. Rules. One common benchmark only (Terminal-Bench 2.1), count accounts, `cost_total` is API-equivalent, GLM is verbose.
- The October 2026 bench, plotted as time against cost. Two easy tasks (a UI page, a slot finder), three runs each, hidden-check graders, medians. The results file stores no per-run times, so there are no whiskers. Every arm passed 126 of 126 checks, so the bench separates models on speed and cost, not quality. Opus 5.5 low 92 s and 54 s at $0.22 to $0.39 per task. Haiku 5.5 medium 170 s and 120 s at $0.02 to $0.03. DeepSeek v4.1 flash low 476 s and 275 s, the slowest arm.
- Tokens per second misled me. The September formula rated DeepSeek at about 118 tokens per second. In the bench it was the slowest per task, with 28 turns on the UI task against 9 for Opus low. The formula has no term for turns.
- Effort versus turns. Raising effort raised the turn count in every head-to-head pair (Spark slot finder 9 to 23, DeepSeek UI 28 to 40). The likely cause, re-checking, is an inference. The rule stays.
- Handoff arms and the caveat. A handoff costs extra on short tasks and saved money in real long sessions ($2.58 against $1.63 per task, log estimates). Public Terminal-Bench 4.0 has Haiku 5.5 at 39.2% and Sonnet 5.5 at 70.6%, so Haiku on long multi-step work is unproven.
- Prewalk. From the omp docs, a one-shot handoff from the active model to a cheaper one at the first edit, after a todo list exists. Can Bölük's post, "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale." His receipts on SWE-Bench Pro. Sol prewalk into Luna 85% at $1.04 against Sol alone 88% at $1.71. Opus 4.8 prewalk into Flash 78% at $1.46 against Opus alone 85% at $2.78. Zahid's own experience. It took extra time on some tasks, a Haiku target was too expensive, a DeepSeek target too slow, and it is off now.
- Cost. October 2026 was 270k requests and 41B tokens, an API-equivalent price of $7.3k, while Zahid paid about $200. That is about 36x. 97 percent of tokens were cache reads, and two thirds of requests came from subagents.
- The subscription journey. September 2026. GLM Max was his own, a one-year plan bought cheap at the launch price. Codex Pro came from the office. Devin Pro and OpenCode Go were his own. When the Claude 5.5 series arrived he went all in on Claude, because "Claude 5.5 series quality is GOAT". Now 2x Claude Max plus OpenCode Go, usually about $100 per month and about $200 now. At least 12 providers were tried over time.

**Transition.** "A fast, well-chosen engine still forgets everything tomorrow. The next pillar is what the agent knows."

### 4. Pillar 2, knowledge (32-47 min)

**Key theme.** Skills are reusable knowledge. Memory is what carries across projects. Specs keep agents on track.

**Stories.**
- The skill rule: "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- Favorites to show. The poteto-mode port and the principle-check-every-layer principle that Zahid added to it, placed after the layered instructions. The per-domain area skills. His own omp plugins, which were a main reason he picked omp.
- Autolearn story. Auto-on created too many skills. He consolidated them into 14 domain skills plus a lint, and now triggers autolearn by hand after a session that taught something.
- Memory as a journey. Mnemopi, then Hindsight in June 2026. Cognee tried in September and removed in October. Verdict: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project."
- Context and compaction. omp's compaction (shake and snapcompact) plus the memory layer keep long sessions usable.
- Specs and tasks. Why beads was dropped. Agents got smarter, beads is not really human-readable, and agents now retain context better. Replaced by GitHub issues plus coordinator ledgers.

**Transition.** "One agent with good knowledge is useful. The real jump came when I ran many at once."

### 5. Pillar 3, the crew (47-65 min)

**Key theme.** Parallel agents need separation, one coordinator, and gates that demand proof.

**Stories.**
- Worktrees. One worktree per task, opened as a Tern tab by the tern-worktrees plugin Zahid wrote.
- Mesh. Why many sessions on one machine collide, and how omp-agent-mesh (own plugin, Effect-based) provides repo groups, presence, waking messages, file claims, and subagent attribution.
- The SHIP coordinator. A normal omp session that owns merging. It ran about three days (November 2 to 5), with a 276-line ledger. It runs the poteto skill set that Zahid ported to omp, introduced in Pillar 2. A reset with a chat question at minute 55 opens this part. Workers report MERGE-READY with a PR and SHA, freeze the head, and get one fix round. An independent reviewer writes a report.
- Base-branch coordination is solved, not open. Many PRs against one base are handled by his own mesh plugin (omp-agent-mesh) plus one spawned coordinator agent that guides the workers. One writer per branch, and the coordinator merges in sequence. Present it as solved.
- Long-run guardrails. Frozen heads, ledgers, independent review, and proof requirements.
- Review gates and proof. Proof ladder: a recording for UI, command output for API or CLI, a run link for CI, the test command when nothing is visible. Alkhidmah goes further, since `verify.ts` must fail on master and pass on the branch. PR body ends with a "Not verified" line.
- What he still checks by hand: UI and visual feel, and UX.
- **Demo check (about minute 60).** Open the demo PR. Walk its body, its proof, and its gate results.

**Transition.** "All of this runs on machines, and machines hold secrets and production access. So the last pillar is boring and important."

### 6. Infra and guardrails (65-74 min)

**Key theme.** Make repos bootable in one command, and make every dangerous action reversible or dry-run.

**Stories.**
- Remote dev servers. Agents work on servers, and the phone only sends prompts and voice.
- Terminal journey, already introduced, kept short here.
- Per-worktree setup. One command from a fresh worktree to a running, seeded stack, with isolated ports and databases.
- Secrets. omp obfuscates secrets by default, which hides values from the model but does not manage them. Machines use Infisical and people use Bitwarden.
- Damage-control rules block destructive commands such as `rm -rf`, hard reset, force push, and `DROP`.
- Dry run in production. Production is read-only by default. Write scripts run as dry run, then backup, then apply with expected counts, then verify. The dry-run output becomes the runbook.
- omp-org-account-router. It keeps each session on the right GitHub account for work or personal repos.

**Transition.** "That is the setup that works. Now the part that does not."

### 7. Open problems (74-79 min)

**Key theme.** Honest limits. This section builds trust. Exactly three problems, the three Zahid picked.

**Stories.**
- Agent-made UI still looks fat and ugly. It needs design skills and manual feedback.
- Env and seeding per worktree is slow and heavy. One fix took a seed from 652 s to 171 s, and it is still heavy.
- RAM on the shared box. Agents plus CI runners compete, an uncapped test run hit 38 GB, and `verify.ts` refuses to run below 15 GiB free.

**Boundaries.** Base-branch coordination is not an open problem. It belongs to section 5 as solved.

**Transition.** "So where does that leave us?"

### 8. Close and Q&A (79-90 min)

**Key theme.** One claim, one action.

- Restate the claim.
- The one action: the skill rule, "more than twice, make it a skill".
- Q&A with the prepared list below.

## Content boundaries

**Include.**
- Real numbers from the usage stats, labeled as API-equivalent price.
- Real tool history with reasons, including the ones Zahid cannot fully remember.
- PR #804 as the reference story.
- Zahid's own plugins, as examples of extensibility.
- Open problems, stated plainly.

**Exclude.**
- Any secret value, token, IP, email, or phone number.
- Customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- Any secret-handling incident. Secrets appear only as practice.
- Instructions for dormant tools. Antigravity, OMO, Amp, Cognee, Paseo, and beads appear only as history and lessons.
- Effort claims beyond the October bench. Effort level is not recorded per request in the usage stats.
- Account counts of other people and quota percentages from the subscription notes.
- Presenting base-branch coordination as an open problem.
- Teammate names beyond first names already public in PRs. Otherwise write "QA".

## Demo checkpoints

| Minute | Action | Fallback |
|---|---|---|
| About 15 | Start. Choose a small real Alkhidmah issue, create the worktree, send one prompt from the Tern Android app, and show the phone screen mirrored next to the laptop. | Play the recorded backup. |
| About 40 | Optional glance at progress, only if it fits a natural pause. | Skip. |
| About 60 | Check. Open the demo PR and show its body, proof, and gates. | Show the recorded result and the PR #804 body as the reference. |

Say aloud that the demo runs while Zahid talks about other things, which is how he works.

## Q&A prep

1. **Is it worth about $200 per month?** In October 2026 the same work would price at about $7.3k at list price, and he paid about $200. 97 percent of tokens were cache reads. The API-equivalent figure is list price, not money paid.
2. **Why not stay with Claude Code?** Extensibility was the main reason. omp lets him write plugins such as the mesh and the account router. It also has multi-provider logins, autolearn, Hindsight memory, and compaction he trusts. Claude Code is a fine start for most people.
3. **Is it safe to let agents near production?** Production is read-only by default. Writes go through dry run, backup, apply with expected counts, and verify. Damage-control rules block destructive commands, and secrets are obfuscated and kept in Infisical or Bitwarden.
4. **Do you read the code?** Independent reviewers, gates, and proof requirements do the first pass. He still checks UI feel and UX by hand.
5. **Why did you drop beads?** Agents got smarter, beads is not really human-readable, and omp's compaction plus the memory layer retain context better now. GitHub issues plus coordinator ledgers replaced it.
6. **What if a provider bans or limits you?** It happened. Subscriptions were being banned on OpenCode, and a Google account was banned on Antigravity. Because the model is swappable and omp supports many providers, he moved on. At least 12 providers have been tried.
7. **Which effort level should I use?** Low for execution, high for plans and hard debugging, medium for review, and max almost never. This is a rule of thumb. Effort per request is not recorded, so he cannot show a per-effort speed chart.
8. **Can a beginner copy this?** Start with one habit. When you do the same work a third time, write a skill. Then ask for proof in every PR. Skip mesh and coordinators until you really run many agents.
9. **Why did you go all in on Claude?** Quality. "Claude 5.5 series quality is GOAT." In September he ran GLM Max (his own, a cheap one-year launch plan), Codex Pro (from the office), Devin Pro and OpenCode Go. His value formula said which plan was cheap, and the Claude 5.5 series won on quality.
10. **Is prewalk worth it?** The author's receipts on SWE-Bench Pro say yes for long, read-heavy tasks. In Zahid's runs it added time on some tasks and the cheap target was too expensive or too slow, so he turned it off. Test it on your own workload.
11. **How do many agents merge into one base branch?** His mesh plugin plus one coordinator agent. One writer per branch, and the coordinator merges in sequence after an independent review.

## Notes for the outline writers

- Keep all timings above. The presenter outline has 48 slides and 7 section dividers, and the detailed outline has 37. Both rehearse to about 72 minutes of material. The clock windows are in the presenter outline run of show.
- Each pillar section needs one visual: a number, a diagram, or a screenshot.
- Put the claim on the opening and closing slides in the same words.
- Pillar 1 centers on the benchmark lab. Take its facts from `references/referensi-benchmark-lab.md`.
