# Speaker guide: Benchmarking My Coding Agent Setup

Delivery plan for Zahid. 90 min, Zoom, English, mixed Indonesian developer audience, casual community format. The deck is v4, 73 slides, 86 minutes of talking and 4 minutes of Q&A.

Evidence tags. **strong** = replicated or meta-analysed. **moderate** = one or two controlled studies or a peer-reviewed review. **weak** = correlational, expert opinion, or rubric. **practitioner** = convention with no primary study found. `[INFERENCE]` marks my own reasoning, not a sourced finding. Source names refer to the list at the end. The speaking evidence base is thin, so most items are weak or practitioner. Do not oversell them.

## 1. Throughline and the three stories

**Throughline.** The model is a swappable part, and what lets one engineer ship from a phone is the setup around it: skills, proof, coordination and guardrails. [Anderson, one through-line; weak] Every story below either supports this line or shows where it breaks. [Anderson, weak]

Open with a "what is" the audience already accepts (everyone uses agents, almost nobody measures them), then the "what could be" the phone fix makes concrete. [Duarte sparkline; weak]

**The three stories to land.** One concrete story per section, number after the story, not stacked on it. [Small, Loewenstein & Slovic 2007, moderate for the effect, weak for transfer to talks; Dahlstrom 2014, moderate]

| # | Story | Slides | The point it proves | Number to say after the story |
|---|---|---|---|---|
| 1 | Phone fix. 9:29 on a plane, QA warning to QA pass | 2, 3, 49 (the before and after frames, as the callback), 54 | One engineer can ship from a phone | 65 minutes (08:52 to 09:57) |
| 2 | The bench. The fastest model on paper was the slowest in my hands, every model passed, so speed and cost separated | 15, 17, 18 | Measure your own workload, do not trust a trick | 476 seconds for DeepSeek flash against 92 for Opus; 126 of 126 checks in the notes |
| 3 | SHIP coordinator. Idle agents never saw the messages, so one writer per branch and one coordinator | 41, 46 | Coordination and proof beat a bigger model | 353 decisions in the ledger, 2 to 7 November |

If time runs short, cut in the order of presenter.md: slide 45 first (my plugins, 1 min, the only [Opsional] slide, say it on slide 44), then skip the compaction sentence on slide 32 (0.5 min). Every other slide holds the answer to an organizer question, so none is cut. If the clock is still behind, shorten the chat reading on the dividers. **Never cut the core.** That is the claim, the benchmark story and its proof (slides 15 to 22), skills, mesh and the coordinator hub, the PR proof frames, the production steps, and what is still hard, plus the two demo slides (13 and 54).

**The X quote on slide 5 is confirmed verbatim.** The line "I improved 15 LLMs at coding in one afternoon. Only the harness changed." is the exact title of Can Bölük's article on X (x.com/_can1357/status/2021828033640911196). It was checked against the live page on 2026-11-05, and the screenshot on the slide shows it. Say "article", not "post". The slide headline is a short paraphrase ("Only the harness changed, and 15 models got better."), so read the exact title aloud from the screenshot.

## 2. Rehearsal plan

Dates are relative to talk day (T-0). Nothing here has a primary study behind the counts. Practice before an audience is correlated with better speeches. [Menzel & Carrell 1994 via Smith thesis; weak-moderate] The counts are `[INFERENCE]`. [practitioner]

| When | What | Done when |
|---|---|---|
| T-7 | Write the throughline and the opening and closing scripts (below). Mark 1 to 2 s pause points in the slide notes. [Liu, Nakajima et al. 2022; moderate-weak] Run 1: full out-loud run-through alone, timed per section against the run of show. The talk is now 86 minutes, so Q&A has only 4. [practitioner] | Section times on paper, gaps over 20% flagged |
| T-7 | Record one 2-min section (suggest slide 15, the story of the fastest model on paper). Count words and divide by minutes. Target 130 to 150 wpm. [Tauroza & Allison 1990 via Nesi 2001; moderate for norms, target is `[INFERENCE]`] Count fillers in the same clip. [Corley & Stewart 2008; moderate for what fillers are] | wpm and filler count noted |
| T-3 | Run 2: full run-through out loud with 4 or more watchers, or recorded and watched back. [Smith thesis; weak-moderate] Watchers get one job: say where they lost the thread. Include a live phone demo from start to the PR. | Notes from watchers, demo run end to end once |
| T-3 | Rehearse the demo switch to the recording out loud, with the fallback sentence (section 5). [Low, Simple Talk; weak] | Switch takes under 10 s |
| T-1 | Run 3: opening (slides 1 to 6) and closing (slides 71 to 73) word for word, three times each, without notes. [Anderson valley of awkwardness; weak] Middle stays as bullets. Final audio and screen-share test on the real Zoom (section 3). | Opening and closing from memory |
| T-0 morning | Cyclic sighing, 5 min (section 8). One quiet read of the opening script. No new content. | Calm, not cramming |

**Time each section against the clock windows.** The windows are 0 to 6 (Opening), 6 to 15 (My journey), 15 to 30 (Part 1), 30 to 45 (Part 2), 45 to 57 (Part 3), 57 to 67.5 (Part 4), 67.5 to 76 (Part 5), 76 to 83 (What is still hard) and 83 to 86 (Close), then Q&A. Talk time inside them is 6, 9, 15, 15, 12, 10.5, 8.5, 7 and 3 minutes, 86 in total. Q&A takes the last 4 minutes, from 86:00 to about 90:00. The deck builds with those clock values, and the dividers show no minutes, so keep your own clock. Log actual minutes per section at T-7 and T-3. If a section runs over, pick cuts from the cut order in presenter.md, do not speed up. [practitioner]

### Opening script, memorize word for word (about 6 min, slides 1 to 6)

Drawn from the `Say:` lines of slides 1 to 6 in presenter.md. Pause 1 to 2 s where marked `/`. [Liu, Nakajima et al. 2022; moderate-weak] The faces carry a title, a phone screenshot, a four-point timeline, the claim hub, the quote screenshot and the map, so every number below comes from your voice.

> **Slide 1, title (0:00).** Hello everyone, and thank you to Mas Zikrul and SWE Growth. / This is a casual talk about one real setup. / I will show real numbers, and I will also show what still does not work. / If a word of mine is unclear, ask in chat, and I will say it again. /
>
> **Slide 2, the phone screenshot (0:30).** This is my phone at 9:29 in the morning. / I was sitting in the plane, before takeoff. / I spoke a prompt, and my agent had just reproduced a bug on a real running stack. / Let me show you how I got there. /
>
> **Slide 3, the timeline (1:30).** QA found one more problem on a pull request that was already approved. / At 9:26 I pasted the finding into my session from the phone. / The agent recorded the bug, fixed it, and updated the PR. / QA passed it at 9:57, / and most of that time I was not touching it. /
>
> **Slide 4, the claim (2:30).** Here is the claim of this talk. / The model is a swappable part. / The setup around it does the work. / I see four parts in the setup, skills, proof, coordination and guardrails. / Every part of the talk either supports this claim or shows where it breaks. /
>
> **Slide 5, the quote (3:30).** This is not only me saying this. / Can Bölük is the author of omp. / He wrote that he improved 15 models at coding in one afternoon, and only the harness changed. / A harness is the program around the model. / I will explain it on the slide after the journey. /
>
> **Slide 6, the map (5:00).** Before we start, here is the plan. / First my journey, the tools I tried and why I left. / Part 1 is choosing models and paying for them. / Part 2 is teaching the agent. / Part 3 is many agents at once. / Part 4 is trusting the result. / Part 5 is running it safely. / Then what is still hard. / Ask in chat at any time. I will answer at the end.

The line in the first slide, "If a word of mine is unclear...", is not in the `Say:` of slide 1. It comes from the old script and keeps the second-language promise (section 6). Keep it. The number "65 minutes" is in the Evidence line of slide 3, not in `Say:`. Say it after the story if you want it: "Sixty-five... minutes, from the warning to the pass." The map on slide 6 is the same list that appears as a strip at the bottom of every divider, with a "you are here" label, so the audience can find their question again later.

### Closing script, memorize word for word (about 3 min, slides 71 to 73)

Drawn from the `Say:` lines of slides 71 to 73. Say the claim slowly, then the rule, then stop. [Duarte: audiences remember the last thing; weak] Slide 71 shows the five principles under the claim, so you can read down the list as you speak.

> **Slide 71, the five principles and the claim (83:00).** Here are the five principles again. / Measure it on your own work. / Do it twice, make it a skill. / One writer per branch. / Show proof, not "done". / Make it safe to walk away. / The model is a swappable part, and the setup does the work. / If you do one thing on Monday, write a skill the third time you repeat a task. /
>
> **Slide 72, links (84:30).** These are the links if you want to dig deeper. / The omp repo, the prewalk article, Can Bölük's article on X, and two plugins I wrote. / The slides link goes in the chat. /
>
> **Slide 73, questions (85:00).** Questions are welcome, in chat or out loud. / Thank you, SWE Growth. / The slides link is in the chat. / My GitHub handle is masrurimz if you want to follow up.

The two small habits (ask for proof in every PR, dry-run anything that touches production) live in the Evidence line of slide 71. Hold them for Q&A, because the slide-71 Say ends on the skill rule. Q&A has only 4 minutes, so start it on time at 86:00.

## 3. Zoom setup checklist

- [ ] **Audio first.** Wired headset or close external mic. Record a 1-min test on the exact Zoom setup and listen back on headphones. [Newman & Schwarz 2018; moderate] Degraded audio lowered ratings of the talk, the speaker's intelligence and likeability.
- [ ] If audio is poor on the day, say so once at the start. [Newman & Schwarz 2018, moderate by proxy]
- [ ] **Camera at eye level.** Slides or notes window just under the lens, and look slightly below the lens. Perceived eye contact peaked about 2 degrees below the lens in a 17-person photo study. [Gao et al. 2025; weak-moderate] Look at the lens at section starts and transitions. [`INFERENCE`; practitioner]
- [ ] **Hide self-view** after framing. Shrink the Zoom window. Constant self-view and big close-up faces are tiring. [Bailenson 2021, via Stanford summary; weak-moderate]
- [ ] Front light, head in the upper third, arm's length from the camera. Stand if the layout allows. [`INFERENCE`; practitioner. Bailenson suggests movement helps; weak-moderate]
- [ ] **Screen-share hygiene.** [practitioner, no primary study]
  - Do Not Disturb on, all notifications off.
  - Separate Chrome profile with nothing logged in but what the demo needs, no bookmarks bar.
  - Terminal font size 20 or larger. Check it at 50% zoom on a recorded share.
  - Close Slack and WhatsApp desktop, email, and any tab with customer or tenant names.
- [ ] **Phone mirroring for the demo.** The audience must see the real phone. `scrcpy` over USB or Wi-Fi is the usual tool for mirroring an Android screen to a window. Checked on x1: `adb` is installed at `/usr/bin/adb`, `scrcpy` is not on PATH, so install it first and test. [INFERENCE; practitioner] Share the scrcpy window next to the browser window, not the whole desktop. Turn off phone notifications and enable Do Not Disturb on the phone too.
- [ ] **Slides view.** Prefer sharing only the slide window, with presenter view and notes on the second screen or in a separate window under the lens. Google Slides presenter view in "Present" mode opens its own window, so share that window, not the entire screen. [practitioner; `INFERENCE` on exact behavior, test it at T-1]
- [ ] Slide text must be readable in the Zoom window. Body 28 pt or larger is the deck's working rule. Verify on a recorded share. [Khalid blog via slide-methodology; weak]
- [ ] Recording on, and a second local recording as a safeguard. [practitioner]
- [ ] Chat window open on the second screen. Co-host or friend watches chat and flags questions. [practitioner]

## 4. Section delivery cues

Pause 1 to 2 s after the opening line, after the number, and before each slide change. [Liu, Nakajima et al. 2022; moderate-weak] The chat questions for Parts 1 to 5 and for What is still hard are the exact text on the deck's dividers (slides 14, 26, 39, 48, 56 and 65). The journey question comes from the slide 7 notes, because the journey has no divider. Slide 59 (accidents) also asks one question from its notes. The opening and the close have none. On Zoom, a silent wait can read as a dead line, so name a person or ask for a chat reaction, then wait 5 s. [Tauroza & Allison via Nesi 2001, weak for Zoom; practitioner] Mode changes every 10 to 15 minutes reset attention, and the chat prompts and demos are those resets. [Szpunar, Moulton & Schacter 2013 and related, via slide-methodology; moderate for drift, weak for the exact interval]

| Clock | Section | Opening line | Chat question | Number to say slowly | Transition line |
|---|---|---|---|---|---|
| 0 to 6 | Opening, slides 1 to 6 | "This is my phone at 9:29 in the morning. I was sitting in the plane, before takeoff." | none | 65 minutes | "Before we start, here is the plan. First my journey." |
| 6 to 15 | My journey, slides 7 to 13 | "Copilot opened to everyone in June 2022, and I started then, years before Claude Code existed. Then Claude Code inside VS Code." | Slide 7, from the notes: "Which coding agent do you use today?" | 2,200 requests in May, 270,000 in October | "The agent is working while I keep talking. Now, choosing models and paying for them." |
| 15 to 30 | Part 1, slides 14 to 25 | "The fastest model on paper was the slowest in my hands." | Divider, slide 14: "Per token or per subscription? Tell us in chat." | 476 seconds for DeepSeek flash, 92 for Opus | "A fast, well-chosen engine still forgets everything tomorrow. Next, teaching the agent." |
| 30 to 45 | Part 2, slides 26 to 38 | "Autolearn made too many skills, so I merged them." | Divider, slide 26: "Which task do you repeat with your agent more than twice? Tell us in chat." | 14 area skills, 4,635 rule injections since June | "One agent with good knowledge is useful. The real jump came when I ran many at once." |
| 45 to 57 | Part 3, slides 39 to 47 | "This is every working hour since September. Most hours I have three agents going." Then, slide 41, "Idle agents never saw the messages sent to them." | Divider, slide 39: "How many agents do you run at once? Tell us in chat." | 39% of hours had 4 to 9 agents, 101 worktrees, 353 decisions in the ledger | "Many agents write a lot of code. How do I trust it? Remember the plane." |
| 57 to 67.5 | Part 4, slides 48 to 55 | "Remember the plane? This is the proof that came with that fix." | Divider, slide 48: "Which part of your agent's work do you still check by hand? Tell us in chat." | 3 failed runs on the old code, 3 passed with the fix | "That is proof. Now, running it safely." |
| 67.5 to 76 | Part 5, slides 56 to 64 | "Every production change goes dry run, backup, apply, then verify." | Divider, slide 56: "Where do your agents run: laptop, server or cloud? Tell us in chat." Slide 59, from the notes: "Has an agent ever deleted something it should not have?" | about 244 volumes, 11 reviews | "So far, what works. Now let me be honest about what still does not." |
| 76 to 83 | What is still hard, slides 65 to 70 | "Now the honest part. Four things are still hard for me." | Divider, slide 65: "What still breaks for you? Tell us in chat." | 538 CI runs in one day. 171 seconds, down from 652. 89% of the SSD, 447 GB of Docker. 38 GB | "Let me bring it back to the claim." |
| 83 to 86 | Close, slides 71 to 73 | "Here are the five principles again." | none | none | "Questions are welcome, in chat or out loud." |

The dividers show no minutes and no "Ask chat" label. Say the chat question as printed, then wait 5 s, then read two or three answers aloud. Each divider also carries a seven-segment map strip with a "you are here" label, so point at it as you say the part's topic.

Say "if I paid per token" every time a dollar figure appears on a slide. It is list price, not money paid. The notes call it API-equivalent. [presenter.md rule; practitioner]

## 5. Live demo playbook

All of this is practitioner convention. No primary study found on live-demo handling. [Low, Simple Talk, weak: anecdotal; speaking-methodology section 6, weak]

**Pre-staged state checklist (T-1 and again one hour before).**
- [ ] Issue chosen: a small real issue from the Alkhidmah backlog, with scope you know the agent can finish in the time. Prompt typed in your own style and saved as a draft in the Tern app.
- [ ] Worktree clean: no stale branch, no leftover stash. Known-good state recorded.
- [ ] Stack running: dev stack up, warm cache, terminal in the right directory, ports checked.
- [ ] Mesh reachable from the phone session.
- [ ] Recording ready and tested: a full run of the same demo, cued to the exact frame, one action away. Plus screenshots of the PR page. [Low, Simple Talk, weak]
- [ ] Phone mirror window placed, readable, notifications off (section 3).
- [ ] No customer or tenant names visible in the issue, branch, or PR.

**At 13:30 (slide 13).** Send the prompt, say what you expect, then go straight to slide 14. Do not wait for the agent. [presenter.md slide 13 note]

**Narration lines while waiting.** Silence reads as lost floor on Zoom, so narrate the step, the expected output, and the reason. [Tauroza & Allison via Nesi; weak. `INFERENCE`] Read the output aloud. [practitioner]
- "I sent the prompt. The agent will create a worktree, then trace the impacted flow."
- "While it works, notice it is not asking me anything. The rules around it carry the structure."
- "Here I expect a pull request with a Verification section. I will check that at slide 54, around 65:00."

**90 s time-box.** If a live step has not produced its expected output in 90 s, do not debug. Switch. [practitioner, never debug live; Low, weak]

**Fallback sentence, rehearsed.** "The live run is slow today, so here is the recording from this morning." Then narrate live over the video, never play it silent. [Low, Simple Talk, weak]

**The check at 65:00 (slide 54).**
- If the run finished, open the PR, scroll to Verification, and walk through the body in 60 s. Check three things aloud: Why, proof, and an honest "Not verified".
- If it did not finish, say which step it is on, show the recording, and keep slide 54 up. It shows the PR #804 body as the reference, cropped to the draft click bullet and its before and after table. The slide has no expected-output cards, so name Why, proof and Not verified aloud. PR #804 has no "Not verified:" line, so say that aloud. [presenter.md slide 54 note]
- Never wait for the agent.

## 6. Delivering in English as a second language

The evidence here is small. A mild accent did not lower truth ratings once listeners were warned about processing difficulty, and a heavy accent still did. [Lev-Ari & Keysar 2010; moderate, two small experiments, not Indonesian speech] No study found on Indonesian-accented English. [`INFERENCE`] Intelligibility is the lever, not accent removal. [`INFERENCE`]

- **Slow down at numbers and terms.** Say the number, pause, then the unit. "Sixty-five... minutes." [INFERENCE from Newman & Schwarz 2018 on processing difficulty; moderate for the audio finding, practitioner for this use]
- **Say the key term aloud as well as showing it.** Harness, worktree, mesh, coordinator, skill. Define each on the slide where it first appears, as the `Say:` lines do (harness on slide 10, SHIP on slide 13, skill on slide 27, worktree on slide 43, mesh on slide 44). [`INFERENCE`; practitioner]
- **Articulate word endings and key nouns.** For example "worktrees", "tokens", "checks". [`INFERENCE`; practitioner]
- **Pauses, not fillers.** A silent pause carries the same "I am thinking" signal as "um". Plan transitions rather than policing fillers mid-talk. [Corley & Stewart 2008; moderate]
- **Pace.** About 130 to 150 wpm, slightly slower than conversation. [Tauroza & Allison via Nesi 2001; moderate for norms; Matsuura et al. 2014 was not read, so no L2 rate claim]
- **Indonesian phrases for warmth are fine.** The format is a casual community talk, and the deck already uses "Wajib" and "Opsional" labels. One short phrase at the start or when thanking the organizer, such as "terima kasih", is natural. [`INFERENCE`; practitioner] Do not switch language for explanations, the recording is English.
- **Idioms to avoid.** "Ballpark", "silver bullet", "low-hanging fruit", "game changer", "under the hood", "move the needle", "boil the ocean", "it is a wrap". Say the plain meaning instead. [`INFERENCE`; practitioner] Keep "TIL" only because the deck explains it.
- **Say once that unclear words can be asked in chat.** Already in the opening script. [`INFERENCE` from Lev-Ari & Keysar 2010; moderate]

## 7. Q&A

Q&A has only 4 minutes in total, from 86:00 to about 90:00. Keep a fixed block and stop at the end. [Toastmasters Q&A rubric; weak] Repeat or restate every question before answering, because the recording and some listeners will not hear it. [practitioner] Answer the core in two or three sentences, then link back to the throughline. [practitioner] Most organizer questions are already answered on slides, so point to the slide number instead of repeating the whole story. With 4 minutes, take two or three questions and pick the ones the chat voted for. Short answers below use only numbers from the slides.

| Question | Short answer |
|---|---|
| How much does it cost for a beginner? | "I do not know a beginner budget. My own October was about $200 paid, against $7.3k if I paid per token, because 97% of tokens were cache reads. Start with one subscription and one skill. Slide 24 has three money tips." |
| Which model for which role? | "I pick once per job, not per prompt. Chat is Opus at low effort. Plan and hard bugs are Opus at high. UI design is Sonnet at high. Review is Opus at medium. Exploring is Haiku. Slide 17 has the cards." |
| Is it safe for production? | "Prod is read-only by default. Every write goes dry run, backup, guarded apply, verify. Secrets are obfuscated, the model sees placeholders." |
| Is it safe to run agents for days? | "The SHIP coordinator ledger has 353 decisions from 2 to 7 November. One coordinator, one writer per branch, an independent reviewer, and a frozen verdict. I watch the coordinator, not each branch. Slide 59 has three accidents and the three guardrails they gave me." |
| How do I start? | "One skill. When you do the same work more than twice, write it as a skill." |
| Why not Cursor or Claude Code alone? | "Both are harnesses. I started with Copilot in VS Code, then used Claude Code inside VS Code, so it was an early step for me. I left for reasons about my workload, not a verdict on the tools. I use omp because I can write my own plugins, which is why mesh exists." |
| What about prewalk? | "Plan with the strong model, let a small one type. On my long tasks it was cheaper, but slower, and UI work needed a better model, so it is off. Can Bölük's test with his own models cut cost a lot, but that is his workload, not mine. Test it on yours. Slides 20 and 21." |
| Why is prewalk off? | "It was cheaper on my long tasks, but slower, and tasks took too long to finish. UI work also needed a better model than Haiku, so my task agents run Sonnet at medium with no handoff. On short tasks it cost the same or more. A second try on 24 and 25 October, with DeepSeek as the cheap model, was really slow." |
| Does effort matter? | "On two easy tasks, higher effort meant more steps. That is two easy tasks, not a quality ranking. The cause is my inference, the step counts are measured. My rule is low to do, medium to review, high to plan and for hard bugs, and max almost never because it is slow and gave little gain. Slides 17 and 19." |
| What happened to Antigravity? | "It was the first tool I used with a proper plan mode, memory and design artifacts, and its screen was built around agents. My Google account got banned. I still use it in one place, because omp uses its image model. Slide 9." |
| How do you write specs so agents do not get lost? | "Wireframe first, from the product. Then folders and files, then data and flow, and I check each layer. All of it goes into one markdown file in a plans folder for the feature. No hooks for tasks, GitHub issues and the coordinator's ledger hold the work. Slides 36 and 37." |
| What checks run before you look at a PR? | "Five. The language server on every edit, lint and types, tests shaped like the testing trophy, reviewer agents that scale with risk, and me for UI and feel. Slide 52." |
| Why did you try Paseo? | "For easier managed worktrees. Tern replaced it. Slide 63." |
| How do you organize skills? | "By area, inspired by Tiago Forte's PARA method. That gives my 14 area skills. My favorites are poteto-mode and show-me. Slide 29." |
| Why did you leave VS Code? | "Running agents in parallel. One agent in an editor is fine, four agents in four editors is not. I moved to Ghostty and Neovim so the memory goes to the agents, not the windows. That is my own reason and I did not measure it, so I have no memory number. Slide 8." |
| How many agents do you run at once? | "In a typical hour, three. In 39 percent of my working hours since September it was four to nine. That works because the agents control the dev infra, so they start the stack, seed it and test it without me. A folder counts as one, so this is workstreams, not processes. Slide 40." |
| What are rules? | "A rule is a small file. Some are always in the prompt. Others wait for a pattern. When the agent types pytest without a memory cap, omp stops the stream, adds the rule, and the agent rewrites the command. It stepped in 4,635 times since June, 1,424 of them my two memory caps. Slide 34." |
| Is CI a problem for you? | "Yes. On one day in November my alkhidmah repo ran 538 CI runs, and 1 in 10 took 16 minutes or more. I am testing larger runners and spreading the load over free runners. Nothing is settled. Slide 67." |
| What is your next infra step? | "A plan, not a result. Each stack in its own VM, paused when idle and woken when an agent needs it. A paused VM still takes disk, and my SSD is 89 percent full with 447 GB in Docker, so a bigger SSD comes first. Slides 69 and 70." |

**"I don't know" line.** "I do not know. I have not tested that. If you send it in chat, I will try it and answer in the follow-up." Say it plainly, offer a way to find out. [practitioner]

**Seeded first question if chat is quiet.** Ask a friend to post one in chat at the start of Q&A. [practitioner] Suggested: "What is the one thing you would do first if you only had a day?" Also pre-write 2 backups: "Which of your own skills do you use most?" and "What still breaks?" (the divider on slide 65 already asked the second one, so reuse those chat answers). If nothing arrives after the friend's question, name the first listed question yourself and answer it, then say "I will take the next one in chat or aloud." Do not wait in silence. [Tauroza & Allison via Nesi 2001, weak for Zoom]

## 8. Nerves

- **Reappraise as excitement.** Before going live, say "I am excited" aloud 2 to 3 times. In lab studies, saying it raised excitement, performance, and perceived persuasiveness and competence, and it did not reduce anxiety. [Brooks 2014; moderate] A brief framing of arousal as helpful also improved responses during a speech task. [Jamieson, Nock & Mendes 2013; moderate]
- **Cyclic sighing, 5 min.** The morning of the talk and 2 min before going live. Double inhale through the nose, long exhale through the mouth. Five minutes daily for a month improved mood and lowered respiratory rate more than mindfulness. [Balban et al. 2023, abstract read; moderate for daily practice, weak for acute pre-talk use]
- **First-minute plan.** [Anderson, trust then curiosity; weak. Opening ideas are `INFERENCE`]
  1. Look at the lens, smile, say hello.
  2. Name one friendly face on the grid, then the organizer's thanks.
  3. Say the opening script line by line, slowly, pausing after "9:29" and "65 minutes".
  4. Do not ask a chat question yet, the opening has none. The first one is on slide 7 at 6:00, and the first divider question is on slide 14 at 15:00.
  5. By 1:00, you are already in the phone story. The story carries you, not the script.
- If your voice shakes or you lose the line, stop, breathe out, and say the next sentence of the script. Silence is fine. [Corley & Stewart 2008, moderate; `INFERENCE`]

## 9. After the talk

- [ ] Share slides and the recording link, with a timestamped index. [practitioner]
- [ ] List the questions asked and the ones unanswered. Reply in writing, in the same channel. [practitioner]
- [ ] Review the recording: wpm on a 2-min section, filler count, silences that felt wrong, and whether the delivered throughline matches the planned one. [Tauroza & Allison via Nesi 2001, moderate for norms; Smith thesis, weak; Anderson, weak]
- [ ] Log which sections ran over and which cuts you used, then update the run of show.
- [ ] Note what to change next time. Do not rehearse the recording again until the next talk.

## Sources

Names used above, linked only from `speaking-methodology.md` section 10. Items marked "not read" were not relied on.

- Newman & Schwarz 2018, Good Sound, Good Research: https://gwern.net/doc/design/visualization/2018-newman.pdf
- Brooks 2014, Get Excited: https://www.apa.org/pubs/journals/releases/xge-a0035325.pdf
- Jamieson, Nock & Mendes 2013: https://escholarship.org/content/qt9n46p04q/qt9n46p04q.pdf
- Balban et al. 2023: https://pubmed.ncbi.nlm.nih.gov/36630953
- Anderson, HBR 2013 via TED Blog: https://blog.ted.com/chris-anderson-shares-his-tips-for-giving-a-killer-presentation
- Anderson, Forbes 2016: https://www.forbes.com/sites/danschawbel/2016/05/03/chris-anderson-the-secret-to-speaking-at-the-ted-annual-conference/
- Duarte, structure and story: https://www.duarte.com/blog/move-presentation-audience-with-story-techniques-in-presentations/
- Dahlstrom 2014, PNAS: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183170/
- Small, Loewenstein & Slovic 2007: https://www.cmu.edu/dietrich/sds/docs/loewenstein/SympathyCallous.pdf
- Nesi 2001, summarising Tauroza & Allison 1990: https://www.coventry.ac.uk/globalassets/media/global/05-research-section-assets/research/british-academic-spoken-english-base/publications-pdfs/evidence-from-the-literature-language-across-boundaries.pdf
- Liu, Nakajima et al. 2022: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.778018/full
- Corley & Stewart 2008: https://martincorley.org/offprints/corley.stewart_08.pdf
- Lev-Ari & Keysar 2010: https://mdl.uchicago.edu/research/lev-ari-2010-why-dont-we-believe-non-native-speakers-the-influence-of-accent-on-credibility
- Smith thesis, summarising Menzel & Carrell 1994: https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=miami1058484247&disposition=inline
- Gao et al. 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12439499/
- Bailenson 2021 via Stanford Report: https://news.stanford.edu/stories/2021/02/four-causes-zoom-fatigue-solutions
- Toastmasters Q&A rubric: https://content.toastmasters.org/image/upload/8413E-evaluation-resource-ff.pdf
- Low, Simple Talk (cited in slide-methodology.md section 6, not in speaking-methodology.md): no link given here.
