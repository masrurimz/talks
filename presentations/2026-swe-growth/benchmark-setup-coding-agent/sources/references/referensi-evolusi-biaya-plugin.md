# Reference digest: tool journey, harness, plugins, terminal, models, cost, memory

Summary. This digest tells how Zahid's setup evolved and what it costs. It covers the tool journey (Claude Code, OMO on OpenCode, Amp, a short Antigravity side trip, then omp), what a harness is, why omp won (it is extensible), the plugins he wrote, the terminal journey (OpenChamber, Ghostty, herdr, Paseo, Tern), model routing per role with an effort rule and a speed table, cost and subscriptions (including why he went back to Claude), prewalk, the habit of constant benchmarking, the memory journey (Mnemopi, Hindsight, Cognee), the autolearn story, why beads was dropped, and his one rule for when to write a skill. The benchmark lab itself (value formula, October 2026 bench, effort versus turns, prewalk with receipts) is in `referensi-benchmark-lab.md`. This digest keeps the short version.
Numbers come from `omp stats` re-aggregated on 2026-11-05 (`~/.omp/stats.db`, table `message_rollup`, x1-dev, 2026-03-07 to 2026-11-05) and from Zahid's own answers in the grilling rounds of 2026-11-05. Prices are omp's API-equivalent estimate, the list price of the tokens. They are not money paid. Items marked [INFERENCE] were not confirmed.
No secret values, emails or addresses appear in this file.

---

## 1. Tool journey

### Key facts

- Zahid started with Claude Code. Some tasks were not good enough and he wanted more efficiency, so he moved on.
- Next was OMO (oh-my-opencode, an extension of OpenCode). First he used it as a pure CLI, then found OpenChamber, a web UI. OMO had many issues and limits because it is an extension of another tool, and quality was not as good. Claude and OpenAI subscriptions were also getting banned on OpenCode.
- He switched to Amp because it was more mature. On Amp he mostly went through a proxy (CLIProxyAPI) so he could get very large usage. Amp was the longest stay. It had cross-agent communication and could spawn other agents.
- Antigravity was a short side trip. He used it at first while it had good free usage and features like plan annotations and session artifacts. He left because it is heavy, quality and limits disappointed him, and the Google account got banned (prompt dated 2026-03-10).
- Why he left Amp: he forgot. The slide says "I forgot why I left Amp, but omp is better because..." and then lists the reasons in section 3.
- Where omp stands: the longest and current tool. Since 2026-03-07 on x1-dev main.

### Data timeline (follow this order on the slide)

| Date | Tool | Evidence |
| --- | --- | --- |
| 2025-07-29 | Gemini CLI folder first appears on m5 (`~/.gemini`) | file dates on m5 |
| 2025-10-19 | Claude Code | first session on m5 |
| 2025-10-20 | OpenCode | 215 sessions on m5 |
| 2025-12-22 to 2026-03-16 | Amp | longest stay |
| 2026-02-23 | omp on m5 | 37 session folders |
| 2026-03-07 | omp on x1-dev main, the workstation | start of `stats.db` |
| 2026-03 | oh-my-opencode prompts concentrated on x1 | prompt log |

- The m5 and x1 split is part of the story. m5 is the Mac used for first tries and review. x1-dev is the Linux workstation where the real work runs.

### Quotable

> I forgot why I left Amp, but omp is better because...
> (slide line, Zahid's own framing)

---

## 2. What a harness is

### Key facts

- The audience is mixed. Some use Claude Code or Cursor. Few know omp. Explain "harness" in one slide.
- A harness is the program around the model. The model only reads text and writes text. The harness gives it tools (read, edit, search, shell), runs the loop, keeps the session, compacts context when it fills, loads instructions and skills, and enforces guardrails.
- Claude Code, Cursor, OpenCode, Amp and omp are harnesses. The model behind them can be swapped. That is the claim of the talk: the model is a swappable part.
- omp is the harness he uses. Its live home is `~/.omp/agent/`. It holds config, model roles, instruction files, extensions, skills, rules and session files (see `referensi-setup-dan-infra.md`, section 1).

---

## 3. Why omp

### Key facts

Zahid's reasons, in his order of weight.

1. It is extensible. He writes his own plugins and extensions, and this was a main reason he chose it. Section 4 lists them.
2. Autolearn. The agent can turn a session lesson into a skill (section 8).
3. Hindsight memory as a backend (section 8).
4. Multi-provider subscription logins, so one setup can use several subscriptions and fall back between them.
5. Good compaction. omp compacts with `snapcompact`, then `remote`, then `soft`, with a 70% threshold and idle compaction after 60 seconds (`~/.omp/agent/config.yml`, `compaction:`). He cites this as one reason beads became unnecessary (section 9).

### Story/example

The test of "extensible" is that the pieces he needed did not exist, so he built them: the mesh, the GitHub account router and the worktree manager for his terminal are all his own plugins.

---

## 4. His plugins

### Key facts

Evidence is `~/.omp/plugins/omp-plugins.lock.json` and the repos under `~/work/labs/`.

| Plugin or extension | What it does | State |
| --- | --- | --- |
| `omp-agent-mesh` | Own Effect-based mesh engine. Repo groups, presence, waking messages, throttled sends, file claims, subagent attribution. | Enabled. 7 commits, 2026-10-25 and 2026-10-26. |
| `omp-org-account-router` | Restricts each session to the GitHub organisation's OAuth account. The office account serves org repos and personal accounts serve personal repos. | Enabled. 2026-11-03 to 2026-11-05. |
| `poteto-mode.ts` (extension) | Autoloads the poteto-mode skill once per context. | Live. |
| `herdr-omp-agent-state.ts` (extension) | Reports agent state to herdr panes. | Live. |
| `orca-*` (extensions) | Status hooks for the Orca terminal. | Older, predecessor of Tern. |
| `tern-worktrees` | Tern plugin plus the `tern-wt` CLI plus a skill. Opens git worktrees as Tern tabs and tears them down. | v0.3.2. |
| `paseo-omp` | Paseo plugins for the Paseo app. | 237 commits, Sep to Oct 2026. |
| `opencode-go-multi-auth` | Rotates several OpenCode Go accounts. | Apr to May 2026. |
| `luvus-omp-mosh` | Phone notification bridge. | Dormant. |
| `omp-anthropic-sub`, `omp-muse-sub` | Subscription routing experiments. | The muse one retired 2026-10-10. |

- Also `omp-skills`: the repo where the poteto and pstack skill sets are ported to omp, with upstream branches kept clean (`referensi-skills-prompt-dan-config.md`, topic 3a).
- `omp-agent-mesh` and `tern-worktrees` are the two worth a full slide each. Mesh is covered in `referensi-mesh-koordinator-mobile.md`. Worktrees in `referensi-setup-dan-infra.md`.

### Quotable

```
description = "Opens git worktrees as Tern tabs, and creates, relocates and tears them down."
```
(`~/work/labs/tern-worktrees/plugin.toml`)

---

## 5. Terminal journey

### Key facts

Order, in his words: OpenChamber, then Ghostty (windows and tabs) because of omp, then herdr to manage worktrees and open sessions, then Paseo to find something easier with more managed worktrees, and now Tern. He says he just uses Tern now.

| Step | Why | Evidence |
| --- | --- | --- |
| OpenChamber | Web UI for OpenCode and OMO | service present 2026-05 |
| Ghostty | omp is a terminal program, so windows and tabs | |
| herdr | Manage worktrees and open sessions as panes | 2026-06-27 migrated from zellij, used to October |
| Paseo | Easier, with more managed worktrees | evaluated 2026-06-23 "to replace the openchamber and opencode web"; busy in October (46 prompts); 2026-10-16 "stop the paseo daemon" |
| Tern (from Stencil) | One app for tabs, worktrees and the phone | current, plus his `tern-worktrees` plugin |

- Orca sat before Tern in the plugin list. Three `orca-*` extensions are still on disk.
- [INFERENCE] Tern runs on the workstation and the Android app reaches it. That is how the cold-open phone fix was done (`referensi-mesh-koordinator-mobile.md`, topic 8).

---

## 6. Model routing and the effort rule

### Key facts

- Roles live in `~/.omp/agent/config.yml` under `modelRoles`. A role is a named job with its own model and thinking level.

| Role | Model | Effort |
| --- | --- | --- |
| default | Opus 5.5 | low |
| plan, slow | Opus 5.5 | high |
| reviewer | Opus 5.5 | medium |
| task (subagent worker) | Sonnet 5.5 | medium |
| scout, sonic, fast | Haiku 5.5 | fast |
| advisor, designer | Sonnet 5.5 | high |

- Effort rule of thumb, confirmed by Zahid. Low for execution, because it is fast. High for plans and hard debugging. Medium for review. Max almost never, because it is slow and the gain is small.
- Fallback routing is config. A model can fall back to a backup on a second provider, and usage-aware fallback keeps a reserve on each Anthropic account so one quota wall does not stop a long run (`referensi-setup-dan-infra.md`, section 1).
- Effort level is not recorded per request in the stats, so the stats back the rule only with model speed. His October 2026 bench is the measured evidence. Raising effort raised the turn count in every head-to-head pair (`referensi-benchmark-lab.md`, section 3).

### Speed table (Anthropic, since 2026-10-01, average per request)

| Model | Role | Requests | Avg duration | Time to first token | Output tokens/s |
| --- | --- | --- | --- | --- | --- |
| Haiku 5.5 | subagent | 73k | 6.3 s | 1.4 s | 130 |
| Sonnet 5.5 | subagent | 53k | 6.1 s | 1.3 s | 95 |
| Opus 5.5 | main | 52k | 8.3 s | 2.6 s | 66 |
| Opus 5.5 | subagent | 35k | 6.9 s | 1.7 s | 72 |

- Other providers, all time: GLM 5.3 at 34 tokens/s, Codex 5.6 luna at 28 tokens/s, DeepSeek v4.1 flash through OpenCode Go at 91 tokens/s.

### Story/example

The setup spends thinking where it pays. The main chat plans at high effort and then hands work to Sonnet workers at medium and Haiku scouts. A review runs at medium on the strongest model. Routing changed about every two to four weeks over the autumn (config backups named by date and reason in `~/.omp/agent/`).

### Quotable

> Low for execution, high for plans and hard debugging, medium for review, max almost never. (Zahid's rule of thumb)

---

## 7. Cost, subscriptions and benchmarking

### Key facts

All prices are API-equivalent: the list price of the tokens. They are not money paid.

**All time (2026-03-07 to 2026-11-05, x1-dev)**

- 11,842 sessions, 833,553 model requests, 138B tokens.
- API-equivalent price $25.9k. Without prompt caching the same work would price at $158.7k.

**Per month**

| Month | Requests | Tokens | API-equivalent | Without cache | Cache-read share of tokens | Subagent share of requests | Project or worktree folders |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-03 | 36k | 2.8B | $1.0k | $4.3k | 85.2% | 45% | 21 |
| 2026-04 | 0.8k | 0.05B | $3 | $5 | 80.5% | 13% | 5 |
| 2026-05 | 2.2k | 0.2B | $59 | $245 | 94.8% | 17% | 9 |
| 2026-06 | 23k | 3.6B | $1.0k | $4.2k | 95.8% | 15% | 32 |
| 2026-07 | 46k | 7.8B | $2.2k | $9.8k | 96.5% | 28% | 56 |
| 2026-08 | 174k | 25.7B | $5.5k | $29.2k | 96.4% | 74% | 82 |
| 2026-09 | 235k | 50.2B | $6.6k | $32.1k | 96.7% | 53% | 132 |
| 2026-10 | 270k | 41.1B | $7.3k | $58.2k | 97.1% | 66% | 277 |
| 2026-11 (1 to 5) | 47k | 6.7B | $2.1k | $20.7k | 97.6% | 64% | 38 |

- Headline for the cost slide: October 2026 was 270k requests and 41B tokens, an API-equivalent price of $7.3k, and he paid about $200. That is roughly 36 times. 97% of tokens were cache reads. Two thirds of requests came from subagents. 277 project or worktree folders were active that month.
- The jump from 23k requests in June to 174k in August is the shift from one chat at a time to many agents at once.

**Subscriptions**

- Now: 2x Claude Max plus OpenCode Go, all his own. Spend is usually about $100 per month and is now about $200 because he needs to push a lot. Dollar numbers are fine to show.
- Before the Claude 5.5 series (September 2026 portfolio, `~/.omp/agent/managed-skills/omp-ops/references/zahid-ai-subscription-portfolio.md`, verified 2026-09-14). GLM Max was his own, a one-year plan bought cheap at the launch price. Codex Pro came from the office. Devin Pro and OpenCode Go were his own.
- Why back to Claude: quality. When the Claude 5.5 series arrived he went all in on Claude, because "Claude 5.5 series quality is GOAT".
- Anthropic-only in November so far. In October: anthropic 187k requests, muse-sub 37k, opencode-go 22k, muse-code 18k, commandcode 5k.

**Providers tried (all time, by requests)**

anthropic 240k, zai (GLM, his own Max plan) 224k, openai-codex (office Codex Pro) 128k, muse-sub 91k, opencode-go 59k, muse-code 18k, devin 10k, alibaba-coding-plan 9.6k, commandcode 9.3k, xiaomi-token-plan 9.0k, kimi-code 7.3k, github-copilot 5.7k.

- At least 12 providers tried. This is the benchmarking habit: he constantly tries new agents and models, and his prompt log holds benchmark and model-comparison sessions.


**Prewalk experiment**

- Definition, from the omp docs (`omp://prewalk.md`). Prewalk is a one-shot handoff from the active model to a faster or cheaper model after planning reaches implementation. An armed prewalk injects a planning nudge. A successful `todo` call opens the gate. At the first `edit` or `write` the session switches to the target (default the `@smol` role), prunes the planning instruction and steers with an implementation checklist. It is off by default. Flags are `--prewalk`, `--prewalk-into <model>` and `/prewalk`.
- Source of the idea. Can Bölük (omp author, Stencil), "You only need the frontier model for one single edit", 2026-07-13, https://stencil.so/blog/prewalk. Receipts and quotes are in `referensi-benchmark-lab.md`, section 6.
- Zahid's facts, from his prompts, first setup first. On 2026-10-14 he wrote "default will be opus low default prewalk will be into haiku high", so his first setup was Opus 5.5 low planning and a prewalk handoff into Haiku 5.5 high. On 2026-10-23 he wrote "the issue now task is taking too long to complete", then "disable the prewalk and go with sonnet medium for task". On 2026-11-07 he said it was cheaper for longer tasks but slower, and that he switched to Sonnet medium because he needed better UI work. There are no numbers for the Opus low into Haiku high setup, so "cheaper on long tasks" for it is his own account. Config now, `task` and `poteto-agent` run Sonnet 5.5 medium and `task.agentPrewalk` is off for both.
- Second try. On 2026-10-24 he turned prewalk on into Haiku 5.5 medium. On 2026-10-25 he moved the target to DeepSeek v4.1 flash for cost. It was really slow, so he turned prewalk off the same day. In his October bench, prewalk cost the same or more on short tasks (Sonnet 5.5 medium into Haiku 5.5 medium, UI task, $0.36 against $0.24 alone, 157 s against 94 s).
- The lesson: plan with the strong model and execute with the cheap one. On his long tasks it was cheaper but slower. A log estimate at 50 or more turns (about $2.58 against $1.63, not graded) points the same way on cost. On short tasks it costs the same or more, so test it on your own workload.

### Story/example

The stats show a lot produced for a small amount of money, and he says so himself. Prompt caching does much of the work: the same October workload would price at $58.2k without cache. The rest is routing, with cheap fast models for scouting and mid-tier models for workers.

### Quotable

> October 2026: 270k requests, 41B tokens, $7.3k API-equivalent, about $200 paid. (`omp stats`, 2026-11-05)

---

## 8. Memory journey, skills and autolearn

### Key facts

**Memory**

- First Mnemopi, then Hindsight. The data migration is dated 2026-06-28. The config backup that switched the backend is dated 2026-09-18 (`config.yml.bak-pre-hindsight-20260918`). Say "mid-2026" on a slide and keep both dates in notes only.
- Rollback was designed in. The old Mnemopi data stays untouched under `~/.omp/agent/memories/mnemopi/`, and flipping `memory.backend` back reverts.
- Cognee was tried in 2026-09 and destroyed on 2026-10-19.
- Retain triggers are session startup (watermark-gated), before compaction, and an explicit tool call. The payload is distilled conclusions.
- Tell this as a memory journey: three systems, one kept.

**Skills versus memory**

- His words: "Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project."
- Skills: reusable knowledge, written down, versioned in git, one folder per domain. He keeps 14 domain skills and a lint (`referensi-skills-prompt-dan-config.md`, topic 3b).
- Memory: what carries across projects without being written as a skill.

**Autolearn**

- Autolearn lets the agent mint skills from a session.
- Auto-on minted too many skills. He consolidated them into 14 domain skills plus a lint.
- Now he triggers autolearn manually, after a session that taught something.

**His skill rule**

> When you see you are doing the same work more than twice, it is a candidate for a skill, so the agent can do it for you.

### Story/example

Auto everything was the first mistake. The agent wrote a skill for every small thing, and the index grew past use. The consolidation fixed the count, and the lint keeps it fixed. The manual trigger puts the human back in the one place where judgment matters: was this lesson worth keeping?

### Show on screen

- The 14 domain skill names.
- The `principle-check-every-layer` skill, his own principle added to poteto.
- Three-row ladder: Mnemopi, Hindsight, Cognee (crossed out).

### Quotable

> Skills and references are for TIL and reusable knowledge, while memory is what you do cross-project. (Zahid, 2026-11-05)

---

## 9. Beads dropped

### Key facts

- Beads was an issue and dependency tracker for agent work. He dropped it.
- Reasons, his words in short: agents got smarter. Beads is not really human-readable. Agents now retain context better, thanks to omp's compaction (`snapcompact`, shake) and the memory layer.
- What replaced it: GitHub issues plus the coordinator's ledger files (the SHIP ledger is a TSV with 276 lines over about three days, `referensi-mesh-koordinator-mobile.md`, topic 7).

### Story/example

A tool that exists to make up for a weakness in the agent loses its job when the loop improves. Humans can read a GitHub issue and a TSV row. They could not read the beads store. The replacement is plainer and works.

