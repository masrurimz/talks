# Reference digest: the benchmark lab (value formula, October 2026 bench, prewalk, subscriptions)

Summary. This digest is the core of Part 1 ("Measure it on your own work") and matches the talk title. Zahid does not pick models by reputation. He has a value formula that turns a subscription into an effective price per million tokens, a small October 2026 bench of his own with hidden-check graders, a measured finding that higher effort means more steps, and a record of subscriptions from September (several providers) to now (all in on Claude 5.5). It also covers prewalk, a handoff from a strong model to a cheaper one, using the omp docs and the author's post, and why Zahid turned it off. Last, it holds one public quote that supports the claim of the talk, that the harness matters more than the model.

Evidence paths starting with `MS/` mean `~/.omp/agent/managed-skills/`. The bench scripts and data live in `~/.omp/agent/bench/`. Dollar figures per task are the list price of the tokens (API-equivalent), not money paid. Items marked [INFERENCE] come from the source notes and are not confirmed. No secret values, emails, addresses or customer names appear here. Account counts of other people and quota percentages are left out on purpose.

---

## 1. The value formula

### Key facts

- Problem. A sticker price per million tokens lies. A model at $25 per 1M and a model at $2 per 1M can perform the same, and a subscription changes what a token costs. The formula puts quality, subscription and speed on one line. (`MS/omp-ops/references/omp-sub-value-ranking.md`, "Formula")
- The four lines.

```
Value Multiplier    = Quota $ / Subscription cost
Effective $/1M      = Blended $/1M / Value Multiplier
Value Score         = Benchmark / Effective $/1M
Speed-adjusted QSPD = (Benchmark x tok/s) / (Effective $/1M x 1000)
```

- Higher is better. The formula catches the "$25 per 1M versus $2 per 1M at the same performance" trap.
- Procedure. Query `~/.omp/stats.db` for 30 days of requests, tokens, cost, time to first token and tokens per second. Pull one common benchmark for every candidate. Get each subscription's quota in dollars per window and its cost. Compute the four numbers, rank, apply a quality floor, then pick the highest QSPD above the floor.
- Rules he wrote down after getting burned.
  - Use one common benchmark only. Terminal-Bench 2.1 covers every candidate. Never mix SWE-bench Verified, Terminal-Bench and SWE-Pro.
  - Count the accounts. Two accounts of one plan double the quota and leave the multiplier unchanged.
  - `cost_total` in the stats is API-equivalent, not spend.
  - GLM is verbose. DeepSeek may use 30 to 50 percent fewer tokens for the same work.
- Worked example from September 2026. DeepSeek V4.1-Flash scored 90.6 on Terminal-Bench 2.1 at about 118 tokens per second. GLM-5.3 scored 88.2 at about 42. The two scores are close, and GLM loses about 4 times on the speed-adjusted value. (`MS/omp-ops/references/zahid-ai-subscription-portfolio.md`, "Formula" and the Terminal-Bench 2.1 ranking, 2026-09-14)

### Story/example

The formula is the answer to "which subscription is worth it". It explains why the September portfolio in section 5 held several plans, each used where its effective price was lowest.

### Show on screen

- The four formula lines in a code block.
- One row of the September ranking, DeepSeek against GLM, with tokens per second beside the score.

---

## 2. The October 2026 bench

### Key facts

- Method. Fixed harness. Two easy tasks, three runs each, graded by hidden checks. Task one is a UI page (`index.html`). Task two is a logic task (`slots.py`, a slot finder). Numbers are medians. Scripts are in `~/.omp/agent/bench/`, per-run data in `results-2026-10.json`, the playbook in `MS/omp-ops/playbooks/model-bench.md`. (`MS/omp-ops/references/model-bench-results.md`)
- Result that shapes the whole lesson. Every arm passed 126 of 126 checks. The bench does not separate models on quality. It separates them on speed and cost.

**Solo arms (median time per task, list-price cost per task)**

| Setup | UI | Slot finder | Cost per task |
| --- | --- | --- | --- |
| Opus 5.5 low | 92 s | 54 s | $0.22 to $0.39 |
| Sonnet 5.5 medium | 94 s | 84 s | $0.17 to $0.24 |
| Spark 1.3 low | 103 s | 71 s | $0.08 to $0.15 |
| Spark 1.3 contributor low | 121 s | 88 s | about $0.01, flat plan |
| Haiku 5.5 medium | 170 s | 120 s | $0.02 to $0.03 |
| Haiku 5.5 high | 207 s | 240 s | $0.04 to $0.05 |
| Wonder 1.0 low | 136 s | 252 s | $0.39 to $0.41 |
| DeepSeek v4.1 flash low (CommandCode) | 476 s | 275 s | $0.04 to $0.07 |
| DeepSeek v4.1 flash high (CommandCode) | 661 s | 542 s | not measured |

- Fast and cheap are different lanes. Opus low is the fastest and costs the most per task. Haiku medium costs a few cents and takes about twice as long. DeepSeek is cheap per token and the slowest arm, because it took far more turns, not because each call was slow. Its fast variant made 40 to 56 UI turns against 28 for the regular one.
- Medium effort on Spark and Wonder added time with no measured quality gain. Wonder is not a subagent model, since it was slow at every effort.
- Spark 1.3 contributor at low effort is the cheap-lane sweet spot. It was faster than Haiku medium on both tasks.

### Story/example

The bench gives a lane map. Opus is fast, so it plans and reviews. Sonnet and Haiku carry volume. DeepSeek looks cheap on a price list and is expensive in minutes.

### Show on screen

- The solo arms table with the cost column highlighted, and the line "126/126 on every arm" in large type.

### Quotable

> Every arm passed every check, so this bench does not rank quality. (`model-bench-results.md`, "Read on quality")

---

## 3. Effort versus turns

### Key facts

- Finding. Raising effort raised the turn count in every head-to-head pair. Lower effort gave fewer turns and fewer tokens. The common guess that low effort costs more steps is wrong on these tasks. (`model-bench-results.md`, "Effort versus turn count")

| Model | Task | Lower effort turns | Higher effort turns |
| --- | --- | --- | --- |
| Haiku 5.5 | slot finder | 12 (medium) | 16 (high) |
| Haiku 5.5 | UI | 15 (medium) | 16 (high) |
| Spark plain | slot finder | 9 (low) | 23 (medium) |
| Spark plain | UI | 17 (low) | 23 (medium) |
| Spark contributor | slot finder | 9 (low) | 20 (medium) |
| Spark contributor | UI | 19 (low) | 22 (medium) |
| Sonnet 5.5 | slot finder | 4 (low) | 5 (medium) |
| Sonnet 5.5 | UI | 7 (low) | 10 (medium) |
| DeepSeek flash | slot finder | 22 (low) | 40 (high) |
| DeepSeek flash | UI | 28 (low) | 40 (high) |

- The turn counts are measured, over three runs per arm. The likely cause is verification. Higher effort re-reads and re-checks, and each check is a turn. The cause is an inference in the source. [INFERENCE]
- His rule is unchanged and now has data behind its first half. Low for execution, high for plans and hard debugging, medium for review, max almost never. The bench covers execution on easy tasks. The "high for plans" half is still his judgment.

### Story/example

More thinking sounds free when you are not the one waiting. On a task a model can already do, extra effort seems to buy extra checking, and each check is another round trip. [INFERENCE]

### Show on screen

- The Spark and DeepSeek rows as a bar pair (9 against 23, 28 against 40).
- The rule line "low execute, high plan and hard debug, medium review, max almost never".

---

## 4. Handoff arms, the lesson, and the Terminal-Bench caveat

### Key facts

**Handoff arms**

| Setup | UI | Slot finder | Cost per task |
| --- | --- | --- | --- |
| Opus 5.5 low to Sonnet 5.5 low | 136 s | 84 s | $0.35 to $0.48 |
| Sonnet 5.5 medium to Haiku 5.5 medium | 157 s | 127 s | $0.17 to $0.36 |

- On short tasks a handoff costs extra. The second model re-reads the conversation after the switch, so you pay for the read twice. The prewalk target inherits the starter's effort, which is why the first arm is low into low. The handoff did not fire in 3 of the 18 prewalk runs, which stayed on the starter model.
- Real long sessions showed the reverse on cost. At 50 or more turns, Sonnet medium alone cost about $2.58 a task and Sonnet medium handing off to Haiku medium cost $1.63. These log numbers are estimates from uncontrolled work, not graded results. Say so on the slide. They carry no timing, so they say nothing about speed.

**The lesson, in one sentence.** Every arm passed, so quality did not separate the models. Speed and cost did. On easy tasks the cheapest lane that passes wins, and a plain price list hides how many minutes it takes.

**Terminal-Bench caveat**

- The bench is two easy tasks. It cannot say how a model behaves on long multi-step work.
- Public Terminal-Bench 4.0 puts Haiku 5.5 at 39.2 percent and Sonnet 5.5 at 70.6 percent. Anthropic says Haiku can report a change as done without running a check at low or medium effort. Treat Haiku on long multi-step work as unproven until a harder task is benched. (`model-bench-results.md`, "Read on quality")
- Do not compare these 4.0 figures with the Terminal-Bench 2.1 scores in section 1. They are different versions. Rule: one benchmark per comparison.

### Story/example

A handoff is not a free discount. It pays off when the expensive model's reading is the cost, which is long sessions, and it loses when the task is short. That is the same point prewalk makes in section 6.

### Show on screen

- The two handoff rows next to the two solo rows they came from.
- A one-line warning card, "easy tasks, 3 runs, hidden checks, not a quality ranking".

---

## 5. Subscriptions, September 2026 versus now

### Key facts

- Corrected history, in his words. GLM Max was his own, a one-year plan bought cheap at the launch price. Codex Pro came from the office. Devin Pro and OpenCode Go were his own. When the Claude 5.5 series arrived he went all in on Claude. Reason, in his words, "Claude 5.5 series quality is GOAT".

| | September 2026 | Now (November 2026) |
| --- | --- | --- |
| Own | GLM Max (one-year plan bought at a cheap launch price, listed at $168 a month), Devin Pro ($20 a month), OpenCode Go (2 accounts, $10 a month each) | 2x Claude Max, OpenCode Go |
| Office | Codex Pro | none (November requests are 100 percent Anthropic) |
| Default model | `standard-fast` preset, glm-5.3 default, muse-spark smol, swe-2 for plan and advisor | Opus 5.5 low default, Sonnet 5.5 medium tasks, Haiku 5.5 scouts |
| Monthly spend | not recorded in these sources | usually about $100, now about $200 |

- Evidence for the September column. `MS/omp-ops/references/zahid-ai-subscription-portfolio.md`, verified 2026-09-14.
- Requests tell the same story. All time, by requests, anthropic 240k, zai (GLM) 224k, openai-codex 128k, muse-sub 91k, opencode-go 59k, at least 12 providers (`omp stats`, 2026-11-05). In October anthropic had 187k requests, muse-sub 37k, opencode-go 22k, muse-code 18k, commandcode 5k. November so far is 100 percent Anthropic.
- The cost headline stays the same. October 2026 was 270k requests and 41B tokens, an API-equivalent price of $7.3k, and he paid about $200 (roughly 36 times). 97 percent of tokens were cache reads.
- Why back to Claude, in one line. Quality. In his words, "Claude 5.5 series quality is GOAT". For contrast, the September data had GLM-5.3 at 42 tokens per second, "slow", and it was demoted to fallback-only in the `standard-fast` preset (`zahid-ai-subscription-portfolio.md`).

### Story/example

The September portfolio was built with the formula. Several plans, each used for the job where its effective price was lowest. When the Claude 5.5 series arrived he stopped optimizing price per token and went all in on quality.

### Show on screen

- Two columns, September and now, with the "own" and "office" tags on each plan.
- The last row with "about $100 usual, about $200 now" and "$7.3k API-equivalent in October".

### Quotable

> Claude 5.5 series quality is GOAT. (Zahid, round 4 answers, 2026-11-05)

---

## 6. Prewalk

### Key facts

**Definition from the omp docs (`omp://prewalk.md`).**

- Prewalk is a one-shot handoff from the active model to a faster or cheaper model after planning reaches implementation. The starting model inspects the repository, creates a todo list and begins the change. Then the target model continues the same session.
- How it fires. An armed prewalk injects a planning nudge. A successful `todo` call opens the gate. At the first `edit` or `write` the session switches to the target, prunes the planning instruction, and steers the target with an implementation checklist. The switch happens once.
- Off by default. The target is `prewalk.into`, which defaults to the `@smol` role. Flags are `--prewalk`, `--prewalk-into <model>` and `/prewalk`. Subagents have separate controls, `task.agentPrewalk`.

**Source of the idea.** Can Bölük, the author of omp (Stencil), "You only need the frontier model for one single edit", 2026-07-13, https://stencil.so/blog/prewalk .

- Core claim. "Opus fixing things does not cost money. Opus reading things costs money." In the author's own token data, only 9 percent of 1.81 billion tokens across about 2 million tool calls were edits. The author calls the sample anecdotal. The bill is essentially the number of reads.
- Why a plain plan handoff fails. A /plan handoff (Opus plans read-only, Gemini Flash implements) cost $3.18 per task, 12.7 minutes, 84.6 percent pass. Opus alone cost $2.78, 10.1 minutes, 84.6 percent. The cheap model has to read the code again, so the reading is paid twice. The post says a plan is a postcard and an executor needs the trajectory.
- Method. "Hand off a trajectory, not a fairytale." Keep the context, swap the model after the first edit lands, and delete the planning instruction so the cheap model thinks it planned and began on its own.

**Can Bölük's receipts, SWE-Bench Pro (from the post). His models and his workload, not Zahid's.**

| Arm | Pass | Cost per task | Time |
| --- | --- | --- | --- |
| GPT 5.6 Luna alone | 77% | $0.60 | 570 s |
| GPT 5.6 Sol prewalk into Luna | 85% | $1.04 | 300 s |
| GPT 5.6 Sol alone | 88% | $1.71 | 372 s |
| Gemini Flash 3.5 alone | 60% | $1.16 | 360 s |
| Opus 4.8 prewalk into Flash | 78% | $1.46 | 402 s |
| Opus 4.8 alone | 85% | $2.78 | 606 s |

- The post's own summaries. "97% of Sol's pass rate at 61% of the cost" and "92% of Opus at 53% of the cost, 1.5x the speed". His test cut cost 39 to 47 percent for 3 to 7 points of pass rate.

**Zahid's own bench and timeline.**

- Bench, Claude 5.5 only, 2 tasks (UI page, slot finder) x 3 runs, medians, every arm 126 of 126, API-equivalent cost per task. Opus 5.5 low alone $0.39 (UI) and $0.22 (slot finder). Prewalk Opus 5.5 low into Sonnet 5.5 low $0.48 and $0.35. Sonnet 5.5 medium alone $0.24 and $0.17. Prewalk Sonnet 5.5 medium into Haiku 5.5 medium $0.36 and $0.17 (a tie on slot finder).
- Bench times. Prewalk was slower in every pair with a solo run to compare. Opus 5.5 low alone 92 s (UI) and 54 s (slot finder), with prewalk 136 s and 84 s. Sonnet 5.5 medium alone 94 s and 84 s, with prewalk 157 s and 127 s. The bench has no solo Opus medium arm, so do not say "every prewalk arm was slower".
- Timeline from his prompts, first setup first. On 2026-10-14 he wrote "default will be opus low default prewalk will be into haiku high". That was his first setup, Opus 5.5 low plans and prewalk hands off into Haiku 5.5 high. On 2026-10-23 he wrote "the issue now task is taking too long to complete", then "disable the prewalk and go with sonnet medium for task". On 2026-11-07 he said prewalk was cheaper for longer tasks but slower, and that he switched to Sonnet medium because he needed better UI work. There are no numbers for the Opus low into Haiku high setup, so "cheaper on long tasks" for it is his own account.
- Second try. On 2026-10-24 he turned prewalk on into Haiku 5.5 medium (Sonnet medium into Haiku medium). On 2026-10-25 he moved the target to DeepSeek v4.1 flash for cost. It was really slow, so he turned it off the same day. This matches the bench, where DeepSeek flash was the slowest arm at 476 s on the UI task.
- Config now. `task` and `poteto-agent` run Sonnet 5.5 medium, and `task.agentPrewalk` is off for both. On short tasks prewalk cost the same or more. The log estimate ($2.58 against $1.63 at 50 or more turns, Sonnet medium alone against Sonnet medium into Haiku medium) is an estimate from uncontrolled work, not graded.
- Say clearly that the receipts above are Can Bölük's numbers with his models, and the verdict "off" is Zahid's own experience on his own work.

### Story/example

The two results do not fight. The author measured long, hard tasks where reading dominates, and the handoff saves money there. In Zahid's runs the target added minutes, and his bench handoff arms show extra cost on short tasks. The lesson for the audience is to test a trick on their own workload before keeping it.

### Show on screen

- Two ribbons, "plan then re-read" against "keep the trajectory", or the table above with the Sol row highlighted.
- A card "Zahid, prewalk, off now" with the reasons (cheaper on long tasks but slower, UI work needed a better model, short tasks cost the same or more, the DeepSeek second try was really slow).

### Quotable

> Opus fixing things does not cost money. Opus reading things costs money. (Can Bölük, stencil.so/blog/prewalk)

> Hand off a trajectory, not a fairytale. (same post)

---

## 7. The harness-only quote

### Key facts

- The same author posted on X that he "improved 15 LLMs at coding in one afternoon" and that only the harness changed. Wording as captured in the round 4 notes, "I improved 15 LLMs at coding in one afternoon. Only the harness changed." https://x.com/_can1357/status/2021828033640911196
- Use. It is outside evidence for the talk's claim, that the model is a swappable part and the setup around it does the work. Put it on the claim slide or the journey section, with the attribution and the link.
- Care. The post was not re-fetched while writing this digest. Check the exact words on the live post before putting them on a slide in quotation marks.
- Tern is made by Stencil, the company behind omp's author. Say "Tern, from Stencil". [INFERENCE] from Zahid's remark and the Stencil blog, so do not state more than that.

### Show on screen

- The quote as a card with the author's name and "omp author, Stencil".

### Quotable

> I improved 15 LLMs at coding in one afternoon. Only the harness changed. (Can Bölük, X)
