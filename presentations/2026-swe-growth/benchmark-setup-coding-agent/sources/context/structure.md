# Structure: Benchmarking My Coding Agent Setup

Total slot is 90 minutes. The deck (v4) has 73 numbered slides and 86 minutes of talking. The other 4 minutes are Q&A, from 86:00 to about 90:00. The talk has an opening with a map, a journey, five principles told as five parts, a section on what is still hard, and a close. The v3 deck added 8 slides so that all 12 organizer questions are answered on slides. The v4 deck added 5 more. A parallel-agents reason for leaving the editor, a rules slide, a busy-hour slide, and the CI queue and full disk problems, so the talk grew from 68 to 73 slides and from 80 to 86 minutes.

## The claim

The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails. The opening says it on slide 4 and the close says it again on slide 71, in the same words.

## The five principles

Each principle is told through one story. The story comes first and the principle name comes after it, so the audience hears the moment before the rule.

| # | Principle (verbatim) | Story that carries it | Slides |
|---|---|---|---|
| 1 | Measure it on your own work | The fastest model on paper was the slowest in Zahid's hands. DeepSeek flash ran at about 118 tokens per second on paper, and took 476 s on the UI task against 92 s for Opus. | 15 (story), 16 (principle) |
| 2 | Do it twice, make it a skill | Autolearn made too many skills, so he merged them into 14 area skills, added a lint, and now triggers autolearn by hand. | 27 to 28 (story), 30 (principle) |
| 3 | One writer per branch | Idle agents never saw the messages sent to them. Now each branch has exactly one writer, and one coordinator merges in order. | 41 (story), 42 (principle) |
| 4 | Show proof, not "done" | The plane fix. PR #804 came with before and after recordings, and the test failed on the old code and passed with the fix. | 49 to 50 (story), 51 (principle) |
| 5 | Make it safe to walk away | Every production change goes dry run, backup, apply, then verify, as steps a human can repeat. | 57 (story), 58 (principle) |

## Narrative arc

The arc moves from proof (the phone fix), to the map of the talk, to how it got built (the journey), to five principles, to limits, and back to the claim.

| Clock | Section | Slides | Talk time | Organizer questions |
|---|---|---|---|---|
| 0-6 | Opening, with the map | 1 to 6 | 6 min | none |
| 6-15 | My journey (the demo starts at slide 13, clock 13:30) | 7 to 13 | 9 min | 1 |
| 15-30 | Part 1. Choosing models and paying for them (principle 1) | 14 to 25 | 15 min | 2, 3, 11 |
| 30-45 | Part 2. Teaching the agent (principle 2) | 26 to 38 | 15 min | 5, 7, 8 |
| 45-57 | Part 3. Many agents at once (principle 3) | 39 to 47 | 12 min | 4, 6 |
| 57-67.5 | Part 4. Trusting the result (principle 4, the demo check is slide 54 at 65:00) | 48 to 55 | 10.5 min | 9 |
| 67.5-76 | Part 5. Running it safely (principle 5) | 56 to 64 | 8.5 min | 6, 10 |
| 76-83 | What is still hard | 65 to 70 | 7 min | 12 |
| 83-86 | Close | 71 to 73 | 3 min | none |

Talk time per section is 6, 9, 15, 15, 12, 10.5, 8.5, 7 and 3 minutes, which adds to 86. Q&A is the last 4 minutes, from 86:00 to about 90:00. The organizer topic numbers are the 12 questions in `brief.md`.

## The map

Slide 6 has the headline "Today we go from my first tool to what is still hard." and shows a seven-row map. It is one list in `deck/content.py` (`MAP`) with a name and a short line per row. The same list draws a small seven-segment strip at the bottom of every divider (Part 1 to Part 5 and What is still hard), with the current segment in the accent colour and a "you are here" label. The divider titles come from `MAP`, so the part names exist in one place only. The map names no principle, because the audience has not heard the principles yet.

| Map row | Short line | Where it lands | Organizer questions |
|---|---|---|---|
| My journey | The tools I tried, and why I left | My journey | 1 |
| 1 Choosing models and paying for them | Which model, and what it costs | Part 1 | 2, 3, 11 |
| 2 Teaching the agent | Skills, memory, and plans | Part 2 | 5, 7, 8 |
| 3 Many agents at once | One coordinator, many workers | Part 3 | 4, 6 |
| 4 Trusting the result | Checks before I merge | Part 4 | 9 |
| 5 Running it safely | Servers, secrets, production | Part 5 | 6, 10 |
| What is still hard | What I have not solved yet | What is still hard | 12 |

The map slide has its own face-word limit, raised for the map layout only, as a per-layout limit in `deck/build.py`.

## Section shape

Each of the five parts runs in the same order.

1. **Divider.** "Part N" plus the part name from `MAP`, not the principle name, so the principle can come after the story. It carries one chat question to the audience, with no minutes and no "Ask chat" label, and the map strip at the bottom.
2. **Story.** One or two slides about a real moment. The number comes after the story, never stacked on it.
3. **Principle.** The principle name, large, with at most one plain line under it.
4. **Proof.** One to eight slides, each with one idea and one picture. Part 1 has eight (slides 17 to 24), because it matches the title and keeps every benchmark slide.
5. **Try this.** One line the audience can do this week.

The opening, the journey and the close have no divider and no principle slide. What is still hard has a divider (slide 65), drawn like the Part dividers, and no principle slide.

## Section details

### Opening (0-6 min, slides 1 to 6)

**Key theme.** The payoff first. A real bug, fixed and proven from a phone, so the audience asks "how". Then the map, so each person sees the plan of the talk. Organizer question numbers stay in these notes and never appear on a slide or in a `Say:` line.

**Slides.**
- 1. Title.
- 2. The 9:29 phone screenshot. Zahid was on board the plane before takeoff, using the Tern Android app.
- 3. PR #804 timeline. QA flagged the bug at 08:52, Zahid pasted it in at 09:26 from his phone, the agent recorded the bug at 09:29, and QA passed the fix at 09:57, 65 minutes after the warning (times in WIB, in the notes).
- 4. The claim, with the model in grey and the four parts (skills, proof, coordination, guardrails) with equal weight.
- 5. Can Bölük, the author of omp, on X: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." The slide shows the article screenshot. The link is on the Links slide (72).
- 6. The map. Headline "Today we go from my first tool to what is still hard." Seven rows, one per section of the talk, each with a name and a short line. Zahid reads the rows, says the audience can ask in chat at any time, and says he will answer at the end.

**Transition.** "To explain how that was possible, I need to show how I got here, and it was not a straight line."

### My journey (6-15 min, slides 7 to 13)

**Key theme.** Every tool switch had a concrete reason, and the reasons point to the same needs: running many agents without a heavy app, extensibility and quality.

**Slides.**
- 7. A six-event timeline, with no date scale, because the folder dates on disk conflict with the order Zahid gave. 2022 VS Code and Copilot, at launch (Zahid confirmed he started when Copilot became generally available, 2022-06-21, long before Claude Code existed). 2025 Claude Code in VS Code. July 2025 Gemini tooling. October 2025 OpenCode with OmO (token hungry). December 2025 Ghostty, Neovim and Amp (lighter). February 2026 omp (extensible, the last one, highlighted). Antigravity has no dated event, so it is not on the timeline and has its own slide. Chat question 1 is asked here, from the notes ("Which coding agent do you use today?").
- 8. Running agents in parallel pushed him out of the editor. VS Code is one agent and a heavy app. The terminal (Ghostty and Neovim) means many agents and less memory. His own reason, not measured, so no memory number is quoted.
- 9. Antigravity. The first tool Zahid used with a proper plan mode, memory, design artifacts and an agent-first screen instead of an editor-first one. His Google account was banned, and omp still uses its image model.
- 10. A harness is everything around the model: tools, context, memory and rules, drawn as a hub with the model in the middle.
- 11. Why omp. He can extend it, so he fixes his own problems. Plugins he writes, autolearn, Hindsight memory, multi-provider logins, good compaction. "I forgot why I left Amp" stays as a joke, then the real answer.
- 12. From one chat at a time to many agents at once. Requests per month, 2.2k in May to 270k in October.
- 13. Live demo start. Pick a small real Alkhidmah issue, create a worktree, send one prompt from the Tern Android app, and leave it running. Clock 13:30.

**Boundaries.** Dormant tools appear only as history, one line each. Do not teach how to use them. The terminal journey is in Part 5 (slide 63). Do not draw the journey to a date scale, and do not say Claude Code came before Copilot or Gemini. The dates in the notes of slide 7 are folder dates and product launch dates, not an adoption calendar.

**Transition.** "Whatever tool I used, the question was always the same. Which model does which job, and what does it cost?"

### Part 1. Choosing models and paying for them (15-30 min, slides 14 to 25)

**Chat question (slide 14).** "Per token or per subscription? Tell us in chat."

**Story (slide 15).** The fastest model on paper was the slowest in his hands. The bars show seconds on the UI task, Opus 5.5 low 92 s, Sonnet 5.5 medium 94 s, Haiku 5.5 medium 170 s, DeepSeek flash low 476 s. DeepSeek took 28 steps against 9 for Opus. The September formula had no term for steps.

**Principle (slide 16).** Measure it on your own work.

**Proof.**
- 17. Each job gets its own model. Live config: chat is Opus at low effort, plan and hard bugs are Opus at high, UI design is Sonnet at high, review is Opus at medium, and exploring is Haiku. Rule of thumb: low to do, medium to review, high to plan and for hard bugs, max almost never because it is slow and gave little gain. The `designer` agent appears in 316 session files, mostly UI redesign tasks.
- 18. Every model passed, so speed and price decided. The bench was two easy tasks, three runs each, hidden-check graders, medians. Every model passed 126 of 126 checks.
- 19. Thinking harder made the agent take more steps. Raising effort raised the step count in every pair (Spark slot finder 9 to 23, DeepSeek UI 28 to 40). The cause, re-checking, is an inference. "More steps probably means a longer wait" is also an inference, because high-effort runs were not timed.
- 20 and 21. Prewalk, a handoff from the big model to a cheaper one at the first edit. His first setup (14 Oct) was Opus 5.5 low planning and Haiku 5.5 high editing. On his long tasks it was cheaper, but slower, and tasks took too long to finish (his own account, no numbers for that setup). On 23 Oct he moved his task agents to Sonnet 5.5 medium with no prewalk, because UI work needed a better model than Haiku. On the short bench tasks it cost the same or more. Opus 5.5 low alone $0.39 (UI) and $0.22 (slot finder) against $0.48 and $0.35 with prewalk. Sonnet 5.5 medium alone $0.24 and $0.17 against $0.36 and $0.17 (a tie) with prewalk. In the bench, prewalk was slower in every pair with a solo run to compare: Opus low 92 s to 136 s (UI) and 54 s to 84 s (slot finder), Sonnet medium 94 s to 157 s and 84 s to 127 s. A log estimate at 50 or more turns, Sonnet medium alone about $2.58 a task against $1.63 into Haiku medium, is an estimate from uncontrolled work, not graded. Second try on 24 and 25 Oct, Haiku then DeepSeek v4.1 flash, really slow. Can Bölük's own test, with his models, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not Zahid's.
- 22. $7,300 worth of tokens, and he paid about $200. October 2026 was 270k requests and 41B tokens. The $7.3k is list price, not money paid. 97 percent of tokens were cache reads.
- 23. When Claude 5.5 quality moved, he moved. The September portfolio (GLM Max, Codex Pro, Devin Pro, OpenCode Go) became 2x Claude Max plus OpenCode Go. At least 12 providers were tried.
- 24. Three money tips from his own bills. A flat plan plus prompt caching. A cheap model (Haiku) to search and a strong one (Opus at high) to plan. Test a cost trick on your own work before you trust it, because prewalk was cheaper on his long tasks, but slower. Organizer question 11.

**Try this (slide 25).** Time one real task of yours on two different models.

**Source of facts.** Every number is in `references/referensi-benchmark-lab.md` or in the notes of `presenter.md`. The value formula is cut from the slides and lives in the notes of slide 15.

**Transition.** "A fast, well-chosen engine still forgets everything tomorrow. The next part is what the agent knows."

### Part 2. Teaching the agent (30-45 min, slides 26 to 38)

**Chat question (slide 26).** "Which task do you repeat with your agent more than twice? Tell us in chat."

**Story (slides 27 and 28).** Autolearn made too many skills. He merged them into 14 area skills, added a lint that found 0 errors, and now triggers autolearn by hand after a session that taught something.

**Principle (slide 30).** Do it twice, make it a skill. The rule, in his words: "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."

**Proof.**
- 29. One skill per area, like PARA. He organizes skills by area, inspired by Tiago Forte's PARA method (Projects, Areas, Resources, Archives). His skills follow the Areas box, which gives the 14 area skills. Favorites are poteto-mode and show-me. This slide sits between the story and the principle. Organizer question 8.
- 31. Skills hold how to do a thing, and memory holds what he did and decided.
- 32. Memory as a journey. Mnemopi, then Hindsight in June 2026, Cognee tried in September and removed in October. Compaction is a sentence in the notes, and the first thing to cut.
- 33. Loose prompts, because the files around them hold the structure.
- 34. A rule steps in the moment the agent types a risky command. A rule is a small file. Some are always in the prompt (check every layer, PR body shape, skill layout). Others wait for a pattern, such as pytest or vitest without a memory cap. omp calls this TTSR, time traveling stream rules. It watches the streamed output, stops on a match, injects the rule, and the agent rewrites the command. Rules stepped in 4,635 times since June. 1,424 were his two memory caps (test-runner-resource-cap 1,187 and pytest-resource-cap 237). The rest were omp's own TypeScript rules (ts-no-tiny-functions 1,691, ts-set-map 847, and others). This is where the 38 GB test run ends up. One uncapped run once took 38 GB of RAM, and the rule is the fix.
- 35. poteto-mode, 25 principles, and the one he added, check every layer.
- 36. Before any code, the agent draws the screen. A neutral wireframe, then folders and files, then data and flow, checked layer by layer, saved in one markdown file per feature so subagents do not wander. The show-me skill draws the wireframes. Organizer questions 5 and 8.
- 37. Why beads was dropped. Agents got smarter, beads is not really human-readable, and they retain context better now. No hooks for tasks. GitHub issues and the coordinator's ledger hold the work, and CI does the checking.

**Try this (slide 38).** Write the skill the third time you repeat a task.

**Transition.** "One agent with good knowledge is useful. The real jump came when I ran many at once."

### Part 3. Many agents at once (45-57 min, slides 39 to 47)

**Chat question (slide 39).** "How many agents do you run at once? Tell us in chat."

**Busy hour (slide 40).** Right after the divider, so the chat answers have a number to compare with. On a busy hour, 4 to 9 agents work at once. 39% of his working hours had 4 to 9 agents, and the typical hour had 3. The bars show hours per agent count, 1 to 9 and 10+. This only works because the agents have full control of the dev infra. They start the stack, seed it and test it without him. A folder is a worktree or repo, so this counts workstreams, not processes. Organizer question 4.

**Story (slide 41).** Idle sessions never see a mesh message, so a coordinator's broadcast was lost on agents whose sessions had ended. The coordinator wrote the lesson in its own ledger. Messages are not enough, each branch needs exactly one writer.

**Principle (slide 42).** One writer per branch.

**Proof.**
- 43. Every agent task gets its own copy of the repo. A worktree is its own copy of the repo. The `tern-wt list` output had 101 worktrees, from the tern-worktrees plugin he wrote.
- 44. Mesh lets agents see what the others are holding. Three agent cards re-typeset from the real `mesh peers` capture, with the SHIP row holding the production release.
- 45 (optional, the only one in the deck). He wrote the mesh plugin himself, and the plugin list shows it running.
- 46. One coordinator merges after an independent review. SHIP is a normal omp session. Its ledger has 353 decisions from 2 to 7 November. Workers send `MERGE-READY #<pr> <full sha>`, the coordinator freezes the head, an independent reviewer writes a verdict, and a failure gets one fix round. Base-branch coordination is solved, not open.

**Try this (slide 47).** When you run two agents, give each its own worktree.

**Transition.** "Many agents write a lot of code. How do I trust it? Remember the plane."

### Part 4. Trusting the result (57-67.5 min, slides 48 to 55)

**Chat question (slide 48).** "Which part of your agent's work do you still check by hand? Tell us in chat."

**Story (slides 49 and 50).** "Remember the plane? This is the proof that came with that fix." The PR #804 before and after frames, then the test that failed on the old code and passed with the fix. Three failed, three passed.

**Principle (slide 51).** Show proof, not "done". The proof ladder is a recording for UI, command output for API or CLI, a run link for CI, and the test command when nothing is visible. The PR body shape (Why, proof, Not verified) is in the notes.

**Proof.**
- 52. Five checks run before he looks. LSP diagnostics after every edit, lint and type checks, tests shaped like the Testing Trophy (plus a formal-verification skill for risky logic), reviewer agents that scale with risk, and Zahid, who still checks UI and feel by hand. Organizer question 9.
- 53. A second agent checks the work and freezes its verdict at one commit. The review report is from PR #580.
- 54. Demo check at clock 65:00. Open the demo PR from the phone and walk its body for Why, proof, and an honest "Not verified" line. PR #804 has no "Not verified" line, so say that aloud if it is the fallback. Time-box to 90 s.

**Try this (slide 55).** Ask for a before and after clip in your next PR.

**Transition.** "That is proof. Now, running it safely."

### Part 5. Running it safely (67.5-76 min, slides 56 to 64)

**Chat question (slide 56).** "Where do your agents run: laptop, server or cloud? Tell us in chat."

**Story (slide 57).** Every production change goes dry run, backup, apply, then verify. Production is read-only by default, and the dry-run output becomes the runbook.

**Principle (slide 58).** Make it safe to walk away.

**Proof.**
- 59. Three accidents gave three guardrails, from the coordinator's ledger. A reset in the main checkout wiped the shared dev database, and the devkit now refuses any reset path that reaches it (PR #574). A reviewer agent's Docker prune deleted about 244 unused volumes, and Docker cleanup is now banned for every agent. One masking tool went through 11 reviews, and there is now a two-round review cap. Chat question from the notes: "Has an agent ever deleted something it should not have?" Organizer question 6.
- 60. Three layers protect his secrets. omp hides values from the model, damage-control rules block destructive commands such as `rm -rf`, force push and `DROP`, and Infisical (machines) and Bitwarden (people) store the secrets.
- 61. Proof runs away from his workstation, and production is read-only.
- 62. One command takes a fresh worktree to a running stack.
- 63. The terminal journey. OpenChamber, Ghostty, herdr, Paseo (tried for easier managed worktrees), and now Tern.

**Try this (slide 64).** Make every production change start with a dry run.

**Transition.** "That is the setup that works. Now the part that does not."

### What is still hard (76-83 min, slides 65 to 70)

**Key theme.** Honest limits. Four open problems and the plan for the fourth, one short slide each, after a divider. The divider (slide 65) asks "What still breaks for you? Tell us in chat." Its spoken line names the four problems and says that base branches used to be on this list and that Part 3 showed how the coordinator solved it.

- 65. Divider, What is still hard, with the map strip.
- 66. A proof clip shows a button works, not that the screen looks right. Agent-built UI still needs design skills and his feedback. He still checks UI, visual feel and UX by hand. Reuse the Part 4 answers here.
- 67. Nine agents means nine PRs, and CI becomes the queue. One day in November, 5 November in WIB, the alkhidmah repo ran 538 CI runs (previews, checks, end-to-end tests). 1 in 10 runs took 16 minutes or more (90th percentile 16.0 minutes that day). Larger runners and spreading load over free runners are experiments, nothing is settled.
- 68. Setting up the environment and the seed data for a worktree dropped from 652 s to 171 s, and every new worktree still pays 171 s. The analytics app at work is heavier, a large time series stack with a long seed, and its seed time is not measured.
- 69. Every branch wants its own full stack, and the disk is full. 89% of a 1 TB SSD used (777 GB of 902 GB). Docker holds 447 GB (images 173.7, volumes 114.8, build cache 158.7, which sums to 447.2). One uncapped test run took 38 GB of RAM, shown muted because it is RAM, not disk. This replaces the old memory slide. The memory rule itself is on slide 34.
- 70. Next, stacks he can pause and wake up. One VM per stack, paused when idle, woken when an agent needs it. A paused VM still costs disk, so a bigger SSD comes first. A plan, not a result. Nothing is shipped.

**Boundaries.** Base-branch coordination is not an open problem. It belongs to Part 3 as solved. Slide 70 is a plan, so say so plainly and do not quote any result for it.

**Transition.** "Let me bring it back to the claim."

### Close (83-86 min, slides 71 to 73)

**Key theme.** One claim, one action.

- 71. The five principles as five short lines, with the claim. The one action: write a skill the third time you repeat a task.
- 72. Links, public URLs only, checked on 2026-11-06. The omp repo, the prewalk article, Can Bölük's article on X, and two of Zahid's plugins.
- 73. Questions, in chat or out loud. Q&A runs from 86:00 and has 4 minutes.

## Content boundaries

Six rules decide what goes on a slide. They were set in v2 and still hold in v4. They are checked by the lint in `deck/build.py`.

1. **One audience.** Every slide speaks to the people on Zoom. Sources, dates, caveats, timing and chat cues live in the speaker notes (`sources/outlines/presenter.md`).
2. **No source lines.** A quote carries the speaker's name next to it. The one Links slide (72) is for anyone who wants to dig.
3. **Headlines in Zahid's words.** About 10 words, hard cap 12. Plain English, no bench jargon such as "arm", "median", "API-equivalent" or "head-to-head". Say "steps", not "turns", and "if I paid per token" where list price is needed.
4. **One picture per slide.** A screenshot, one or two big numbers, or a simple diagram. About 25 words on the face besides the headline, hard cap 30. The map slide has its own limit of about 60 words.
5. **One story per section.** Divider, story, principle, proof, then one thing to try.
6. **The lint enforces it.** It fails on source lines, file paths, ISO dates, "Minute N", "Ask chat" and the jargon list. It also checks headline length, face word count, and a `Say:` line on every slide and an `Evidence:` line on every slide with a digit. Slide faces never show organizer question numbers.

**Include.**
- Real numbers from the usage stats, labeled in the notes as API-equivalent (list price, not money paid).
- Real tool history with reasons, including the ones Zahid cannot fully remember.
- PR #804 as the reference story, opening on slides 2 and 3 and called back on slides 49 and 50.
- Zahid's own plugins, as examples of extensibility.
- Open problems, stated plainly.

**Exclude.**
- Any secret value, token, IP, email, or phone number.
- Customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- Any secret-handling incident. Secrets appear only as practice. The three accidents on slide 59 are agent-run reset, Docker cleanup and review-loop incidents from the ledger, and none involves a secret.
- Instructions for dormant tools. Antigravity, OMO, Amp, Cognee, Paseo, and beads appear only as history and lessons.
- Effort claims beyond the October bench and Zahid's own rule. Effort level is not recorded per request in the usage stats.
- Account counts of other people and quota percentages from the subscription notes.
- Presenting base-branch coordination as an open problem.
- Real `docs/plans/**` wireframes. Slide 36 uses a newly drawn neutral wireframe.
- Teammate names beyond first names already public in PRs. Otherwise write "QA".
- Numbers, quotes or links that are not in `content.py`, `presenter.md` or `references/`.

## Demo checkpoints

| Clock | Slide | Action | Fallback |
|---|---|---|---|
| 13:30 | 13 | Start. Choose a small real Alkhidmah issue, create the worktree, send one prompt from the Tern Android app, and show the phone screen mirrored next to the laptop. Then go straight to slide 14. | Play the recorded backup. |
| 65:00 | 54 | Check. Open the demo PR and show its body, proof, and gates. | Show the recorded result and the PR #804 body as the reference. |

Say aloud that the demo runs while Zahid talks about other things, which is how he works. The recording is never named on a slide.

## Q&A prep

Q&A has only 4 minutes, from 86:00 to about 90:00, so most answers should point to a slide.

1. **Is it worth about $200 per month?** In October 2026 the same work would price at about $7.3k at list price, and he paid about $200. 97 percent of tokens were cache reads. The API-equivalent figure is list price, not money paid. Slide 24 has three money tips.
2. **Why not stay with Claude Code?** He started with Copilot in VS Code, then used Claude Code inside VS Code, so it was an early step, not a rejection. Extensibility was the main reason for omp. omp lets him write plugins such as the mesh and the account router. It also has multi-provider logins, autolearn, Hindsight memory, and compaction he trusts. Claude Code is a fine start for most people.
3. **Is it safe to let agents near production?** Production is read-only by default. Writes go through dry run, backup, apply with expected counts, and verify. Damage-control rules block destructive commands, and secrets are obfuscated and kept in Infisical or Bitwarden.
4. **Do you read the code?** Five checks run first (slide 52). Independent reviewers, gates, and proof requirements do the first pass. He still checks UI feel and UX by hand.
5. **Why did you drop beads?** Agents got smarter, beads is not really human-readable, and omp's compaction plus the memory layer retain context better now. GitHub issues plus coordinator ledgers replaced it, and CI does the checking.
6. **What if a provider bans or limits you?** A Google account was banned on Antigravity. Because the model is swappable and omp supports many providers, he moved on. At least 12 providers have been tried.
7. **Which effort level should I use?** Low to do, medium to review, high to plan and for hard bugs, and max almost never because it is slow and gave little gain. This is a rule of thumb. Raising effort raised the step count in every pair he measured. Effort per request is not recorded, so he cannot show a per-effort speed chart.
8. **Can a beginner copy this?** Start with one habit. When you do the same work a third time, write a skill. Then ask for proof in every PR. Skip mesh and coordinators until you really run many agents.
9. **Why did you go all in on Claude?** Quality. "Claude 5.5 series quality is GOAT." In September he ran GLM Max (his own, a cheap one-year launch plan), Codex Pro (from the office), Devin Pro and OpenCode Go. Then the Claude 5.5 series arrived and won on quality.
10. **Is prewalk worth it?** Can Bölük's test with his own models says yes for long, read-heavy tasks (cost down 39 to 47 percent for 3 to 7 points of pass rate). In Zahid's own work it was cheaper on long tasks but slower, and on short bench tasks it cost the same or more and was slower in every pair with a solo run to compare. He moved his task agents to Sonnet medium with no handoff because UI work needed a better model. A second try with DeepSeek was really slow. Test it on your own workload.
11. **How do many agents merge into one base branch?** His mesh plugin plus one coordinator agent. One writer per branch, and the coordinator merges in sequence after an independent review.
12. **What went wrong when agents ran for days?** Three accidents gave three guardrails (slide 59). A reset wiped the shared dev database, so the devkit refuses such resets. A Docker prune deleted about 244 unused volumes, so Docker cleanup is banned for agents. A masking tool went through 11 reviews, so reviews are capped at two rounds.
13. **How do you write specs?** Wireframe first, then folders and files, then data and flow, checked layer by layer, in one markdown file per feature (slide 36). The show-me skill draws the wireframes.
14. **Why did you try Paseo?** For easier managed worktrees. Tern replaced it (slide 63).
15. **How do you organize skills?** By area, inspired by PARA (slide 29). That gives 14 area skills. Favorites are poteto-mode and show-me.
16. **Why did you leave VS Code?** Running agents in parallel. One agent in an editor is fine, but four agents in four editors is not, so he moved to Ghostty and Neovim so the memory goes to the agents, not the windows (slide 8). It is his own reason and it is not measured, so quote no memory number.
17. **How many agents run at once?** 3 in a typical hour. 39% of his working hours since September had 4 to 9, and 13 hours had 10 or more (slide 40). It works because the agents control the dev infra themselves. A folder is a worktree or repo, so this counts workstreams, not processes.
18. **What are rules, and how are they different from skills?** A rule is a small file. Some are always in the prompt. Others wait for a pattern, so when the agent types pytest without a memory cap, omp (TTSR) stops the stream, adds the rule, and the agent rewrites the command. 4,635 injections since June, 1,424 of them his two memory caps (slide 34). A skill is how to do a thing and loads when the work matches.
19. **Is CI a bottleneck?** Yes. One day in November his alkhidmah repo ran 538 CI runs and 1 in 10 took 16 minutes or more. He is testing larger runners and spreading load over free runners. Nothing is settled (slide 67).
20. **What is next for your infra?** A plan, not a result. Each stack in its own VM, paused when idle and woken when an agent needs it. A paused VM still takes disk, so a bigger SSD comes first. The disk is at 89%, and Docker holds 447 GB (slides 69 and 70).

## Notes for the outline writers

- The deck is built from `deck/content.py`. The speaker notes in `sources/outlines/presenter.md` are read by slide number, one section per slide, each with `Say:` and `Evidence:`. Dividers also have `Chat:`.
- The deck has 73 slides, and dividers are numbered slides. Timings and clocks are in the run of show above and in the presenter notes.
- Each part needs one picture per slide: a number, a diagram, or a screenshot.
- Put the claim on the opening and closing slides in the same words.
- Part 1 centers on the benchmark lab. Take its facts from `references/referensi-benchmark-lab.md`.
