# Structure: Benchmarking My Coding Agent Setup

Total slot is 90 minutes. The deck has 60 numbered slides and 71 minutes of talking. The other 19 minutes are slack and Q&A, from 71:00 to about 90:00. The talk has an opening, a journey, five principles told as five parts, a section on what is still hard, and a close.

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails. The opening says it on slide 4 and the close says it again on slide 58, in the same words.

## The five principles

Each principle is told through one story. The story comes first and the principle name comes after it, so the audience hears the moment before the rule.

| # | Principle (verbatim) | Story that carries it | Slides |
|---|---|---|---|
| 1 | Measure it on your own work | The fastest model on paper was the slowest in Zahid's hands. DeepSeek flash ran at about 118 tokens per second on paper, and took 476 s on the UI task against 92 s for Opus. | 12 (story), 13 (principle) |
| 2 | Do it twice, make it a skill | Autolearn made too many skills, so he merged them into 14 area skills, added a lint, and now triggers autolearn by hand. | 23 to 24 (story), 25 (principle) |
| 3 | One writer per branch | Idle agents never saw the messages sent to them. Now each branch has exactly one writer, and one coordinator merges in order. | 33 (story), 34 (principle) |
| 4 | Show proof, not "done" | The plane fix. PR #804 came with before and after recordings, and the test failed on the old code and passed with the fix. | 41 to 42 (story), 43 (principle) |
| 5 | Make it safe to walk away | Every production change goes dry run, backup, apply, then verify, as steps a human can repeat. | 48 (story), 49 (principle) |

## Narrative arc

The arc moves from proof (the phone fix), to how it got built (the journey), to five principles, to limits, and back to the claim.

| Clock | Section | Slides | Organizer questions |
|---|---|---|---|
| 0-5 | Opening | 1 to 5 | none |
| 5-12 | My journey (the demo starts at slide 10, clock 10:30) | 6 to 10 | 1 |
| 12-26 | Part 1. Choosing models and paying for them (principle 1) | 11 to 21 | 2, 3, 11 |
| 26-37 | Part 2. Teaching the agent (principle 2) | 22 to 31 | 5, 7, 8 |
| 37-48 | Part 3. Many agents at once (principle 3) | 32 to 39 | 4 |
| 48-57 | Part 4. Trusting the result (principle 4, the demo check is slide 45 at 54:30) | 40 to 46 | 9 |
| 57-64 | Part 5. Running it safely (principle 5) | 47 to 54 | 6, 10 |
| 64-68 | What's still hard | 55 to 57 | 12 |
| 68-71 | Close | 58 to 60 | none |

Talk time per section is 5, 7, 14, 11, 11, 9, 7, 4 and 3 minutes, which adds to 71. The organizer topic numbers are the 12 questions in `brief.md`.

## Section shape

Each of the five parts runs in the same order.

1. **Divider.** "Part N" plus a plain topic, not the principle name, so the principle can come after the story. It carries one chat question to the audience, with no minutes and no "Ask chat" label.
2. **Story.** One or two slides about a real moment. The number comes after the story, never stacked on it.
3. **Principle.** The principle name, large, with at most one plain line under it.
4. **Proof.** One to five slides, each with one idea and one picture. Part 1 has seven, because it matches the title and keeps every benchmark slide.
5. **Try this.** One line the audience can do this week.

The opening, the journey, What's still hard and the close have no divider and no principle slide.

## Section details

### Opening (0-5 min, slides 1 to 5)

**Key theme.** The payoff first. A real bug, fixed and proven from a phone, so the audience asks "how".

**Slides.**
- 1. Title.
- 2. The 9:29 phone screenshot. Zahid was on board the plane before takeoff, using the Tern Android app.
- 3. PR #804 timeline. QA flagged the bug at 08:52, Zahid pasted it in at 09:26 from his phone, the agent recorded the bug at 09:29, and QA passed the fix at 09:57, 65 minutes after the warning (times in WIB, in the notes).
- 4. The claim, with the model in grey and the four parts (skills, proof, coordination, guardrails) with equal weight.
- 5. Can Bölük, the author of omp, on X: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." The slide shows the article screenshot. The link is on the Links slide (59).

**Transition.** "To explain how that was possible, I need to show how I got here, and it was not a straight line."

### My journey (5-12 min, slides 6 to 10)

**Key theme.** Every tool switch had a concrete reason, and the reasons point to the same needs: extensibility, usage limits, and quality.

**Slides.**
- 6. Tool timeline with one short reason per tool. Gemini tooling from July 2025, Claude Code from October 2025 (not good enough for some tasks), OpenCode with oh-my-opencode (many issues, subscription bans), Amp from December 2025 to March 2026 (the longest stay, "I forgot why I left Amp"), omp since February 2026 on m5 and March 2026 on x1. Antigravity is in the notes only. Chat question 1 is asked here, from the notes.
- 7. A harness is everything around the model: tools, context, memory and rules, drawn as a hub with the model in the middle.
- 8. Why omp. He can extend it, so he fixes his own problems. Plugins he writes, autolearn, Hindsight memory, multi-provider logins, good compaction.
- 9. From one chat at a time to many agents at once. Requests per month, 2.2k in May to 270k in October.
- 10. Live demo start. Pick a small real Alkhidmah issue, create a worktree, send one prompt from the Tern Android app, and leave it running. Clock 10:30.

**Boundaries.** Dormant tools appear only as history, one line each. Do not teach how to use them. The terminal journey is optional and sits in Part 5 (slide 53).

**Transition.** "Whatever tool I used, the question was always the same. Which model does which job, and what does it cost?"

### Part 1. Choosing models and paying for them (12-26 min, slides 11 to 21)

**Chat question (slide 11).** "Per token or per subscription? Tell us in chat."

**Story (slide 12).** The fastest model on paper was the slowest in his hands. The bars show seconds on the UI task, Opus 5.5 low 92 s, Sonnet 5.5 medium 94 s, Haiku 5.5 medium 170 s, DeepSeek flash low 476 s. DeepSeek took 28 steps against 9 for Opus. The September formula had no term for steps.

**Principle (slide 13).** Measure it on your own work.

**Proof.**
- 14. Each job gets its own model. Live config: default is Opus at low effort, plan is Opus at high, reviewer is Opus at medium, task is Sonnet at medium, and scout and sonic use fast Haiku.
- 15. Every model passed, so speed and price decided. The bench was two easy tasks, three runs each, hidden-check graders, medians. Every model passed 126 of 126 checks.
- 16. Thinking harder made the agent take more steps. Raising effort raised the step count in every pair (Spark slot finder 9 to 23, DeepSeek UI 28 to 40). The cause, re-checking, is an inference.
- 17 and 18. Prewalk, a handoff from the big model to a cheaper one at the first edit. On his tasks it was never cheaper. Opus 5.5 low alone $0.39 against $0.48 with prewalk, and Sonnet 5.5 medium alone $0.24 against $0.36. The slot-finder pairs ($0.22 against $0.35, and a tie at $0.17) are in the notes. Can Bölük's own test, with his models, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not Zahid's.
- 19. $7,300 worth of tokens, and he paid about $200. October 2026 was 270k requests and 41B tokens. The $7.3k is list price, not money paid. 97 percent of tokens were cache reads.
- 20. When Claude 5.5 quality moved, he moved. The September portfolio (GLM Max, Codex Pro, Devin Pro, OpenCode Go) became 2x Claude Max plus OpenCode Go. At least 12 providers were tried.

**Try this (slide 21).** Time one real task of yours on two different models.

**Source of facts.** Every number is in `references/referensi-benchmark-lab.md`. The value formula is cut from the slides and lives in the notes of slide 12.

**Transition.** "A fast, well-chosen engine still forgets everything tomorrow. The next part is what the agent knows."

### Part 2. Teaching the agent (26-37 min, slides 22 to 31)

**Chat question (slide 22).** "Which task do you repeat with your agent more than twice? Tell us in chat."

**Story (slides 23 and 24).** Autolearn made too many skills. He merged them into 14 area skills, added a lint that found 0 errors, and now triggers autolearn by hand after a session that taught something.

**Principle (slide 25).** Do it twice, make it a skill. The rule, in his words: "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."

**Proof.**
- 26. Skills hold how to do a thing, and memory holds what he did and decided.
- 27. Memory as a journey. Mnemopi, then Hindsight in June 2026, Cognee tried in September and removed in October. Compaction is a sentence in the notes.
- 28 (optional). Loose prompts, because the files around them hold the structure.
- 29. poteto-mode, 25 principles, and the one he added, check every layer.
- 30 (optional). Why beads was dropped. Agents got smarter, beads is not really human-readable, and they retain context better now.

**Try this (slide 31).** Write the skill the third time you repeat a task.

**Transition.** "One agent with good knowledge is useful. The real jump came when I ran many at once."

### Part 3. Many agents at once (37-48 min, slides 32 to 39)

**Chat question (slide 32).** "How many agents do you run at once? Tell us in chat."

**Story (slide 33).** Idle sessions never see a mesh message, so a coordinator's broadcast was lost on agents whose sessions had ended. The coordinator wrote the lesson in its own ledger. Messages are not enough, each branch needs exactly one writer.

**Principle (slide 34).** One writer per branch.

**Proof.**
- 35. Every agent task gets its own copy of the repo. A worktree is its own copy of the repo. The `tern-wt list` screenshot shows 1 of 101 worktrees, from the tern-worktrees plugin he wrote.
- 36. Mesh lets agents see what the others are holding. The `mesh peers` screenshot, with the SHIP row holding the production release.
- 37 (optional). He wrote the mesh plugin himself, and the plugin list shows it running.
- 38. One coordinator merges after an independent review. SHIP is a normal omp session that ran about three days (2 to 5 November) with a 276-line ledger. Workers report MERGE-READY with a PR and SHA, the coordinator freezes the head, an independent reviewer writes a verdict, and a failure gets one fix round. Base-branch coordination is solved, not open.

**Try this (slide 39).** When you run two agents, give each its own worktree.

**Transition.** "Many agents write a lot of code. How do I trust it? Remember the plane."

### Part 4. Trusting the result (48-57 min, slides 40 to 46)

**Chat question (slide 40).** "Which part of your agent's work do you still check by hand? Tell us in chat."

**Story (slides 41 and 42).** "Remember the plane? This is the proof that came with that fix." The PR #804 before and after frames, then the test that failed on the old code and passed with the fix. Three failed, three passed.

**Principle (slide 43).** Show proof, not "done". The proof ladder is a recording for UI, command output for API or CLI, a run link for CI, and the test command when nothing is visible. The PR body shape (Why, proof, Not verified) is in the notes.

**Proof.**
- 44. A second agent checks the work and freezes its verdict at one commit. The review report screenshot is from PR #580.
- 45. Demo check at clock 54:30. Open the demo PR from the phone and walk its body for Why, proof, and an honest "Not verified" line. PR #804 has no "Not verified" line, so say that aloud if it is the fallback. Time-box to 90 s.

**Try this (slide 46).** Ask for a before and after clip in your next PR.

**Transition.** "That is proof. Now, running it safely."

### Part 5. Running it safely (57-64 min, slides 47 to 54)

**Chat question (slide 47).** "Where do your agents run: laptop, server or cloud? Tell us in chat."

**Story (slide 48).** Every production change goes dry run, backup, apply, then verify. Production is read-only by default, and the dry-run output becomes the runbook.

**Principle (slide 49).** Make it safe to walk away.

**Proof.**
- 50. Three layers protect his secrets. omp hides values from the model, damage-control rules block destructive commands such as `rm -rf`, force push and `DROP`, and Infisical (machines) and Bitwarden (people) store the secrets.
- 51. Proof runs away from his workstation, and production is read-only.
- 52 (optional). One command takes a fresh worktree to a running stack.
- 53 (optional, first to cut). The terminal journey. OpenChamber, Ghostty, herdr, Paseo, and now Tern.

**Try this (slide 54).** Make every production change start with a dry run.

**Transition.** "That is the setup that works. Now the part that does not."

### What's still hard (64-68 min, slides 55 to 57)

**Key theme.** Honest limits. Exactly three problems, the three Zahid picked, one short slide each. There is no divider and no new chat question. Slide 55 reuses the Part 4 answers.

- 55. A proof clip shows a button works, not that the screen looks right. He still checks UI, visual feel and UX by hand.
- 56. Setting up a worktree dropped from 652 s to 171 s, and every new worktree still pays 171 s.
- 57. One test run used 38 GB of RAM. A rule now caps memory, and `verify.ts` refuses to run below 15 GiB free.

**Boundaries.** Base-branch coordination is not an open problem. It belongs to Part 3 as solved.

**Transition.** "Let me bring it back to the claim."

### Close (68-71 min, slides 58 to 60)

**Key theme.** One claim, one action.

- 58. The five principles as five short lines, with the claim. The one action: write a skill the third time you repeat a task.
- 59. Links, public URLs only, checked on 2026-11-06. The omp repo, the prewalk article, Can Bölük's article on X, and two of Zahid's plugins.
- 60. Questions, in chat or out loud. Q&A runs from 71:00.

## Content boundaries

The six rules of the v2 deck decide what goes on a slide. They are checked by the lint in `deck/build.py`.

1. **One audience.** Every slide speaks to the people on Zoom. Sources, dates, caveats, timing and chat cues live in the speaker notes (`sources/outlines/presenter.md`).
2. **No source lines.** A quote carries the speaker's name next to it. The one Links slide (59) is for anyone who wants to dig.
3. **Headlines in Zahid's words.** About 10 words, hard cap 12. Plain English, no bench jargon such as "arm", "median", "API-equivalent" or "head-to-head". Say "steps", not "turns", and "if I paid per token" where list price is needed.
4. **One picture per slide.** A screenshot, one or two big numbers, or a simple diagram. About 25 words on the face besides the headline, hard cap 30.
5. **One story per section.** Divider, story, principle, proof, then one thing to try.
6. **The lint enforces it.** It fails on source lines, file paths, ISO dates, "Minute N", "Ask chat" and the jargon list. It also checks headline length, face word count, and a `Say:` line on every slide and an `Evidence:` line on every slide with a digit.

**Include.**
- Real numbers from the usage stats, labeled in the notes as API-equivalent (list price, not money paid).
- Real tool history with reasons, including the ones Zahid cannot fully remember.
- PR #804 as the reference story, opening on slides 2 and 3 and called back on slides 41 and 42.
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
- Numbers, quotes or links that are not in `content.py`, `presenter.md` or `references/`.

## Demo checkpoints

| Clock | Slide | Action | Fallback |
|---|---|---|---|
| 10:30 | 10 | Start. Choose a small real Alkhidmah issue, create the worktree, send one prompt from the Tern Android app, and show the phone screen mirrored next to the laptop. Then go straight to slide 11. | Play the recorded backup. |
| 54:30 | 45 | Check. Open the demo PR and show its body, proof, and gates. | Show the recorded result and the PR #804 body as the reference. |

Say aloud that the demo runs while Zahid talks about other things, which is how he works. The recording is never named on a slide.

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
10. **Is prewalk worth it?** Can Bölük's test with his own models says yes for long, read-heavy tasks (cost down 39 to 47 percent for 3 to 7 points of pass rate). In Zahid's runs on short tasks it was never cheaper, and the DeepSeek target was too slow, so he turned it off. Test it on your own workload.
11. **How do many agents merge into one base branch?** His mesh plugin plus one coordinator agent. One writer per branch, and the coordinator merges in sequence after an independent review.

## Notes for the outline writers

- The deck is built from `deck/content.py`. The speaker notes in `sources/outlines/presenter.md` are read by slide number, one section per slide, each with `Say:` and `Evidence:`. Dividers also have `Chat:`.
- The deck has 60 slides, and dividers are numbered slides. Timings and clocks are in the run of show above and in the presenter notes.
- Each part needs one picture per slide: a number, a diagram, or a screenshot.
- Put the claim on the opening and closing slides in the same words.
- Part 1 centers on the benchmark lab. Take its facts from `references/referensi-benchmark-lab.md`.
