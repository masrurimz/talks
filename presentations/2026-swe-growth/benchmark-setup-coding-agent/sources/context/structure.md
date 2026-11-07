# Structure: Benchmarking My Coding Agent Setup

Total slot is 90 minutes. The deck (v3) has 68 numbered slides and 80 minutes of talking. The other 10 minutes are slack and Q&A, from 80:00 to about 90:00. The talk has an opening with a map, a journey, five principles told as five parts, a section on what is still hard, and a close. The v3 deck added 8 slides so that all 12 organizer questions are answered on slides.

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails. The opening says it on slide 4 and the close says it again on slide 66, in the same words.

## The five principles

Each principle is told through one story. The story comes first and the principle name comes after it, so the audience hears the moment before the rule.

| # | Principle (verbatim) | Story that carries it | Slides |
|---|---|---|---|
| 1 | Measure it on your own work | The fastest model on paper was the slowest in Zahid's hands. DeepSeek flash ran at about 118 tokens per second on paper, and took 476 s on the UI task against 92 s for Opus. | 14 (story), 15 (principle) |
| 2 | Do it twice, make it a skill | Autolearn made too many skills, so he merged them into 14 area skills, added a lint, and now triggers autolearn by hand. | 26 to 27 (story), 29 (principle) |
| 3 | One writer per branch | Idle agents never saw the messages sent to them. Now each branch has exactly one writer, and one coordinator merges in order. | 38 (story), 39 (principle) |
| 4 | Show proof, not "done" | The plane fix. PR #804 came with before and after recordings, and the test failed on the old code and passed with the fix. | 46 to 47 (story), 48 (principle) |
| 5 | Make it safe to walk away | Every production change goes dry run, backup, apply, then verify, as steps a human can repeat. | 54 (story), 55 (principle) |

## Narrative arc

The arc moves from proof (the phone fix), to the map of the talk, to how it got built (the journey), to five principles, to limits, and back to the claim.

| Clock | Section | Slides | Talk time | Organizer questions |
|---|---|---|---|---|
| 0-6 | Opening, with the map | 1 to 6 | 6 min | none |
| 6-14 | My journey (the demo starts at slide 12, clock 12:30) | 7 to 12 | 8 min | 1 |
| 14-29 | Part 1. Choosing models and paying for them (principle 1) | 13 to 24 | 15 min | 2, 3, 11 |
| 29-42.5 | Part 2. Teaching the agent (principle 2) | 25 to 36 | 13.5 min | 5, 7, 8 |
| 42.5-53.5 | Part 3. Many agents at once (principle 3) | 37 to 44 | 11 min | 4, 6 |
| 53.5-64 | Part 4. Trusting the result (principle 4, the demo check is slide 51 at 61:30) | 45 to 52 | 10.5 min | 9 |
| 64-72.5 | Part 5. Running it safely (principle 5) | 53 to 61 | 8.5 min | 6, 10 |
| 72.5-77 | What is still hard | 62 to 65 | 4.5 min | 12 |
| 77-80 | Close | 66 to 68 | 3 min | none |

Talk time per section is 6, 8, 15, 13.5, 11, 10.5, 8.5, 4.5 and 3 minutes, which adds to 80. Q&A and slack are the last 10 minutes. The organizer topic numbers are the 12 questions in `brief.md`.

## The map

Slide 6 shows a seven-row map. It is one list in `deck/content.py` (`MAP`). The same list draws a small seven-segment strip at the bottom of every divider (Part 1 to Part 5 and What is still hard), with the current segment in the accent colour and a "you are here" label.

| Map row | Where it lands | Organizer questions |
|---|---|---|
| My journey. Tools and why I switched | My journey | 1 |
| 1 Measure it on your own work. Models, effort, cost | Part 1 | 2, 3, 11 |
| 2 Do it twice, make it a skill. Skills, memory, specs | Part 2 | 5, 7, 8 |
| 3 One writer per branch. Many agents, long runs | Part 3 | 4, 6 |
| 4 Show proof, not "done". Review and quality | Part 4 | 9 |
| 5 Make it safe to walk away. Infra and secrets | Part 5 | 6, 10 |
| What is still hard. Open problems | What is still hard | 12 |

The map slide has its own face-word limit (about 60 words) as a per-layout limit in `deck/build.py`.

## Section shape

Each of the five parts runs in the same order.

1. **Divider.** "Part N" plus a plain topic, not the principle name, so the principle can come after the story. It carries one chat question to the audience, with no minutes and no "Ask chat" label, and the map strip at the bottom.
2. **Story.** One or two slides about a real moment. The number comes after the story, never stacked on it.
3. **Principle.** The principle name, large, with at most one plain line under it.
4. **Proof.** One to eight slides, each with one idea and one picture. Part 1 has eight (slides 16 to 23), because it matches the title and keeps every benchmark slide.
5. **Try this.** One line the audience can do this week.

The opening, the journey and the close have no divider and no principle slide. What is still hard has a divider (slide 62), drawn like the Part dividers, and no principle slide.

## Section details

### Opening (0-6 min, slides 1 to 6)

**Key theme.** The payoff first. A real bug, fixed and proven from a phone, so the audience asks "how". Then the map, so each person sees where their question lands.

**Slides.**
- 1. Title.
- 2. The 9:29 phone screenshot. Zahid was on board the plane before takeoff, using the Tern Android app.
- 3. PR #804 timeline. QA flagged the bug at 08:52, Zahid pasted it in at 09:26 from his phone, the agent recorded the bug at 09:29, and QA passed the fix at 09:57, 65 minutes after the warning (times in WIB, in the notes).
- 4. The claim, with the model in grey and the four parts (skills, proof, coordination, guardrails) with equal weight.
- 5. Can Bölük, the author of omp, on X: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." The slide shows the article screenshot. The link is on the Links slide (67).
- 6. The map. Seven rows, one per section of the talk, with the topics each one covers. Zahid says that the audience's questions are in there, and that they can ask in chat at any time.

**Transition.** "To explain how that was possible, I need to show how I got here, and it was not a straight line."

### My journey (6-14 min, slides 7 to 12)

**Key theme.** Every tool switch had a concrete reason, and the reasons point to the same needs: extensibility and quality.

**Slides.**
- 7. Tool timeline with one short reason per tool. Gemini tooling from July 2025, Claude Code from October 2025 (not good enough for some tasks), OpenCode with OmO (token hungry, slow, tests that did not catch much), Amp from December 2025 to March 2026 (the longest stay, "I forgot why I left Amp"), omp since February 2026 on m5 and March 2026 on x1. Antigravity has no dated bar, so it is not on the chart and has its own slide. Chat question 1 is asked here, from the notes.
- 8. Antigravity. The first tool Zahid used with a proper plan mode, memory, design artifacts and an agent-first screen instead of an editor-first one. His Google account was banned, and omp still uses its image model.
- 9. A harness is everything around the model: tools, context, memory and rules, drawn as a hub with the model in the middle.
- 10. Why omp. He can extend it, so he fixes his own problems. Plugins he writes, autolearn, Hindsight memory, multi-provider logins, good compaction.
- 11. From one chat at a time to many agents at once. Requests per month, 2.2k in May to 270k in October.
- 12. Live demo start. Pick a small real Alkhidmah issue, create a worktree, send one prompt from the Tern Android app, and leave it running. Clock 12:30.

**Boundaries.** Dormant tools appear only as history, one line each. Do not teach how to use them. The terminal journey is in Part 5 (slide 60).

**Transition.** "Whatever tool I used, the question was always the same. Which model does which job, and what does it cost?"

### Part 1. Choosing models and paying for them (14-29 min, slides 13 to 24)

**Chat question (slide 13).** "Per token or per subscription? Tell us in chat."

**Story (slide 14).** The fastest model on paper was the slowest in his hands. The bars show seconds on the UI task, Opus 5.5 low 92 s, Sonnet 5.5 medium 94 s, Haiku 5.5 medium 170 s, DeepSeek flash low 476 s. DeepSeek took 28 steps against 9 for Opus. The September formula had no term for steps.

**Principle (slide 15).** Measure it on your own work.

**Proof.**
- 16. Each job gets its own model. Live config: chat is Opus at low effort, plan and hard bugs are Opus at high, UI design is Sonnet at high, review is Opus at medium, and exploring is Haiku. Rule of thumb: low to do, medium to review, high to plan and for hard bugs, max almost never because it is slow and gave little gain. The `designer` agent appears in 316 session files, mostly UI redesign tasks.
- 17. Every model passed, so speed and price decided. The bench was two easy tasks, three runs each, hidden-check graders, medians. Every model passed 126 of 126 checks.
- 18. Thinking harder made the agent take more steps. Raising effort raised the step count in every pair (Spark slot finder 9 to 23, DeepSeek UI 28 to 40). The cause, re-checking, is an inference. "More steps probably means a longer wait" is also an inference, because high-effort runs were not timed.
- 19 and 20. Prewalk, a handoff from the big model to a cheaper one at the first edit. On his tasks it was never cheaper. Opus 5.5 low alone $0.39 against $0.48 with prewalk, and Sonnet 5.5 medium alone $0.24 against $0.36. The slot-finder pairs ($0.22 against $0.35, and a tie at $0.17) are in the notes. Can Bölük's own test, with his models, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not Zahid's.
- 21. $7,300 worth of tokens, and he paid about $200. October 2026 was 270k requests and 41B tokens. The $7.3k is list price, not money paid. 97 percent of tokens were cache reads.
- 22. When Claude 5.5 quality moved, he moved. The September portfolio (GLM Max, Codex Pro, Devin Pro, OpenCode Go) became 2x Claude Max plus OpenCode Go. At least 12 providers were tried.
- 23. Three money tips from his own bills. A flat plan plus prompt caching. A cheap model (Haiku) to search and a strong one (Opus at high) to plan. Test a cost trick on your own work before you trust it, because prewalk was never cheaper on his tasks. Organizer question 11.

**Try this (slide 24).** Time one real task of yours on two different models.

**Source of facts.** Every number is in `references/referensi-benchmark-lab.md` or in the notes of `presenter.md`. The value formula is cut from the slides and lives in the notes of slide 14.

**Transition.** "A fast, well-chosen engine still forgets everything tomorrow. The next part is what the agent knows."

### Part 2. Teaching the agent (29-42.5 min, slides 25 to 36)

**Chat question (slide 25).** "Which task do you repeat with your agent more than twice? Tell us in chat."

**Story (slides 26 and 27).** Autolearn made too many skills. He merged them into 14 area skills, added a lint that found 0 errors, and now triggers autolearn by hand after a session that taught something.

**Principle (slide 29).** Do it twice, make it a skill. The rule, in his words: "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."

**Proof.**
- 28. One skill per area, like PARA. He organizes skills by area, inspired by Tiago Forte's PARA method (Projects, Areas, Resources, Archives). His skills follow the Areas box, which gives the 14 area skills. Favorites are poteto-mode and show-me. This slide sits between the story and the principle. Organizer question 8.
- 30. Skills hold how to do a thing, and memory holds what he did and decided.
- 31. Memory as a journey. Mnemopi, then Hindsight in June 2026, Cognee tried in September and removed in October. Compaction is a sentence in the notes, and the first thing to cut.
- 32. Loose prompts, because the files around them hold the structure.
- 33. poteto-mode, 25 principles, and the one he added, check every layer.
- 34. Before any code, the agent draws the screen. A neutral wireframe, then folders and files, then data and flow, checked layer by layer, saved in one markdown file per feature so subagents do not wander. The show-me skill draws the wireframes. Organizer questions 5 and 8.
- 35. Why beads was dropped. Agents got smarter, beads is not really human-readable, and they retain context better now. No hooks for tasks. GitHub issues and the coordinator's ledger hold the work, and CI does the checking.

**Try this (slide 36).** Write the skill the third time you repeat a task.

**Transition.** "One agent with good knowledge is useful. The real jump came when I ran many at once."

### Part 3. Many agents at once (42.5-53.5 min, slides 37 to 44)

**Chat question (slide 37).** "How many agents do you run at once? Tell us in chat."

**Story (slide 38).** Idle sessions never see a mesh message, so a coordinator's broadcast was lost on agents whose sessions had ended. The coordinator wrote the lesson in its own ledger. Messages are not enough, each branch needs exactly one writer.

**Principle (slide 39).** One writer per branch.

**Proof.**
- 40. Every agent task gets its own copy of the repo. A worktree is its own copy of the repo. The `tern-wt list` output had 101 worktrees, from the tern-worktrees plugin he wrote.
- 41. Mesh lets agents see what the others are holding. Three agent cards re-typeset from the real `mesh peers` capture, with the SHIP row holding the production release.
- 42 (optional, the only one in the deck). He wrote the mesh plugin himself, and the plugin list shows it running.
- 43. One coordinator merges after an independent review. SHIP is a normal omp session. Its ledger has 353 decisions from 2 to 7 November. Workers send `MERGE-READY #<pr> <full sha>`, the coordinator freezes the head, an independent reviewer writes a verdict, and a failure gets one fix round. Base-branch coordination is solved, not open.

**Try this (slide 44).** When you run two agents, give each its own worktree.

**Transition.** "Many agents write a lot of code. How do I trust it? Remember the plane."

### Part 4. Trusting the result (53.5-64 min, slides 45 to 52)

**Chat question (slide 45).** "Which part of your agent's work do you still check by hand? Tell us in chat."

**Story (slides 46 and 47).** "Remember the plane? This is the proof that came with that fix." The PR #804 before and after frames, then the test that failed on the old code and passed with the fix. Three failed, three passed.

**Principle (slide 48).** Show proof, not "done". The proof ladder is a recording for UI, command output for API or CLI, a run link for CI, and the test command when nothing is visible. The PR body shape (Why, proof, Not verified) is in the notes.

**Proof.**
- 49. Five checks run before he looks. LSP diagnostics after every edit, lint and type checks, tests shaped like the Testing Trophy (plus a formal-verification skill for risky logic), reviewer agents that scale with risk, and Zahid, who still checks UI and feel by hand. Organizer question 9.
- 50. A second agent checks the work and freezes its verdict at one commit. The review report is from PR #580.
- 51. Demo check at clock 61:30. Open the demo PR from the phone and walk its body for Why, proof, and an honest "Not verified" line. PR #804 has no "Not verified" line, so say that aloud if it is the fallback. Time-box to 90 s.

**Try this (slide 52).** Ask for a before and after clip in your next PR.

**Transition.** "That is proof. Now, running it safely."

### Part 5. Running it safely (64-72.5 min, slides 53 to 61)

**Chat question (slide 53).** "Where do your agents run: laptop, server or cloud? Tell us in chat."

**Story (slide 54).** Every production change goes dry run, backup, apply, then verify. Production is read-only by default, and the dry-run output becomes the runbook.

**Principle (slide 55).** Make it safe to walk away.

**Proof.**
- 56. Three accidents gave three guardrails, from the coordinator's ledger. A reset in the main checkout wiped the shared dev database, and the devkit now refuses any reset path that reaches it (PR #574). A reviewer agent's Docker prune deleted about 244 unused volumes, and Docker cleanup is now banned for every agent. One masking tool went through 11 reviews, and there is now a two-round review cap. Chat question from the notes: "Has an agent ever deleted something it should not have?" Organizer question 6.
- 57. Three layers protect his secrets. omp hides values from the model, damage-control rules block destructive commands such as `rm -rf`, force push and `DROP`, and Infisical (machines) and Bitwarden (people) store the secrets.
- 58. Proof runs away from his workstation, and production is read-only.
- 59. One command takes a fresh worktree to a running stack.
- 60. The terminal journey. OpenChamber, Ghostty, herdr, Paseo (tried for easier managed worktrees), and now Tern.

**Try this (slide 61).** Make every production change start with a dry run.

**Transition.** "That is the setup that works. Now the part that does not."

### What is still hard (72.5-77 min, slides 62 to 65)

**Key theme.** Honest limits. Exactly three problems, one short slide each, after a divider. The divider (slide 62) asks "What still breaks for you? Tell us in chat." and says that base branches were asked about and that Part 3 showed how he solved it.

- 62. Divider, What is still hard, with the map strip.
- 63. A proof clip shows a button works, not that the screen looks right. Agent-built UI still needs design skills and his feedback. He still checks UI, visual feel and UX by hand. Reuse the Part 4 answers here.
- 64. Setting up the environment and the seed data for a worktree dropped from 652 s to 171 s, and every new worktree still pays 171 s.
- 65. One test run used 38 GB of RAM on the shared box. A rule now caps memory, and `verify.ts` refuses to run below 15 GiB free.

**Boundaries.** Base-branch coordination is not an open problem. It belongs to Part 3 as solved.

**Transition.** "Let me bring it back to the claim."

### Close (77-80 min, slides 66 to 68)

**Key theme.** One claim, one action.

- 66. The five principles as five short lines, with the claim. The one action: write a skill the third time you repeat a task.
- 67. Links, public URLs only, checked on 2026-11-06. The omp repo, the prewalk article, Can Bölük's article on X, and two of Zahid's plugins.
- 68. Questions, in chat or out loud. Q&A runs from 80:00 and has 10 minutes with slack.

## Content boundaries

Six rules decide what goes on a slide. They were set in v2 and still hold in v3. They are checked by the lint in `deck/build.py`.

1. **One audience.** Every slide speaks to the people on Zoom. Sources, dates, caveats, timing and chat cues live in the speaker notes (`sources/outlines/presenter.md`).
2. **No source lines.** A quote carries the speaker's name next to it. The one Links slide (67) is for anyone who wants to dig.
3. **Headlines in Zahid's words.** About 10 words, hard cap 12. Plain English, no bench jargon such as "arm", "median", "API-equivalent" or "head-to-head". Say "steps", not "turns", and "if I paid per token" where list price is needed.
4. **One picture per slide.** A screenshot, one or two big numbers, or a simple diagram. About 25 words on the face besides the headline, hard cap 30. The map slide has its own limit of about 60 words.
5. **One story per section.** Divider, story, principle, proof, then one thing to try.
6. **The lint enforces it.** It fails on source lines, file paths, ISO dates, "Minute N", "Ask chat" and the jargon list. It also checks headline length, face word count, and a `Say:` line on every slide and an `Evidence:` line on every slide with a digit. Slide faces never show organizer question numbers.

**Include.**
- Real numbers from the usage stats, labeled in the notes as API-equivalent (list price, not money paid).
- Real tool history with reasons, including the ones Zahid cannot fully remember.
- PR #804 as the reference story, opening on slides 2 and 3 and called back on slides 46 and 47.
- Zahid's own plugins, as examples of extensibility.
- Open problems, stated plainly.

**Exclude.**
- Any secret value, token, IP, email, or phone number.
- Customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- Any secret-handling incident. Secrets appear only as practice. The three accidents on slide 56 are agent-run reset, Docker cleanup and review-loop incidents from the ledger, and none involves a secret.
- Instructions for dormant tools. Antigravity, OMO, Amp, Cognee, Paseo, and beads appear only as history and lessons.
- Effort claims beyond the October bench and Zahid's own rule. Effort level is not recorded per request in the usage stats.
- Account counts of other people and quota percentages from the subscription notes.
- Presenting base-branch coordination as an open problem.
- Real `docs/plans/**` wireframes. Slide 34 uses a newly drawn neutral wireframe.
- Teammate names beyond first names already public in PRs. Otherwise write "QA".
- Numbers, quotes or links that are not in `content.py`, `presenter.md` or `references/`.

## Demo checkpoints

| Clock | Slide | Action | Fallback |
|---|---|---|---|
| 12:30 | 12 | Start. Choose a small real Alkhidmah issue, create the worktree, send one prompt from the Tern Android app, and show the phone screen mirrored next to the laptop. Then go straight to slide 13. | Play the recorded backup. |
| 61:30 | 51 | Check. Open the demo PR and show its body, proof, and gates. | Show the recorded result and the PR #804 body as the reference. |

Say aloud that the demo runs while Zahid talks about other things, which is how he works. The recording is never named on a slide.

## Q&A prep

Q&A has only 10 minutes, so most answers should point to a slide.

1. **Is it worth about $200 per month?** In October 2026 the same work would price at about $7.3k at list price, and he paid about $200. 97 percent of tokens were cache reads. The API-equivalent figure is list price, not money paid. Slide 23 has three money tips.
2. **Why not stay with Claude Code?** Extensibility was the main reason. omp lets him write plugins such as the mesh and the account router. It also has multi-provider logins, autolearn, Hindsight memory, and compaction he trusts. Claude Code is a fine start for most people.
3. **Is it safe to let agents near production?** Production is read-only by default. Writes go through dry run, backup, apply with expected counts, and verify. Damage-control rules block destructive commands, and secrets are obfuscated and kept in Infisical or Bitwarden.
4. **Do you read the code?** Five checks run first (slide 49). Independent reviewers, gates, and proof requirements do the first pass. He still checks UI feel and UX by hand.
5. **Why did you drop beads?** Agents got smarter, beads is not really human-readable, and omp's compaction plus the memory layer retain context better now. GitHub issues plus coordinator ledgers replaced it, and CI does the checking.
6. **What if a provider bans or limits you?** A Google account was banned on Antigravity. Because the model is swappable and omp supports many providers, he moved on. At least 12 providers have been tried.
7. **Which effort level should I use?** Low to do, medium to review, high to plan and for hard bugs, and max almost never because it is slow and gave little gain. This is a rule of thumb. Raising effort raised the step count in every pair he measured. Effort per request is not recorded, so he cannot show a per-effort speed chart.
8. **Can a beginner copy this?** Start with one habit. When you do the same work a third time, write a skill. Then ask for proof in every PR. Skip mesh and coordinators until you really run many agents.
9. **Why did you go all in on Claude?** Quality. "Claude 5.5 series quality is GOAT." In September he ran GLM Max (his own, a cheap one-year launch plan), Codex Pro (from the office), Devin Pro and OpenCode Go. Then the Claude 5.5 series arrived and won on quality.
10. **Is prewalk worth it?** Can Bölük's test with his own models says yes for long, read-heavy tasks (cost down 39 to 47 percent for 3 to 7 points of pass rate). In Zahid's runs on short tasks it was never cheaper, and the DeepSeek target was too slow, so he turned it off. Test it on your own workload.
11. **How do many agents merge into one base branch?** His mesh plugin plus one coordinator agent. One writer per branch, and the coordinator merges in sequence after an independent review.
12. **What went wrong when agents ran for days?** Three accidents gave three guardrails (slide 56). A reset wiped the shared dev database, so the devkit refuses such resets. A Docker prune deleted about 244 unused volumes, so Docker cleanup is banned for agents. A masking tool went through 11 reviews, so reviews are capped at two rounds.
13. **How do you write specs?** Wireframe first, then folders and files, then data and flow, checked layer by layer, in one markdown file per feature (slide 34). The show-me skill draws the wireframes.
14. **Why did you try Paseo?** For easier managed worktrees. Tern replaced it (slide 60).
15. **How do you organize skills?** By area, inspired by PARA (slide 28). That gives 14 area skills. Favorites are poteto-mode and show-me.

## Notes for the outline writers

- The deck is built from `deck/content.py`. The speaker notes in `sources/outlines/presenter.md` are read by slide number, one section per slide, each with `Say:` and `Evidence:`. Dividers also have `Chat:`.
- The deck has 68 slides, and dividers are numbered slides. Timings and clocks are in the run of show above and in the presenter notes.
- Each part needs one picture per slide: a number, a diagram, or a screenshot.
- Put the claim on the opening and closing slides in the same words.
- Part 1 centers on the benchmark lab. Take its facts from `references/referensi-benchmark-lab.md`.
