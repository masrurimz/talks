# Benchmarking My Coding Agent Setup: One Engineer, Many Agents
## Presenter outline, live talk for SWE Growth

**SWE Growth community (Mas Zikrul), online on Zoom**
**90 minutes. All slides in English.**
**Speaker: Zahid**

## Notes for the presenter
- This is the v2 deck. It has 60 slides, and dividers are numbered slides. The plan is 71 minutes of talking and 19 minutes of slack and Q&A. The build lint checks that the slide timings add up to 71 and that each clock value follows from the one before.
- The slides speak to the audience. Sources, dates, caveats, timing and chat cues live here, in the speaker notes. Each block has `Say:` (what you say, in your own words) and `Evidence:` (the facts behind the slide, for questions).
- Timing is minutes of talking. The clock value is the target, not a promise.
- Label **[Wajib]** means keep the slide. Label **[Opsional]** means cut it if time is short.
- Each part runs divider, story, principle, proof, then one thing to try. The story comes first. The number or the principle comes after it.
- Say "if I paid per token" every time a dollar figure appears on a slide. It is the list price of the tokens, not money paid. In the notes this is called API-equivalent.
- The claim, which every part supports or limits. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."
- Live demo checkpoints. Start at about minute 10 (slide 10). Check the PR at about minute 54 (slide 45). A recording of the full run is ready, and it is never named on a slide. The phone screen is shared next to the laptop.
- Terms are defined where they first appear, in the `Say:` line. Harness (slide 7), SHIP (slide 10), skill (slide 23), poteto-mode (slide 29), worktree (slide 35), mesh (slide 36). The v1 glossary slide is cut.

## Run of show

| Clock | Section | Slides | Talk time | Organizer questions |
|---|---|---|---|---|
| 0:00 to 5:00 | Opening | 1 to 5 | 5 min | none |
| 5:00 to 12:00 | My journey (demo starts) | 6 to 10 | 7 min | 1 |
| 12:00 to 26:00 | Part 1. Measure it on your own work | 11 to 21 | 14 min | 2, 3, 11 |
| 26:00 to 37:00 | Part 2. Do it twice, make it a skill | 22 to 31 | 11 min | 5, 7, 8 |
| 37:00 to 48:00 | Part 3. One writer per branch | 32 to 39 | 11 min | 4 |
| 48:00 to 57:00 | Part 4. Show proof, not "done" (demo check) | 40 to 46 | 9 min | 9 |
| 57:00 to 64:00 | Part 5. Make it safe to walk away | 47 to 54 | 7 min | 6, 10 |
| 64:00 to 68:00 | What is still hard | 55 to 57 | 4 min | 12 |
| 68:00 to 71:00 | Close | 58 to 60 | 3 min | none |

Total talk time is 71 minutes (5 + 7 + 14 + 11 + 11 + 9 + 7 + 4 + 3). Q&A and slack are the other 19 minutes. Part 1 has seven proof slides, more than the five the shape suggests, because the content map keeps every benchmark slide. Protect Part 1, because it matches the title.

## Cut order if time is short
Cut in this order. Each cut saves about the time shown.
1. Slide 53 (terminal journey), 0.5 min. Say the five names in one breath.
2. Slide 30 (why beads was dropped), 0.5 min. Say one sentence on slide 28.
3. Slide 52 (per-worktree setup), 0.5 min.
4. Slide 37 (my plugins), 1 min. Say it on slide 36.
5. Slide 28 (loose prompts), 1 min.
6. On slide 27, skip the compaction sentence, 0.5 min.

The core stays intact. The claim, the benchmark story and its proof (slides 12 to 19), skills, mesh and the coordinator hub, the PR proof frames, the production steps, and what is still hard.

## Coverage of the 12 organizer questions

| # | Question | Slides |
|---|---|---|
| 1 | Tool evolution and why each switch | 6, 7, 8 |
| 2 | Model routing per role | 14, 15 |
| 3 | Effort and thinking level | 14, 16 |
| 4 | Orchestration and parallel agents | 33, 35, 36, 37, 38 |
| 5 | Task and spec management, beads | 28, 30 |
| 6 | Long-horizon runs and guardrails | 33, 38, 48 |
| 7 | Memory and context | 26, 27 |
| 8 | Own skills, favorites | 23, 24, 25, 29 |
| 9 | Review and quality gate, manual checks | 41, 42, 44, 55 |
| 10 | Supporting infra | 50, 51, 52, 53 |
| 11 | Cost and subscription strategy | 12, 15, 17, 18, 19, 20 |
| 12 | Open problems | 55, 56, 57 |

---

# Opening (0:00 to 5:00)

## Slide 1 [Wajib] Title
**Timing:** 0.5 min (clock 0:00)
**Delivery:** Look at the lens, not at the slide. Say the throughline in one sentence: the model is swappable, and the setup around it ships the work. Speak at 130 to 150 words per minute.
**Say:** Hello everyone, and thank you to Mas Zikrul and SWE Growth. This is a casual talk about one real setup. I will show real numbers, and I will also show what still does not work.
**Evidence:** Title card, dark background, no logos of model vendors. SWE Growth community, online. The subtitle names the speaker. The talk is 90 minutes on Zoom in English, for a mixed Indonesian developer audience.

## Slide 2 [Wajib] The 9:29 phone screenshot
**Timing:** 1.0 min (clock 0:30)
**Say:** This is my phone at 9:29 in the morning. I was sitting in the plane, before takeoff. I spoke a prompt, and my agent had just reproduced a bug on a real running stack. Let me show you how I got there.
**Evidence:** Tuesday, 27 October 2026, 9:29 WIB, on board the plane before takeoff. An omp session on a phone in the Tern Android app, chat style, with a mic in the composer. The agent had just reproduced a bug on a real stack. The full phone screenshot has serial numbers blurred, with 9:29 and the mic circled. Two enlarged crops carry the labels "9:29 WIB" and "voice prompt". The file is `sources/references/screenshot-omp-mobile-0929.png`.

## Slide 3 [Wajib] QA flagged the bug and passed the fix
**Timing:** 1.0 min (clock 1:30)
**Say:** QA found one more problem on a pull request that was already approved. At 9:26 I pasted the finding into my session from the phone. The agent recorded the bug, fixed it, and updated the PR. QA passed it at 9:57, and most of that time I was not touching it.
**Evidence:** GinaV2 PR #804, 26 to 27 October 2026. Timeline. 08:52 QA posts a warning on an already approved PR, clicking a draft sensor opens the edit modal. 09:26 I paste the finding into the session from the phone, with the prompt "Fix those own changes proof and update pr". 09:29 the agent records the before clip. 09:31 the PR body is updated. 09:57 QA passes, 65 minutes after the warning. The markers are spaced by clock time, so the gaps are visible. The slide labels them 34 minutes (08:52 to 09:26) and 28 minutes (09:29 to 09:57). The 09:31 PR update is 26 minutes before the pass. The two close events (09:26 and 09:29) share one label under the axis. The slide shows four points. The 09:31 update is in this note only.

## Slide 4 [Wajib] The claim
**Timing:** 1.0 min (clock 2:30)
**Say:** Here is the claim of this talk. The model is a swappable part. The setup around it does the work. I see four parts in the setup, skills, proof, coordination and guardrails. Every part of the talk either supports this claim or shows where it breaks.
**Evidence:** The claim in full. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails." The four parts carry equal weight, and the model box is grey on purpose. Promise one action to take home at the end. The talk has five principles, one per part after the journey.

## Slide 5 [Wajib] Outside evidence for the claim
**Timing:** 1.5 min (clock 3:30)
**Say:** This is not only me saying this. Can Bölük is the author of omp. He wrote that he improved 15 models at coding in one afternoon, and only the harness changed. A harness is the program around the model. I will explain it on the slide after the journey.
**Evidence:** The quote is the exact title of his X article, checked against the live page on 2026-11-05. Say "article", not "post". The screenshot shows the article header with the hero image, "Can Bölük @can1357", and a box on the title. The article URL is on the Links slide (slide 59). This is the claim of the talk from someone with no reason to flatter my setup.

---

# My journey (5:00 to 12:00)

## Slide 6 [Wajib] My tool journey and why each switch
**Timing:** 2.0 min (clock 5:00)
**Delivery:** Pause 1 to 2 s after the headline. Look at the lens when you say it.
**Chat:** Ask "Which coding agent do you use today?" in chat and read two or three answers aloud. This is organizer question 1.
**Say:** This is from my own files, not from memory. I started with Gemini tooling, then Claude Code, then OpenCode, then Amp, and now omp. Each bar ends with the reason I left. Claude Code was not good enough for some tasks. OpenCode had many issues and accounts were getting banned. For Amp, honestly, I forgot why I left. omp stayed because I can extend it.
**Evidence:** Gemini tooling on the Mac (m5) from July 2025, Claude Code from 2025-10-19, OpenCode with oh-my-opencode from 2025-10-20, Amp from 2025-12-22 to 2026-03-16, omp from 2026-02-23 on m5 and as the main tool on x1 since 2026-03-07. One word per switch. Claude Code, quality. OpenCode, bans. Amp, "I forgot why I left Amp". omp, extensible. Antigravity is not on the chart because I have no date. Good free usage, plan annotations, session artifacts. Then it was heavy, quality and limits got worse, and my Google account got banned. Dates are the first session I find for each tool in omp stats (`~/.omp/stats.db`) and the session folders. A bar ends at the next tool's first session, except Amp, whose end is dated. Point out the overlap between Amp and omp. Be honest. The reasons are about my workload and the time, not a verdict on the tools. Claude Code, some tasks were not good enough and I wanted more efficiency. OpenCode, many issues and Claude and OpenAI subscriptions were getting banned. Amp was mature, with cross-agent messages and spawned agents, and I mostly used a proxy (CLIProxyAPI) for very large usage. Claude Code to OpenCode was within one day by first session, so its bar is a sliver. OpenCode had 215 sessions on m5 and a web UI called OpenChamber.

## Slide 7 [Wajib] What is a harness
**Timing:** 1.0 min (clock 7:00)
**Say:** A harness is the program around the model. It gives the model tools, context, memory and rules. Claude Code, Cursor and omp are harnesses. Claude, GPT and GLM are models. You can swap the model and keep the harness. This talk is about the harness.
**Evidence:** Many of you use Claude Code or Cursor, so keep this to two sentences and move on. Harness examples are Claude Code, Cursor, OpenCode, Amp and omp. Model examples are Claude, GPT and GLM. The v1 glossary slide ("six terms before they appear", after Mayer's pre-training principle of multimedia learning) is cut. Each term is now defined by you, in plain words, on the slide where it first appears. Many listeners work in a second language, so do not rush.

## Slide 8 [Wajib] Why omp
**Timing:** 1.5 min (clock 8:00)
**Say:** I forgot why I left Amp, but omp is better because I can extend it. When something hurts, I write a plugin. Autolearn means the agent writes a skill after a session. Hindsight is the memory tool I use. Compaction means the agent shortens a long chat so it can keep going. The next parts are full of plugins I wrote.
**Evidence:** My reasons for omp, 2026-11-05, from `~/.omp/agent/config.yml`. Plugins I write, autolearn, Hindsight memory, multi-provider subscription logins, and good compaction. That extensibility is why the later slides exist. Mesh, the org account router and the worktree plugin are all mine. A harness you can extend lets you fix your own problems, which is why the setup keeps moving. Say the joke about forgetting Amp once, then give the real answer. A small screenshot of `ls ~/.omp/agent/extensions/` was planned and not captured.

## Slide 9 [Wajib] From one chat to many agents
**Timing:** 1.0 min (clock 9:30)
**Say:** This is how many requests my agents made each month. In May it was 2,200. In October it was 270,000. Between June and August I moved from one chat at a time to many agents at once. That change is why the rest of the talk is about coordination.
**Evidence:** Requests per month from omp stats (`~/.omp/stats.db`), re-aggregated 2026-11-05. May 2.2k, June 23k, July 46k, August 174k, September 235k, October 270k, and 47k for 1 to 5 November (partial month, not on the slide). June to August is the move from one chat at a time to many agents at once. March and April are not shown, because no reference explains the dip. The cost side of October is on slide 19.

## Slide 10 [Wajib] Live demo, start from the phone
**Timing:** 1.5 min (clock 10:30)
**Delivery:** Narrate each step and name the expected output before you press send. Time-box this to 90 s. If the run is slow or fails, say exactly: "The live run is slow today, so here is the recording from this morning." Then play the recording and move on. Do not debug live.
**Say:** Now the live demo. You are looking at my real phone. I will send one prompt from the Tern Android app. It asks for a new worktree, a trace of the flow, a fix, and a PR with proof in the body. SHIP is my coordinator agent, and poteto is a keyword that loads my agent-style skill. The agent works while I keep talking, and we open the PR later.
**Evidence:** A small real issue from the Alkhidmah backlog. The slide shows the prompt text only. Goal is a PR with proof in the body, checked at about minute 54 (slide 45). The recording of the full run is cued in a second window, and it is not named on any slide. The phone mirror sits next to the laptop with the Tern session open and the prompt typed in my own style. After sending the prompt, go straight to the next slide.

---

# Part 1. Measure it on your own work (12:00 to 26:00)

Part 1 is built on `references/referensi-benchmark-lab.md`. The story is one engineer who measures. A model per role, a value formula, a bench of his own, a finding about effort, a handoff trick he tested and turned off, and a subscription journey that ended with "all in on Claude 5.5".

## Slide 11 [Wajib] Divider, Part 1
**Timing:** 1.0 min (clock 12:00)
**Delivery:** Look at the lens. Throughline: I pick models with a bench I built, not a feeling.
**Chat:** Ask "Per token or per subscription? Tell us in chat." Wait 5 s before you speak. Read two or three answers aloud. Use them on slide 19, where I say what I pay. This is organizer question 11.
**Say:** Part 1 is about choosing models and paying for them. How do you pay for your agent today, per token or with a subscription? Tell us in chat. I will come back to your answers when I show my own bill.
**Evidence:** Divider for Part 1 of 5. The principle for this part comes after the story, on slide 13.

## Slide 12 [Wajib] The fastest model on paper was the slowest in my hands
**Timing:** 2.0 min (clock 13:00)
**Say:** In September I ranked models with a formula. It liked DeepSeek flash, because on paper it runs at 118 tokens per second. Then I ran a real task. Opus finished in 92 seconds. DeepSeek needed 476 seconds, with 28 steps against 9 for Opus. Each step was fast, but there were many more steps. My formula had no term for steps.
**Evidence:** My October 2026 bench, UI task, 3 runs each, medians. Opus 5.5 low 92 s with 9 turns, Sonnet 5.5 medium 94 s with 10 turns, Haiku 5.5 medium 170 s with 15 turns, DeepSeek flash low 476 s with 28 turns. Tokens per second is speed per call, and a task is many calls. September ranking (2026-09-14). DeepSeek V4.1-Flash scored 90.6 on Terminal-Bench 2.1 at about 118 tokens per second. GLM-5.3 scored 88.2 at about 42. The formula, which is cut from the slides. Value Multiplier = Quota $ / Subscription cost. Effective $/1M = Blended $/1M / Value Multiplier. Value Score = Benchmark / Effective $/1M. Speed-adjusted QSPD = (Benchmark x tok/s) / (Effective $/1M x 1000). A price per million tokens misleads, because a subscription changes what a token costs. Rules. One common benchmark only (Terminal-Bench 2.1). Count the accounts. `cost_total` is API-equivalent, not spend. GLM is verbose, so compare tokens used too. The September numbers are a point in time. This is the honest part of the benchmark story. Turn counts are medians over three runs on the UI task.

## Slide 13 [Wajib] Principle 1, measure it on your own work
**Timing:** 0.5 min (clock 15:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the first principle. Measure it on your own work. A benchmark on paper is a guess. Your own task is the test.
**Evidence:** Principle 1 of 5. The proof slides that follow are the routing per job, the bench result, the effort finding, prewalk, the cost and the plan change.

## Slide 14 [Wajib] Each job gets its own model
**Timing:** 1.5 min (clock 15:30)
**Delivery:** Pause 1 to 2 s after the headline.
**Say:** I do not pick a model per prompt. I pick one per job. When I chat with the agent, I use Opus at low effort. For planning I use Opus at high, and for review Opus at medium. The helper agents that do the work run Sonnet at medium. The small fast model, Haiku, does the quick searches. My rule of thumb is low to do, medium to review, high to plan, and max almost never.
**Evidence:** The roles from `~/.omp/agent/config.yml` (`modelRoles` and `task.agentModelOverrides`). Chat is the default role, Opus 5.5 at low. Plan is Opus 5.5 at high, and so is slow. Reviewer is Opus 5.5 at medium. Task agents run Sonnet 5.5 at medium. Scout and sonic follow `@fast`, and smol is Haiku 5.5 at auto. Advisor and designer are Sonnet at high. The slide shows five jobs only. Effort rule. Low for execution, high for plans and hard debugging, medium for review, max almost never. The next slides test the first half with a bench. Speed since 2026-10-01 (Anthropic, average per request) is Haiku 130 output tokens per second, Sonnet 95, Opus 66. These speeds are left off the slide on purpose, because slide 12 says tokens per second misled me. A fallback chain and a second account take over when a quota runs out. Time to first token is 2.6 seconds for Opus as main against 1.4 for Haiku. Effort is not recorded per request, so I cannot chart it from my usage. That is why I built a bench. Add the `modelRoles` block cropped so no account details show, if you have it open.

## Slide 15 [Wajib] Every model passed, speed and price decided
**Timing:** 2.0 min (clock 17:00)
**Say:** I wrote two easy tasks, a UI page and a slot finder. I ran each model three times. Every model passed all the checks, so quality did not separate them. Read the chart left to right for speed and bottom to top for cost. Opus is the fastest. Haiku is the cheapest Claude model. DeepSeek is far on the right. Nothing sits in the bottom left corner. This is two easy tasks, not a quality ranking.
**Evidence:** My October 2026 bench, 2 tasks x 3 runs, medians, hidden-check graders. Results file `~/.omp/agent/bench/results-2026-10.json`. Every arm passed 126 of 126 checks. Cost is API-equivalent, the list price of the tokens, not money paid, and it spans both tasks. The horizontal axis is the UI task median. The vertical bar is the range between the two task medians. The run spread is not stored per run in the results file, so the chart has no whiskers. Opus low is the fastest. Haiku medium is the cheapest of the Claude arms. DeepSeek is the slowest arm. Model names on the slide are shortened. The full setups are below.

| Setup | UI | Slot finder | Cost per task (API-equivalent) |
|---|---|---|---|
| Opus 5.5 low | 92 s | 54 s | $0.22 to $0.39 |
| Sonnet 5.5 medium | 94 s | 84 s | $0.17 to $0.24 |
| Spark 1.3 low | 103 s | 71 s | $0.08 to $0.15 |
| Haiku 5.5 medium | 170 s | 120 s | $0.02 to $0.03 |
| Wonder 1.0 low | 136 s | 252 s | $0.39 to $0.41 |
| DeepSeek v4.1 flash low | 476 s | 275 s | $0.04 to $0.07 |

## Slide 16 [Wajib] Thinking harder made the agent take more steps
**Timing:** 1.5 min (clock 19:00)
**Say:** I expected high effort to give better answers for the same cost. On these tasks it did something else. When I raised the thinking effort, the agent took more steps every time. Spark went from 9 to 23 steps. DeepSeek went from 28 to 40. My guess is checking, but that is my guess. The step counts are measured.
**Evidence:** My October 2026 bench, 2 tasks x 3 runs, medians. Pairs, lower effort then higher effort. Haiku slot finder 12 turns (medium) to 16 (high). Spark slot finder 9 (low) to 23 (medium). Sonnet UI 7 (low) to 10 (medium). DeepSeek UI 28 (low) to 40 (high). The likely cause is checking. Higher effort re-reads and re-checks, and each check is a turn. This cause is an inference. The turn counts are measured. My rule stays. Low for execution, high for plans and hard debugging, medium for review, max almost never. This covers execution on easy work. The "high for plans" half is my judgment.

## Slide 17 [Wajib] Plan with the big model, let a small one type
**Timing:** 1.0 min (clock 20:30)
**Say:** Prewalk is a trick from Can Bölük. The strong model reads the code and writes a todo list. At the first edit, omp switches the same session to a cheaper model. The cheap model makes the edits. The idea is that reading costs money and editing is cheap. I tested it on my own work.
**Evidence:** Prewalk is off by default in omp. The starting model, here Opus 5.5, reads the repo and writes a todo list. At the first file edit, omp switches the same session to a cheaper or faster model. Source is the omp docs and stencil.so/blog/prewalk by Can Bölük. Reading is what costs money. Edits were about 9% of the tokens in his logs. Two lines from his post, said aloud and not shown. "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale", meaning the cheap model keeps the real work history, not a made-up summary. Say what a todo list is in one breath. Only Claude 5.5 names are on the slide.

## Slide 18 [Wajib] On my tasks prewalk was never cheaper
**Timing:** 1.5 min (clock 21:30)
**Say:** Here is what happened on my tasks. The slide shows the UI task. Opus alone cost 39 cents. With prewalk it cost 48 cents. Sonnet alone cost 24 cents, and with prewalk 36 cents. The tie happened on the other task, the slot finder. There, Sonnet into Haiku cost 17 cents both ways. Across both tasks, prewalk was never cheaper. The lesson is simple. Test a trick on your own workload, because it may work for someone else and not for you.
**Evidence:** My October 2026 bench, Claude 5.5, 2 tasks x 3 runs, medians, API-equivalent cost. Every arm passed all 126 checks, so this compares cost only. Opus 5.5 low alone cost $0.22 (slot finder) and $0.39 (UI). Prewalk into Sonnet 5.5 low cost $0.35 and $0.48. Sonnet 5.5 medium alone cost $0.17 and $0.24. Prewalk into Haiku 5.5 medium cost $0.17 and $0.36. The slot finder pairs ($0.22 against $0.35, and the tie at $0.17) are in this note only. Timeline. 24 Oct I turned prewalk on into Haiku. 25 Oct I moved the target to DeepSeek to save money. It was really slow, so I turned prewalk off the same day. On short tasks the cheaper model re-reads the conversation after the switch, so the run costs more. The handoff did not fire in 3 of 18 prewalk runs, which stayed on the starter model. My log estimates suggest it helps on long sessions, $2.58 against $1.63 for Sonnet medium alone against Sonnet medium into Haiku medium, but those are estimates, not graded. Public Terminal-Bench 4.0 has Haiku 5.5 at 39.2% and Sonnet 5.5 at 70.6%, so Haiku on long multi-step work is unproven. Can Bölük's own test with other models, not mine, GPT-5.6 Sol into Luna and Opus 4.8 into Flash on SWE-Bench Pro, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not mine. Untried next step is a faster cheap target. Say "never cheaper", not "cost more", because one pair tied.

## Slide 19 [Wajib] Cost in October
**Timing:** 1.5 min (clock 23:00)
**Say:** In October my agents used tokens that would cost about 7,300 dollars at list price. I paid about 200 dollars. One flat subscription plus caching carries a lot of work. Most of the tokens were cache reads, and those are cheap. I usually pay about 100 dollars a month, and this month about 200 because I push a lot.
**Evidence:** October 2026 from omp stats (`~/.omp/stats.db`), re-aggregated 2026-11-05. 270k requests, 41B tokens, $7.3k API-equivalent (the list price of the tokens, not money paid). I paid about $200. That is roughly 36 times less. 97% of tokens were cache reads. Without caching the same work prices at $58.2k. Two thirds of requests came from subagents. I pay for 2x Claude Max and OpenCode Go. Usually about $100 a month, now about $200. Cache reads are cheap, which is why the multiple is so large. Use the chat answers from the Part 1 divider here.

## Slide 20 [Wajib] When quality moved, I moved
**Timing:** 1.0 min (clock 24:30)
**Say:** The formula tells me which plan is cheap. It does not tell me which model is good. When the Claude 5.5 models arrived, I changed my plans. In my own words, Claude 5.5 quality is GOAT, which means greatest of all time. The model is the part I swap most often, and that links back to the claim.
**Evidence:** Plans verified 2026-09-14, usage by provider from omp stats 2026-11-05. September 2026. GLM Max, my own one-year plan bought cheap at the launch price. Codex Pro from the office. Devin Pro and OpenCode Go, my own. The default model was GLM-5.3. Eight months, at least 12 providers, by requests. Anthropic 240k, GLM 224k, Codex 128k. November so far is Anthropic only. Then the Claude 5.5 series arrived and I went all in on Claude. The quote is "Claude 5.5 series quality is GOAT". Close the part with "The model is the part I swap most often".

## Slide 21 [Wajib] Try this, time one real task
**Timing:** 0.5 min (clock 25:30)
**Say:** Here is one thing to try this week. Take one real task you do often. Run it on two different models and write down the time. That takes one afternoon, and then you know.
**Evidence:** The audience action for Part 1. No new numbers.

---

# Part 2. Do it twice, make it a skill (26:00 to 37:00)

## Slide 22 [Wajib] Divider, Part 2
**Timing:** 1.0 min (clock 26:00)
**Delivery:** Look at the lens. Throughline: the model is swappable, and what stays is what the agent knows.
**Chat:** Ask "Which task do you repeat with your agent more than twice? Tell us in chat." Wait 5 s. Read two or three answers aloud. Come back to them on slide 25 and on the try slide. This is organizer question 8.
**Say:** Part 2 is about teaching the agent. Think about your own work for a moment. Which task do you repeat with your agent more than twice? Tell us in chat.
**Evidence:** Divider for Part 2 of 5. The principle for this part comes after the story, on slide 25.

## Slide 23 [Wajib] Autolearn made too many skills
**Timing:** 2.0 min (clock 27:00)
**Say:** A skill is a short file the agent loads when the work matches. Autolearn is a feature where the agent writes a skill after a session. I turned it on and it created too many small skills. So I merged them into 14 area skills, one for each area of work. Now I run autolearn by hand, after a session that taught me something. Auto-on was too much noise, and a human decides what is worth keeping.
**Evidence:** The config line is `autolearn: { enabled: true, autoContinue: false }` in `~/.omp/agent/config.yml`. My own account, 2026-11-05. Many small skills, then 14 domain skills plus a lint, then a manual trigger after a session that taught something. This is a small guardrail for knowledge, not for code.

## Slide 24 [Wajib] The skills lint
**Timing:** 1.0 min (clock 29:00)
**Say:** To keep the 14 skills clean, I wrote a lint script. It checks the layout and exits with an error if something is wrong. A pre-commit hook runs it. The last run found 0 errors. The layout rule became a script, not a longer instruction.
**Evidence:** The omp-skills repo, `scripts/skills_lint.py`, run 2026-11-05. 14 area skills, one folder per domain, not per task. Examples are infra-ops, groundup-ops, alkhidmah-ops, git-pr-workflow, omp-ops, comms-ops, thesis-ops. `SKILL.md` is only a router. Playbooks are step lists to follow. References are facts to look up. The lint exits 1 on errors, and a pre-commit hook runs it. The real output reads "14 skills, 0 errors, 1 warnings". The warn line is cropped out because it names a personal reference file. The tree of `managed-skills/` stays in this note. A task reads one router and then one playbook, so unrelated work stays out of each other's context. When a lesson shows up, it goes into the matching area skill, not into a new skill.

## Slide 25 [Wajib] Principle 2, do it twice, make it a skill
**Timing:** 1.0 min (clock 30:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the second principle, and the one action I want you to take home. When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you. Tell one honest story here. A routine I repeated three times, like a deploy or a WhatsApp template check, became a skill.
**Evidence:** The rule in my words. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." A skill is a short file the agent loads when the work matches. It can include playbooks (steps to follow) and references (facts to look up). The folder shape is `SKILL.md`, `playbooks/`, `references/`. This rule returns at the close, on slide 58.

## Slide 26 [Wajib] Skills versus memory
**Timing:** 1.0 min (clock 31:00)
**Say:** Skills and memory do two different jobs. A skill holds how to do a thing, like the steps of a deploy. Memory holds what I did and decided, across projects. For example, a skill says how to run the release. Memory says that we chose one plan last month and why.
**Evidence:** In my words. "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project." TIL means "today I learned". Two stores, two jobs. The quote is said, not shown, because the headline carries the idea. Give one example for each side.

## Slide 27 [Wajib] Memory, and compaction
**Timing:** 2.0 min (clock 32:00)
**Say:** I do not trust one memory tool, so I tried three. I kept Hindsight because it fits the cross-project job, and the cost is controlled. It saves a note every 10 turns, because saving on every run is the most expensive option. Compaction is a second layer. When a chat gets long, the agent shortens it with three methods in order, so you do not need to watch the context window.
**Evidence:** Memory journey. Mnemopi before 2026-06-28, then Hindsight from 2026-06-28 (kept), then Cognee tried in September 2026 and destroyed on 2026-10-19. Config. `memory: backend: hindsight`, `hindsight: retainMode: last-turn, retainEveryNTurns: 10, retainOverlapTurns: 2`. The old data stayed untouched, so rollback is one config flip. Source is `~/.omp/agent/config.yml` and the Hindsight migration notes of 2026-06-28. Compaction (this was v1 slide 25, cut as a slide). Three methods in order, snapcompact, then remote, then soft. It starts at 70% of the context window, and compacts when idle after 60 seconds. Good compaction is one reason I dropped task tracking tools. "You do not need to watch the context window. You need a harness that compacts well and a memory layer behind it."

## Slide 28 [Opsional] My prompts are loose on purpose
**Timing:** 1.0 min (clock 34:00)
**Say:** I paste raw context into the agent. A WhatsApp message from QA, a screenshot, a spreadsheet. I do not write a ticket first. The structure is in the files around the prompt, not in the prompt. When I hand work to a subagent, the brief has one shape, target, change and contract.
**Evidence:** Instructions are layered. A short global file (`~/.omp/agent/AGENTS.md`) with hard rules. Small rule files in `~/.omp/agent/rules`, loaded always or on a regex. A repo AGENTS.md where the nearest file wins. Nested AGENTS.md files with a size budget that is checked. The brief for subagents has Target, Change, Contract. "My prompts are loose on purpose. The agent finds structure in the files around it. The brief shape is what I use one level down."

## Slide 29 [Wajib] 25 principles, and one of them is mine
**Timing:** 1.0 min (clock 35:00)
**Say:** poteto-mode is an agent-style skill. I ported it to omp. It brings 25 principles and 23 playbooks, and it makes the agent say which principle shaped each decision. One principle is my own, check every layer. For any plan or review, the agent must look at three layers, product and the human walk, structure, and data and flow. Agents fix the layer they are looking at, and this rule makes them look at the other two.
**Evidence:** poteto-mode is an agent style skill from the pstack plugin (MIT license, upstream by poteto). I ported it to omp and keep a fork. 25 principles (11 core, 6 architecture, 5 verification, 2 delegation, 1 meta) and 23 playbooks. Examples are Prove It Works, Fix Root Causes, Never Block on the Human, and playbooks for bug fix, babysit, shipping and orchestrate. Run the count of principles and playbooks before the talk and say the real number. The skill demands a visible effect. The reply must name each principle that shaped a decision and the choice it changed. I end many prompts with the word "poteto", and an extension loads the skill once per context. Check every layer is my own principle, added on top of poteto. For any design, plan, review or build, give findings on three layers or one line on why a layer does not apply. A rule file loads it on every turn for the main agent, reviewers and task agents. An example agent reply with three findings goes here when it is captured. This folds the v1 poteto-mode slide and the v1 check-every-layer slide.

## Slide 30 [Opsional] Why beads was dropped
**Timing:** 0.5 min (clock 36:00)
**Say:** Beads is a task tracker that I used on purpose and then removed. Agents got smarter, so they need less task tracking. Beads is also hard for humans to read. Now I use GitHub issues and the logs of my coordinator.
**Evidence:** My own account, 2026-11-05, and the SHIP coordinator ledger. Agents got smarter. Beads is not really human-readable. Agents keep context better now with compaction and the memory layer. It is fine to remove a tool when the model gets better.

## Slide 31 [Wajib] Try this, write the skill
**Timing:** 0.5 min (clock 36:30)
**Say:** Here is the thing to try. The next time you repeat a task for the third time, stop. Write it down as a skill, even a small one. Next time the agent does it for you.
**Evidence:** The audience action for Part 2. Link to the answers from the chat question on slide 22.

---

# Part 3. One writer per branch (37:00 to 48:00)

## Slide 32 [Wajib] Divider, Part 3
**Timing:** 1.0 min (clock 37:00)
**Delivery:** Look at the lens. Throughline: parallel agents stay safe because of the setup around them.
**Chat:** Ask "How many agents do you run at once? Tell us in chat." Wait 5 s. Read two or three answers aloud. If someone says one, say that is a fine place to start. This is organizer question 4.
**Say:** Part 3 is about running many agents at once. How many agents do you run at the same time? Tell us in chat.
**Evidence:** Divider for Part 3 of 5. The principle for this part comes after the story, on slide 34.

## Slide 33 [Wajib] Idle agents never saw the messages
**Timing:** 2.0 min (clock 38:00)
**Say:** Here is something that went wrong. My agents talk to each other with a plugin I call mesh. The coordinator sent a message to every agent. But an agent that has gone idle does not wake up when a message arrives, so those agents never read it. So now each branch gets one owner agent that is running. My coordinator wrote this lesson in its own log: "idle sessions don't wake on mesh messages; each branch needs one writer". Messages are not enough. Ownership has to be clear.
**Evidence:** SHIP coordinator ledger, 2026-11-02. The ledger rows are "started fresh owners for #488 ... because their sessions had ended and never saw the broadcast" and "idle sessions don't wake on mesh messages; each branch needs one writer". The second row was the old slide quote, now only said aloud. Idle sessions do not wake on mesh messages. A session that ended never sees a broadcast. So each branch gets one writer. A dead owner is replaced by a fresh one, and the reason goes into the ledger. Subagents and sessions outside the configured roots get `MESH_NOT_JOINED`. This is the lesson from running agents for days. The word mesh stays off this slide face because slide 36 defines it.

## Slide 34 [Wajib] Principle 3, one writer per branch
**Timing:** 1.0 min (clock 40:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the third principle. One writer per branch. You can have many agents and many branches. But on each branch, exactly one agent writes. Two writers on one branch is how work gets lost.
**Evidence:** Principle 3 of 5. The proof slides that follow are worktrees, mesh, my plugins and the coordinator.

## Slide 35 [Wajib] Every agent task gets its own copy of the repo
**Timing:** 2.0 min (clock 41:00)
**Say:** A worktree is its own copy of the repo. Every task gets one, so agents never share a working folder. Each copy has its own folder and its own branch, for one agent. I built a small command called tern-wt to manage them. Tern, my terminal app, makes each copy as a tab and offers to remove it when I close the tab. The skill tells the agent to use that one command and not to remove a worktree it did not create.
**Evidence:** The slide is a diagram. One repo in the middle, three copies around it. The real `tern-wt list --all` output had 101 worktrees. One of them was dirty, with 83 changes, owned by tern. The screenshot `deck/assets/tern-wt-list.png` stays on disk and is not on the slide. My plugin `tern-worktrees` has three parts. A Tern plugin (branch picker, keep or tear down on close), a CLI `tern-wt`, and a skill that is the contract agents follow. `tern-wt` prints one JSON object with stable error codes such as `dirty_worktree`. A copy-on-write clone brings `.env` and `node_modules` along. One command is the one implementation of each git and GitHub step. The rule "use tern-wt, not git worktree" stays in this note. The repo is not public, so it is not on the Links slide.

## Slide 36 [Wajib] Mesh, how agents see each other
**Timing:** 2.0 min (clock 43:00)
**Say:** Mesh means agents see what the others are holding. Many sessions share one machine, one set of ports, and one Docker daemon. Before heavy work, an agent checks who else is working. If a peer is running the same job, it waits and sends a message. These three cards are real agents. The last one is my SHIP coordinator, holding the production release until I say go.
**Evidence:** The three cards are re-typeset from the real `mesh peers` capture taken 2026-11-05, not a screenshot. ADDR agent, "#580 round 2 PASS at 56b3b308a, frozen and merge-ready, waiting for the owner's go". SEARCH agent, "#579 merged as 3e7320e63. Nothing held". SHIP coordinator, "queue empty. Master fffb86f48, staging green. Prod release ... held for operator go". Handles and hashes are left off the slide. The capture counted 19 peers in 8 repo groups. 8 were in the Alkhidmah group, and 11 more in 6 other repos. The caption uses the 19. The raw screenshot `deck/assets/mesh-peers.png` stays on disk. Many omp sessions share one machine, one set of ports, one Docker daemon. Mesh stops two agents running the same heavy job or editing the same file. Actions are `peers`, `note`, `send`, `broadcast`, `claim`, `release`. Edits to a file another agent claimed are blocked automatically. The shared event log had 10,083 lines on 2026-11-05. 101 session files used the tool. The AGENTS.md rule text stays in this note. If the clock is early, make a one-minute live `peers` call.

## Slide 37 [Opsional] I wrote the mesh plugin myself
**Timing:** 1.0 min (clock 45:00)
**Say:** This is why I chose omp. When something hurts, I write a plugin. Here is my plugin list, and the mesh plugin is enabled. It took seven commits over two days. It is public, and the link is at the end.
**Evidence:** Source is the omp plugin lockfile (`~/.omp/plugins/omp-plugins.lock.json`), with `ls ~/.omp/agent/extensions/` below it and omp-agent-mesh boxed. omp-agent-mesh (my own Effect-based engine) is the hero. Seven more, each written when something hurt. omp-org-account-router, tern-worktrees, poteto-mode, paseo-omp, opencode-go-multi-auth, herdr state hooks, and muse-sub (retired 2026-10-10). The org account router puts office repos on the office account and personal repos on personal accounts. paseo-omp has 237 commits from September to October 2026.

## Slide 38 [Wajib] One coordinator merges after an independent review
**Timing:** 1.5 min (clock 46:00)
**Say:** I do not watch every branch. I watch one coordinator. A worker opens a PR with proof and says it is ready. The coordinator freezes that version and asks an independent reviewer to check it. If the review passes, the coordinator merges, one branch at a time. If it fails, the findings go back for one fix round.
**Evidence:** A coordinator is an ordinary omp session, not a daemon. The SHIP run lasted about three days (2 to 5 November) and kept a 276-line ledger (2026-11-03). Ledgers from SHIP and the merge queue, 2026-10-29 to 2026-11-05. Worker contract. Do not merge. Send `MERGE-READY #<pr> <full sha>`. The coordinator freezes the head. An independent reviewer writes a verdict file. PASS means squash merge and clean up. FAIL means findings go back, one fix round, in one push. Product questions go to the coordinator, not to me. Each decision is one row with a reason. The ledger columns are ts, phase, decision, why, evidence, result. Base branch coordination is solved by my omp-agent-mesh plugin plus one spawned coordinator agent that guides the workers. Many PRs against one base branch need someone who knows the state of every branch. When mesh cannot reach a worker, the coordinator reads that worker's session file and types into its tab. The loop still runs. Example. When a reviewer proves a PR leaks data on a throwaway database, the coordinator decides whether it blocks the release, and writes down why. "This used to be my hardest problem. It is not an open problem for me now." This folds two v1 slides, the coordinator loop and base branch coordination.

## Slide 39 [Wajib] Try this, one worktree per agent
**Timing:** 0.5 min (clock 47:30)
**Say:** Here is the thing to try. When you run two agents on one repo, give each its own worktree. It is one git command. It stops the two agents from stepping on each other.
**Evidence:** The audience action for Part 3. The command is `git worktree add`. Link to the chat answers from slide 32.

---

# Part 4. Show proof, not "done" (48:00 to 57:00)

## Slide 40 [Wajib] Divider, Part 4
**Timing:** 1.0 min (clock 48:00)
**Delivery:** Look at the lens. Throughline: an agent saying done is not proof.
**Chat:** Ask "Which part of your agent's work do you still check by hand? Tell us in chat." Wait 5 s. Read two or three answers aloud. Come back to them on slide 55, where I say what I still check by hand. This is organizer question 9.
**Say:** Part 4 is about trusting the result. When your agent says it is done, what do you still check by hand? Tell us in chat.
**Evidence:** Divider for Part 4 of 5. The principle for this part comes after the story, on slide 43.

## Slide 41 [Wajib] The proof that came with the plane fix
**Timing:** 1.5 min (clock 49:00)
**Say:** Remember the plane? This is the proof that came with that fix. Same sensor, same click. On the left, before the fix, clicking a draft opens the edit modal. On the right, after the fix, the click only selects the sensor. The pencil in Machine Information still opens the modal.
**Evidence:** GinaV2 PR #804 attached recordings, frame at 14 seconds, serial numbers hidden. Point at the modal on the left, then at the same click on the right. The agent recorded the before clip at 09:29 and the after clip during the fix. This moved from the opening in v1 to here as the callback.

## Slide 42 [Wajib] Red on the old code, green with the fix
**Timing:** 1.5 min (clock 50:30)
**Say:** The PR also has a test result. Three test runs failed on the old code. The same three passed with the fix. It used the same data that broke staging. A failing run before and a passing run after is the proof. It shows the test can actually fail.
**Evidence:** GinaV2 PR #804 body, Verification section. The line says the Python gateway test file had 3 failed on the old code, with the same gateway value and None that staging returned, and 3 pass with the fix. The screenshot `deck/assets/pr804-verification.png` stays on disk. It is still used by the demo PR slide. Red on old code, green with the fix.

## Slide 43 [Wajib] Principle 4, show proof, not done
**Timing:** 1.0 min (clock 52:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the fourth principle. Show proof, not "done". A PR is ready when it shows evidence, not when the agent says so. For me, proof means a recording for what you can see, and a command with real output for everything else.
**Evidence:** PR body shape. A PR body is a briefing, one minute for a reviewer who already has the diff. Sections in order are Why, How, What changed, Scope, Tradeoffs, Blast Radius, Verification. Verification has one bullet per claim, proof beside it, and ends with "Not verified:" and a list, or "Not verified: none". Proof ladder. Take the first rung that shows the claim. Recording for visible behavior (before and after for a bug). Command and real output for API or CLI. Run link for CI. Test command and result when nothing is visible. There is no magic validate command. Proof comes from the Prove It Works principle and this PR shape. Every proof link is one the agent produced or opened in that session. GinaV2 PRs open as drafts. The seven section names and the four rungs are said aloud, not drawn.

## Slide 44 [Wajib] A second agent freezes its verdict
**Timing:** 1.5 min (clock 53:00)
**Say:** The reviewer does not trust the author. A second agent reads the PR in a clean worktree and freezes its verdict at one commit. Here the verdict is pass with notes. It checked that the test fails on main and passes on the PR, that it merges cleanly, that the types check and that lint is clean. If a new commit lands, it gets a new review round. I still check the UI and the visual feel by hand.
**Evidence:** Coordinator review report for PR #580, 2026-11-05, re-typeset as a card. Frozen verdict "PASS+NOTES at head 592b92ae9". Gate table. The `verify.ts` verdict is PROVEN. Red run on master `f160aa8c4` (2026-11-05T06-17-41), green run on head (2026-11-05T06-22-39), 4 of 4 passed. Desktop 1280 and mobile 390. `merge-tree` with origin/master is clean. `check-types` is clean on head and on the merged tree. `bunx vp check` is clean on head and on the merged tree. Also unit and e2e on a throwaway database that is removed after. The reviewer checked that `gh pr view` returned the same head at the start and at the end. Findings are tagged P2 or P3 with confidence, file and line, and a fix. Real FAILs included a README command that errored when run as written. The screenshot `deck/assets/review-580-gates.png` stays on disk.

## Slide 45 [Wajib] Demo check, the PR from the phone
**Timing:** 2.0 min (clock 54:30)
**Delivery:** Name the expected output first: Why, proof, Not verified. Time-box this to 90 s. If the PR is not ready or the page is slow, say exactly: "The live run is slow today, so here is the recording from this morning." Then show the recording and the PR #804 body as the reference. Read what is on screen aloud.
**Say:** Now let us open the PR my agent made from the phone. I look for three things. A Why section, proof in the body, and an honest Not verified line. If it finished, I walk through the body now. If it did not finish, I say which step it is on and show the recording. I do not wait for it.
**Evidence:** Live. The PR page in the browser, scrolled to Verification. If the PR is not ready, the slide is the fallback view. The PR #804 body, rendered from the PR markdown with GitHub's renderer, cropped to the draft click bullet and its before and after table. The slide shows no expected-output cards, so name Why, proof and Not verified aloud. PR #804 has no "Not verified:" line, say so. If the run finished, walk through the body in 60 seconds. Show the recording or screenshots the agent attached. Source is the GinaV2 PR #804 body.

## Slide 46 [Wajib] Try this, ask for a clip
**Timing:** 0.5 min (clock 56:30)
**Say:** Here is the thing to try. In your next PR, ask the agent for a before and after clip. It costs one sentence in the prompt. Reviewers will thank you.
**Evidence:** The audience action for Part 4. Link to the chat answers from slide 40.

---

# Part 5. Make it safe to walk away (57:00 to 64:00)

## Slide 47 [Wajib] Divider, Part 5
**Timing:** 1.0 min (clock 57:00)
**Delivery:** Look at the lens. Throughline: the machines and rules around the agent are the setup.
**Chat:** Ask "Where do your agents run: laptop, server or cloud? Tell us in chat." Wait 5 s. Read two or three answers aloud. Use them on slide 51, where I show my machines. This is organizer question 10.
**Say:** Part 5 is about running it safely. Where do your agents run, on a laptop, a server or the cloud? Tell us in chat.
**Evidence:** Divider for Part 5 of 5. The principle for this part comes after the story, on slide 49.

## Slide 48 [Wajib] Every production change goes four steps
**Timing:** 1.5 min (clock 58:00)
**Say:** Every production change follows the same four steps. First a dry run, which runs the real update inside a transaction and rolls it back. Then a backup. Then the apply, with the expected row counts checked. Then verify the result. My prompt is simple. "Dry run first, then show me what will be changed." That way a colleague can confirm the list. A human can repeat every step.
**Evidence:** My groundup-ops dry-run runbook and my prompt of 2026-11-05. Prod is read-only by default. No writes without approval. Show the plan before anything heavy. Every write goes dry run, backup, guarded apply, verify. Dry run runs the real update inside a transaction, rolls back, and prints the preview table and counts. Apply needs `--apply`, and a wrong row count rolls back. A deploy is done only when the running version is verified, not when the job is green. The deploy call is an acceptance receipt, not a rollout receipt.

## Slide 49 [Wajib] Principle 5, make it safe to walk away
**Timing:** 0.5 min (clock 59:30)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the fifth principle. Make it safe to walk away. A human can repeat every step, and secrets stay hidden. Then I can leave the agent working and go on a plane.
**Evidence:** Principle 5 of 5. The proof slides that follow are secrets, the machine map, one-command setup and the terminal journey.

## Slide 50 [Wajib] Three layers protect my secrets
**Timing:** 1.5 min (clock 60:00)
**Say:** These are layers. The first hides values from the model, so it sees placeholders and not the real secret. The second blocks dangerous commands, like rm -rf, a force push, or DROP TABLE. The third decides where secrets live. Infisical for machines, Bitwarden for humans. Hiding a value is not the same as managing a secret.
**Evidence:** Source is `~/dotfiles/omp/agent/damage-control-rules.yaml` and `~/.omp/agent/config.yml` (secrets). omp obfuscates secrets by default. Damage-control rules block `rm -rf`, `git reset --hard`, force push, `DROP TABLE`. `~/.ssh/` is zero access. `.env` files are read-only. Secrets come from Infisical (machines) or Bitwarden (humans). Never print them. In my own words, obfuscation is not secret management. Say the zero access and read-only details aloud, they are not on the slide. The rules file with `zeroAccessPaths` and `readOnlyPaths` goes here when captured.

## Slide 51 [Wajib] Proof runs away from my workstation
**Timing:** 1.0 min (clock 61:30)
**Say:** My workstation is busy running agents, so proof runs on other machines. A shared dev box runs one stack per user. A batch box runs jobs. An office box runs staging. Production is read-only by default. I never show my ssh config on stage.
**Evidence:** Machine map snapshot, 2026-11-05. x1 is the Linux workstation that runs the agents. The Mac (m5) is for review and browser. Both are on one private network. A shared dev box runs one compose stack per user, so proof comes from a real running stack away from the workstation. Another box handles batch jobs and the NAS. An office box runs staging. Cloud production is reached through IAP tunnels and is read-only by default. Agents use plain ssh aliases. No IPs or host addresses on the slide.

## Slide 52 [Opsional] One command, one running stack
**Timing:** 0.5 min (clock 62:30)
**Say:** A new worktree needs a running stack. I do not configure it by hand. I run one command, bun run bootstrap. The ports and the database come from the branch name, so two worktrees never fight over a port.
**Evidence:** Source is the Alkhidmah devkit README, `bun run bootstrap`, from a fresh clone or a fresh worktree. Ports and database tier come from arithmetic on the branch slug. GinaV2 uses one shared env file, symlinked as `.env` in every checkout. The agent never configures a stack by hand. The setup is in the repo, so a new worktree is a command. Real `bootstrap` output (ports, tier) goes here when captured.

## Slide 53 [Opsional] Each terminal step removed one chore
**Timing:** 0.5 min (clock 63:00)
**Say:** My terminal changed five times. Each step removed one chore. OpenChamber gave me a web UI for OpenCode. Ghostty gave me windows and tabs. herdr handled worktrees and sessions. I tried Paseo and stopped it. Now I use Tern, and it has an Android app for my phone.
**Evidence:** My terminal history. OpenChamber, then the Ghostty terminal (windows and tabs) because of omp, then herdr for worktrees and sessions (migration 2026-06-27). Tried Paseo to get something easier with more managed worktrees, evaluated 2026-06-23, daemon stopped 2026-10-16. Now Tern, from Stencil, and I just use Tern. I stopped on Tern because worktrees, tabs and the phone are in one place.

## Slide 54 [Wajib] Try this, dry run first
**Timing:** 0.5 min (clock 63:30)
**Say:** Here is the thing to try. Before your next production change, ask for a dry run. Ask the agent to show you what will change. Then decide.
**Evidence:** The audience action for Part 5. Link to the chat answers from slide 47.

---

# What is still hard (64:00 to 68:00)

## Slide 55 [Wajib] A proof clip cannot judge how a screen looks
**Timing:** 1.5 min (clock 64:00)
**Delivery:** Pause 1 to 2 s after the headline. Look at the lens when you say it.
**Say:** I want to be honest about three open problems. The first one is the screen. A clip proves that a button works. It does not prove that the screen looks right. So I still check UI, visual feel and UX by hand. Use the chat answers from Part 4 here. The next two slides are the other two problems.
**Evidence:** Agent-built UI is still fat and ugly. It needs design skills and my manual feedback. The things I still check by hand are UI and visual feel, and UX. Proof clips show that a button works. They do not show that it looks right. Two screenshots side by side, one agent-built screen before design feedback and one after, go here when captured (Alkhidmah, no customer data). "This is honest. The agent can prove a flow works. It cannot yet tell me the screen feels right."

## Slide 56 [Wajib] Worktree setup is still too slow
**Timing:** 1.0 min (clock 65:30)
**Say:** The second problem is setup time. Each new worktree needs a database with test data, which we call a seed. One fix took it from 652 seconds to 171 seconds. That is better, and it is still too slow. Agents create many worktrees, and each one pays 171 seconds.
**Evidence:** My own timing of the per-worktree seed, before and after one fix. Setting up a database and seed per worktree is slow and heavy. Every new worktree pays this cost, and agents create many. "Parallel agents are only as cheap as a worktree is. 171 seconds is better, and still too slow."

## Slide 57 [Wajib] One test run used 38 GB of RAM
**Timing:** 1.5 min (clock 66:30)
**Say:** The third problem is memory. Agents and two CI runners share one workstation. One test run without a cap reached 38 GB. The fix was not a memory upgrade. It was a rule that fires when a test command appears, and it tells the agent to cap memory first. A rule with a condition on the command is a cheap guardrail.
**Evidence:** Memory-cap rule in `~/.omp/agent/rules`, verify script threshold, on my shared workstation. An uncapped test run reached 38 GB. A rule now fires when test commands appear. It tells the agent to cap memory and check free RAM first. The verify script refuses to run below 15 GiB free. These are two different numbers. 38 GB is what one run reached. 15 GiB is the free memory the script needs before it starts. A memory graph of the run goes here if one is captured.

---

# Close (68:00 to 71:00)

## Slide 58 [Wajib] The five principles and the claim
**Timing:** 1.5 min (clock 68:00)
**Delivery:** Say the claim slowly, then pause 1 to 2 s. Look at the lens.
**Say:** Here are the five principles again. Measure it on your own work. Do it twice, make it a skill. One writer per branch. Show proof, not "done". Make it safe to walk away. The model is a swappable part, and the setup does the work. If you do one thing on Monday, write a skill the third time you repeat a task.
**Evidence:** The claim in full. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails." The skill rule. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." Two small habits that cost nothing. Ask for proof in every PR. Dry-run anything that touches production. Say the claim again, slowly, then the rule, then stop.

## Slide 59 [Wajib] Links
**Timing:** 0.5 min (clock 69:30)
**Say:** These are the links if you want to dig deeper. The omp repo, the prewalk article, Can Bölük's article on X, and two plugins I wrote. The slides link goes in the chat.
**Evidence:** Every URL was checked on 2026-11-06. github.com/can1357/oh-my-pi, `gh repo view` shows PUBLIC and HTTP 200. stencil.so/blog/prewalk, HTTP 200 and the page is the prewalk article by Can Bölük. x.com/_can1357/status/2021828033640911196, HTTP 200 for the real id and 404 for made-up ids, and the article title matches the screenshot. github.com/masrurimz/omp-agent-mesh and github.com/masrurimz/omp-org-account-router, `gh repo view` shows PUBLIC and HTTP 200. Left out. tern-worktrees, because no public repo under my account was found. omp-skills, because it is private.

## Slide 60 [Wajib] Questions
**Timing:** 1.0 min (clock 70:00)
**Delivery:** For every question, repeat the question, answer the core, and link back to the claim. Say "I don't know" plainly and offer a follow-up path. If the room is quiet, use a seed question from the Q&A prep below. Keep the phone mirror open for a live peek at `mesh peers` or the PR.
**Say:** Questions are welcome, in chat or out loud. Thank you, SWE Growth. The slides link is in the chat. My GitHub handle is masrurimz if you want to follow up.
**Evidence:** Q&A starts at 71:00 and runs to about 90:00 with slack. GitHub handle @masrurimz. No QR code, because Drive sharing is not decided.

---

# Q&A prep

Likely questions. How much does it cost for a beginner. Which model for which role. Is it safe to run agents for days. Why not Claude Code alone. How to start with one skill.

Why is prewalk off? On my short tasks it cost the same or more, and the one time I tried a cheaper target (DeepSeek) it was really slow. It may still help on long sessions and with a faster cheap target, which I have not tried. See slide 18.

Seed question if quiet. What is the first task you would turn into a skill?
