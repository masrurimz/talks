# Benchmarking My Coding Agent Setup: One Engineer, Many Agents
## Presenter outline, live talk for SWE Growth

**SWE Growth community (Mas Zikrul), online on Zoom**
**90 minutes. All slides in English.**
**Speaker: Zahid**

## Notes for the presenter
- Total plan is 48 numbered slides, one unnumbered before and after page that follows slide 3, and 7 section dividers (56 pages), and 72 minutes of talking. The other 18 minutes are slack (0 to 3 minutes per section), the live demo, and 6 minutes of Q&A at the end. The build lint checks that the slide timings add up to 72 and that each clock value follows from the one before.
- Pillar 1 is the benchmark lab (slides 12 to 17). It is the part that matches the title, so protect it. Cut elsewhere first.
- Slide timing is minutes of talking. The clock value is the section start plus the running total. It is the target, not a promise. A divider resets the clock to its own minute.
- Label **[Wajib]** means keep the slide. Label **[Opsional]** means cut it if time is short.
- Rule for every slide. One idea, at most three key points, and the picture does the work.
- Say "API-equivalent" every time a dollar figure appears. It is the list price of the tokens, not money paid.
- Dividers carry the section name, the minute, a progress strip and one chat question. The claim sentence of a section is the headline of its first content slide.
- The claim, which every section supports or limits. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."
- Live demo checkpoints. Start at about minute 15 (slide 10). Check the PR at about minute 60 (slide 37). A recording of the full run is ready, and it is never named on a slide. The phone screen is shared next to the laptop.
- Delivery cues sit at the top of the notes under "Delivery:". Every section opener, both demo slides, the close and the Q&A slide have one.

## Run of show

| Clock | Section | Slides | Talk time | Organizer questions |
|---|---|---|---|---|
| 0:00 to 7:00 | Cold open | 1 to 7 | 7 min | none |
| 7:00 to 15:00 | The journey | 8 to 9 | 5 min | 1 |
| 15:00 to 32:00 | Pillar 1, the benchmark lab (demo starts) | 10 to 19 | 15 min | 2, 3, 11 |
| 32:00 to 47:00 | Pillar 2, knowledge | 20 to 29 | 14 min | 5, 7, 8 |
| 47:00 to 65:00 | Pillar 3, the crew (reset at 55:00, demo check) | 30 to 38 | 17 min | 4, 6, 9 |
| 65:00 to 74:00 | Infra and guardrails | 39 to 43 | 7.5 min | 10 |
| 74:00 to 79:00 | Open problems | 44 to 46 | 5 min | 12 |
| 79:00 to 90:00 | Close and Q&A | 47 to 48 | 1.5 min plus 6 min Q&A | none |

Total talk time is 72 minutes (7 + 5 + 15 + 14 + 17 + 7.5 + 5 + 1.5). Slack is 12 minutes inside the windows plus 6 minutes of Q&A.

## Cut order if time is short
Cut in this order. Each cut saves about the time shown.
1. Slide 25 (compaction), 1 min. Say one sentence on slide 24.
2. Slide 40 (terminal journey), 1 min. Say the five names in one breath.
3. Slide 33 (long runs, one writer per branch), 1 min. Slide 34 carries the loop.
4. Slide 41 (per-worktree setup), 1 min.
5. Slide 29 (why beads was dropped), 1 min. Say one sentence on slide 26.

The core stays intact. The claim, the benchmark lab (slides 12 to 17), the cost slide, skills, mesh and the coordinator loop with base-branch coordination, the proof ladder, and open problems.

## Coverage of the 12 organizer questions

| # | Question | Slides |
|---|---|---|
| 1 | Tool evolution and why each switch | 8, 9 |
| 2 | Model routing per role | 11, 13 |
| 3 | Effort and thinking level | 11, 15 |
| 4 | Orchestration and parallel agents | 30, 31, 32, 34, 35 |
| 5 | Task and spec management, beads | 26, 29 |
| 6 | Long-horizon runs and guardrails | 33, 34 |
| 7 | Memory and context | 20, 23, 24, 25 |
| 8 | Own skills, favorites | 21, 22, 27, 28, 31 |
| 9 | Review and quality gate, manual checks | 28, 36, 38, 44 |
| 10 | Supporting infra | 39, 40, 41, 42, 43 |
| 11 | Cost and subscription strategy | 12, 13, 14, 16, 17, 18, 19 |
| 12 | Open problems | 44, 45, 46 |

---

# Section 1. Cold open (0:00 to 7:00)

## Slide 1 [Wajib] Title
**Timing:** 0.5 min (clock 0:00)
**Delivery:** Look at the lens, not at the slide. Say the throughline in one sentence: the model is swappable, and the setup around it ships the work. Speak at 130 to 150 words per minute.
**Key points**
- Benchmarking My Coding Agent Setup: One Engineer, Many Agents.
- SWE Growth community, online.
- Zahid.

**Visual hint:** Title card. Dark background, one line of subtitle. No logos of model vendors.
**Speaker note:** Thank the organizer and say hello. Say this is a casual talk about one real setup, with real numbers, including what still does not work.

## Slide 2 [Wajib] The 9:29 phone screenshot
**Timing:** 1.5 min (clock 0:30)
**Key points**
- Tuesday, 27 October 2026, 9:29 in the morning, WIB. I was already on board the plane, before takeoff.
- An omp session on a phone, chat style, with a mic in the composer.
- The agent had just reproduced a bug on a real stack.

**Visual hint:** Full phone screenshot on the right, serial numbers blurred, 9:29 and the mic circled. Two enlarged crops on the left, each with a direct label: "9:29 WIB" and "voice prompt".
**Speaker note:** "This is my phone at 9:29. I was sitting in the plane, before takeoff. I spoke the prompt, and the agent had just reproduced a bug on a real stack. Let me show you how I got there."

## Slide 3 [Wajib] PR #804, from QA warning to QA pass in 65 minutes
**Timing:** 1.5 min (clock 2:00)
**Key points**
- 08:52 QA posts a warning on an already approved PR. Clicking a draft sensor opens the edit modal.
- 09:26 I paste the finding into the session from the phone. "Fix those own changes proof and update pr". 09:29 before recording, 09:31 PR body updated.
- 09:57 QA passes. The markers are spaced by clock time, so the 34 minute gap and the 26 minute gap are visible.

**Visual hint:** Proportional timeline with five markers (08:52, 09:26, 09:29, 09:31, 09:57). The three close events share one label under the axis. Source is the PR #804 loop in the mesh reference. The next page has no number and takes 15 seconds of this slide's time. It shows the draft click frame from the before clip and from the after clip, each labelled Before and After on the picture.
**Speaker note:** "QA found one more thing on a PR that was already approved. I pasted it into the same session. The agent recorded a before clip, fixed it, recorded an after clip and updated the PR body. QA passed the PR 65 minutes after the warning, and most of that time I was not touching it."

## Slide 4 [Wajib] The claim, and the four parts around any model
**Timing:** 1.0 min (clock 3:30)
**Key points**
- "The model is a swappable part. What lets one engineer ship from a phone is the setup around it."
- Four parts around the model: skills, proof, coordination, guardrails. They carry equal weight. The model is drawn in grey on purpose.
- Three pillars today: the engine, knowledge, the crew. Then infra, open problems and one action to take home.

**Visual hint:** A grey box "Model" in the center with four equal cobalt boxes around it. No pillar strip.
**Speaker note:** State the claim slowly. Tell the audience that every section either supports it or shows where it breaks. Promise one action to take home at the end.

## Slide 5 [Wajib] What is a harness?
**Timing:** 1.0 min (clock 4:30)
**Key points**
- A harness is the program around the model. It gives the model tools, context, memory, and rules.
- Claude Code, Cursor, OpenCode, Amp and omp are harnesses. Claude, GPT and GLM are models.
- Swap the model and keep the harness, or the other way around. This talk is about the harness.

**Visual hint:** Two-layer diagram. Top "harness: tools, context, memory, rules" with the audience's own tools. Bottom "model".
**Speaker note:** Many of you use Claude Code or Cursor, so this is a short refresher. Keep it to two sentences and move on. The next quote now reads as evidence, not jargon.

## Slide 6 [Wajib] Six terms before they appear
**Timing:** 1.0 min (clock 5:30)
**Key points**
- Harness, worktree, skill, mesh, SHIP, poteto-mode. Each one gets one line now, and a full slide later.
- Worktree is a separate checkout of a repo, one per task. Skill is a file the agent loads when needed.
- Mesh is my plugin so agents see each other. SHIP is my coordinator agent. poteto-mode is my agent-style skill.

**Visual hint:** Two columns of three terms, each with a one-line gloss. Pre-training slide, after Mayer: name the key terms before the lesson uses them.
**Speaker note:** Say each term aloud, slowly, with its gloss. Tell the audience they will hear these six words again, and they do not need to remember more than the gloss. Many listeners are working in a second language, so do not rush.

## Slide 7 [Wajib] Outside evidence for the claim
**Timing:** 0.5 min (clock 6:30)
**Key points**
- Can Bölük, the author of omp: "I improved 15 LLMs at coding in one afternoon. Only the harness changed."
- This is the claim of the talk from someone with no reason to flatter my setup.

**Visual hint:** The real X article header, cropped to the hero image and the title. A box marks the title, which is the quote word for word. The headline says "article on X", not "post".
**Speaker note:** "This is the author of omp, not me. He changed only the harness and moved 15 models." The quote is the exact title of his X article, checked against the live page on 2026-11-05. Say "article", not "post".

---

# Section 2. The journey (7:00 to 15:00)

## Slide 8 [Wajib] My tool journey and why each switch
**Timing:** 3.0 min (clock 7:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- Gemini tooling on the Mac (m5) from July 2025, Claude Code from 2025-10-19, OpenCode with oh-my-opencode from 2025-10-20, Amp from 2025-12-22 to 2026-03-16, omp from 2026-02-23 on m5 and as the main tool on x1 since 2026-03-07.
- One word per switch: Claude Code, quality. OpenCode, bans. Amp, "I forgot why I left Amp". omp, extensible.
- Antigravity is not on the chart because I have no date. Good free usage, plan annotations, session artifacts. Then it was heavy, quality and limits got worse, and my Google account got banned.

**Visual hint:** Gantt chart from July 2025 to November 2026. Bars overlap where I used two tools (Amp and omp). The reason is one word at the end of each bar. A bar ends at the next tool's first session, except Amp, whose end is dated.
**Speaker note:** "This is from my own files, not from memory. The dates are the first session I find for each tool." Point out the overlap between Amp and omp. Be honest. The reasons are about my workload and the time, not a verdict on the tools. Claude Code, some tasks were not good enough and I wanted more efficiency. OpenCode, many issues and Claude and OpenAI subscriptions were getting banned. Amp was mature, with cross-agent messages and spawned agents, and I mostly used a proxy (CLIProxyAPI) for very large usage. Claude Code to OpenCode was within one day by first session, so its bar is a sliver. OpenCode had 215 sessions on m5 and a web UI called OpenChamber.

## Slide 9 [Wajib] Why omp
**Timing:** 2.0 min (clock 10:00)
**Key points**
- "I forgot why I left Amp, but omp is better because" it is extensible. I write my own plugins.
- Autolearn, Hindsight memory, multi-provider subscription logins, and good compaction.
- That extensibility is why the later slides exist. Mesh, the org account router and the worktree plugin are all mine.

**Visual hint:** Five cards (plugins, autolearn, memory, logins, compaction) with plugins highlighted. Add one small screenshot of `ls ~/.omp/agent/extensions/` when it is captured.
**Speaker note:** Say the joke about forgetting once. Then give the real answer. A harness you can extend lets you fix your own problems, which is why the setup keeps moving. Autolearn means the agent writes a skill after a session.

---

# Section 3. Pillar 1, the benchmark lab (15:00 to 32:00)

Pillar 1 is built on `references/referensi-benchmark-lab.md`. The story is one engineer who measures. A model per role, a value formula, a bench of his own, a finding about effort, a handoff trick he tested and turned off, and a subscription journey that ended with "all in on Claude 5.5".

## Slide 10 [Wajib] Live demo, start from the phone
**Timing:** 1.0 min (clock 15:00)
**Delivery:** Narrate each step and name the expected output before you press send. Time-box this to 90 s. If the run is slow or fails, say exactly: "The live run is slow today, so here is the recording from this morning." Then play the recording and move on. Do not debug live.
**Key points**
- A small real issue from the Alkhidmah backlog.
- I send one prompt from the Tern Android app. The agent works while I keep talking.
- Goal is a PR with proof in the body. We check it at about minute 60.

**Visual hint:** Live. Phone mirror next to the laptop, Tern session open, the prompt typed in my own style. The slide shows the prompt text only.
**Speaker note:** Say that the audience sees my real phone. Send the prompt, then go straight to the next slide. The recording of the full run is cued in a second window, and it is not named on any slide.

## Slide 11 [Wajib] Model routing per role and the effort rule
**Timing:** 1.5 min (clock 16:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline.
**Key points**
- Each role has a model and an effort level. Default is Opus at low. Plan is Opus at high. Reviewer is Opus at medium. Task agents run Sonnet at medium. Scout and sonic run Haiku, the fast model.
- Effort rule. Low for execution, high for plans and hard debugging, medium for review, max almost never. The next slides test the first half with a bench.
- Speed since October (Anthropic, average per request) is Haiku 130 output tokens per second, Sonnet 95, Opus 66. A fallback chain and a second account take over when a quota runs out.

**Visual hint:** Table of roles with model and effort. One speed line under it. Add the `modelRoles` block from `config.yml`, cropped so no account details show.
**Speaker note:** "I do not pick a model per prompt. I pick it once per role. The expensive model plans and reviews. The cheap fast model explores. Effort is not recorded per request, so I cannot chart it from my usage. That is why I built a bench." Time to first token is 2.6 seconds for Opus as main against 1.4 for Haiku.

## Slide 12 [Wajib] The value formula
**Timing:** 1.5 min (clock 17:30)
**Key points**
- A price per million tokens misleads, because a subscription changes what a token costs. Value Multiplier is quota dollars divided by subscription cost. Effective price per 1M is blended price divided by the multiplier.
- Value Score is the benchmark divided by the effective price. The speed-adjusted score also multiplies by tokens per second.
- Rules. One common benchmark only (Terminal-Bench 2.1). Count the accounts. `cost_total` is API-equivalent, not spend. GLM is verbose, so compare tokens used too.

**Visual hint:** The four formula lines in a code block. Under it one September row, DeepSeek V4.1-Flash (90.6, about 118 tokens per second) against GLM-5.3 (88.2, about 42).
**Speaker note:** "This is how I decided what to buy. It is a spreadsheet, not a feeling." Say the September numbers are a point in time. Plant the question: the formula multiplies by tokens per second, so what happens to a model that is fast per token?

## Slide 13 [Wajib] My own bench, October 2026
**Timing:** 2.0 min (clock 19:00)
**Key points**
- Two easy tasks, a UI page and a slot finder. Three runs each, hidden-check graders, medians.
- Every arm passed 126 of 126 checks. So quality did not separate the models. Speed and cost did.
- Opus low is fastest. Haiku medium is cheapest of the Claude arms. DeepSeek is far to the right, the slowest arm. The run spread is not stored per run in the results file, so the chart shows medians and no whiskers.

**Visual hint:** Plot. Time on the horizontal axis (UI task median), cost range on the vertical axis (a bar from the lower to the higher task median). Direct labels, Opus low highlighted, no legend.
**Speaker note:** "Cost is list price, API-equivalent. Read the chart left to right for speed and bottom to top for cost. Nothing is in the bottom left corner." Say this is two easy tasks, not a quality ranking. Slot finder times, for questions: Opus low 54 s, Sonnet medium 84 s, Spark low 71 s, Haiku medium 120 s, Wonder low 252 s, DeepSeek flash low 275 s.

| Setup | UI | Slot finder | Cost per task (API-equivalent) |
|---|---|---|---|
| Opus 5.5 low | 92 s | 54 s | $0.22 to $0.39 |
| Sonnet 5.5 medium | 94 s | 84 s | $0.17 to $0.24 |
| Spark 1.3 low | 103 s | 71 s | $0.08 to $0.15 |
| Haiku 5.5 medium | 170 s | 120 s | $0.02 to $0.03 |
| Wonder 1.0 low | 136 s | 252 s | $0.39 to $0.41 |
| DeepSeek v4.1 flash low | 476 s | 275 s | $0.04 to $0.07 |

## Slide 14 [Wajib] Tokens per second misled me
**Timing:** 1.5 min (clock 21:00)
**Key points**
- On paper, in September, DeepSeek V4.1-Flash ran at about 118 tokens per second against about 42 for GLM-5.3. The formula liked it.
- In the bench, the same family was the slowest per task, 476 s on the UI task, with 28 turns against 9 for Opus low.
- Each call was fast. There were far more calls. The formula has no term for turns.

**Visual hint:** Four horizontal bars of UI task time (Opus low 92 s, Sonnet medium 94 s, Haiku medium 170 s, DeepSeek flash low 476 s), each labelled with its turn count. DeepSeek highlighted.
**Speaker note:** "I measured, and my first method was wrong. Tokens per second is speed per call. A task is many calls." This is the honest part of the benchmark story. Turn counts are medians over three runs on the UI task.

## Slide 15 [Wajib] Effort versus turns
**Timing:** 1.5 min (clock 22:30)
**Key points**
- Raising effort raised the turn count in every head-to-head pair. Spark slot finder went from 9 to 23 turns. DeepSeek UI went from 28 to 40.
- The likely cause is checking. Higher effort re-reads and re-checks, and each check is a turn. This cause is an inference. The turn counts are measured.
- My rule stays. Low for execution, high for plans and hard debugging, medium for review, max almost never.

**Visual hint:** Paired bars for four rows (Haiku slot finder 12 to 16, Spark slot finder 9 to 23, Sonnet UI 7 to 10, DeepSeek UI 28 to 40). Each bar names its effort level. The rule line under it.
**Speaker note:** "I expected low effort to cost more steps. It was the other way round on these tasks." Say it covers execution on easy work. The "high for plans" half is my judgment.

## Slide 16 [Wajib] Prewalk, plan with the strong model and type with the cheap one
**Timing:** 1.0 min (clock 24:00)
**Key points**
- Prewalk is off by default in omp. The starting model, here Opus 5.5, reads the repo and writes a todo list.
- At the first file edit, omp switches the same session to a cheaper or faster model, which makes the edits.
- The reasoning, from Can Bölük (the omp author). Reading is what costs money. Edits were about 9% of the tokens in his logs.

**Visual hint:** Three steps in a row (Opus 5.5 reads and writes a todo list, omp switches models at the first edit, a cheaper model makes the edits). The switch step highlighted. One caption line under it. Only Claude 5.5 names on the slide.
**Speaker note:** "Prewalk means plan with the strong model, type with the cheap one." Say what a todo list is in one breath. Two lines from his post, said aloud and not shown: "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale", meaning the cheap model keeps the real work history, not a made-up summary. Next slide is what happened when I tried it.

## Slide 17 [Wajib] Prewalk on my short tasks, and why it is off
**Timing:** 2.0 min (clock 25:00)
**Key points**
- Opus 5.5 low alone cost $0.22 (slot finder) and $0.39 (UI). Prewalk into Sonnet 5.5 low cost $0.35 and $0.48.
- Sonnet 5.5 medium alone cost $0.17 and $0.24. Prewalk into Haiku 5.5 medium cost $0.17 and $0.36.
- Timeline. 24 Oct I turned prewalk on into Haiku. 25 Oct I moved the target to DeepSeek to save money. It was really slow, so I turned prewalk off the same day.

**Visual hint:** Paired bars, four rows (slot finder and UI for each pair), alone against prewalk, dollar labels on the bars. The UI Sonnet to Haiku pair ($0.24 against $0.36) highlighted. The timeline in the caption.
**Speaker note:** Every arm passed all 126 checks, so this compares cost only. On short tasks the cheaper model re-reads the conversation after the switch, so the run costs more. The handoff did not fire in 3 of 18 prewalk runs, which stayed on the starter model. My log estimates suggest it helps on long sessions, $2.58 against $1.63 for Sonnet medium alone against Sonnet medium into Haiku medium, but those are estimates, not graded. Public Terminal-Bench 4.0 has Haiku 5.5 at 39.2% and Sonnet 5.5 at 70.6%, so Haiku on long multi-step work is unproven. Can Bölük's own test with other models, not mine, GPT-5.6 Sol into Luna and Opus 4.8 into Flash on SWE-Bench Pro, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not mine. Untried next step is a faster cheap target. Lesson. Test a trick on your own workload.

## Slide 18 [Wajib] Cost, October 2026
**Timing:** 1.5 min (clock 27:00)
**Key points**
- October 2026. 270k requests, 41B tokens, $7.3k API-equivalent. I paid about $200. That is roughly 36 times less.
- 97% of tokens were cache reads. Without caching the same work prices at $58.2k. Two thirds of requests came from subagents.
- I pay for 2x Claude Max and OpenCode Go. Usually about $100 a month, now about $200 because I push a lot. June to August is the move from one chat at a time to many agents at once.

**Visual hint:** Big number pair "$7.3k" against "about $200", with the 36x and its reason. Bar chart of requests per month from May to November (2.2k, 23k, 46k, 174k, 235k, 270k, 47k for 1 to 5 November). March and April are not shown, because no reference explains the dip.
**Speaker note:** "API-equivalent means the list price of these tokens. It is not money I paid. The point is that one flat subscription plus caching carries a lot of work." Cache reads are cheap, which is why the multiple is so large.

## Slide 19 [Wajib] The subscription journey, ending in all in on Claude 5.5
**Timing:** 1.5 min (clock 28:30)
**Key points**
- September 2026. GLM Max, my own one-year plan bought cheap at the launch price. Codex Pro from the office. Devin Pro and OpenCode Go, my own. The default model was GLM-5.3.
- Eight months, at least 12 providers, by requests. Anthropic 240k, GLM 224k, Codex 128k. November so far is Anthropic only.
- Then the Claude 5.5 series arrived and I went all in on Claude. "Claude 5.5 series quality is GOAT." GOAT means greatest of all time.

**Visual hint:** Two cards, September and now. The quote has its gloss in brackets.
**Speaker note:** "The formula says which plan is cheap. It does not say which model is good. When quality moved, I moved." Close the section with "The model is the part I swap most often", and link back to the claim and the harness quote.

---

# Section 4. Pillar 2, knowledge (32:00 to 47:00)

## Slide 20 [Wajib] Skills are for TIL, memory is for cross-project
**Timing:** 1.0 min (clock 32:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project."
- Skills hold how to do a thing. Memory holds what I did and decided.
- Two stores, two jobs. Today we look at both.

**Visual hint:** Two cards. Left "skills and references", right "memory". The quote is said, not shown, because the headline carries the idea.
**Speaker note:** Say TIL means "today I learned". Give one example for each side.

## Slide 21 [Wajib] The skill rule
**Timing:** 2.0 min (clock 33:00)
**Key points**
- "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- This is the one action I want you to take home.
- A skill is a short file the agent loads when the work matches. It can include playbooks (steps to follow) and references (facts to look up).

**Visual hint:** The quote in large type. Under it a small folder tree `SKILL.md`, `playbooks/`, `references/`.
**Speaker note:** Tell one honest story. A routine you repeated three times, like a deploy or a WhatsApp template check, became a skill. Say this slide returns at the close.

## Slide 22 [Wajib] Area skills, one per domain
**Timing:** 2.0 min (clock 35:00)
**Key points**
- 14 area skills, one folder per domain, not per task. Examples are infra-ops, groundup-ops, alkhidmah-ops, git-pr-workflow, omp-ops, comms-ops, thesis-ops.
- `SKILL.md` is only a router. Playbooks are step lists to follow. References are facts to look up.
- A lint script checks layout and exits 1 on errors. A pre-commit hook runs it. The layout rule became a script, not a longer instruction.

**Visual hint:** The real lint output, cropped to the command and the summary line "14 skills, 0 errors, 1 warnings". The warn line is cropped out because it names a personal reference file. The tree of `managed-skills/` stays in the notes, and the lint is the slide.
**Speaker note:** "A task reads one router and then one playbook. Unrelated work stays out of each other's context. When a lesson shows up, it goes into the matching area skill, not into a new skill."

## Slide 23 [Wajib] Autolearn story
**Timing:** 1.0 min (clock 37:00)
**Key points**
- I turned autolearn on and let it create skills after each session. It created too many.
- I consolidated them into 14 domain skills and added the lint.
- Now I trigger autolearn by hand, after a session that taught something.

**Visual hint:** Three-step line. Many small skills, 14 domain skills plus lint, manual trigger. Small config line `autolearn: { enabled: true, autoContinue: false }`.
**Speaker note:** "Auto-on was too much noise. A human decides what is worth keeping. That is a small guardrail for knowledge, not for code."

## Slide 24 [Wajib] Memory journey
**Timing:** 2.0 min (clock 38:00)
**Key points**
- Mnemopi to Hindsight on 2026-06-28. Cognee tried in September 2026 and destroyed on 2026-10-19.
- Hindsight keeps the cross-project facts. It retains every 10 turns, because retaining on every run is the most expensive option.
- The old data stayed untouched, so rollback is one config flip.

**Visual hint:** Three-stage timeline (Mnemopi, Hindsight, Cognee tried and removed). Config snippet below.
**Speaker note:** "I do not trust one memory tool. I tried three. Hindsight stayed because it fits the cross-project job and the cost is controlled."

## Slide 25 [Opsional] Context and compaction
**Timing:** 1.0 min (clock 40:00)
**Key points**
- Compaction tries three methods in order. snapcompact, then remote, then soft.
- It starts at 70% of the context window, and compacts when idle after 60 seconds.
- Good compaction is one reason I dropped task tracking tools.

**Visual hint:** Small flow with three boxes (snapcompact, remote, soft) and the threshold line under it.
**Speaker note:** Keep it practical. "You do not need to watch the context window. You need a harness that compacts well and a memory layer behind it."

## Slide 26 [Wajib] Specs and instructions
**Timing:** 1.0 min (clock 41:00)
**Key points**
- I paste raw context. QA's WhatsApp message, screenshots, spreadsheets. No ticket needed. The structure is in the rules, not in my prompt.
- Instructions are layered. A short global file, small rule files, and a repo AGENTS.md where the nearest file wins and a size budget is checked.
- When I hand work to subagents, the brief has one shape. Target, Change, Contract.

**Visual hint:** Layer diagram (global file, rules, repo AGENTS.md, nested AGENTS.md). Next to it the three brief headings.
**Speaker note:** "My prompts are loose on purpose. The agent finds structure in the files around it. The brief shape is what I use one level down."

## Slide 27 [Wajib] The poteto skill set, ported to omp
**Timing:** 1.5 min (clock 42:00)
**Key points**
- poteto-mode is an agent style skill from the pstack plugin (MIT, upstream by poteto). I ported it to omp and keep a fork.
- 25 principles and 23 playbooks. Examples are Prove It Works, Fix Root Causes, Never Block on the Human, and playbooks for bug fix, babysit, shipping and orchestrate.
- The skill demands a visible effect. The reply must name each principle that shaped a decision and the choice it changed.

**Visual hint:** Two cards. Left "25 principles" (11 core, 6 architecture, 5 verification, 2 delegation, 1 meta). Right the playbook names.
**Speaker note:** Explain the keyword. I end many prompts with the word "poteto", and an extension loads the skill once per context. Run the count of principles and playbooks before the talk and say the real number.

## Slide 28 [Wajib] My favorite, principle-check-every-layer
**Timing:** 1.5 min (clock 43:30)
**Key points**
- It is my own principle, added on top of poteto.
- For any design, plan, review or build, give findings on three layers or one line on why a layer does not apply. Product and the human walk, structure, and data and flow.
- A rule file loads it on every turn for the main agent, reviewers and task agents.

**Visual hint:** Three stacked layers with the rule line under them. An example agent reply with three findings goes here when it is captured.
**Speaker note:** "Agents fix the layer they are looking at. This rule forces them to look at the other two."

## Slide 29 [Wajib] Why beads was dropped
**Timing:** 1.0 min (clock 45:00)
**Key points**
- Agents got smarter, so they need less task tracking.
- Beads is not really human-readable.
- Agents keep context better now with compaction and the memory layer. I use GitHub issues plus coordinator ledgers instead.

**Visual hint:** Muted card "beads, dropped" next to the replacement "GitHub issues plus ledgers".
**Speaker note:** "This is the one tool I used on purpose and then removed. It is fine to remove a tool when the model gets better."

---

# Section 5. Pillar 3, the crew (47:00 to 65:00)

## Slide 30 [Wajib] Worktrees, one per task
**Timing:** 2.0 min (clock 47:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- Every task gets its own git worktree, so agents never share a working directory.
- My plugin `tern-worktrees` has three parts. A Tern plugin (branch picker, keep or tear down on close), a CLI `tern-wt`, and a skill that is the contract agents follow.
- `tern-wt` prints one JSON object with stable error codes such as `dirty_worktree`. A copy-on-write clone brings `.env` and `node_modules` along.

**Visual hint:** The real `tern-wt list --all` JSON, cropped to the header and two of 101 worktrees, with the dirty one boxed (83 changes, owner tern). The rule "use tern-wt, not git worktree" stays in the notes.
**Speaker note:** "One CLI is the one implementation of each git and GitHub step. The skill tells the agent to use it and not to remove a worktree it did not create."

## Slide 31 [Wajib] My custom omp plugins
**Timing:** 2.0 min (clock 49:00)
**Key points**
- omp-agent-mesh (my own Effect-based engine) is the hero. It lets parallel agents see each other.
- Seven more, each written when something hurt. omp-org-account-router, tern-worktrees, poteto-mode, paseo-omp, opencode-go-multi-auth, herdr state hooks, and muse-sub (retired 2026-10-10).
- The org account router puts office repos on the office account and personal repos on personal accounts. paseo-omp has 237 commits from September to October 2026.

**Visual hint:** The real plugin listing. Enabled lockfile entries on top, `ls ~/.omp/agent/extensions/` below, with omp-agent-mesh boxed. The list of seven more plugins stays in the notes.
**Speaker note:** "This is the reason I chose omp. When something hurts, I write a plugin. The mesh plugin took seven commits over two days."

## Slide 32 [Wajib] Mesh, how agents talk
**Timing:** 2.5 min (clock 51:00)
**Key points**
- Many omp sessions share one machine, one set of ports, one Docker daemon. Mesh stops two agents running the same heavy job or editing the same file.
- Actions are `peers`, `note`, `send`, `broadcast`, `claim`, `release`. Edits to a file another agent claimed are blocked automatically.
- The shared event log had 10,083 lines on 2026-11-05. 101 session files used the tool.

**Visual hint:** The real `mesh peers` output, 8 peers with their one-line status and what each holds, and the SHIP row boxed ("Prod release ... held for operator go"). The AGENTS.md rule text and the 10,083 line count stay in the notes.
**Speaker note:** "Before heavy work, an agent checks who else is working. If a peer is running the same Docker job, it waits and sends a message instead of running in parallel." If the clock is early, make a one-minute live `peers` call.

## Slide 33 [Opsional] Long runs need one writer per branch
**Timing:** 1.0 min (clock 53:30)
**Key points**
- Idle sessions do not wake on mesh messages. A session that ended never sees a broadcast.
- So each branch gets one writer. A dead owner is replaced by a fresh one, and the reason goes into the ledger.
- Subagents and sessions outside the configured roots get `MESH_NOT_JOINED`.

**Visual hint:** The ledger rows as a quote card, dated 2026-11-02.
**Speaker note:** "This is the lesson from running agents for days. Messages are not enough. Ownership has to be clear."

## Slide 34 [Wajib] The SHIP coordinator loop
**Timing:** 3.0 min (clock 55:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- A coordinator is an ordinary omp session, not a daemon. The SHIP run lasted about three days (2 to 5 November) and kept a 276-line ledger.
- Worker contract. Do not merge. Send `MERGE-READY #<pr> <full sha>`. Freeze the head. An independent reviewer reviews it. One fix round, in one push.
- Product questions go to the coordinator, not to me. Each decision is one row with a reason. The ledger columns are ts, phase, decision, why, evidence, result.

**Visual hint:** Five-step flow with the reviewer highlighted and the FAIL loop drawn. Three real ledger rows with customer names removed go here when captured.
**Speaker note:** "I do not watch every branch. I watch one coordinator. When a reviewer proves a PR leaks data on a throwaway database, the coordinator decides whether it blocks the release, and writes down why."

## Slide 35 [Wajib] Base branch coordination, solved by mesh and one coordinator
**Timing:** 1.0 min (clock 58:00)
**Key points**
- Many PRs against one base branch need someone who knows the state of every branch. This is solved by my omp-agent-mesh plugin plus one spawned coordinator agent that guides the workers.
- One writer per branch. Workers never merge. The coordinator merges in sequence after an independent review.
- When mesh cannot reach a worker, the coordinator reads that worker's session file and types into its tab. The loop still runs.

**Visual hint:** One coordinator with workers on separate branches. Solid lines for mesh messages, dotted for the session-file fallback.
**Speaker note:** "This used to be my hardest problem. It is not an open problem for me now." Link to slides 32, 33 and 34.

## Slide 36 [Wajib] Review report and gates
**Timing:** 1.5 min (clock 59:00)
**Key points**
- The verdict is frozen at one commit. Example "Frozen verdict: PASS+NOTES at head 592b92ae9".
- A gates table. `verify.ts` verdict PROVEN (red on master, green on head, desktop 1280 and mobile 390), merge-tree clean, check-types, architecture lint, unit and e2e on a throwaway database that is removed after.
- Findings are tagged P2 or P3 with confidence, file and line, and a fix. Real FAILs included a README command that errored when run as written.

**Visual hint:** The first screen of the real review report for PR #580. The frozen verdict line is boxed, and the gates table runs below it. No words are changed. The throwaway database name is below the cut.
**Speaker note:** "The reviewer does not trust the author. It runs the README verbatim in a clean worktree and tests on a throwaway database." Say what I still check by hand. UI and visual feel.

## Slide 37 [Wajib] Demo check, the PR from the phone
**Timing:** 2.0 min (clock 60:30)
**Delivery:** Name the expected output first: Why, proof, Not verified. Time-box this to 90 s. If the PR is not ready or the page is slow, say exactly: "The live run is slow today, so here is the recording from this morning." Then show the recording and the PR #804 body as the reference. Read what is on screen aloud.
**Key points**
- Open the PR from the demo.
- Does the body have Why, proof, and an honest "Not verified"?
- Show the recording or screenshots the agent attached.

**Visual hint:** Live. The PR page in the browser, scrolled to Verification. If the PR is not ready, the slide is the fallback view: the PR #804 body, rendered from the PR markdown with GitHub's renderer, cropped to the draft click bullet and its before and after table. The slide itself shows no expected-output cards, so name Why, proof and Not verified aloud. PR #804 has no "Not verified:" line, say so.
**Speaker note:** If the run finished, walk through the body in 60 seconds. If it did not finish, say what step it is on and show the recording. Do not wait for it.

## Slide 38 [Wajib] PR body shape and the proof ladder
**Timing:** 2.0 min (clock 62:30)
**Key points**
- A PR body is a briefing, one minute for a reviewer who already has the diff. Sections in order are Why, How, What changed, Scope, Tradeoffs, Blast Radius, Verification.
- Verification has one bullet per claim, proof beside it, and ends with "Not verified:" and a list, or "Not verified: none".
- Proof ladder. Take the first rung that shows the claim. Recording for visible behavior (before and after for a bug). Command and real output for API or CLI. Run link for CI. Test command and result when nothing is visible.

**Visual hint:** The PR #804 Verification section, rendered from the PR markdown, with the pytest red-then-green bullet boxed. The seven section names and the four-rung proof ladder are said aloud, not drawn.
**Speaker note:** "There is no magic validate command. Proof comes from the Prove It Works principle and this PR shape. Every proof link is one the agent produced or opened in that session." Mention that GinaV2 PRs open as drafts.

---

# Section 6. Infra and guardrails (65:00 to 74:00)

## Slide 39 [Wajib] Infra map
**Timing:** 1.5 min (clock 65:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- x1 is the Linux workstation that runs the agents. The Mac (m5) is for review and browser. Both are on one private network.
- A shared dev box runs one compose stack per user, so proof comes from a real running stack away from the workstation. Another box handles batch jobs and the NAS. An office box runs staging.
- Cloud production is reached through IAP tunnels and is read-only by default.

**Visual hint:** The machine map as a hub. No IPs or host addresses.
**Speaker note:** "Agents use plain ssh aliases. I never show the ssh config on stage. The point is separation. The workstation is busy with agents, so proof runs elsewhere."

## Slide 40 [Wajib] Terminal journey
**Timing:** 1.0 min (clock 66:30)
**Key points**
- OpenChamber, then the Ghostty terminal (windows and tabs) because of omp, then herdr for worktrees and sessions.
- Tried Paseo to get something easier with more managed worktrees. Stopped its daemon on 2026-10-16.
- Now Tern, from Stencil, and I just use Tern. It has an Android app for the phone.

**Visual hint:** Five-step horizontal line (OpenChamber, Ghostty, herdr, Paseo, Tern) with dates where known.
**Speaker note:** "Each step removed one chore. I stopped on Tern because worktrees, tabs and the phone are in one place."

## Slide 41 [Opsional] Per-worktree setup
**Timing:** 1.0 min (clock 67:30)
**Key points**
- One command takes a fresh worktree to a running stack. For Alkhidmah, `bun run bootstrap`.
- Ports and database tier come from arithmetic on the branch slug, so two worktrees never fight over a port.
- GinaV2 uses one shared env file, symlinked as `.env` in every checkout.

**Visual hint:** The command. Real `bootstrap` output (ports, tier) goes here when captured.
**Speaker note:** "The agent never configures a stack by hand. The setup is in the repo, so a new worktree is a command."

## Slide 42 [Wajib] Secrets and damage control
**Timing:** 1.5 min (clock 68:30)
**Key points**
- omp obfuscates secrets by default. The model sees placeholders, not values.
- Damage-control rules block `rm -rf`, `git reset --hard`, force push, `DROP TABLE`. `~/.ssh/` is zero access. `.env` files are read-only.
- Secrets come from Infisical (machines) or Bitwarden (humans). Never print them. In my own words, obfuscation is not secret management.

**Visual hint:** Three short cards (obfuscation, damage control, secret managers). The rules file with `zeroAccessPaths` and `readOnlyPaths` goes here when captured.
**Speaker note:** "These are layers. The first hides values from the model. The second limits what a command can do. The third decides where values live." Say the zero access and read-only details aloud, they are not on the slide.

## Slide 43 [Wajib] Production is read-only, dry run first
**Timing:** 2.5 min (clock 70:00)
**Key points**
- Prod is read-only by default. No writes without approval. Show the plan before anything heavy.
- Every write goes dry run, backup, guarded apply, verify. Dry run runs the real update inside a transaction, rolls back, and prints the preview table and counts. Apply needs `--apply`, and a wrong row count rolls back.
- A deploy is done only when the running version is verified, not when the job is green.

**Visual hint:** Four-step flow (dry run, backup, apply with expected counts, verify). The prompt "dry run first then show me what will be changed" under it.
**Speaker note:** Give the real prompt. "I tell the agent dry run first and show me the list, so a colleague can confirm." Then the deploy lesson. The deploy call is an acceptance receipt, not a rollout receipt.

---

# Section 7. Open problems (74:00 to 79:00)

## Slide 44 [Wajib] Open problem, the agent UI and the manual checks
**Timing:** 1.5 min (clock 74:00)
**Delivery:** Pause 1 to 2 s after the claim in the headline. Look at the lens when you say it.
**Key points**
- Agent-built UI is still fat and ugly. It needs design skills and my manual feedback.
- The things I still check by hand are UI and visual feel, and UX.
- Proof clips show that a button works. They do not show that it looks right.

**Visual hint:** Two cards now. Two screenshots side by side, one agent-built screen before design feedback and one after, go here when captured (Alkhidmah, no customer data).
**Speaker note:** "This is honest. The agent can prove a flow works. It cannot yet tell me the screen feels right." Name the other two problems, the next two slides, in one breath.

## Slide 45 [Wajib] Open problem, env and seeding per worktree
**Timing:** 1.5 min (clock 75:30)
**Key points**
- Setting up a database and seed per worktree is slow and heavy.
- One fix took a seed from 652 s to 171 s.
- Every new worktree pays this cost, and agents create many.

**Visual hint:** Bar pair, 652 s against 171 s. Caption "Every new worktree pays 171 s".
**Speaker note:** "Parallel agents are only as cheap as a worktree is. 171 seconds is better, and still too slow."

## Slide 46 [Wajib] Open problem, RAM on the shared box
**Timing:** 2.0 min (clock 77:00)
**Key points**
- Agents and two CI runners share one workstation. An uncapped test run reached 38 GB.
- A rule now fires when test commands appear. It tells the agent to cap memory and check free RAM first.
- The verify script refuses to run below 15 GiB free. These are two different numbers. 38 GB is what one run reached. 15 GiB is the free memory the script needs before it starts.

**Visual hint:** Two number cards with the relation in words. A memory graph of the run goes here if one is captured.
**Speaker note:** "The fix was a rule that fires on the command, not a memory upgrade. A rule with a regex condition is a cheap guardrail."

---

# Section 8. Close and Q&A (79:00 to 90:00)

## Slide 47 [Wajib] The claim, and one action
**Timing:** 1.0 min (clock 79:00)
**Delivery:** Say the claim slowly, then pause 1 to 2 s. Look at the lens. Then open the floor. For every question, repeat the question, answer the core, and link back to the claim.
**Key points**
- The model is a swappable part. Skills, proof, coordination and guardrails are the setup around it.
- One action for Monday. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you."
- Two small habits that cost nothing. Ask for proof in every PR. Dry-run anything that touches production.

**Visual hint:** The skill rule as one large quote. The three Monday actions in the line under it.
**Speaker note:** Say the claim again, slowly. Then say the rule. Then stop.

## Slide 48 [Wajib] Q and A
**Timing:** 0.5 min (clock 80:00), then 6 min Q&A (to 86:30)
**Delivery:** Repeat the question, answer it, link back to the claim. Say "I don't know" plainly and offer a follow-up path. If the room is quiet, use a seed question from the list below. Keep the phone mirror open for a live peek at `mesh peers` or the PR.
**Key points**
- Questions are welcome in chat or aloud.
- GitHub handle @masrurimz. The slides link goes into the chat.
- Thank you, SWE Growth.

**Visual hint:** Handle in large type, "Slides link in the chat" under it. No QR code, because Drive sharing is not decided.
**Speaker note:** Likely questions to prepare. How much does it cost for a beginner. Which model for which role. Is it safe to run agents for days. Why not Claude Code alone. How to start with one skill. Why is prewalk off? On my short tasks it cost the same or more, and the one time I tried a cheaper target (DeepSeek) it was really slow. It may still help on long sessions and with a faster cheap target, which I have not tried. Seed question if quiet: what is the first task you would turn into a skill?
