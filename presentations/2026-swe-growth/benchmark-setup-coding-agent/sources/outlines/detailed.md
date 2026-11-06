# Benchmarking My Coding Agent Setup: One Engineer, Many Agents
## Detailed outline, self-reading deck (v2)

**SWE Growth community. Online on Zoom, 90 minutes. All slides in English.**
**Speaker: Zahid**

## How to use this outline
- This is the deck people read after the talk, without the speaker. It has 40 slides. The live deck in `presenter.md` has 60.
- It follows the same v2 story as the live deck. Five principles, each told through a story. Every part runs story, principle, proof, try this.
- Each slide has a headline of at most 12 words and about 50 words of text on the face, in short plain sentences. Each slide has one picture.
- A slide face never shows a file path, an internal date, a source line or bench jargon. Use "steps", not "turns". Do not use "arm", "median", "API-equivalent" or "head-to-head".
- Where a dollar figure appears, say "if I paid per token". It is the list price of the tokens, not money paid. State real spend separately.
- Credits sit next to a quote, for example "Can Bölük, omp author". No footers. All links go on the last slide.
- Every fact comes from `presenter.md` (its `Evidence:` lines) or from `references/`. Nothing is invented.
- No secret values, hosts, emails or customer names. Teammates are "QA".

## The claim
The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails.

## The five principles
1. Measure it on your own work
2. Do it twice, make it a skill
3. One writer per branch
4. Show proof, not "done"
5. Make it safe to walk away

## Slide map

| Part | Slides |
|---|---|
| Opening | 1 to 4 |
| My journey | 5 to 7 |
| Part 1. Choosing models and paying for them | 8 to 16 |
| Part 2. Teaching the agent | 17 to 22 |
| Part 3. Many agents at once | 23 to 28 |
| Part 4. Trusting the result | 29 to 32 |
| Part 5. Running it safely | 33 to 37 |
| What is still hard | 38 |
| Close | 39 and 40 |

---

# Opening

## Slide 1. Benchmarking my coding agent setup
**On the slide:** Title. "One engineer, many agents." "Zahid, SWE Growth."
**Picture:** Title card, dark background, no vendor logos.

## Slide 2. I fixed a bug from my phone, on a plane
**On the slide:** QA flagged the bug at 08:52. I pasted it into my agent from my phone at 09:26. The agent proved the bug, fixed it and updated the pull request. QA passed it at 09:57. That is 65 minutes.
**Picture:** The real phone screenshot at 9:29, with a four-point timeline: 08:52 QA warns, 09:26 I paste the finding, 09:29 agent shows the bug, 09:57 QA passes.
**Facts behind it:** Pull request #804. The phone app was the Tern Android app, and I was on board the plane before takeoff. The prompt was "Fix those own changes proof and update pr". The finding was that clicking a draft sensor opened the edit modal.

## Slide 3. The model is a swappable part
**On the slide:** The model is a swappable part. The setup around it does the work. Four parts: skills, proof, coordination, guardrails.
**Picture:** A grey model box in the centre. Four boxes around it, one per part.

## Slide 4. Someone else found the same thing
**On the slide:** "I improved 15 LLMs at coding in one afternoon. Only the harness changed." Can Bölük, omp author.
**Picture:** The screenshot of the article header with the title boxed.

---

# My journey

## Slide 5. A harness is the program around the model
**On the slide:** The model thinks. The harness gives it tools, context, memory and rules. Claude Code, Cursor and omp are harnesses. Claude, GPT and GLM are models. You can swap the model and keep the harness.
**Picture:** Diagram with the model in the middle and four boxes around it: tools, context, memory, rules.

## Slide 6. Every tool switch had a reason
**On the slide:** Claude Code, then OpenCode, then Amp, then omp. Claude Code was not good enough for some tasks. OpenCode had many issues and accounts were getting banned. Amp: I forgot why I left. omp stayed because I can extend it.
**Picture:** A timeline with five steps and one short reason under each. Antigravity is a small side trip before Claude Code, because of a ban and heavy use.

## Slide 7. omp is better because I can extend it
**On the slide:** When something hurts, I write a plugin. Autolearn: the agent writes a skill after a session. Hindsight: my memory tool. Compaction: the agent shortens a long chat so it can keep going.
**Picture:** A row of five icons: plugins, autolearn, memory, logins, compaction.
**Facts behind it:** Mesh, the org account router and the worktree plugin are all mine. Multi-provider subscription logins are the fifth item.

---

# Part 1. Choosing models and paying for them

## Slide 8. The fastest model on paper was the slowest in my hands
**On the slide:** On paper, DeepSeek flash runs at 118 tokens a second. On my UI task it took 476 seconds. Opus took 92. DeepSeek needed 28 steps. Opus needed 9.
**Picture:** Bars in seconds on the UI task. Opus low 92, Sonnet medium 94, Haiku medium 170, DeepSeek flash low 476. DeepSeek is highlighted, with "118 tokens a second on paper" next to it.
**Facts behind it:** My September ranking formula had no term for steps. Each step was fast, but there were many more of them.

## Slide 9. Principle 1. Measure it on your own work
**On the slide:** Measure it on your own work. A benchmark on paper is a guess. Your own task is the test.
**Picture:** The principle name, large, with one plain line under it.

## Slide 10. Each job gets its own model
**On the slide:** I pick a model per job, not per prompt. Chat: Opus, low effort. Planning: Opus, high. Review: Opus, medium. Helper agents: Sonnet, medium. Quick searches: Haiku. Rule of thumb: low to do, medium to review, high to plan, max almost never.
**Picture:** A five-row table with job, model and effort.

## Slide 11. Every model passed. Speed and price decided
**On the slide:** Two easy tasks, three runs each. Every model passed all 126 checks. Opus was fastest. Haiku was the cheapest Claude model. DeepSeek was by far the slowest. This is not a quality ranking.
**Picture:** A table with seconds on the UI task and price per task if I paid per token. Opus low 92 s, $0.22 to $0.39. Sonnet medium 94 s, $0.17 to $0.24. Haiku medium 170 s, $0.02 to $0.03. DeepSeek flash low 476 s, $0.04 to $0.07.

## Slide 12. Thinking harder made the agent take more steps
**On the slide:** I expected better answers for the same cost. Instead, higher effort meant more steps in every pair I tested. Spark: 9 to 23. DeepSeek: 28 to 40. My guess is that it checks more. The step counts are measured. The reason is a guess.
**Picture:** Paired bars, lower effort next to higher effort, for four pairs.
**Facts behind it:** Haiku slot finder 12 to 16. Sonnet UI 7 to 10. Low for execution on easy work is what this covers. "High for plans" is my judgment.

## Slide 13. Plan with the big model, let a small one type
**On the slide:** Prewalk is a trick from Can Bölük. The strong model reads the code and writes a todo list. At the first edit, the same session switches to a cheaper model. "Opus fixing things does not cost money. Opus reading things costs money." Can Bölük, omp author.
**Picture:** A four-step line: plan, todo list, first edit, swap model.
**Facts behind it:** It is off by default in omp. In his logs, edits were about 9% of the tokens.

## Slide 14. On my tasks prewalk was never cheaper
**On the slide:** UI task. Opus alone: 39 cents. With prewalk: 48 cents. Sonnet alone: 24 cents. With prewalk: 36 cents. On the other task, one pair tied at 17 cents. Test a trick on your own work. It may help someone else and not you.
**Picture:** Paired bars, alone next to prewalk, for the UI task. Prices are what it would cost if I paid per token.
**Facts behind it:** On short tasks the cheaper model re-reads the conversation after the switch. The handoff did not fire in 3 of 18 prewalk runs. I tried DeepSeek as the cheap target, it was really slow, and I turned prewalk off the same day. It may still help on long sessions, which I have not tested.

## Slide 15. In October I paid about $200 for $7.3k of tokens
**On the slide:** In October my agents used tokens worth $7.3k if I paid per token. I paid about $200. 270,000 requests. 41 billion tokens. 97% were cache reads, and those are cheap. I usually pay about $100 a month.
**Picture:** Two big numbers, "$7.3k if I paid per token" and "about $200 paid". A small chart of requests per month, from 2.2k in May to 270k in October.
**Facts behind it:** I pay for two Claude Max plans and OpenCode Go. In September my plans were GLM Max (my own, bought cheap at the launch price), Codex Pro from the office, and Devin Pro and OpenCode Go (my own). When the Claude 5.5 models arrived, I went all in on Claude. My words: "Claude 5.5 series quality is GOAT". Between June and August I moved from one chat at a time to many agents at once.

## Slide 16. Try this. Time one real task
**On the slide:** Take one real task you do often. Run it on two different models. Write down the time.
**Picture:** Two stopwatches side by side.

---

# Part 2. Teaching the agent

## Slide 17. Autolearn made too many skills
**On the slide:** A skill is a short file the agent loads when the work matches. Autolearn lets the agent write one after a session. I turned it on and got too many small skills. I merged them into 14 area skills and wrote a lint to keep them tidy. The last run found 0 errors. Now I run autolearn by hand.
**Picture:** The real screenshot of the lint result.
**Facts behind it:** The lint exits with an error if the layout is wrong, and a pre-commit hook runs it. Each area skill is a router, with playbooks (steps to follow) and references (facts to look up). The layout rule became a script, not a longer instruction.

## Slide 18. Principle 2. Do it twice, make it a skill
**On the slide:** Do it twice, make it a skill. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." Zahid.
**Picture:** The principle name, large, with the rule under it.

## Slide 19. Skills hold how. Memory holds what happened
**On the slide:** A skill holds how to do a thing, like the steps of a deploy. Memory holds what I did and decided, across projects. I kept Hindsight, and it saves a note once per 10 rounds of chat to keep the cost down. When a chat gets long, the agent shortens it so I do not watch the context window.
**Picture:** Two columns, skills and memory, with one example each.
**Facts behind it:** My words: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project." Before Hindsight I used Mnemopi, and I tried Cognee and removed it. The old data stayed untouched, so going back is one setting. Compaction uses three methods in order. It starts at 70% of the context window.

## Slide 20. My prompts are loose on purpose
**On the slide:** I paste raw context into the agent. A WhatsApp message from QA. A screenshot. A spreadsheet. The structure is in the files around the prompt. I dropped the task tracker beads, because agents got smarter and beads is hard for humans to read. I use GitHub issues and the coordinator logs now.
**Picture:** Layers of instructions, from a short global file down to the repo, with "beads" struck through.
**Facts behind it:** When I hand work to a helper agent, the brief has one shape: target, change and contract.

## Slide 21. 25 principles, and one of them is mine
**On the slide:** poteto-mode is an agent-style skill I ported to omp. It brings 25 principles and 23 playbooks. The agent must say which principle shaped each decision. My own principle is check every layer: product and the human walk, structure, and data and flow.
**Picture:** Three stacked layers, each with one example finding.
**Facts behind it:** It comes from the pstack plugin under an MIT licence, written by poteto. Check every layer is my own principle, added on top. The count is 11 core, 6 architecture, 5 verification, 2 delegation and 1 meta.

## Slide 22. Try this. Write the skill
**On the slide:** The next time you repeat a task for the third time, stop. Write it down as a skill, even a small one.
**Picture:** A short checklist with three boxes, the third one ticked.

---

# Part 3. Many agents at once

## Slide 23. Idle agents never saw the messages
**On the slide:** My agents talk to each other through a plugin I call mesh. My coordinator sent a message to every agent. Idle agents do not wake up for a message, so they never read it. The coordinator wrote in its log: "idle sessions don't wake on mesh messages; each branch needs one writer".
**Picture:** One coordinator sending a message. Some agents receive it. Two idle agents stay grey.

## Slide 24. Principle 3. One writer per branch
**On the slide:** One writer per branch. Many agents and many branches are fine. On each branch, exactly one agent writes.
**Picture:** The principle name, large, with one plain line under it.

## Slide 25. Every agent task gets its own copy of the repo
**On the slide:** A worktree is its own copy of the repo. Every task gets one, so agents never share a working folder. I built a small command, tern-wt, to manage them. The skill tells the agent to use that one command and not to remove a worktree it did not create.
**Picture:** One repo in the middle and three copies around it.
**Facts behind it:** The real list showed 101 worktrees. Tern, my terminal app, makes each copy a tab and offers to remove it when the tab closes.

## Slide 26. Mesh: agents see what the others are holding
**On the slide:** Many agents share one machine, one set of ports and one Docker daemon. Before heavy work, an agent checks who else is working. If a peer runs the same job, it waits. I wrote mesh myself, and it took seven commits.
**Picture:** Three real agent cards: one coordinator holding the production release, one waiting for the owner's go, one with nothing held.
**Facts behind it:** The capture showed 19 agents in 8 repo groups. My other plugins include an account router that puts office repos on the office account and personal repos on personal accounts.

## Slide 27. One coordinator merges after an independent review
**On the slide:** I do not watch every branch. I watch one coordinator. A worker opens a pull request with proof and says it is ready. The coordinator freezes it and asks an independent reviewer. If the review passes, the coordinator merges, one at a time. If it fails, the findings go back for one fix round.
**Picture:** A loop with worker, coordinator, reviewer and the pull request.
**Facts behind it:** The coordinator is an ordinary omp session. One run lasted about three days and kept a 276-line log. Every decision is one row with a reason. Product questions go to the coordinator, not to me. I decide merges of finished work and hold production releases.

## Slide 28. Try this. One worktree per agent
**On the slide:** When you run two agents on one repo, give each its own worktree. It is one git command.
**Picture:** Two folders, each with its own branch label.

---

# Part 4. Trusting the result

## Slide 29. The plane fix came with proof
**On the slide:** Remember the plane? On the left, before the fix, clicking a draft opens the edit modal. On the right, after the fix, the click only selects the sensor. Three test runs failed on the old code. The same three passed with the fix.
**Picture:** The real before and after frames from the pull request, side by side. Below, "3 failed, then 3 passed".
**Facts behind it:** The test used the same data that broke staging. A failing run before and a passing run after shows the test can really fail.

## Slide 30. Principle 4. Show proof, not "done"
**On the slide:** Show proof, not "done". A pull request is ready when it shows evidence. Recording for what you can see. Command and real output for everything else.
**Picture:** A four-rung ladder: recording, command output, run link, test result.
**Facts behind it:** A good pull request body has Why, How, What changed, Scope, Tradeoffs, Blast Radius and Verification. Verification ends with "Not verified:" and a list, or "Not verified: none". Take the first rung that shows the claim.

## Slide 31. A second agent freezes its verdict
**On the slide:** A second agent reads the pull request in a clean copy and freezes its verdict at one commit. It checks that the test fails on the old code and passes on the new, that it merges cleanly and that lint is clean. A new commit means a new review. I still check the UI by hand.
**Picture:** The real review report, re-typeset as a card: "PASS with notes".

## Slide 32. Try this. Ask for a clip
**On the slide:** In your next pull request, ask the agent for a before and after clip. It costs one sentence.
**Picture:** A pull request with two video thumbnails, before and after.

---

# Part 5. Running it safely

## Slide 33. Every production change goes four steps
**On the slide:** Dry run. Backup. Apply with the expected row counts. Verify. A dry run runs the real update inside a transaction and rolls it back. A human can repeat every step. My prompt: "dry run first then show me what will be changed".
**Picture:** Four boxes in a row, in that order.
**Facts behind it:** Production is read-only by default. A deploy is done only when the running version is verified, not when the job is green.

## Slide 34. Principle 5. Make it safe to walk away
**On the slide:** Make it safe to walk away. A human can repeat every step. Secrets stay hidden. Then I can leave the agent working and go on a plane.
**Picture:** The principle name, large, with one plain line under it.

## Slide 35. Three layers protect my secrets
**On the slide:** First, values are hidden from the model, so it sees placeholders. Second, dangerous commands are blocked, like rm -rf, force push and DROP TABLE. Third, secrets live in managed storage. Infisical for machines, Bitwarden for humans. Hiding a value is not the same as managing a secret.
**Picture:** Three stacked cards, one per layer.

## Slide 36. Proof runs away from my workstation
**On the slide:** My workstation is busy running agents, so proof runs on other machines. A shared dev box runs one stack per user. A batch box runs jobs. An office box runs staging. Production is read-only. A new worktree gets a running stack from one command.
**Picture:** A simple machine map with no addresses.
**Facts behind it:** In Alkhidmah the command is `bun run bootstrap`. Ports and database come from the branch name, so two worktrees never fight over a port.

## Slide 37. Try this. Dry run first
**On the slide:** Before your next production change, ask the agent to show you what will change. Then decide.
**Picture:** A preview table with a "dry run" label.

---

# What is still hard

## Slide 38. Three things are still hard
**On the slide:** A proof clip cannot judge how a screen looks, so I still check UI and feel by hand. Seeding a database for each worktree is still slow. One fix took it from 652 seconds to 171 seconds. One test run without a memory cap reached 38 GB of RAM.
**Picture:** Three cards with one number each. "By hand", "171 s", "38 GB".
**Facts behind it:** A rule now fires when a test command appears and tells the agent to cap memory first. The fix for RAM was a rule, not more memory.

---

# Close

## Slide 39. Five principles, one claim
**On the slide:** Measure it on your own work. Do it twice, make it a skill. One writer per branch. Show proof, not "done". Make it safe to walk away. The model is a swappable part. The setup does the work.
**Picture:** Five numbered lines, with the claim below.

## Slide 40. Links
**On the slide:** The omp repo. The prewalk article by Can Bölük. Can Bölük's article on X. Two plugins I wrote: omp-agent-mesh and omp-org-account-router.
**Picture:** Five links, as short readable addresses.
**Facts behind it:** github.com/can1357/oh-my-pi, stencil.so/blog/prewalk, x.com/_can1357/status/2021828033640911196, github.com/masrurimz/omp-agent-mesh and github.com/masrurimz/omp-org-account-router. Leave out tern-worktrees and the skills repo, which are not public.
