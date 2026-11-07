# Benchmarking My Coding Agent Setup: One Engineer, Many Agents
## Detailed outline, self-reading deck (v4)

**SWE Growth community. Online on Zoom, 90 minutes. All slides in English.**
**Speaker: Zahid**

## How to use this outline
- This is the deck people read after the talk, without the speaker. It has 47 slides. The live deck in `presenter.md` has 73.
- It follows the same v4 story as the live deck. Five principles, each told through a story. Every part runs story, principle, proof, try this. The v3 story answers all 12 organizer questions, so seven slides were added over v2: the map, Antigravity, three money tips, PARA, the wireframe, the five checks and the three accidents. The v4 story adds the tool journey in Zahid's order, the parallel-agents reason for leaving the editor, the rules that step in on risky commands, the busy hour, and the CI queue, full disk and pause-and-wake plan. Here they sit inside existing slides, so this deck keeps its 47 slides. The live deck's dividers have no slide here, because this deck has no dividers. The map slide takes their place.
- Each slide has a headline of at most 12 words and about 50 words of text on the face, in short plain sentences. Each slide has one picture. The map slide may use about 60 words.
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
| Opening | 1 to 5 |
| My journey | 6 to 9 |
| Part 1. Choosing models and paying for them | 10 to 19 |
| Part 2. Teaching the agent | 20 to 27 |
| Part 3. Many agents at once | 28 to 33 |
| Part 4. Trusting the result | 34 to 38 |
| Part 5. Running it safely | 39 to 44 |
| What is still hard | 45 |
| Close | 46 and 47 |

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

## Slide 5. Today we go from my first tool to what is still hard
**On the slide:** My journey: the tools I tried, and why I left. 1 Choosing models and paying for them: which model, and what it costs. 2 Teaching the agent: skills, memory, and plans. 3 Many agents at once: one coordinator, many workers. 4 Trusting the result: checks before I merge. 5 Running it safely: servers, secrets, production. What is still hard: what I have not solved yet.
**Picture:** Seven rows, one per section of the talk, in this order.
**Facts behind it:** In the live talk the same map appears as a strip at the bottom of every divider, and the divider titles come from the same list. This deck has no dividers, so the map is the guide to the sections. The map names no principle, because the reader has not met the principles yet.

---

# My journey

## Slide 6. A harness is the program around the model
**On the slide:** The model thinks. The harness gives it tools, context, memory and rules. Claude Code, Cursor and omp are harnesses. Claude, GPT and GLM are models. You can swap the model and keep the harness.
**Picture:** Diagram with the model in the middle and four boxes around it: tools, context, memory, rules.

## Slide 7. Every tool switch had a reason
**On the slide:** I started with Copilot in VS Code at its 2022 launch, before Claude Code existed. Then Claude Code in VS Code, then Gemini tooling, then OpenCode with OmO, which was token hungry. When I started running agents in parallel, VS Code was too heavy, so I moved to Ghostty, Neovim and Amp. omp stayed because I can extend it.
**Picture:** A six-event timeline with no date scale, in this order: 2022 VS Code and Copilot at launch, 2025 Claude Code in VS Code, July 2025 Gemini tooling, October 2025 OpenCode (OmO) token hungry, December 2025 Ghostty with Neovim and Amp lighter, February 2026 omp extensible (highlighted). Antigravity is not on the timeline. It has the next slide.
**Facts behind it:** The order is the one I gave, not the order of the folder dates on disk, which conflict with it, so there are no bars on a date scale. I started when Copilot became generally available, and Claude Code launched in February 2025. OpenCode: "token hungry, slow, and its tests didn't catch much". Amp: I forgot why I left. One agent in an editor is fine and four agents in four editors is not, so I moved to the terminal so the memory goes to the agents, not the windows. That reason is mine and it is not measured, so there is no memory number.

## Slide 8. Antigravity showed me what an agent-first app looks like
**On the slide:** Antigravity was the first tool I used with a proper plan mode, memory and design artifacts. Its screen was built around agents, not around an editor. My Google account got banned, so I moved on.
**Picture:** Four cards: plan mode, memory, design artifacts, agent-first screen.
**Facts behind it:** I still use it in one place. omp uses its image model when I need a picture. It has no dated bar, so it is not on the timeline.

## Slide 9. omp is better because I can extend it
**On the slide:** When something hurts, I write a plugin. Autolearn: the agent writes a skill after a session. Hindsight: my memory tool. Compaction: the agent shortens a long chat so it can keep going.
**Picture:** A row of five icons: plugins, autolearn, memory, logins, compaction.
**Facts behind it:** Mesh, the org account router and the worktree plugin are all mine. Multi-provider subscription logins are the fifth item. My terminal changed five times and each step removed one chore: OpenChamber, Ghostty, herdr, then Tern. I tried Paseo to get easier managed worktrees, and Tern replaced it. Tern has an Android app for my phone. Ghostty came first because omp is a terminal program, and running agents in parallel is the reason I left the editor (slide 7).

---

# Part 1. Choosing models and paying for them

## Slide 10. The fastest model on paper was the slowest in my hands
**On the slide:** On paper, DeepSeek flash runs at 118 tokens a second. On my UI task it took 476 seconds. Opus took 92. DeepSeek needed 28 steps. Opus needed 9.
**Picture:** Bars in seconds on the UI task. Opus low 92, Sonnet medium 94, Haiku medium 170, DeepSeek flash low 476. DeepSeek is highlighted, with "118 tokens a second on paper" next to it.
**Facts behind it:** My September ranking formula had no term for steps. Each step was fast, but there were many more of them.

## Slide 11. Principle 1. Measure it on your own work
**On the slide:** Measure it on your own work. A benchmark on paper is a guess. Your own task is the test.
**Picture:** The principle name, large, with one plain line under it.

## Slide 12. Each job gets its own model
**On the slide:** I pick a model per job, not per prompt. Chat: Opus, low effort. Plan and hard bugs: Opus, high. UI design: Sonnet, high. Review: Opus, medium. Explore the code: Haiku. Rule of thumb: low to do, medium to review, high to plan and for hard bugs. Max almost never.
**Picture:** A five-row table with job, model and effort.
**Facts behind it:** These are the roles in my live config. The designer agent appears in 316 session files, mostly UI redesign tasks. Search helpers and the fast role use Haiku. Max is slow and gave little gain.

## Slide 13. Every model passed. Speed and price decided
**On the slide:** Two easy tasks, three runs each. Every model passed all 126 checks. Opus was fastest. Haiku was the cheapest Claude model. DeepSeek was by far the slowest. This is not a quality ranking.
**Picture:** A table with seconds on the UI task and price per task if I paid per token. Opus low 92 s, $0.22 to $0.39. Sonnet medium 94 s, $0.17 to $0.24. Haiku medium 170 s, $0.02 to $0.03. DeepSeek flash low 476 s, $0.04 to $0.07.

## Slide 14. Thinking harder made the agent take more steps
**On the slide:** I expected better answers for the same cost. Instead, higher effort meant more steps in every pair I tested. Spark: 9 to 23. DeepSeek: 28 to 40. My guess is that it checks more. The step counts are measured. The reason is a guess. This is why I almost never use max.
**Picture:** Paired bars, lower effort next to higher effort, for four pairs.
**Facts behind it:** Haiku slot finder 12 to 16. Sonnet UI 7 to 10. Low for execution on easy work is what this covers. "High for plans" is my judgment. More steps probably means a longer wait, but that is an inference, because I did not time the high-effort runs.

## Slide 15. Plan with the big model, let a small one type
**On the slide:** Prewalk is a trick from Can Bölük. The strong model reads the code and writes a todo list. At the first edit, the same session switches to a cheaper model. "Opus fixing things does not cost money. Opus reading things costs money." Can Bölük, omp author.
**Picture:** A four-step line: plan, todo list, first edit, swap model.
**Facts behind it:** It is off by default in omp. In his logs, edits were about 9% of the tokens.

## Slide 16. Prewalk was cheaper on long tasks, but slower
**On the slide:** Three steps. Opus low plans, Haiku high edits. Cheaper on long tasks, but slow. UI needed more, so Sonnet medium (this step is highlighted). Under them: On short tasks it cost the same or more. Test a trick on your own work. It may help someone else and not you.
**Picture:** Three steps in a row, the same layout as slide 15, with the third step highlighted.
**Facts behind it:** My first setup, from 14 October, was Opus at low effort planning and Haiku at high effort editing. On my long tasks it was cheaper, but slower, and tasks took too long to finish. That is my own account, with no numbers for that setup. On 23 October I turned prewalk off and moved my task agents to Sonnet at medium, because UI work needed a better model than Haiku. On short test tasks (a UI page and a slot finder, three runs each, medians, prices if I paid per token) prewalk cost the same or more. Opus low alone: 39 and 22 cents. With prewalk: 48 and 35 cents. Sonnet medium alone: 24 and 17 cents. With prewalk: 36 and 17 cents, a tie. In those tests prewalk was slower in every pair with a solo run to compare. Opus low took 92 s and 54 s alone, and 136 s and 84 s with prewalk. Sonnet medium took 94 s and 84 s alone, and 157 s and 127 s with prewalk. On short tasks the cheaper model re-reads the conversation after the switch. The handoff did not fire in 3 of 18 prewalk runs. A rough estimate from my logs, at 50 or more steps, was about $2.58 a task for Sonnet medium alone against $1.63 with a Haiku handoff. That is an estimate from uncontrolled work, not graded. My second try was on 24 and 25 October, first Haiku, then DeepSeek as the cheap model. It was really slow, and I turned it off the same day. Today my task agents run Sonnet at medium with no prewalk.

## Slide 17. In October I paid about $200 for $7.3k of tokens
**On the slide:** In October my agents used tokens worth $7.3k if I paid per token. I paid about $200. 270,000 requests. 41 billion tokens. 97% were cache reads, and those are cheap. I usually pay about $100 a month.
**Picture:** Two big numbers, "$7.3k if I paid per token" and "about $200 paid". A small chart of requests per month, from 2.2k in May to 270k in October.
**Facts behind it:** I pay for two Claude Max plans and OpenCode Go. In September my plans were GLM Max (my own, bought cheap at the launch price), Codex Pro from the office, and Devin Pro and OpenCode Go (my own). When the Claude 5.5 models arrived, I went all in on Claude. My words: "Claude 5.5 series quality is GOAT". Between June and August I moved from one chat at a time to many agents at once.

## Slide 18. Three money tips from my own bills
**On the slide:** One. Pay a flat plan and let caching work. In October, 97% of my tokens were cache reads. Two. Use a cheap model to search, like Haiku, and a strong model to plan, like Opus at high effort. Three. Test any cost trick on your own work before you trust it. Prewalk was cheaper on my long tasks, but slower.
**Picture:** Three tips, one, two and three.
**Facts behind it:** Tip one is the October bill on the previous slide. Tip two follows the model roles. Tip three is the prewalk result.

## Slide 19. Try this. Time one real task
**On the slide:** Take one real task you do often. Run it on two different models. Write down the time.
**Picture:** Two stopwatches side by side.

---

# Part 2. Teaching the agent

## Slide 20. Autolearn made too many skills
**On the slide:** A skill is a short file the agent loads when the work matches. Autolearn lets the agent write one after a session. I turned it on and got too many small skills. I merged them into 14 area skills and wrote a lint to keep them tidy. The last run found 0 errors. Now I run autolearn by hand.
**Picture:** The real screenshot of the lint result.
**Facts behind it:** The lint exits with an error if the layout is wrong, and a pre-commit hook runs it. Each area skill is a router, with playbooks (steps to follow) and references (facts to look up). The layout rule became a script, not a longer instruction.

## Slide 21. Principle 2. Do it twice, make it a skill
**On the slide:** Do it twice, make it a skill. "When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you." Zahid.
**Picture:** The principle name, large, with the rule under it.

## Slide 22. One skill per area of my work, like PARA
**On the slide:** I organize skills by area. The idea comes from Tiago Forte's PARA method. Projects have an end date. Areas never end, like infra or comms. Resources are topics you look things up in. Archives hold finished work. My skills follow Areas. That gives 14 area skills. My favorites are poteto-mode, my workflow skill, and show-me, which draws diagrams and wireframes.
**Picture:** Four PARA boxes, with Areas highlighted and leading to "14 area skills".
**Facts behind it:** PARA is Projects, Areas, Resources, Archives. Each area skill is one folder of work, for example infra-ops and comms-ops.

## Slide 23. Skills hold how. Memory holds what happened
**On the slide:** A skill holds how to do a thing, like the steps of a deploy. Memory holds what I did and decided, across projects. I kept Hindsight, and it saves a note once per 10 rounds of chat to keep the cost down. When a chat gets long, the agent shortens it so I do not watch the context window.
**Picture:** Two columns, skills and memory, with one example each.
**Facts behind it:** My words: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project." Before Hindsight I used Mnemopi, and I tried Cognee and removed it. The old data stayed untouched, so going back is one setting. Compaction uses three methods in order. It starts at 70% of the context window.

## Slide 24. My prompts are loose on purpose
**On the slide:** I paste raw context into the agent. A WhatsApp message from QA. A screenshot. A spreadsheet. The structure is in the files around the prompt. I dropped the task tracker beads, because agents got smarter and beads is hard for humans to read. No hooks for tasks. GitHub issues and the coordinator logs hold the work, and CI does the checking.
**Picture:** Layers of instructions, from a short global file down to the repo, with "beads" struck through.
**Facts behind it:** When I hand work to a helper agent, the brief has one shape: target, change and contract. Rules are small files. Some are always in the prompt, such as check every layer. Others wait for a pattern. When the agent types pytest or vitest without a memory cap, omp stops the stream, adds the rule, and the agent rewrites the command. omp calls this TTSR, time traveling stream rules. Rules stepped in 4,635 times since June. 1,424 were my two memory caps. The rest were omp's own TypeScript rules.

## Slide 25. 25 principles, and one of them is mine
**On the slide:** poteto-mode is an agent-style skill I ported to omp. It brings 25 principles and 23 playbooks. The agent must say which principle shaped each decision. My own principle is check every layer: product and the human walk, structure, and data and flow.
**Picture:** Three stacked layers, each with one example finding.
**Facts behind it:** It comes from the pstack plugin under an MIT licence, written by poteto. Check every layer is my own principle, added on top. The count is 11 core, 6 architecture, 5 verification, 2 delegation and 1 meta.

## Slide 26. Before any code, the agent draws the screen
**On the slide:** I start from the product and ask the agent for a wireframe. The show-me skill draws it. Then we decide the folders and files. Then the data and the flow, and we check each layer. All of it goes into one markdown file in a plans folder for that feature, so helper agents do not wander. That file is the reference.
**Picture:** A neutral wireframe of a generic "Place detail" screen, with numbered notes in the margin. Below it, a strip of three steps: screen, files, data.
**Facts behind it:** The wireframe is a newly drawn example, not one of my apps. Each feature gets a plans folder with wireframe SVGs. I asked the agent to put the technical details and the wireframe in one file so helper agents would not wander. The layer-by-layer check is my check-every-layer principle.

## Slide 27. Try this. Write the skill
**On the slide:** The next time you repeat a task for the third time, stop. Write it down as a skill, even a small one.
**Picture:** A short checklist with three boxes, the third one ticked.

---

# Part 3. Many agents at once

## Slide 28. Idle agents never saw the messages
**On the slide:** My agents talk to each other through a plugin I call mesh. My coordinator sent a message to every agent. Idle agents do not wake up for a message, so they never read it. The coordinator wrote in its log: "idle sessions don't wake on mesh messages; each branch needs one writer".
**Picture:** One coordinator sending a message. Some agents receive it. Two idle agents stay grey.
**Facts behind it:** On a busy hour, 4 to 9 agents work at once. 39% of my working hours since September had 4 to 9 agents, and a typical hour had 3. A folder is a worktree or repo, so this counts workstreams, not processes. It only works because the agents have full control of the dev infra. They start the stack, seed it and test it without me.

## Slide 29. Principle 3. One writer per branch
**On the slide:** One writer per branch. Many agents and many branches are fine. On each branch, exactly one agent writes.
**Picture:** The principle name, large, with one plain line under it.

## Slide 30. Every agent task gets its own copy of the repo
**On the slide:** A worktree is its own copy of the repo. Every task gets one, so agents never share a working folder. I built a small command, tern-wt, to manage them. The skill tells the agent to use that one command and not to remove a worktree it did not create.
**Picture:** One repo in the middle and three copies around it.
**Facts behind it:** The real list showed 101 worktrees. Tern, my terminal app, makes each copy a tab and offers to remove it when the tab closes.

## Slide 31. Mesh: agents see what the others are holding
**On the slide:** Many agents share one machine, one set of ports and one Docker daemon. Before heavy work, an agent checks who else is working. If a peer runs the same job, it waits. I wrote mesh myself, and it took seven commits.
**Picture:** Three real agent cards: one coordinator holding the production release, one waiting for the owner's go, one with nothing held.
**Facts behind it:** The capture showed 19 agents in 8 repo groups. My other plugins include an account router that puts office repos on the office account and personal repos on personal accounts.

## Slide 32. One coordinator merges after an independent review
**On the slide:** I do not watch every branch. I watch one coordinator. A worker opens a pull request with proof and sends one line. It says MERGE-READY, the PR number and the full commit. The coordinator freezes that commit and asks an independent reviewer. If the review passes, the coordinator merges, one at a time. If it fails, the findings go back for one fix round. This also solves base branches.
**Picture:** A loop with worker, coordinator, reviewer and the pull request.
**Facts behind it:** The coordinator is an ordinary omp session. Its log has 353 decisions from 2 to 7 November. Every decision is one row with a reason. Product questions go to the coordinator, not to me. I decide merges of finished work and hold production releases. The coordinator knows the state of every branch, so base-branch coordination is solved, not open.

## Slide 33. Try this. One worktree per agent
**On the slide:** When you run two agents on one repo, give each its own worktree. It is one git command.
**Picture:** Two folders, each with its own branch label.

---

# Part 4. Trusting the result

## Slide 34. The plane fix came with proof
**On the slide:** Remember the plane? On the left, before the fix, clicking a draft opens the edit modal. On the right, after the fix, the click only selects the sensor. Three test runs failed on the old code. The same three passed with the fix.
**Picture:** The real before and after frames from the pull request, side by side. Below, "3 failed, then 3 passed".
**Facts behind it:** The test used the same data that broke staging. A failing run before and a passing run after shows the test can really fail.

## Slide 35. Principle 4. Show proof, not "done"
**On the slide:** Show proof, not "done". A pull request is ready when it shows evidence. Recording for what you can see. Command and real output for everything else.
**Picture:** A four-rung ladder: recording, command output, run link, test result.
**Facts behind it:** A good pull request body has Why, How, What changed, Scope, Tradeoffs, Blast Radius and Verification. Verification ends with "Not verified:" and a list, or "Not verified: none". Take the first rung that shows the claim.

## Slide 36. Five checks run before I look
**On the slide:** One. The language server checks every edit. Two. Lint and type checks. Three. Tests shaped like the testing trophy: static, unit, integration and end to end. A formal-verification skill covers risky logic. Four. Reviewer agents, more of them for more risk. Five. Me, for UI and feel.
**Picture:** A five-step ladder, one rung per check, in this order.
**Facts behind it:** The testing trophy is from Kent C. Dodds. A small fix gets one reviewer. A stack of five pull requests got five. The impersonation pull request got a security reviewer and a product reviewer.

## Slide 37. A second agent freezes its verdict
**On the slide:** A second agent reads the pull request in a clean copy and freezes its verdict at one commit. It checks that the test fails on the old code and passes on the new, that it merges cleanly and that lint is clean. A new commit means a new review. I still check the UI by hand.
**Picture:** The real review report, re-typeset as a card: "PASS with notes".

## Slide 38. Try this. Ask for a clip
**On the slide:** In your next pull request, ask the agent for a before and after clip. It costs one sentence.
**Picture:** A pull request with two video thumbnails, before and after.

---

# Part 5. Running it safely

## Slide 39. Every production change goes four steps
**On the slide:** Dry run. Backup. Apply with the expected row counts. Verify. A dry run runs the real update inside a transaction and rolls it back. A human can repeat every step. My prompt: "dry run first then show me what will be changed".
**Picture:** Four boxes in a row, in that order.
**Facts behind it:** Production is read-only by default. A deploy is done only when the running version is verified, not when the job is green.

## Slide 40. Principle 5. Make it safe to walk away
**On the slide:** Make it safe to walk away. A human can repeat every step. Secrets stay hidden. Then I can leave the agent working and go on a plane.
**Picture:** The principle name, large, with one plain line under it.

## Slide 41. Three accidents gave me three guardrails
**On the slide:** An agent reset the main checkout and wiped the shared dev database. Now the devkit refuses any reset that reaches it. A reviewer agent ran a Docker prune and deleted about 244 unused volumes. Now Docker cleanup is banned for every agent. One masking tool went through 11 reviews. Now reviews are capped at two rounds, then we rethink the design.
**Picture:** Three pairs, accident and guardrail.
**Facts behind it:** All three come from my coordinator's log of 353 decisions. The reset ignored a flag in the main checkout. The devkit fix is PR #574. Each of the 11 reviews fixed one more shape of the same bug.

## Slide 42. Three layers protect my secrets
**On the slide:** First, values are hidden from the model, so it sees placeholders. Second, dangerous commands are blocked, like rm -rf, force push and DROP TABLE. Third, secrets live in managed storage. Infisical for machines, Bitwarden for humans. Hiding a value is not the same as managing a secret.
**Picture:** Three stacked cards, one per layer.

## Slide 43. Proof runs away from my workstation
**On the slide:** My workstation is busy running agents, so proof runs on other machines. A shared dev box runs one stack per user. A batch box runs jobs. An office box runs staging. Production is read-only. A new worktree gets a running stack from one command.
**Picture:** A simple machine map with no addresses.
**Facts behind it:** In Alkhidmah the command is `bun run bootstrap`. Ports and database come from the branch name, so two worktrees never fight over a port.

## Slide 44. Try this. Dry run first
**On the slide:** Before your next production change, ask the agent to show you what will change. Then decide.
**Picture:** A preview table with a "dry run" label.

---

# What is still hard

## Slide 45. Four things are still hard, and one plan is next
**On the slide:** A proof clip cannot judge how a screen looks, so I still check UI by hand. CI is now the queue. Setting up each worktree is still slow, 652 seconds down to 171. My disk is 89% full. Next I try one VM per stack, asleep when idle and awake when an agent needs it. That is a plan, not a result.
**Picture:** Four cards with one number each. "By hand", "538 runs", "171 s", "89%".
**Facts behind it:** CI. One day in November my alkhidmah repo ran 538 CI runs, and 1 in 10 runs took 16 minutes or more. I am testing larger runners and spreading the load over free runners, and nothing is settled. Setup. At work the analytics app is heavier, with a large time series stack and a long seed, and I did not measure that seed. Disk. Docker alone holds 447 GB, and one test run without a memory cap once reached 38 GB of RAM on the shared box. A rule now caps memory, so the fix for RAM was a rule, not more memory. Plan. A sleeping VM still takes disk, so a bigger SSD comes first. Base branches used to be on this list. Part 3 showed how the coordinator solved it.

---

# Close

## Slide 46. Five principles, one claim
**On the slide:** Measure it on your own work. Do it twice, make it a skill. One writer per branch. Show proof, not "done". Make it safe to walk away. The model is a swappable part. The setup does the work.
**Picture:** Five numbered lines, with the claim below.

## Slide 47. Links
**On the slide:** The omp repo. The prewalk article by Can Bölük. Can Bölük's article on X. Two plugins I wrote: omp-agent-mesh and omp-org-account-router.
**Picture:** Five links, as short readable addresses.
**Facts behind it:** github.com/can1357/oh-my-pi, stencil.so/blog/prewalk, x.com/_can1357/status/2021828033640911196, github.com/masrurimz/omp-agent-mesh and github.com/masrurimz/omp-org-account-router. Leave out tern-worktrees and the skills repo, which are not public.
