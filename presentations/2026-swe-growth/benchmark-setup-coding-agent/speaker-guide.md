# Speaker guide: Benchmarking My Coding Agent Setup

Delivery plan for Zahid. 90 min, Zoom, English, mixed Indonesian developer audience, casual community format.

Evidence tags. **strong** = replicated or meta-analysed. **moderate** = one or two controlled studies or a peer-reviewed review. **weak** = correlational, expert opinion, or rubric. **practitioner** = convention with no primary study found. `[INFERENCE]` marks my own reasoning, not a sourced finding. Source names refer to the list at the end. The speaking evidence base is thin, so most items are weak or practitioner. Do not oversell them.

## 1. Throughline and the three stories

**Throughline.** The model is a swappable part, and what lets one engineer ship from a phone is the setup around it: skills, proof, coordination and guardrails. [Anderson, one through-line; weak] Every story below either supports this line or shows where it breaks. [Anderson, weak]

Open with a "what is" the audience already accepts (everyone uses agents, almost nobody measures them), then the "what could be" the phone fix makes concrete. [Duarte sparkline; weak]

**The three stories to land.** One concrete story per section, number after the story, not stacked on it. [Small, Loewenstein & Slovic 2007, moderate for the effect, weak for transfer to talks; Dahlstrom 2014, moderate]

| # | Story | Slides | The point it proves | Number to say after the story |
|---|---|---|---|---|
| 1 | Phone fix. 9:29 on a plane, QA warning to QA pass | 2, 3 (and its before and after page), 37 | One engineer can ship from a phone | 65 minutes (08:52 to 09:57) |
| 2 | The bench. Every arm passed, so speed and cost separated | 13, 14, 15 | Measure your own workload, do not trust a trick | 126 of 126 checks |
| 3 | SHIP coordinator. Watch one coordinator, not every branch | 34, 35 | Coordination and proof beat a bigger model | 3 days, 276-line ledger |

If time runs short, cut in the order of presenter.md: slide 25 first, then 40, 33, 41, 29, 16. **Never cut slides 2, 3 (with its before and after page), 4, 10, 12 to 15, 17, 18, 21, 22, 32, 34, 35, 37, 38, 44 to 46.** That is the core list in presenter.md plus the two demo slides.

**The X quote on slide 7 is confirmed verbatim.** The line "I improved 15 LLMs at coding in one afternoon. Only the harness changed." is the exact title of Can Bölük's article on X (x.com/_can1357/status/2021828033640911196). It was checked against the live page on 2026-11-05, and the screenshot on the slide shows it. Say "article", not "post".

## 2. Rehearsal plan

Dates are relative to talk day (T-0). Nothing here has a primary study behind the counts. Practice before an audience is correlated with better speeches. [Menzel & Carrell 1994 via Smith thesis; weak-moderate] The counts are `[INFERENCE]`. [practitioner]

| When | What | Done when |
|---|---|---|
| T-7 | Write the throughline and the opening and closing scripts (below). Mark 1 to 2 s pause points in the slide notes. [Liu, Nakajima et al. 2022; moderate-weak] Run 1: full out-loud run-through alone, timed per section against the run of show. [practitioner] | Section times on paper, gaps over 20% flagged |
| T-7 | Record one 2-min section (suggest slides 12 and 13). Count words and divide by minutes. Target 130 to 150 wpm. [Tauroza & Allison 1990 via Nesi 2001; moderate for norms, target is `[INFERENCE]`] Count fillers in the same clip. [Corley & Stewart 2008; moderate for what fillers are] | wpm and filler count noted |
| T-3 | Run 2: full run-through out loud with 4 or more watchers, or recorded and watched back. [Smith thesis; weak-moderate] Watchers get one job: say where they lost the thread. Include a live phone demo from start to the PR. | Notes from watchers, demo run end to end once |
| T-3 | Rehearse the demo switch to the recording out loud, with the fallback sentence (section 5). [Low, Simple Talk; weak] | Switch takes under 10 s |
| T-1 | Run 3: opening (slides 1 to 7) and closing (slides 47 to 48) word for word, three times each, without notes. [Anderson valley of awkwardness; weak] Middle stays as bullets. Final audio and screen-share test on the real Zoom (section 3). | Opening and closing from memory |
| T-0 morning | Cyclic sighing, 5 min (section 8). One quiet read of the opening script. No new content. | Calm, not cramming |

**Time each section against the clock windows.** The windows are 0 to 7, 7 to 15, 15 to 30, 30 to 47, 47 to 65, 65 to 74, 74 to 79 and 79 to 90. Talk time inside them is 7, 5, 15, 14, 17, 7.5, 5 and 1.5 minutes, 72 in total, plus 6 minutes of Q&A. The rest is slack and the demo. The Pillar 2 divider on the slide reads minute 32, because the outline keeps 2 minutes of slack at the end of Pillar 1. Log actual minutes per section at T-7 and T-3. If a section runs over, pick cuts from the cut order in presenter.md, do not speed up. [practitioner]

### Opening script, memorize word for word (about 7 min, slides 1 to 7)

Drawn from the slide 1 to 7 notes. Pause 1 to 2 s where marked `/`. [Liu, Nakajima et al. 2022; moderate-weak] Slides 1 to 3 and the claim are word for word. Slides 5 to 7 are short lines, say them slowly.

> Hello everyone, and thank you, Mas Zikrul and SWE Growth, for having me. / I am Zahid. / This is a casual talk about one real setup, with real numbers, and with the parts that still do not work. /
>
> Please put questions in chat any time. If a word of mine is unclear, ask, and I will say it again. /
>
> Let me start with my phone. / This is my phone at 9:29 in the morning, on Tuesday, the 27th of October. / I was sitting in the plane, before takeoff. / The agent had just reproduced a bug on a real stack, and it was about to fix it. /
>
> Here is what happened. / At 8:52, QA found one more problem on a pull request that was already approved. / At 9:26, I pasted it into the same session, from my phone. / The agent recorded a before clip, fixed it, recorded an after clip, and updated the pull request body. / At 9:57, QA tested the PR and passed it. / Sixty-five minutes after the warning. /
>
> Here is the same click, before and after. / Before the fix, a click on a draft sensor opens the edit modal. / After the fix, the click only selects the sensor. /
>
> So how did one engineer, on a phone, get there? / Here is my claim. / The model is a swappable part. / What lets one engineer ship from a phone is the setup around it. / Four parts: skills, proof, coordination, and guardrails. / Every section today either supports this claim, or shows you where it breaks. / And at the end, I will give you one action to take home. /
>
> Quick word on one term, because I will use it all talk. / A harness is the program around the model. / It gives the model tools, context, memory, and rules. / Claude Code, Cursor, OpenCode, Amp and omp are harnesses. Claude, GPT and GLM are models. / This talk is about the harness. /
>
> Six terms come back today. / Harness: the program around the model. / Worktree: a separate checkout of a repo, one per task. / Skill: a file the agent loads when needed. / Mesh: a plugin so agents see each other. / SHIP: my coordinator agent, it merges. / poteto-mode: my agent-style skill. / You only need to remember that one line for each. /
>
> I am not the only one who sees this. / Can Bölük is the author of omp. / He wrote an article on X, and its title is: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." / That is the claim of this talk, from someone with no reason to flatter my setup.

### Closing script, memorize word for word (about 1.5 min, slides 47 to 48)

Drawn from slides 47 and 48. Stop after the last line. [Duarte: audiences remember the last thing; weak] The old "three lines to remember" slide is gone, so there is nothing to read after the action.

> So, back to the claim. / The model is a swappable part. / Skills, proof, coordination and guardrails are the setup around it. /
>
> Here is the one action for Monday. / "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." /
>
> Two small habits that cost nothing. / Ask for proof in every pull request. / And dry-run anything that touches production. /
>
> Thank you, SWE Growth. / Questions are welcome in chat or aloud, and the slides link is in the chat. / Now, your questions.

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

Pause 1 to 2 s after the opening line, after the number, and before each slide change. [Liu, Nakajima et al. 2022; moderate-weak] The chat questions are the exact text on the deck's dividers, plus the reset at minute 55. The cold open and the close have none. On Zoom, a silent wait can read as a dead line, so name a person or ask for a chat reaction, then wait 5 s. [Tauroza & Allison via Nesi 2001, weak for Zoom; practitioner] Mode changes every 10 to 15 minutes reset attention, and the chat prompts and demos are those resets. [Szpunar, Moulton & Schacter 2013 and related, via slide-methodology; moderate for drift, weak for the exact interval]

| Clock | Section | Opening line | Chat question (divider text) | Number to say slowly | Transition line |
|---|---|---|---|---|---|
| 0 to 7 | Cold open, slides 1 to 7 | "This is my phone at 9:29, on a plane, before takeoff." | none | 65 minutes | "So that is the claim. Now, the journey: which tools I used, and why I switched." |
| 7 to 15 | The journey, slides 8 to 9 | "Every tool switch had a reason, and omp stayed because I can extend it." | "Which coding agent do you use today?" | Amp, December to March, my longest stay | "A harness you can extend lets me fix my own problems. Now, the benchmark lab, and the demo starts from my phone." |
| 15 to 30 | Pillar 1, the benchmark lab, slides 10 to 19 | "I send one prompt from my phone, and the agent works while I keep talking." | "Do you pay per token or per subscription?" | 126 of 126 | "The formula says which plan is cheap. It does not say which model is good. When quality moved, I moved." |
| 30 to 47 | Pillar 2, knowledge, slides 20 to 29 | "Skills hold how to do a thing, and memory holds what I did and decided." | "Which task do you repeat with your agent more than twice?" | 14 area skills | "Knowledge is only useful if someone can act on it. Next, the crew." |
| 47 to 65 | Pillar 3, the crew, slides 30 to 33 | "Every task gets its own worktree, so agents never share a directory." | "How many agents do you run at once?" | 101 worktrees | "Worktrees are the floor. Now, one coordinator." |
| 55, inside 47 to 65 | Pillar 3, one coordinator, slides 34 to 38 | "I watch one coordinator, and it merges only after an independent review." | "Who decides when an agent's PR is ready to merge?" | 3 days, 276-line ledger | "Now let me check the pull request from the phone." (demo check, section 5) |
| 65 to 74 | Infra and guardrails, slides 39 to 43 | "Proof runs away from the workstation, and production stays read-only." | "Where do your agents run: laptop, server or cloud?" | none | "So far, what works. Now let me be honest about what still does not." |
| 74 to 79 | Open problems, slides 44 to 46 | "Three problems are open, and the first is that a proof clip cannot judge how a screen looks." | "Which part of your agent's work do you still check by hand?" | 171 seconds, down from 652. 38 GB | "Let me bring it back to the claim." |
| 79 to 90 | Close and Q&A, slides 47 to 48 | "Back to the claim. The model is a swappable part." | none. Slide 48 says questions are welcome in chat or aloud | none | "Thank you, SWE Growth. Now, your questions." |

The dividers carry the minutes 7, 15, 32, 47, 55, 65 and 74. Pillar 2 starts at 30 in the windows above and reads 32 on its divider. Say the chat question as printed, then wait 5 s.

Say "API-equivalent" every time a dollar figure appears. It is list price, not money paid. [presenter.md rule; practitioner]

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

**At minute 15 (slide 10).** Send the prompt, say what you expect, then go straight to slide 11. Do not wait for the agent. [presenter.md slide 10 note]

**Narration lines while waiting.** Silence reads as lost floor on Zoom, so narrate the step, the expected output, and the reason. [Tauroza & Allison via Nesi; weak. `INFERENCE`] Read the output aloud. [practitioner]
- "I sent the prompt. The agent will create a worktree, then trace the impacted flow."
- "While it works, notice it is not asking me anything. The rules around it carry the structure."
- "Here I expect a pull request with a Verification section. I will check that at minute 60."

**90 s time-box.** If a live step has not produced its expected output in 90 s, do not debug. Switch. [practitioner, never debug live; Low, weak]

**Fallback sentence, rehearsed.** "The live run is slow today, so here is the recording from this morning." Then narrate live over the video, never play it silent. [Low, Simple Talk, weak]

**Minute-60 check (slide 37).**
- If the run finished, open the PR, scroll to Verification, and walk through the body in 60 s. Check three things aloud: Why, proof, and an honest "Not verified".
- If it did not finish, say which step it is on, show the recording, and keep slide 37 up. It shows the PR #804 body as the reference: the draft click bullet and its before and after table. PR #804 has no "Not verified:" line, so say that aloud. [presenter.md slide 37 note]
- Never wait for the agent.

## 6. Delivering in English as a second language

The evidence here is small. A mild accent did not lower truth ratings once listeners were warned about processing difficulty, and a heavy accent still did. [Lev-Ari & Keysar 2010; moderate, two small experiments, not Indonesian speech] No study found on Indonesian-accented English. [`INFERENCE`] Intelligibility is the lever, not accent removal. [`INFERENCE`]

- **Slow down at numbers and terms.** Say the number, pause, then the unit. "Sixty-five... minutes." [INFERENCE from Newman & Schwarz 2018 on processing difficulty; moderate for the audio finding, practitioner for this use]
- **Say the key term aloud as well as showing it.** Harness, worktree, coordinator, API-equivalent, base branch. [`INFERENCE`; practitioner]
- **Articulate word endings and key nouns.** For example "worktrees", "tokens", "checks". [`INFERENCE`; practitioner]
- **Pauses, not fillers.** A silent pause carries the same "I am thinking" signal as "um". Plan transitions rather than policing fillers mid-talk. [Corley & Stewart 2008; moderate]
- **Pace.** About 130 to 150 wpm, slightly slower than conversation. [Tauroza & Allison via Nesi 2001; moderate for norms; Matsuura et al. 2014 was not read, so no L2 rate claim]
- **Indonesian phrases for warmth are fine.** The format is a casual community talk, and the deck already uses "Wajib" and "Opsional" labels. One short phrase at the start or when thanking the organizer, such as "terima kasih", is natural. [`INFERENCE`; practitioner] Do not switch language for explanations, the recording is English.
- **Idioms to avoid.** "Ballpark", "silver bullet", "low-hanging fruit", "game changer", "under the hood", "move the needle", "boil the ocean", "it is a wrap". Say the plain meaning instead. [`INFERENCE`; practitioner] Keep "TIL" only because the deck explains it.
- **Say once that unclear words can be asked in chat.** Already in the opening script. [`INFERENCE` from Lev-Ari & Keysar 2010; moderate]

## 7. Q&A

Reserve a fixed 6 min block. [Toastmasters Q&A rubric; weak] Repeat or restate every question before answering, because the recording and some listeners will not hear it. [practitioner] Answer the core in two or three sentences, then link back to the throughline. [practitioner] Short answers below use only numbers from the slides.

| Question | Short answer |
|---|---|
| How much does it cost for a beginner? | "I do not know a beginner budget. My own October was about $200 paid, against $7.3k API-equivalent list price, because 97% of tokens were cache reads. Start with one subscription and one skill." |
| Which model for which role? | "I pick once per role, not per prompt. Opus plans and reviews, Sonnet runs tasks, Haiku explores. Effort is low for execution, high for plans. Slide 11 has the table." |
| Is it safe for production? | "Prod is read-only by default. Every write goes dry run, backup, guarded apply, verify. Secrets are obfuscated, the model sees placeholders." |
| Is it safe to run agents for days? | "The SHIP run lasted about three days. One coordinator, one writer per branch, an independent reviewer, and a frozen verdict. I watch the coordinator, not each branch." |
| How do I start? | "One skill. When you do the same work more than twice, write it as a skill." |
| Why not Cursor or Claude Code alone? | "Both are harnesses and I used Claude Code first. I left for reasons about my workload and the time, not a verdict on the tools. I use omp because I can write my own plugins, which is why mesh exists." |
| What about prewalk? | "Plan with the strong model, type with the cheap one. On my short tasks it cost the same or more, so it is off. Can Bölük's test with his own models cut cost a lot, but that is his workload, not mine. Test it on yours." |
| Why is prewalk off? | "On my short tasks it cost the same or more. I tried Haiku as the target on 24 October, then DeepSeek on 25 October to save money, and it was really slow. It may still help on long sessions or with a faster cheap target, which I have not tried." |
| Does effort matter? | "On two easy tasks, higher effort meant more turns. That is two easy tasks, not a quality ranking. The cause is my inference, the turn counts are measured." |

**"I don't know" line.** "I do not know. I have not tested that. If you send it in chat, I will try it and answer in the follow-up." Say it plainly, offer a way to find out. [practitioner]

**Seeded first question if chat is quiet.** Ask a friend to post one in chat at the start of Q&A. [practitioner] Suggested: "What is the one thing you would do first if you only had a day?" Also pre-write 2 backups: "Which of your own skills do you use most?" and "What still breaks?" If nothing arrives after the friend's question, name the first listed question yourself and answer it, then say "I will take the next one in chat or aloud." Do not wait in silence. [Tauroza & Allison via Nesi 2001, weak for Zoom]

## 8. Nerves

- **Reappraise as excitement.** Before going live, say "I am excited" aloud 2 to 3 times. In lab studies, saying it raised excitement, performance, and perceived persuasiveness and competence, and it did not reduce anxiety. [Brooks 2014; moderate] A brief framing of arousal as helpful also improved responses during a speech task. [Jamieson, Nock & Mendes 2013; moderate]
- **Cyclic sighing, 5 min.** The morning of the talk and 2 min before going live. Double inhale through the nose, long exhale through the mouth. Five minutes daily for a month improved mood and lowered respiratory rate more than mindfulness. [Balban et al. 2023, abstract read; moderate for daily practice, weak for acute pre-talk use]
- **First-minute plan.** [Anderson, trust then curiosity; weak. Opening ideas are `INFERENCE`]
  1. Look at the lens, smile, say hello.
  2. Name one friendly face on the grid, then the organizer's thanks.
  3. Say the opening script line by line, slowly, pausing after "9:29" and "65 minutes".
  4. Do not ask a chat question yet, the cold open has none. The first one is on the divider at minute 7.
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
