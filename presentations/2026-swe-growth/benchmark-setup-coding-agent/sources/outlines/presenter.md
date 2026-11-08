# Benchmarking My Coding Agent Setup: One Engineer, Many Agents
## Presenter outline, live talk for SWE Growth

**SWE Growth community (Mas Zikrul), online on Zoom**
**90 minutes. All slides in English.**
**Speaker: Zahid**

## Notes for the presenter
- This is the v4 deck. It has 73 slides, and dividers are numbered slides. The plan is 86 minutes of talking and 4 minutes of Q&A. The build lint checks that the slide timings add up to 86 and that each clock value follows from the one before.
- The slides speak to the audience. Sources, dates, caveats, timing and chat cues live here, in the speaker notes. Each block has `Say:` (what you say, in your own words) and `Evidence:` (the facts behind the slide, for questions).
- Timing is minutes of talking. The clock value is the target, not a promise.
- Label **[Wajib]** means keep the slide. Label **[Opsional]** means cut it if time is short. Every slide that answers an organizer question is Wajib.
- Each part runs divider, story, principle, proof, then one thing to try. The story comes first. The number or the principle comes after it.
- Say "if I paid per token" every time a dollar figure appears on a slide. It is the list price of the tokens, not money paid. In the notes this is called API-equivalent.
- The claim, which every part supports or limits. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."
- Live demo checkpoints. Start at about minute 13 (slide 13). Check the PR at about minute 65 (slide 54). A recording of the full run is ready, and it is never named on a slide. The phone screen is shared next to the laptop.
- Terms are defined where they first appear, in the `Say:` line. Harness (slide 10), SHIP (slide 13), skill (slide 27), poteto-mode (slide 35), worktree (slide 43), mesh (slide 44). The v1 glossary slide is cut.

## Run of show

| Clock | Section | Slides | Talk time | Organizer questions |
|---|---|---|---|---|
| 0:00 to 6:00 | Opening (includes the map) | 1 to 6 | 6 min | none |
| 6:00 to 15:00 | My journey (demo starts) | 7 to 13 | 9 min | 1 |
| 15:00 to 30:00 | Part 1. Measure it on your own work | 14 to 25 | 15 min | 2, 3, 11 |
| 30:00 to 45:00 | Part 2. Do it twice, make it a skill | 26 to 38 | 15 min | 5, 7, 8 |
| 45:00 to 57:00 | Part 3. One writer per branch | 39 to 47 | 12 min | 4, 6 |
| 57:00 to 67:30 | Part 4. Show proof, not "done" (demo check) | 48 to 55 | 10.5 min | 9 |
| 67:30 to 76:00 | Part 5. Make it safe to walk away | 56 to 64 | 8.5 min | 6, 10 |
| 76:00 to 83:00 | What is still hard | 65 to 70 | 7 min | 12 |
| 83:00 to 86:00 | Close | 71 to 73 | 3 min | none |

Total talk time is 86 minutes (6 + 9 + 15 + 15 + 12 + 10.5 + 8.5 + 7 + 3). Q&A is the other 4 minutes. Part 1 has eight proof slides, more than the five the shape suggests, because the content map keeps every benchmark slide. Protect Part 1, because it matches the title.

## Cut order if time is short
Cut in this order. Each cut saves about the time shown.
1. Slide 45 (my plugins), 1 min. Say it on slide 44. It is the only [Opsional] slide.
2. On slide 32, skip the compaction sentence, 0.5 min.

Every other slide holds the answer to an organizer question, so none is cut. If the clock is still behind, shorten the chat reading on the dividers.

The core stays intact. The claim, the benchmark story and its proof (slides 15 to 22), skills, mesh and the coordinator hub, the PR proof frames, the production steps, and what is still hard.

## Coverage of the 12 organizer questions

| # | Question | Slides |
|---|---|---|
| 1 | Tool evolution and why each switch | 7, 8, 9, 10, 11 |
| 2 | Model routing per role | 17, 18 |
| 3 | Effort and thinking level | 17, 19 |
| 4 | Orchestration and parallel agents | 40, 41, 43, 44, 45, 46 |
| 5 | Task and spec management, beads | 33, 36, 37 |
| 6 | Long-horizon runs and guardrails | 41, 46, 57, 59 |
| 7 | Memory and context | 31, 32 |
| 8 | Own skills, favorites | 27, 28, 29, 30, 35, 36 |
| 9 | Review and quality gate, manual checks | 49, 50, 52, 53, 66 |
| 10 | Supporting infra | 60, 61, 62, 63 |
| 11 | Cost and subscription strategy | 15, 18, 20, 21, 22, 23, 24 |
| 12 | Open problems | 65, 66, 67, 68, 69, 70 |

---

# Opening (0:00 to 6:00)

## Slide 1 [Wajib] Title
**Timing:** 0.5 min (clock 0:00)
**Delivery:** Look at the lens, not at the slide. Say the throughline in one sentence: the model is swappable, and the setup around it ships the work. Speak at 130 to 150 words per minute.
**Say:** Hello everyone, and thank you to Mas Zikrul and SWE Growth. This is a casual talk about one real setup. I will show real numbers, and I will also show what still does not work.
**Evidence:** Title card, dark background, no logos of model vendors. SWE Growth community, online. The subtitle names the speaker. The talk is 90 minutes on Zoom in English, for a mixed Indonesian developer audience.

## Slide 2 [Wajib] The 9:29 phone screenshot
**Timing:** 1.0 min (clock 0:30)
**Say:** This is my phone at 9:29 in the morning. I was sitting in the plane, before takeoff. I typed one line from my phone. The agent opened our app on the dev server, took this screenshot itself, and confirmed the bug. Let me show you how I got there.
**Evidence:** Tuesday, 27 October 2026, 9:29 WIB, on board the plane before takeoff. An omp session on a phone in the Tern Android app, chat style. The phone sent text only: at 09:26 Zahid pasted QA's WhatsApp finding and typed one line. The Tern mobile app cannot attach screenshots or files. The screenshot in the chat is the agent's own: headless Chromium on x1 against the groundup-dev stack, one click on a draft sensor, which opened the edit modal. It then recorded `draftclick-before.mp4`. The product screen inside the agent's screenshot is blurred at build time, so only the shape of an open modal shows. Serial numbers are blurred too, and 9:29 is circled. Two enlarged crops carry the labels "9:29 WIB" and "The agent took this screenshot". The file is `sources/references/screenshot-omp-mobile-0929.png`.

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
**Evidence:** The quote is the exact title of his X article, checked against the live page on 2026-11-05. Say "article", not "post". The screenshot shows the article header with the hero image, "Can Bölük @can1357", and a box on the title. The article URL is on the Links slide (slide 72). This is the claim of the talk from someone with no reason to flatter my setup.

## Slide 6 [Wajib] The map
**Timing:** 1.0 min (clock 5:00)
**Say:** Before we start, here is the plan. First my journey, the tools I tried and why I left. Part 1 is choosing models and paying for them. Part 2 is teaching the agent. Part 3 is many agents at once. Part 4 is trusting the result. Part 5 is running it safely. Then what is still hard. Ask in chat at any time. I will answer at the end.
**Evidence:** One list in `deck/content.py` (`MAP`) draws this slide, the strip at the bottom of every divider, and the divider titles, so the part names live in one place. Where the 12 organizer questions land. Tools and why I switched (1) in My journey. Models, effort and cost (2, 3, 11) in Part 1. Skills, memory and specs (5, 7, 8) in Part 2. Many agents (4) and long runs (6) in Part 3. Review and quality (9) in Part 4. Infra and secrets (10) in Part 5, with the accident guardrails (6). Open problems (12) in What is still hard. Question numbers stay off the slide face.

---

# My journey (6:00 to 15:00)

## Slide 7 [Wajib] My tool journey and why each switch
**Timing:** 2.0 min (clock 6:00)
**Delivery:** Pause 1 to 2 s after the headline. Look at the lens when you say it.
**Chat:** Ask "Which coding agent do you use today?" in chat and read two or three answers aloud. This is organizer question 1.
**Say:** Copilot opened to everyone in June 2022, and I started then, years before Claude Code existed. Then Claude Code inside VS Code. Then Gemini, then OpenCode with oh-my-opencode, which was token hungry. When I started running agents in parallel, VS Code was too heavy, so I moved to Ghostty, Neovim and Amp. Then omp, because I can extend it. Each switch had a reason.
**Evidence:** Copilot technical preview was 2021-06-29 as a VS Code extension with a waitlist (GitHub blog, "Introducing GitHub Copilot: your AI pair programmer", https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/). Copilot became generally available to all developers on 2022-06-21 for $10 a month, free for verified students (GitHub blog, https://github.blog/news-insights/product-news/github-copilot-is-generally-available-to-all-developers/). Zahid confirmed on 2026-11-07 that he started at that launch, so the first event reads 2022. Claude Code launched 2025-02-24 (Anthropic, research preview). The VS Code extensions folder on the current Mac dates from 2024-03-13. That only shows when VS Code data on this Mac begins, not when he started. Gemini folder 2025-07-29. OpenCode 2025-10-20. Amp data 2025-12-22, Neovim data 2026-01-04 on the Mac. omp 2026-02-23 on the Mac, main tool on x1 from 2026-03-07. The other `when` labels are approximate years or first-use months from those folders. The slide is a six-event timeline with no date scale, because the disk dates conflict with the order Zahid gave (the Claude data folder on the Mac dates from 2025-10-19, Gemini from 2025-07-29). In his words, "I adopted VS Code Copilot early, before Claude Code even existed". OpenCode reads "token hungry", from his words "I always ran it with OmO. It was token hungry, slow, and its tests didn't catch much." The last event is highlighted because omp is the one that stayed. Antigravity is not on the timeline. It has its own slide (slide 9).

## Slide 8 [Wajib] Running agents in parallel pushed me out of the editor
**Timing:** 1.0 min (clock 8:00)
**Say:** One agent in an editor is fine. Four agents in four editors is not. I moved to the terminal so the memory goes to the agents, not the windows.
**Evidence:** My own reason, 2026-11-07, in my words: "to conserve resource because I start working agent in parallel". Not measured. The slide has two cards. VS Code, "One agent, and a heavy app" (muted). Terminal, "Ghostty and Neovim, many agents, less memory" (highlighted). Do not quote a memory number, there is none.

## Slide 9 [Wajib] Antigravity
**Timing:** 1.0 min (clock 9:00)
**Say:** Before omp, I used Antigravity from Google. It was the first tool I used with a proper plan mode, memory, and design artifacts. Its screen was built around agents, not around an editor. That changed how I thought about a coding tool. My Google account got banned, so I moved on. I still use it in one place, because omp uses its image model when I need a picture.
**Evidence:** Organizer question 1. In Zahid's words, Antigravity was the first tool with a proper plan mode, memory, design artifacts, and an agent-first UI instead of an editor-first one. His Google account was banned (prompt of 2026-03-10). It still serves as omp's image model, `google-antigravity/gemini-3-pro-image`. It has no dated event, so it is not on the timeline on slide 7. The four cards carry headings only, and the caption says it was the first tool with all four.

## Slide 10 [Wajib] What is a harness
**Timing:** 1.0 min (clock 10:00)
**Say:** A harness is the program around the model. It gives the model tools, context, memory and rules. Claude Code, Cursor and omp are harnesses. Claude, GPT and GLM are models. You can swap the model and keep the harness. This talk is about the harness.
**Evidence:** Many of you use Claude Code or Cursor, so keep this to two sentences and move on. Harness examples are Claude Code, Cursor, OpenCode, Amp and omp. Model examples are Claude, GPT and GLM. The v1 glossary slide ("six terms before they appear", after Mayer's pre-training principle of multimedia learning) is cut. Each term is now defined by you, in plain words, on the slide where it first appears. Many listeners work in a second language, so do not rush.

## Slide 11 [Wajib] Why omp
**Timing:** 1.5 min (clock 11:00)
**Say:** I forgot why I left Amp, but omp is better because I can extend it. When something hurts, I write a plugin. Autolearn means the agent writes a skill after a session. Hindsight is the memory tool I use. Compaction means the agent shortens a long chat so it can keep going. The next parts are full of plugins I wrote.
**Evidence:** My reasons for omp, 2026-11-05, from `~/.omp/agent/config.yml`. Plugins I write, autolearn, Hindsight memory, multi-provider subscription logins, and good compaction. That extensibility is why the later slides exist. Mesh, the org account router and the worktree plugin are all mine. A harness you can extend lets you fix your own problems, which is why the setup keeps moving. Say the joke about forgetting Amp once, then give the real answer. A small screenshot of `ls ~/.omp/agent/extensions/` was planned and not captured.

## Slide 12 [Wajib] From one chat to many agents
**Timing:** 1.0 min (clock 12:30)
**Say:** This is my omp stats dashboard, everything since March. Each bar is one day of requests. Until July it is mostly one chat at a time. From August it is many agents at once, and the busiest day had about 30,000 requests. In total that is 840,000 requests and 139 billion tokens. Almost all of those tokens are the same context read again from cache. Keep that in mind, because it is why the bill stays small. That comes back in Part 1. That change to many agents is why the rest of the talk is about coordination.
**Evidence:** omp stats dashboard (`omp stats --port`, range All), captured 2026-11-07 after a fresh sync. The cards read 839,969 requests (3,406 failed, 0.4%), 139B conversation tokens (474M output) and a 97.5% cache rate. In `~/.omp/stats.db`, cache reads are 96.5% of all tokens, which the dashboard's token mix rounds to 97%, the number on the label. Requests per month: March 36k, April 0.8k, May 2.2k, June 23k, July 46k, August 174k, September 235k, October 270k, 1 to 7 November 53k. Tokens per month: June 3.6B, July 7.8B, August 25.7B, September 50.2B, October 41.1B. September has more tokens than October with fewer requests, because September requests were bigger, about 214k tokens each across GLM, muse, Codex and OpenCode Go, against about 154k for Anthropic in October. Why they were bigger is not measured. The busiest day is 18 October in UTC with 31,448 requests (the tallest bar), or 19 October in WIB with 27,845, so say "about 30,000". March is the first month of stats on this workstation. There is no recorded reason for the April dip; if asked, say so. The cost side of October is on slide 22.

## Slide 13 [Wajib] Live demo, start from the phone
**Timing:** 1.5 min (clock 13:30)
**Delivery:** Narrate each step and name the expected output before you press send. Time-box this to 90 s. If the run is slow or fails, say exactly: "The live run is slow today, so here is the recording from this morning." Then play the recording and move on. Do not debug live.
**Say:** Now the live demo. You are looking at my real phone. I will send one prompt from the Tern Android app. It asks for a new worktree, a trace of the flow, a fix, and a PR with proof in the body. SHIP is my coordinator agent, and poteto is a keyword that loads my agent-style skill. The agent works while I keep talking, and we open the PR later.
**Evidence:** A small real issue from the Alkhidmah backlog. The slide shows the prompt text only. Goal is a PR with proof in the body, checked at about minute 62 (slide 54). The recording of the full run is cued in a second window, and it is not named on any slide. The phone mirror sits next to the laptop with the Tern session open and the prompt typed in my own style. After sending the prompt, go straight to the next slide.

---

# Part 1. Measure it on your own work (15:00 to 30:00)

Part 1 is built on `references/referensi-benchmark-lab.md`. The story is one engineer who measures. A model per role, a value formula, a bench of his own, a finding about effort, a handoff trick he tested and turned off, and a subscription journey that ended with "all in on Claude 5.5".

## Slide 14 [Wajib] Divider, Part 1
**Timing:** 1.0 min (clock 15:00)
**Delivery:** Look at the lens. Throughline: I pick models with a bench I built, not a feeling.
**Chat:** Ask "Per token or per subscription? Tell us in chat." Wait 5 s before you speak. Read two or three answers aloud. Use them on slide 22, where I say what I pay. This is organizer question 11.
**Say:** Part 1 is about choosing models and paying for them. How do you pay for your agent today, per token or with a subscription? Tell us in chat. I will come back to your answers when I show my own bill.
**Evidence:** Divider for Part 1 of 5. The principle for this part comes after the story, on slide 16.

## Slide 15 [Wajib] The fastest model on paper was the slowest in my hands
**Timing:** 2.0 min (clock 16:00)
**Say:** In September I ranked models with a formula. It liked DeepSeek flash, because on paper it runs at 118 tokens per second. Then I ran a real task. Opus finished in 92 seconds. DeepSeek needed 476 seconds, with 28 steps against 9 for Opus. Each step was fast, but there were many more steps. My formula had no term for steps.
**Evidence:** My October 2026 bench, UI task, 3 runs each, medians. Opus 5.5 low 92 s with 9 turns, Sonnet 5.5 medium 94 s with 10 turns, Haiku 5.5 medium 170 s with 15 turns, DeepSeek flash low 476 s with 28 turns. Tokens per second is speed per call, and a task is many calls. September ranking (2026-09-14). DeepSeek V4.1-Flash scored 90.6 on Terminal-Bench 2.1 at about 118 tokens per second. GLM-5.3 scored 88.2 at about 42. The formula, which is cut from the slides. Value Multiplier = Quota $ / Subscription cost. Effective $/1M = Blended $/1M / Value Multiplier. Value Score = Benchmark / Effective $/1M. Speed-adjusted QSPD = (Benchmark x tok/s) / (Effective $/1M x 1000). A price per million tokens misleads, because a subscription changes what a token costs. Rules. One common benchmark only (Terminal-Bench 2.1). Count the accounts. `cost_total` is API-equivalent, not spend. GLM is verbose, so compare tokens used too. The September numbers are a point in time. This is the honest part of the benchmark story. Turn counts are medians over three runs on the UI task.

## Slide 16 [Wajib] Principle 1, measure it on your own work
**Timing:** 0.5 min (clock 18:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the first principle. Measure it on your own work. A benchmark on paper is a guess. Your own task is the test.
**Evidence:** Principle 1 of 5. The proof slides that follow are the routing per job, the bench result, the effort finding, prewalk, the cost and the plan change.

## Slide 17 [Wajib] Each job gets its own model
**Timing:** 1.5 min (clock 18:30)
**Delivery:** Pause 1 to 2 s after the headline.
**Say:** I do not pick a model per prompt. I pick one per job. When I chat with the agent, I use Opus at low effort. For planning and hard bugs I use Opus at high. UI design goes to Sonnet at high. Review gets Opus at medium. Exploring the code goes to Haiku, the small fast model. My rule of thumb is low to do, medium to review, high to plan and for hard bugs. Max I almost never use.
**Evidence:** Organizer questions 2 and 3. The roles from `~/.omp/agent/config.yml` (`modelRoles`, read 2026-11-07). Default is Opus 5.5 at low. Plan and slow are Opus 5.5 at high. Reviewer is Opus 5.5 at medium. Designer and advisor are Sonnet 5.5 at high. Smol, librarian and fast are Haiku 5.5. The designer agent appears in 316 session files, mostly UI redesign tasks. The slide shows five jobs, chat, plan and hard bugs, UI design, review and explore. Effort rule. Low to do, medium to review, high to plan and for hard bugs, max almost never because it is slow and gave little gain. The next slides test the first half with a bench. Speed since 2026-10-01 (Anthropic, average per request) is Haiku 130 output tokens per second, Sonnet 95, Opus 66. These speeds are left off the slide on purpose, because slide 15 says tokens per second misled me. A fallback chain and a second account take over when a quota runs out. Time to first token is 2.6 seconds for Opus as main against 1.4 for Haiku. Effort is not recorded per request, so I cannot chart it from my usage. That is why I built a bench. Add the `modelRoles` block cropped so no account details show, if you have it open.

## Slide 18 [Wajib] Every model passed, speed and price decided
**Timing:** 2.0 min (clock 20:00)
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

## Slide 19 [Wajib] Thinking harder made the agent take more steps
**Timing:** 1.5 min (clock 22:00)
**Say:** I expected high effort to give better answers for the same cost. On these tasks it did something else. When I raised the thinking effort, the agent took more steps every time. Spark went from 9 to 23 steps. DeepSeek went from 28 to 40. My guess is checking, but that is my guess. The step counts are measured. This is why I almost never use max. It is slow, and it gave me little gain. More steps probably means a longer wait, but that is my inference, because I did not time the high-effort runs.
**Evidence:** My October 2026 bench, 2 tasks x 3 runs, medians. Pairs, lower effort then higher effort. Haiku slot finder 12 turns (medium) to 16 (high). Spark slot finder 9 (low) to 23 (medium). Sonnet UI 7 (low) to 10 (medium). DeepSeek UI 28 (low) to 40 (high). The likely cause is checking. Higher effort re-reads and re-checks, and each check is a turn. This cause is an inference. The turn counts are measured. Raising effort raised the turn count in every pair I measured. That more steps means a longer wait is also an inference, because high-effort runs were not timed. My rule stays. Low to do, medium to review, high to plan and for hard bugs, max almost never because it is slow and gave little gain. This covers execution on easy work. The "high for plans" half is my judgment.

## Slide 20 [Wajib] Plan with the big model, let a small one type
**Timing:** 1.0 min (clock 23:30)
**Say:** Prewalk is a trick from Can Bölük. The strong model reads the code and writes a todo list. At the first edit, omp switches the same session to a cheaper model. The cheap model makes the edits. The idea is that reading costs money and editing is cheap. I tested it on my own work.
**Evidence:** Prewalk is off by default in omp. The starting model, here Opus 5.5, reads the repo and writes a todo list. At the first file edit, omp switches the same session to a cheaper or faster model. Source is the omp docs and stencil.so/blog/prewalk by Can Bölük. Reading is what costs money. Edits were about 9% of the tokens in his logs. Two lines from his post, said aloud and not shown. "Opus fixing things does not cost money. Opus reading things costs money." and "Hand off a trajectory, not a fairytale", meaning the cheap model keeps the real work history, not a made-up summary. Say what a todo list is in one breath. Only Claude 5.5 names are on the slide.

## Slide 21 [Wajib] Prewalk was cheaper on long tasks, but slower
**Timing:** 1.5 min (clock 24:30)
**Say:** My first setup was Opus at low effort for planning, and Haiku at high for the edits. On long tasks that was cheaper. But it was slow, and tasks took too long to finish. UI work also needed a better model than Haiku. So I turned the handoff off and moved my task agents to Sonnet at medium. On my short test tasks, prewalk cost the same or more. Test it on your own work.
**Evidence:** First setup, 14 Oct 2026 prompt: "default will be opus low default prewalk will be into haiku high". Opus 5.5 low plans, prewalk into Haiku 5.5 high. 23 Oct prompts: "the issue now task is taking too long to complete" (with the Haiku high prewalk), then "disable the prewalk and go with sonnet medium for task". On 7 Nov I said prewalk was cheaper for longer tasks but slower, and I switched to Sonnet medium because I needed better UI work. There are no numbers for Opus low into Haiku high. "Cheaper on long tasks" for that setup is my own account. The only long-session numbers are a log estimate from uncontrolled work, not graded. At 50 or more turns, Sonnet medium alone is about $2.58 a task against $1.63 into Haiku medium. Bench, short tasks, 2 tasks (UI page, slot finder) x 3 runs, medians, API-equivalent cost, Claude 5.5, every arm passed all 126 checks. Opus low alone cost $0.39 (UI) and $0.22 (slot finder). Opus low into Sonnet low cost $0.48 and $0.35. Sonnet medium alone cost $0.24 and $0.17. Sonnet medium into Haiku medium cost $0.36 and $0.17, a tie on the slot finder. Times. In the bench, prewalk was slower in every pair with a solo run to compare: Opus low 92 s to 136 s (UI) and 54 s to 84 s (slot finder), Sonnet medium 94 s to 157 s and 84 s to 127 s. Second try. 24 Oct Sonnet medium into Haiku medium. 25 Oct DeepSeek v4.1 flash as the target, really slow, and I turned it off the same day. Config now. `task` and `poteto-agent` run Sonnet 5.5 medium, and `task.agentPrewalk` is off for both. Can Bölük's own test with other models, not mine, GPT-5.6 Sol into Luna and Opus 4.8 into Flash on SWE-Bench Pro, cut cost 39 to 47 percent for 3 to 7 points of pass rate. That is his workload, not mine.

## Slide 22 [Wajib] Cost in October
**Timing:** 1.5 min (clock 26:00)
**Say:** In October my agents used tokens that would cost about 7,300 dollars at list price. I paid about 200 dollars. One flat subscription plus caching carries a lot of work. Most of the tokens were cache reads, and those are cheap. I usually pay about 100 dollars a month, and this month about 200 because I push a lot.
**Evidence:** October 2026 from omp stats (`~/.omp/stats.db`), re-aggregated 2026-11-05. 270k requests, 41B tokens, $7.3k API-equivalent (the list price of the tokens, not money paid). I paid about $200. That is roughly 36 times less. 97% of tokens were cache reads. Without caching the same work prices at $58.2k. Two thirds of requests came from subagents. I pay for 2x Claude Max and OpenCode Go. Usually about $100 a month, now about $200. Cache reads are cheap, which is why the multiple is so large. Use the chat answers from the Part 1 divider here.

## Slide 23 [Wajib] When quality moved, I moved
**Timing:** 1.0 min (clock 27:30)
**Say:** When the Claude 5.5 models arrived, I changed my plans. In my own words, Claude 5.5 quality is GOAT, which means greatest of all time. The model is the part I swap most often, and that links back to the claim.
**Evidence:** Plans verified 2026-09-14, usage by provider from omp stats 2026-11-05. September 2026. GLM Max, my own one-year plan bought cheap at the launch price. Codex Pro from the office. Devin Pro and OpenCode Go, my own. The default model was GLM-5.3. Eight months, at least 12 providers, by requests. Anthropic 240k, GLM 224k, Codex 128k. November so far is Anthropic only. Then the Claude 5.5 series arrived and I went all in on Claude. The quote is "Claude 5.5 series quality is GOAT". Close the part with "The model is the part I swap most often".

## Slide 24 [Wajib] Three money tips
**Timing:** 1.0 min (clock 28:30)
**Chat:** Use the answers to the Part 1 divider question here. Ask who pays per token and who pays a flat plan. This is organizer question 11.
**Say:** Three money tips from my own bills. One. Pay a flat plan and let caching work. In October, 97 percent of my tokens were cache reads. Two. Use a cheap model to search, like Haiku, and a strong model to plan, like Opus at high effort. Three. Test any cost trick on your own work before you trust it. Prewalk was cheaper on my long tasks, but slower.
**Evidence:** Organizer question 11. Tip one is from my October 2026 bill (slide 22). 97% of tokens were cache reads, and the same work was worth about $7.3k at list price (API-equivalent, not money paid) against about $200 paid. Tip two follows the model roles on slide 17. Haiku searches, and Opus 5.5 at high effort plans. Tip three is slide 21. Prewalk was cheaper on my long tasks (my own account, plus a log estimate that is not graded) and slower. On the short bench tasks it cost the same or more. No dollar figure is on the slide face, so say "if I paid per token" when you quote one.

## Slide 25 [Wajib] Try this, time one real task
**Timing:** 0.5 min (clock 29:30)
**Say:** Here is one thing to try this week. Take one real task you do often. Run it on two different models and write down the time. That takes one afternoon, and then you know.
**Evidence:** The audience action for Part 1. No new numbers.

---

# Part 2. Do it twice, make it a skill (30:00 to 45:00)

## Slide 26 [Wajib] Divider, Part 2
**Timing:** 1.0 min (clock 30:00)
**Delivery:** Look at the lens. Throughline: the model is swappable, and what stays is what the agent knows.
**Chat:** Ask "Which task do you repeat with your agent more than twice? Tell us in chat." Wait 5 s. Read two or three answers aloud. Come back to them on slide 30 and on the try slide. This is organizer question 8.
**Say:** Part 2 is about teaching the agent. Think about your own work for a moment. Which task do you repeat with your agent more than twice? Tell us in chat.
**Evidence:** Divider for Part 2 of 5. The principle for this part comes after the story, on slide 30.

## Slide 27 [Wajib] Autolearn made too many skills
**Timing:** 2.0 min (clock 31:00)
**Say:** A skill is a short file the agent loads when the work matches. Autolearn is a feature where the agent writes a skill after a session. I turned it on and it created too many small skills. So I merged them into 14 area skills, one for each area of work. Now I run autolearn by hand, after a session that taught me something. Auto-on was too much noise, and a human decides what is worth keeping.
**Evidence:** The config line is `autolearn: { enabled: true, autoContinue: false }` in `~/.omp/agent/config.yml`. My own account, 2026-11-05. Many small skills, then 14 domain skills plus a lint, then a manual trigger after a session that taught something. This is a small guardrail for knowledge, not for code.

## Slide 28 [Wajib] The skills lint
**Timing:** 1.0 min (clock 33:00)
**Say:** To keep the 14 skills clean, I wrote a lint script. It checks the layout and exits with an error if something is wrong. A pre-commit hook runs it. The last run found 0 errors. The layout rule became a script, not a longer instruction.
**Evidence:** The omp-skills repo, `scripts/skills_lint.py`, run 2026-11-05. 14 area skills, one folder per domain, not per task. Examples are infra-ops, groundup-ops, alkhidmah-ops, git-pr-workflow, omp-ops, comms-ops, thesis-ops. `SKILL.md` is only a router. Playbooks are step lists to follow. References are facts to look up. The lint exits 1 on errors, and a pre-commit hook runs it. The real output reads "14 skills, 0 errors, 1 warnings". The warn line is cropped out because it names a personal reference file. The tree of `managed-skills/` stays in this note. A task reads one router and then one playbook, so unrelated work stays out of each other's context. When a lesson shows up, it goes into the matching area skill, not into a new skill.

## Slide 29 [Wajib] One skill per area, like PARA
**Timing:** 1.0 min (clock 34:00)
**Say:** I organize my skills by area. The idea comes from Tiago Forte's PARA method. PARA has four boxes. Projects have an end date. Areas never end, like infra or comms. Resources are topics you look things up in. Archives hold finished work. My skills follow the Areas box. That is how I got 14 area skills, one for each area of my work. My favorites are poteto-mode, my workflow skill, and show-me, which draws diagrams and wireframes.
**Evidence:** Organizer question 8. PARA is Projects, Areas, Resources, Archives, by Tiago Forte (fortelabs.com/blog/para). The card text is the usual PARA meaning, shortened. Areas map to my 14 area skills, one folder per area of work, for example infra-ops and comms-ops (see the lint on slide 28). Favorites are poteto-mode (slide 35) and show-me (draws diagrams and wireframes, slide 36).

## Slide 30 [Wajib] Principle 2, do it twice, make it a skill
**Timing:** 1.0 min (clock 35:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the second principle, and the one action I want you to take home. When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you. Tell one honest story here. A routine I repeated three times, like a deploy or a WhatsApp template check, became a skill.
**Evidence:** The rule in my words. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." A skill is a short file the agent loads when the work matches. It can include playbooks (steps to follow) and references (facts to look up). The folder shape is `SKILL.md`, `playbooks/`, `references/`. This rule returns at the close, on slide 71.

## Slide 31 [Wajib] Skills versus memory
**Timing:** 1.0 min (clock 36:00)
**Say:** Skills and memory do two different jobs. A skill holds how to do a thing, like the steps of a deploy. Memory holds what I did and decided, across projects. For example, a skill says how to run the release. Memory says that we chose one plan last month and why.
**Evidence:** In my words. "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project." TIL means "today I learned". Two stores, two jobs. The quote is said, not shown, because the headline carries the idea. Give one example for each side.

## Slide 32 [Wajib] Memory, and compaction
**Timing:** 2.0 min (clock 37:00)
**Say:** I do not trust one memory tool, so I tried three. I kept Hindsight because it fits the cross-project job, and the cost is controlled. It saves a note every 10 turns, because saving on every run is the most expensive option. Compaction is a second layer. When a chat gets long, the agent shortens it with three methods in order, so you do not need to watch the context window.
**Evidence:** Memory journey. Mnemopi before 2026-06-28, then Hindsight from 2026-06-28 (kept), then Cognee tried in September 2026 and destroyed on 2026-10-19. Config. `memory: backend: hindsight`, `hindsight: retainMode: last-turn, retainEveryNTurns: 10, retainOverlapTurns: 2`. The old data stayed untouched, so rollback is one config flip. Source is `~/.omp/agent/config.yml` and the Hindsight migration notes of 2026-06-28. Compaction (this was v1 slide 29, cut as a slide). Three methods in order, snapcompact, then remote, then soft. It starts at 70% of the context window, and compacts when idle after 60 seconds. Good compaction is one reason I dropped task tracking tools. "You do not need to watch the context window. You need a harness that compacts well and a memory layer behind it."

## Slide 33 [Wajib] My prompts are loose on purpose
**Timing:** 1.0 min (clock 39:00)
**Say:** I paste raw context into the agent. A WhatsApp message from QA, a screenshot, a spreadsheet. I do not write a ticket first. The structure is in the files around the prompt, not in the prompt. When I hand work to a subagent, the brief has one shape, target, change and contract.
**Evidence:** Instructions are layered. A short global file (`~/.omp/agent/AGENTS.md`) with hard rules. Small rule files in `~/.omp/agent/rules`, loaded always or on a regex. A repo AGENTS.md where the nearest file wins. Nested AGENTS.md files with a size budget that is checked. The brief for subagents has Target, Change, Contract. "My prompts are loose on purpose. The agent finds structure in the files around it. The brief shape is what I use one level down."

## Slide 34 [Wajib] A rule steps in the moment the agent types a risky command
**Timing:** 1.5 min (clock 40:00)
**Say:** omp has rules. A rule is a small file. Some are always in the prompt. Others wait for a pattern. When the agent starts typing pytest without a memory cap, omp stops the stream, adds the rule, and the agent rewrites the command. Rules stepped in 4,635 times since June. Most were omp's own TypeScript rules. 1,424 were my two memory caps.
**Evidence:** `~/.omp/agent/rules/` holds 5 files. 3 are `alwaysApply` (check-every-layer, pr-body, managed-skill-layout). 2 have a regex `condition` (pytest-resource-cap, test-runner-resource-cap). omp calls this TTSR (time traveling stream rules). It watches the streamed output, interrupts on a match and injects the rule. Session logs hold 4,635 `ttsr_injection` entries, from 2026-06 to 2026-11-07. test-runner-resource-cap 1,187, pytest-resource-cap 237, which together are the 1,424 memory-cap injections. The rest are omp built-in rules (ts-no-tiny-functions 1,691, ts-set-map 847, and others). The slide has two cards, "Always on" and "On a trigger" (highlighted), and the caption carries the 4,635.

## Slide 35 [Wajib] 25 principles, and one of them is mine
**Timing:** 1.0 min (clock 41:30)
**Say:** poteto-mode is an agent-style skill. I ported it to omp. It brings 25 principles and 23 playbooks, and it makes the agent say which principle shaped each decision. One principle is my own, check every layer. For any plan or review, the agent must look at three layers, product and the human walk, structure, and data and flow. Agents fix the layer they are looking at, and this rule makes them look at the other two.
**Evidence:** poteto-mode is an agent style skill from the pstack plugin (MIT license, upstream by poteto). I ported it to omp and keep a fork. 25 principles (11 core, 6 architecture, 5 verification, 2 delegation, 1 meta) and 23 playbooks. Examples are Prove It Works, Fix Root Causes, Never Block on the Human, and playbooks for bug fix, babysit, shipping and orchestrate. Run the count of principles and playbooks before the talk and say the real number. The skill demands a visible effect. The reply must name each principle that shaped a decision and the choice it changed. I end many prompts with the word "poteto", and an extension loads the skill once per context. Check every layer is my own principle, added on top of poteto. For any design, plan, review or build, give findings on three layers or one line on why a layer does not apply. A rule file loads it on every turn for the main agent, reviewers and task agents. An example agent reply with three findings goes here when it is captured. This folds the v1 poteto-mode slide and the v1 check-every-layer slide.

## Slide 36 [Wajib] Before any code, the agent draws the screen
**Timing:** 1.5 min (clock 42:30)
**Say:** Before any code, the agent draws the screen. This wireframe is a neutral example, not one of my apps. I start from the product and ask the agent for a wireframe. The show-me skill draws it. Then we decide the folders and files. Then the data and the flow, and we check each layer. All of it goes into one markdown file in a plans folder for that feature, so subagents do not wander. That file is the reference.
**Evidence:** Organizer questions 5 and 8. Each feature gets a `docs/plans/<feature>/` folder with wireframe SVGs. On 2026-10-26 I asked the agent to put the technical details and the SVG wireframe in one markdown file, so subagents would not wander. My flow is wireframe first, from the product, then folder and file structure, then data and flow, checked layer by layer with my check-every-layer principle (slide 35), then saved as the final reference. The show-me skill draws the wireframes. The picture on the slide is a newly drawn neutral wireframe (`deck/assets/wireframe-neutral.svg`), not one of the real plan files, which carry app labels. Task management is on slide 37.

## Slide 37 [Wajib] Why beads was dropped
**Timing:** 0.5 min (clock 44:00)
**Say:** Beads is a task tracker that I used on purpose and then removed. Agents got smarter, so they need less task tracking. Beads is also hard for humans to read. No hooks for tasks. GitHub issues and the coordinator's ledger hold the work, and CI does the checking.
**Evidence:** Organizer question 5. My own account, 2026-11-05, and the SHIP coordinator ledger. Agents got smarter. Beads is not really human-readable. Agents keep context better now with compaction and the memory layer. It is fine to remove a tool when the model gets better. The slide face says "No task hooks". Work lives in GitHub issues and the coordinator's ledger, and CI/CD does the checking. The spec flow is on slide 36.

## Slide 38 [Wajib] Try this, write the skill
**Timing:** 0.5 min (clock 44:30)
**Say:** Here is the thing to try. The next time you repeat a task for the third time, stop. Write it down as a skill, even a small one. Next time the agent does it for you.
**Evidence:** The audience action for Part 2. Link to the answers from the chat question on slide 26.

---

# Part 3. One writer per branch (45:00 to 57:00)

## Slide 39 [Wajib] Divider, Part 3
**Timing:** 1.0 min (clock 45:00)
**Delivery:** Look at the lens. Throughline: parallel agents stay safe because of the setup around them.
**Chat:** Ask "How many agents do you run at once? Tell us in chat." Wait 5 s. Read two or three answers aloud. If someone says one, say that is a fine place to start. This is organizer question 4.
**Say:** Part 3 is about running many agents at once. How many agents do you run at the same time? Tell us in chat.
**Evidence:** Divider for Part 3 of 5. The principle for this part comes after the story, on slide 42.

## Slide 40 [Wajib] On a busy hour, 4 to 9 agents work at once
**Timing:** 1.0 min (clock 46:00)
**Chat:** Compare with the chat answers to the Part 3 divider question. If someone said one, say that is a fine place to start. This is organizer question 4.
**Say:** This is every working hour since September. Most hours I have three agents going. In four hours out of ten, it is four to nine. That only works because I gave the agents full control of the dev infra. They start the stack, seed it and test it without me.
**Evidence:** stats.db `message_rollup`, main agents only, distinct project folders with activity in the same hour, 2026-09-01 to 2026-11-07, 1,128 hours. Median 3, 90th percentile 6. 436 of 1,128 hours (39%) had 4 to 9. 13 hours had 10 or more. Two hours at 61 and 62 are batch jobs and are in the 10+ bar only. A folder is a worktree or repo, so this counts workstreams, not processes. The bars are hours per agent count, 1 to 9 and 10+, with values 249, 219, 211, 172, 124, 67, 42, 21, 10, 13. The bar for 4 agents is highlighted. The axis label reads "hours".

## Slide 41 [Wajib] Idle agents never saw the messages
**Timing:** 2.0 min (clock 47:00)
**Say:** Here is something that went wrong. My agents talk to each other with a plugin I call mesh. The coordinator sent a message to every agent. But an agent that has gone idle does not wake up when a message arrives, so those agents never read it. So now each branch gets one owner agent that is running. My coordinator wrote this lesson in its own log: "idle sessions don't wake on mesh messages; each branch needs one writer". Messages are not enough. Ownership has to be clear.
**Evidence:** SHIP coordinator ledger, 2026-11-02. The ledger rows are "started fresh owners for #488 ... because their sessions had ended and never saw the broadcast" and "idle sessions don't wake on mesh messages; each branch needs one writer". The second row was the old slide quote, now only said aloud. Idle sessions do not wake on mesh messages. A session that ended never sees a broadcast. So each branch gets one writer. A dead owner is replaced by a fresh one, and the reason goes into the ledger. Subagents and sessions outside the configured roots get `MESH_NOT_JOINED`. This is the lesson from running agents for days. The word mesh stays off this slide face because slide 44 defines it.

## Slide 42 [Wajib] Principle 3, one writer per branch
**Timing:** 1.0 min (clock 49:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the third principle. One writer per branch. You can have many agents and many branches. But on each branch, exactly one agent writes. Two writers on one branch is how work gets lost.
**Evidence:** Principle 3 of 5. The proof slides that follow are worktrees, mesh, my plugins and the coordinator.

## Slide 43 [Wajib] Every agent task gets its own copy of the repo
**Timing:** 2.0 min (clock 50:00)
**Say:** A worktree is its own copy of the repo. Every task gets one, so agents never share a working folder. Each copy has its own folder and its own branch, for one agent. I built a small command called tern-wt to manage them. Tern, my terminal app, makes each copy as a tab and offers to remove it when I close the tab. The skill tells the agent to use that one command and not to remove a worktree it did not create.
**Evidence:** The slide is a diagram. One repo in the middle, three copies around it. The real `tern-wt list --all` output had 101 worktrees. One of them was dirty, with 83 changes, owned by tern. The screenshot `deck/assets/tern-wt-list.png` stays on disk and is not on the slide. My plugin `tern-worktrees` has three parts. A Tern plugin (branch picker, keep or tear down on close), a CLI `tern-wt`, and a skill that is the contract agents follow. `tern-wt` prints one JSON object with stable error codes such as `dirty_worktree`. A copy-on-write clone brings `.env` and `node_modules` along. One command is the one implementation of each git and GitHub step. The rule "use tern-wt, not git worktree" stays in this note. The repo is not public, so it is not on the Links slide.

## Slide 44 [Wajib] Mesh, how agents see each other
**Timing:** 2.0 min (clock 52:00)
**Say:** Mesh means agents see what the others are holding. Many sessions share one machine, one set of ports, and one Docker daemon. Before heavy work, an agent checks who else is working. If a peer is running the same job, it waits and sends a message. These three cards are real agents. The last one is my SHIP coordinator, holding the production release until I say go.
**Evidence:** The three cards are re-typeset from the real `mesh peers` capture taken 2026-11-05, not a screenshot. ADDR agent, "#580 round 2 PASS at 56b3b308a, frozen and merge-ready, waiting for the owner's go". SEARCH agent, "#579 merged as 3e7320e63. Nothing held". SHIP coordinator, "queue empty. Master fffb86f48, staging green. Prod release ... held for operator go". Handles and hashes are left off the slide. The capture counted 19 peers in 8 repo groups. 8 were in the Alkhidmah group, and 11 more in 6 other repos. The caption uses the 19. The raw screenshot `deck/assets/mesh-peers.png` stays on disk. Many omp sessions share one machine, one set of ports, one Docker daemon. Mesh stops two agents running the same heavy job or editing the same file. Actions are `peers`, `note`, `send`, `broadcast`, `claim`, `release`. Edits to a file another agent claimed are blocked automatically. The shared event log had 10,083 lines on 2026-11-05. 101 session files used the tool. The AGENTS.md rule text stays in this note. If the clock is early, make a one-minute live `peers` call.

## Slide 45 [Opsional] I wrote the mesh plugin myself
**Timing:** 1.0 min (clock 54:00)
**Say:** This is why I chose omp. When something hurts, I write a plugin. Here is my plugin list, and the mesh plugin is enabled. It took seven commits over two days. It is public, and the link is at the end.
**Evidence:** Source is the omp plugin lockfile (`~/.omp/plugins/omp-plugins.lock.json`), with `ls ~/.omp/agent/extensions/` below it and omp-agent-mesh boxed. omp-agent-mesh (my own Effect-based engine) is the hero. Seven more, each written when something hurt. omp-org-account-router, tern-worktrees, poteto-mode, paseo-omp, opencode-go-multi-auth, herdr state hooks, and muse-sub (retired 2026-10-10). The org account router puts office repos on the office account and personal repos on personal accounts. paseo-omp has 237 commits from September to October 2026.

## Slide 46 [Wajib] One coordinator merges after an independent review
**Timing:** 1.5 min (clock 55:00)
**Say:** I do not watch every branch. I watch one coordinator. A worker opens a PR with proof and sends one line. It says MERGE-READY, the PR number and the full commit. The coordinator freezes that commit and asks an independent reviewer to check it. If the review passes, the coordinator merges, one branch at a time. If it fails, the findings go back for one fix round. This also solves base branches, because the coordinator knows the state of every branch.
**Evidence:** A coordinator is an ordinary omp session, not a daemon. The SHIP coordinator ledger has 353 decisions from 2026-11-02 to 2026-11-07. Ledgers from SHIP and the merge queue, 2026-10-29 to 2026-11-05. Worker contract. Do not merge. Send `MERGE-READY #<pr> <full sha>`. The coordinator freezes the head. An independent reviewer writes a verdict file. PASS means squash merge and clean up. FAIL means findings go back, one fix round, in one push. Product questions go to the coordinator, not to me. Each decision is one row with a reason. The ledger columns are ts, phase, decision, why, evidence, result. Base branch coordination is solved by my omp-agent-mesh plugin plus one spawned coordinator agent that guides the workers. Many PRs against one base branch need someone who knows the state of every branch. When mesh cannot reach a worker, the coordinator reads that worker's session file and types into its tab. The loop still runs. Example. When a reviewer proves a PR leaks data on a throwaway database, the coordinator decides whether it blocks the release, and writes down why. "This used to be my hardest problem. It is not an open problem for me now." This folds two v1 slides, the coordinator loop and base branch coordination. Base branches were an organizer question, and the answer is "solved". The slide caption shows the handoff, MERGE-READY and the commit.

## Slide 47 [Wajib] Try this, one worktree per agent
**Timing:** 0.5 min (clock 56:30)
**Say:** Here is the thing to try. When you run two agents on one repo, give each its own worktree. It is one git command. It stops the two agents from stepping on each other.
**Evidence:** The audience action for Part 3. The command is `git worktree add`. Link to the chat answers from slide 39.

---

# Part 4. Show proof, not "done" (57:00 to 67:30)

## Slide 48 [Wajib] Divider, Part 4
**Timing:** 1.0 min (clock 57:00)
**Delivery:** Look at the lens. Throughline: an agent saying done is not proof.
**Chat:** Ask "Which part of your agent's work do you still check by hand? Tell us in chat." Wait 5 s. Read two or three answers aloud. Come back to them on slide 66, where I say what I still check by hand. This is organizer question 9.
**Say:** Part 4 is about trusting the result. When your agent says it is done, what do you still check by hand? Tell us in chat.
**Evidence:** Divider for Part 4 of 5. The principle for this part comes after the story, on slide 51.

## Slide 49 [Wajib] The proof that came with the plane fix
**Timing:** 1.5 min (clock 58:00)
**Say:** Remember the plane? This is the proof that came with that fix. Same sensor, same click. On the left, before the fix, clicking a draft opens the edit modal. On the right, after the fix, the click only selects the sensor. The pencil in Machine Information still opens the modal.
**Evidence:** GinaV2 PR #804 attached recordings, frame at 14 seconds, serial numbers hidden. Point at the modal on the left, then at the same click on the right. The agent recorded the before clip at 09:29 and the after clip during the fix. This moved from the opening in v1 to here as the callback.

## Slide 50 [Wajib] Red on the old code, green with the fix
**Timing:** 1.5 min (clock 59:30)
**Say:** The PR also has a test result. Three test runs failed on the old code. The same three passed with the fix. It used the same data that broke staging. A failing run before and a passing run after is the proof. It shows the test can actually fail.
**Evidence:** GinaV2 PR #804 body, Verification section. The line says the Python gateway test file had 3 failed on the old code, with the same gateway value and None that staging returned, and 3 pass with the fix. The screenshot `deck/assets/pr804-verification.png` stays on disk. It is still used by the demo PR slide. Red on old code, green with the fix.

## Slide 51 [Wajib] Principle 4, show proof, not done
**Timing:** 1.0 min (clock 61:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the fourth principle. Show proof, not "done". A PR is ready when it shows evidence, not when the agent says so. For me, proof means a recording for what you can see, and a command with real output for everything else.
**Evidence:** PR body shape. A PR body is a briefing, one minute for a reviewer who already has the diff. Sections in order are Why, How, What changed, Scope, Tradeoffs, Blast Radius, Verification. Verification has one bullet per claim, proof beside it, and ends with "Not verified:" and a list, or "Not verified: none". Proof ladder. Take the first rung that shows the claim. Recording for visible behavior (before and after for a bug). Command and real output for API or CLI. Run link for CI. Test command and result when nothing is visible. There is no magic validate command. Proof comes from the Prove It Works principle and this PR shape. Every proof link is one the agent produced or opened in that session. GinaV2 PRs open as drafts. The seven section names and the four rungs are said aloud, not drawn.

## Slide 52 [Wajib] Five checks run before I look
**Timing:** 1.5 min (clock 62:00)
**Chat:** Come back to the Part 4 divider answers. Ask which of the five checks people already have. This is organizer question 9.
**Say:** Five checks run before I look at a PR. One. The language server checks every edit as the agent makes it. Two. Lint and type checks. Three. Tests shaped like the testing trophy, from Kent C. Dodds. That means static checks, unit, integration and end to end. For risky logic I also use a formal verification skill. Four. Reviewer agents, and the number scales with the risk. A small fix gets one reviewer. A stack of five PRs got five. The impersonation PR got a security reviewer and a product reviewer. Five. Me. I still check the UI and the feel by hand.
**Evidence:** Organizer question 9. The five checks in order. (1) LSP diagnostics after every edit, `lsp.diagnosticsOnEdit: true`. (2) Lint and type checks. (3) Tests shaped like Kent C. Dodds' Testing Trophy (static, unit, integration, end to end), plus a formal-verification skill for risky logic. (4) Reviewer agents that scale with risk. One reviewer for a small fix, five for a five-PR stack, a security reviewer plus a product reviewer for the impersonation PR. Slide 53 shows what one reviewer freezes. (5) Zahid, who still checks UI and feel by hand (slide 66).

## Slide 53 [Wajib] A second agent freezes its verdict
**Timing:** 1.5 min (clock 63:30)
**Say:** The reviewer does not trust the author. A second agent reads the PR in a clean worktree and freezes its verdict at one commit. Here the verdict is pass with notes. It checked that the test fails on main and passes on the PR, that it merges cleanly, that the types check and that lint is clean. If a new commit lands, it gets a new review round. I still check the UI and the visual feel by hand.
**Evidence:** Coordinator review report for PR #580, 2026-11-05, re-typeset as a card. Frozen verdict "PASS+NOTES at head 592b92ae9". Gate table. The `verify.ts` verdict is PROVEN. Red run on master `f160aa8c4` (2026-11-05T06-17-41), green run on head (2026-11-05T06-22-39), 4 of 4 passed. Desktop 1280 and mobile 390. `merge-tree` with origin/master is clean. `check-types` is clean on head and on the merged tree. `bunx vp check` is clean on head and on the merged tree. Also unit and e2e on a throwaway database that is removed after. The reviewer checked that `gh pr view` returned the same head at the start and at the end. Findings are tagged P2 or P3 with confidence, file and line, and a fix. Real FAILs included a README command that errored when run as written. The screenshot `deck/assets/review-580-gates.png` stays on disk.

## Slide 54 [Wajib] Demo check, the PR from the phone
**Timing:** 2.0 min (clock 65:00)
**Delivery:** Name the expected output first: Why, proof, Not verified. Time-box this to 90 s. If the PR is not ready or the page is slow, say exactly: "The live run is slow today, so here is the recording from this morning." Then show the recording and the PR #804 body as the reference. Read what is on screen aloud.
**Say:** Now let us open the PR my agent made from the phone. I look for three things. A Why section, proof in the body, and an honest Not verified line. If it finished, I walk through the body now. If it did not finish, I say which step it is on and show the recording. I do not wait for it.
**Evidence:** Live. The PR page in the browser, scrolled to Verification. If the PR is not ready, the slide is the fallback view. The PR #804 body, rendered from the PR markdown with GitHub's renderer, cropped to the draft click bullet and its before and after table. The slide shows no expected-output cards, so name Why, proof and Not verified aloud. PR #804 has no "Not verified:" line, say so. If the run finished, walk through the body in 60 seconds. Show the recording or screenshots the agent attached. Source is the GinaV2 PR #804 body.

## Slide 55 [Wajib] Try this, ask for a clip
**Timing:** 0.5 min (clock 67:00)
**Say:** Here is the thing to try. In your next PR, ask the agent for a before and after clip. It costs one sentence in the prompt. Reviewers will thank you.
**Evidence:** The audience action for Part 4. Link to the chat answers from slide 48.

---

# Part 5. Make it safe to walk away (67:30 to 76:00)

## Slide 56 [Wajib] Divider, Part 5
**Timing:** 1.0 min (clock 67:30)
**Delivery:** Look at the lens. Throughline: the machines and rules around the agent are the setup.
**Chat:** Ask "Where do your agents run: laptop, server or cloud? Tell us in chat." Wait 5 s. Read two or three answers aloud. Use them on slide 61, where I show my machines. This is organizer question 10.
**Say:** Part 5 is about running it safely. Where do your agents run, on a laptop, a server or the cloud? Tell us in chat.
**Evidence:** Divider for Part 5 of 5. The principle for this part comes after the story, on slide 58.

## Slide 57 [Wajib] Every production change goes four steps
**Timing:** 1.5 min (clock 68:30)
**Say:** Every production change follows the same four steps. First a dry run, which runs the real update inside a transaction and rolls it back. Then a backup. Then the apply, with the expected row counts checked. Then verify the result. My prompt is simple. "Dry run first, then show me what will be changed." That way a colleague can confirm the list. A human can repeat every step.
**Evidence:** My groundup-ops dry-run runbook and my prompt of 2026-11-05. Prod is read-only by default. No writes without approval. Show the plan before anything heavy. Every write goes dry run, backup, guarded apply, verify. Dry run runs the real update inside a transaction, rolls back, and prints the preview table and counts. Apply needs `--apply`, and a wrong row count rolls back. A deploy is done only when the running version is verified, not when the job is green. The deploy call is an acceptance receipt, not a rollout receipt.

## Slide 58 [Wajib] Principle 5, make it safe to walk away
**Timing:** 0.5 min (clock 70:00)
**Delivery:** Pause 1 to 2 s after the principle. Look at the lens when you say it.
**Say:** This is the fifth principle. Make it safe to walk away. A human can repeat every step, and secrets stay hidden. Then I can leave the agent working and go on a plane.
**Evidence:** Principle 5 of 5. The proof slides that follow are secrets, the machine map, one-command setup and the terminal journey.

## Slide 59 [Wajib] Three accidents gave me three guardrails
**Timing:** 1.5 min (clock 70:30)
**Chat:** Ask "Has an agent ever deleted something it should not have?" Read two or three answers aloud. This is organizer question 6.
**Say:** I let agents run for days, so accidents happen. Here are three from my coordinator's ledger. First, an agent ran a reset in the main checkout. The devkit ignored one flag there and wiped the shared dev database. Now the devkit refuses any reset that reaches the shared database. Second, a reviewer agent ran a Docker prune and deleted about 244 unused volumes on the shared box, with no list of what was lost. Now Docker cleanup is banned for every agent, and the reviewer briefs say so. Third, one masking tool went through 11 reviews, and each one fixed one more shape of the same bug. Now there is a two-round review cap. After two failed rounds, we stop and rethink the design.
**Evidence:** Organizer question 6. The SHIP coordinator ledger has 353 decisions from 2026-11-02 to 2026-11-07. Accident 1, 2026-11-05 01:59 UTC. An agent ran `stack reset --fork -y` in the main checkout, and the devkit ignored `--fork` there and wiped the shared dev database and every fork. Guardrail, PR #574, the devkit now refuses any reset path that reaches the shared database. Accident 2, 2026-11-02. A reviewer agent ran `docker volume prune -f` and deleted about 244 unused volumes on the shared box. Guardrail, Docker cleanup is banned for every agent, and reviewer briefs say so. Accident 3, 2026-11-03. One masking tool went through 11 reviews, each fixing one more regex shape. Guardrail, a two-review-round cap. The handoff line from worker to coordinator is on slide 46.

## Slide 60 [Wajib] Three layers protect my secrets
**Timing:** 1.5 min (clock 72:00)
**Say:** These are layers. The first hides values from the model, so it sees placeholders and not the real secret. The second blocks dangerous commands, like rm -rf, a force push, or DROP TABLE. The third decides where secrets live. Infisical for machines, Bitwarden for humans. Hiding a value is not the same as managing a secret.
**Evidence:** Source is `~/dotfiles/omp/agent/damage-control-rules.yaml` and `~/.omp/agent/config.yml` (secrets). omp obfuscates secrets by default. Damage-control rules block `rm -rf`, `git reset --hard`, force push, `DROP TABLE`. `~/.ssh/` is zero access. `.env` files are read-only. Secrets come from Infisical (machines) or Bitwarden (humans). Never print them. In my own words, obfuscation is not secret management. Say the zero access and read-only details aloud, they are not on the slide. The rules file with `zeroAccessPaths` and `readOnlyPaths` goes here when captured.

## Slide 61 [Wajib] Proof runs away from my workstation
**Timing:** 1.0 min (clock 73:30)
**Say:** My workstation is busy running agents, so proof runs on other machines. A shared dev box runs one stack per user. A batch box runs jobs. An office box runs staging. Production is read-only by default. I never show my ssh config on stage.
**Evidence:** Machine map snapshot, 2026-11-05. x1 is the Linux workstation that runs the agents. The Mac (m5) is for review and browser. Both are on one private network. A shared dev box runs one compose stack per user, so proof comes from a real running stack away from the workstation. Another box handles batch jobs and the NAS. An office box runs staging. Cloud production is reached through IAP tunnels and is read-only by default. Agents use plain ssh aliases. No IPs or host addresses on the slide.

## Slide 62 [Wajib] One command, one running stack
**Timing:** 0.5 min (clock 74:30)
**Say:** A new worktree needs a running stack. I do not configure it by hand. I run one command, bun run bootstrap. The ports and the database come from the branch name, so two worktrees never fight over a port.
**Evidence:** Source is the Alkhidmah devkit README, `bun run bootstrap`, from a fresh clone or a fresh worktree. Ports and database tier come from arithmetic on the branch slug. GinaV2 uses one shared env file, symlinked as `.env` in every checkout. The agent never configures a stack by hand. The setup is in the repo, so a new worktree is a command. Real `bootstrap` output (ports, tier) goes here when captured.

## Slide 63 [Wajib] Each terminal step removed one chore
**Timing:** 0.5 min (clock 75:00)
**Say:** My terminal changed five times. Each step removed one chore. OpenChamber gave me a web UI for OpenCode. Ghostty gave me windows and tabs. herdr handled worktrees and sessions. I tried Paseo to get easier managed worktrees, and Tern replaced it. Now I use Tern, and it has an Android app for my phone.
**Evidence:** My terminal history. Organizer question 10. OpenChamber, then the Ghostty terminal (windows and tabs) because of omp, then herdr for worktrees and sessions (migration 2026-06-27). Tried Paseo to get something easier with more managed worktrees, evaluated 2026-06-23, daemon stopped 2026-10-16. Now Tern, from Stencil, and I just use Tern. I stopped on Tern because worktrees, tabs and the phone are in one place.

## Slide 64 [Wajib] Try this, dry run first
**Timing:** 0.5 min (clock 75:30)
**Say:** Here is the thing to try. Before your next production change, ask for a dry run. Ask the agent to show you what will change. Then decide.
**Evidence:** The audience action for Part 5. Link to the chat answers from slide 56.

---

# What is still hard (76:00 to 83:00)

## Slide 65 [Wajib] Divider, What is still hard
**Timing:** 0.5 min (clock 76:00)
**Delivery:** Look at the lens. Throughline: say the open problems plainly.
**Chat:** Ask "What still breaks for you? Tell us in chat." Wait 5 s. Read two or three answers aloud, and compare them with the four problems and the plan on the next slides. This is organizer question 12.
**Say:** Now the honest part. Four things are still hard for me. First, UI that an agent builds still needs design skills and my feedback. Second, CI is now the queue. Third, setting up the environment and the seed data for each worktree is still slow. Fourth, my disk is full. Then I will show what I am trying next. Base branches used to be on this list. Part 3 showed how the coordinator solved it.
**Evidence:** Divider for What is still hard, the sixth map segment, drawn like the Part dividers with the strip at the bottom. The four open problems are slides 66, 67, 68 and 69, and slide 70 is the plan for the fourth. Base branches were asked about and are answered in Part 3 as solved, by the coordinator on slide 46. Divider notes are the same shape as Part dividers, but this one has no principle slide.

## Slide 66 [Wajib] A proof clip cannot judge how a screen looks
**Timing:** 1.5 min (clock 76:30)
**Delivery:** Pause 1 to 2 s after the headline. Look at the lens when you say it.
**Say:** I want to be honest about four open problems. The screen, CI, the setup for each worktree, and my disk. Base branches used to be on this list. Part 3 showed how the coordinator solved it. The first problem is the screen. A clip proves that a button works. It does not prove that the screen looks right. So I still check UI, visual feel and UX by hand. Use the chat answers from Part 4 here. The next slides are the other three problems.
**Evidence:** Agent-built UI is still fat and ugly. It needs design skills and my manual feedback. The things I still check by hand are UI and visual feel, and UX. Proof clips show that a button works. They do not show that it looks right. Two screenshots side by side, one agent-built screen before design feedback and one after, go here when captured (Alkhidmah, no customer data). "This is honest. The agent can prove a flow works. It cannot yet tell me the screen feels right."

## Slide 67 [Wajib] Nine agents means nine PRs, and CI becomes the queue
**Timing:** 1.5 min (clock 78:00)
**Say:** More agents means more PRs, and every push runs CI. On one day in November my alkhidmah repo ran 538 CI runs: previews, checks and end-to-end tests. CI is now the slowest part of my loop. I am testing larger runners and spreading the load over free runners.
**Evidence:** `gh run list -R alkhidmah-tech/digital-platform --created 2026-11-04T17:00:00Z..2026-11-05T17:00:00Z`, which is 5 November in WIB, returned 538 workflow runs. Preview 148, check 119, e2e 115, link-check 67, deploy 34, readiness 33, runner-bakeoff 9, Dependabot 7. That day the 90th percentile run duration was 16.0 minutes, and 10.2% of runs took 16 minutes or more, which is the "1 in 10" on the slide. 29 runs took 30 minutes or more, and the longest took 82 minutes. From Zahid's 2026-11-05 prompts about joining CI jobs into larger runners and load balancing free runners. The larger and free runners are experiments, nothing is settled.

## Slide 68 [Wajib] Worktree setup is still too slow
**Timing:** 1.0 min (clock 79:30)
**Say:** The third problem is setup time. Each new worktree needs its environment and a database with test data, which we call a seed. One fix took env and seeding from 652 seconds to 171 seconds. That is better, and it is still too slow. At work the analytics app is heavier. It runs a large time series stack, so its seeding takes much longer. Agents create many worktrees, and each one pays that cost.
**Evidence:** My own timing of the per-worktree env and seed setup, before and after one fix. Setting up the environment and a database seed per worktree is slow and heavy. Every new worktree pays this cost, and agents create many. The analytics app at work is heavier, a large time series stack with a long seed. This is from Zahid, 2026-11-07, and its seeding time is not measured here. "Parallel agents are only as cheap as a worktree is. 171 seconds is better, and still too slow."

## Slide 69 [Wajib] Every branch wants its own full stack, and my disk is full
**Timing:** 1.5 min (clock 80:30)
**Say:** At work I build an agentic app on large time series data and analytics. Each branch needs an expensive stack and a long seed. Nine of those do not fit on one machine. My SSD is 89 percent full, and Docker alone holds 447 GB. One uncapped test run once took 38 GB of RAM, which is why the memory rule exists.
**Evidence:** `df -h` on x1, 2026-11-07. 902G filesystem, 777G used, 101G free, 89% used, Samsung 990 PRO 1TB. `docker system df`, same day. Images 173.7 GB, volumes 114.8 GB, build cache 158.7 GB, which is 447.2 GB in total. The 38 GB is from the memory cap rule. An uncapped full test run reached 38 GB of RAM on the shared workstation. The slide mutes that stat because it is RAM, not disk. This replaces the old memory slide. The memory rule itself is on slide 34.

## Slide 70 [Wajib] Next: stacks I can pause and wake up
**Timing:** 1.0 min (clock 82:00)
**Say:** What I am trying now is more aggressive serverless infra. Each stack lives in its own VM. When nobody uses it, it sleeps. When an agent needs it, it wakes up. A sleeping VM still takes disk, so I need a bigger SSD first.
**Evidence:** From Zahid, 2026-11-07. The SSD purchase came up in his 2026-10-25 prompts ("waiting for my ssd"). This is an experiment and nothing is shipped. Say plainly that it is a plan, not a result. The highlighted step is one VM per stack.

---

# Close (83:00 to 86:00)

## Slide 71 [Wajib] The five principles and the claim
**Timing:** 1.5 min (clock 83:00)
**Delivery:** Say the claim slowly, then pause 1 to 2 s. Look at the lens.
**Say:** Here are the five principles again. Measure it on your own work. Do it twice, make it a skill. One writer per branch. Show proof, not "done". Make it safe to walk away. The model is a swappable part, and the setup does the work. If you do one thing on Monday, write a skill the third time you repeat a task.
**Evidence:** The claim in full. "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails." The skill rule. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." Two small habits that cost nothing. Ask for proof in every PR. Dry-run anything that touches production. Say the claim again, slowly, then the rule, then stop.

## Slide 72 [Wajib] Links
**Timing:** 0.5 min (clock 84:30)
**Say:** These are the links if you want to dig deeper. The omp repo, the prewalk article, Can Bölük's article on X, and two plugins I wrote. The slides link goes in the chat.
**Evidence:** Every URL was checked on 2026-11-06. github.com/can1357/oh-my-pi, `gh repo view` shows PUBLIC and HTTP 200. stencil.so/blog/prewalk, HTTP 200 and the page is the prewalk article by Can Bölük. x.com/_can1357/status/2021828033640911196, HTTP 200 for the real id and 404 for made-up ids, and the article title matches the screenshot. github.com/masrurimz/omp-agent-mesh and github.com/masrurimz/omp-org-account-router, `gh repo view` shows PUBLIC and HTTP 200. Left out. tern-worktrees, because no public repo under my account was found. omp-skills, because it is private.

## Slide 73 [Wajib] Questions
**Timing:** 1.0 min (clock 85:00)
**Delivery:** For every question, repeat the question, answer the core, and link back to the claim. Say "I don't know" plainly and offer a follow-up path. If the room is quiet, use a seed question from the Q&A prep below. Keep the phone mirror open for a live peek at `mesh peers` or the PR.
**Say:** Questions are welcome, in chat or out loud. Thank you, SWE Growth. The slides link is in the chat. My GitHub handle is masrurimz if you want to follow up.
**Evidence:** Q&A starts at 86:00 and runs to about 90:00. GitHub handle @masrurimz. No QR code, because Drive sharing is not decided.

---

# Q&A prep

Likely questions. How much does it cost for a beginner. Which model for which role. Is it safe to run agents for days. Why not Claude Code alone. How to start with one skill.

Why is prewalk off? It was cheaper on my long tasks, but slower, and tasks took too long to finish. UI work also needed a better model than Haiku, so my task agents run Sonnet at medium with no handoff. On short tasks it cost the same or more. A second try on 24 and 25 October, with DeepSeek as the cheap model, was really slow. See slides 20 and 21.

Can you send screenshots from your phone? No. The Tern app on my phone sends text only, so I paste QA's message and links. The agent opens our app on the dev server, takes its own screenshots and recordings, and puts them in the PR. The screenshot on slide 2 is one of them.

Seed question if quiet. What is the first task you would turn into a skill?
