# Reference digest: instructions, prompting, skills, and omp config

Summary. Zahid runs coding agents through layered instructions. A short global file holds hard rules, small rule files fire always or on a regex, and each repo has a nearest-wins AGENTS.md with a size budget. He prompts in raw, typo-heavy lines and ends many with the word "poteto" to switch on the poteto-mode skill, which brings 25 principles and 23 playbooks. Domain knowledge sits in 14 managed area skills checked by a lint script. The omp config turns on Hindsight memory and autolearn, and turns off skill auto-injection and Claude skill discovery. Evidence snapshot date is 2026-11-05. Items under "Check before the talk" are known drift.

Where an item came from a note marked [INFERENCE] or [UNVERIFIED], the marker is kept. Where the notes conflict, the extra-facts note wins.

## Topic 2: how he organizes and prompts

### Key facts

- The global file has two sections. "Hard rules" bans Java and every JVM tool on the machine. "Multi-agent coordination (mesh)" tells each agent to run `mesh peers` before touching shared resources, post a `mesh note`, check ports with `ss -ltn`, and `claim` files outside its own worktree. Evidence `~/.omp/agent/AGENTS.md`.
- Always-on rule files live in `~/.omp/agent/rules/`. Each has frontmatter with `alwaysApply` and an `agents:` list.
  - `check-every-layer.md` is `alwaysApply: true` for agents `main`, `reviewer`, `task`. It points at `skill://principle-check-every-layer`.
  - `managed-skill-layout.md` targets `main`. A lesson goes into the matching area skill, not into a new skill.
  - `pr-body.md` targets `main` and `task`. PR text follows `pr-body-shape` and wins over poteto's own shape.
- Two rules are regex-triggered. `pytest-resource-cap.md` and `test-runner-resource-cap.md` carry a `condition:` regex on the command or text. When it matches, the harness interrupts and injects a memory cap. Evidence `~/.omp/agent/rules/pytest-resource-cap.md`, `~/.omp/agent/rules/test-runner-resource-cap.md`.
- The cap rules exist because an uncapped full-suite pytest reached 38 GB resident memory on the shared x1-dev box and thrashed swap. The rule says to wrap pytest in `systemd-run --user --scope -p MemoryMax=8G`, pass `--maxWorkers=2` to jest and vitest, and check `free -h` first (wait if under 15 GB available). Evidence `local://talk-extra-facts.md`, section "Rules that fired live during this research".
- Those two rules fired live while the research for this talk ran. The research text only mentioned the rule file names, and the regex matched. [Observed in this session: the same interrupts fired again while this digest was prepared. No tests were run.]
- Repo-level AGENTS.md files exist in about 17 `~/work/labs/*` repos, in the Nimbly, Alkhidmah, MAS and portier work folders, and in a thesis repo. Evidence `~/work/nimbly/AGENTS.md`, `~/work/alkhidmah/main_digital-platform/AGENTS.md`.
- Nearest file wins. The Alkhidmah root file says so in one line, and carries a router table that maps a task to the file to open. It has 19 rules and 4 traps, with nested `db/AGENTS.md` and `auth/AGENTS.md`.
- The size budget is enforced by a check. A coordinator message reported one nested file at 4218 bytes against a 4096 budget. A `bun run docs:agents` run reported "14 nested files fit their budgets." Evidence `~/.omp/agent/mesh/feed.jsonl` (entry dated 2026-10-28).
- Subagent briefs follow one shape. The opening line is "Complete assignment thoroughly:", then `# Target`, `# Change`, and `# Contract` (or `# Output`). A brief names the file to write, the facts that must appear, and what not to leak. Evidence a `DomainResearch.jsonl` session file for the GinaV2 agentic-reasoning worktree, user message at line 9.
- The poteto-mode skill is autoloaded by an extension once per context lifetime. It skips subagents and plan or vibe modes. Off switch is the file `~/.omp/agent/poteto-mode.off`. Evidence `~/work/labs/omp-skills/SYNC.md`, section "OMP adaptation rules".
- Prompts paste raw context. Seen in prompt history are WhatsApp threads, HAR dumps, screenshots, Excalidraw JSON, and spreadsheets. Evidence `local://talk-extra-facts.md`.
- Voice input is on. The config has `stt` enabled with `submitTrigger: say-submit`, and a mic icon is visible in the phone screenshot of the mobile fix. Evidence live `~/.omp/agent/config.yml`.
- `/handoff` is a user-level skill (`~/.omp/agent/skills/handoff`). It appears in a real prompt as "/handoff i will be doing all the testing on staging".

### Story/example

On 2026-10-26 Zahid pasted a QA engineer's WhatsApp report straight into a fresh session and wrote one line. It told the agent to do the fix, then ssh to groundup-dev, start the stack there, and capture screenshots or a recording so the PR body carries proof. The line ended with "own all the changes poteto". No spec, no ticket. The next morning, from his phone, he pasted a second finding with "Fix those own changes proof and update pr", and the agent recorded a before video, applied the fix, recorded an after video, and updated the PR body. The brief shape (Target, Change, Contract) shows up one level down, when the main agent hands research to subagents. His own prompts stay loose. The structure lives in the rules and skills that load around them.

### Show on screen

- `cat ~/.omp/agent/AGENTS.md` for the Java ban and the mesh block.
- `ls ~/.omp/agent/rules/` then `cat ~/.omp/agent/rules/check-every-layer.md`.
- `head -40 ~/work/alkhidmah/main_digital-platform/AGENTS.md` for the router table and nearest-wins line.
- `cat ~/.omp/agent/rules/pytest-resource-cap.md` to show the `condition:` frontmatter (read only, do not trigger it with a real test run on stage).
- A redacted prompt-history excerpt with the typo lines below.

### Quotable

Real prompts, typos kept. Dates are from the extra-facts note.

```
dry run first then show me what will be changed
```
```
go stack and ship all include proof also in pr
```
```
creare new workgtree and trace teh impacted and related flow tehn fix, and then open a pr also include proof there and coordiate with SHIP
```
```
i will follow all your recommendations now implement those and open pr then while waiting pr ci you can ask codex review to review your implementations poteto
```
```
We wont deploy staging aji will pull and test on pr
```

The tester's first name appears in the last prompt. Replace it with "QA" on a slide if you prefer.

Rule text.

```
NEVER run Java or any JVM tool (java, TLC/tla2tools, jar files, gradle, maven, etc.). Java is banned on this machine.
```
```
The **nearest** `AGENTS.md` wins, and nested files carry only their own scope.
```

## Topic 3a: poteto-mode, pstack, and the principles

### Key facts

- poteto-mode is the "agent style" skill. Its description reads "poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work." It is marked `disable-model-invocation: true`, so only the user or the extension loads it. Evidence `~/.agents/skills/poteto-mode/SKILL.md`.
- Origin and license. It is the pstack plugin by poteto, from the `cursor/plugins/pstack` upstream, MIT licensed. The README bio says he worked on large codebases at Meta, Netflix, and Cursor and is on the React core team. Evidence `~/work/labs/omp-skills/pstack/README.md`, section "license".
- Zahid keeps a fork in `~/work/labs/omp-skills`. The repo holds `pstack/`, `matt/` (forks of 18 skills from another upstream), `local/skills/`, `omp/extensions/poteto-mode.ts`, and `scripts/`. Evidence `~/work/labs/omp-skills/SYNC.md`.
- Branch rule. `upstream/<source>` branches hold upstream files exactly and are never edited by hand. `main` holds the OMP adaptation. The reflog shows a merge of `upstream/pstack` at commit 88d4751. Evidence `~/work/labs/omp-skills/SYNC.md`.
- Live skills are symlinks into this checkout, installed by `scripts/link.sh`. Evidence `~/work/labs/omp-skills/scripts/link.sh`.
- Adaptation choices recorded in the reflog. Cursor's `explore` maps to `scout`, `generalPurpose` maps to `task`, and the `poteto-agent` delegate is pinned to the `task` model. Evidence reflog subjects, `.git/logs/HEAD`.
- The index has 25 principles. 11 Core, 6 Architecture, 5 Verification, 2 Delegation, 1 Meta. Examples are Laziness Protocol, Model the Domain, Prove It Works, Fix Root Causes, Guard the Context Window, and Never Block on the Human. Evidence `~/.agents/skills/poteto-mode/SKILL.md`, section "Principles".
- One principle is his. `principle-check-every-layer` is "ours, not upstream" per SYNC.md. It asks for findings on three layers (Product/UX, Structure, Data/Flow) or a one-line reason a layer does not apply. A rule file loads it on every main, reviewer, and task turn. Evidence `~/work/labs/omp-skills/pstack/skills/principle-check-every-layer/SKILL.md`.
- The skill demands a visible effect. "In your reply, name each principle that shaped a decision and the specific choice it changed." Evidence poteto-mode `SKILL.md`, "Non-negotiables".
- 23 playbooks sit in `~/.agents/skills/poteto-mode/playbooks/`. They are authoring-a-skill, autonomous-run, autopilot-full, autopilot-stack, babysit, bug-fix, eval, feature, hillclimb, investigation, multi-phase-plan, opening-a-pr, orchestrate, pause-safely, perf-issue, prototype, refactoring, runtime-forensics, session-pickup, shipping, trace-forensics, visual-parity, worktree-cleanup.
- Support files. `references/bugbot-triage.md` and `scripts/` (`worktree-audit.sh`, `watch-pr`, `orch`).
- Related skills in the same family. `pstack-omp` maps pstack roles to OMP task agents. `setup-pstack` writes per-role model choices to `~/.omp/agent/pstack-models.md`. `show-me-your-work` writes a TSV decision log with one row per decision. Evidence `~/.agents/skills/`.
- Delegation defaults in the skill. Subagents get file pointers, not inlined context. Code delegates tier by difficulty. The parent owns every result and reviews the diff itself. A fresh subagent takes each new round, not a resumed one.
- Live config pins `poteto-agent` and `task` to a mid-tier model at medium effort, and `scout` and `sonic` to the fast model. Evidence live `~/.omp/agent/config.yml`, key `task.agentModelOverrides`.
- The skill's reply rules are written for prose. Short declarative sentences, no long dashes, no mid-sentence colons. The talk can point out that the same rules guided this digest through the `unslop` skill.

### Story/example

The main chat acts as a playbook runner and the work goes to delegates. On 2026-11-02 the SHIP session in the Alkhidmah repo was told to "coordinate MAKTAB and SCOPE so they ship PR properly". The coordinator kept a 276-line TSV ledger with columns ts, phase, decision, why, evidence, result, which is the show-me-your-work format. One row says it started fresh owners for a PR "because their sessions had ended and never saw the broadcast", with the reason "idle sessions don't wake on mesh messages; each branch needs one writer". That is the fresh-subagent rule from poteto-mode, observed in a real run.

### Show on screen

- `sed -n 1,40p ~/.agents/skills/poteto-mode/SKILL.md` for the trigger list.
- `ls ~/.agents/skills/poteto-mode/playbooks` (23 files).
- `ls -d ~/.agents/skills/principle-*` and count (expect 25; run the count before the talk).
- `cat ~/work/labs/omp-skills/SYNC.md` for the upstream branch rule and install map.
- `cat ~/work/labs/omp-skills/pstack/skills/principle-check-every-layer/SKILL.md`.
- `cat ~/.omp/agent/rules/check-every-layer.md`.
- `head -5 ~/work/alkhidmah/coord/2026-11-03-ship.tsv` (ledger, columns only, check rows for customer data first).

### Quotable

```
The Principles section below grounds every trigger. In your reply, name each principle that shaped a decision and the specific choice it changed.
```
```
fork it. improve it. make it yours. PRs are welcome!
```
```
idle sessions don't wake on mesh messages; each branch needs one writer
```

## Topic 3b: area skills per domain, and the lint

### Key facts

- Skills load from three roots. `~/.omp/agent/managed-skills/` holds the 14 area skills. `~/.agents/skills/` holds the poteto family and shared skills. `~/work/labs/omp-skills/` is the git source of truth for poteto, pstack, and matt skills. Evidence `~/work/labs/omp-skills/SYNC.md`.
- The 14 area skills are `alkhidmah-ops`, `alumni-ops`, `astronvim-ops`, `career-ops`, `comms-ops`, `eng-toolkit`, `git-pr-workflow`, `groundup-ops`, `infra-ops`, `nimbly-ops`, `omp-ops`, `thesis-ops`, `warga-ai`, `worktree-herdr`. Evidence `~/.omp/agent/managed-skills/`.
- The pattern is one folder per domain, not per task. `SKILL.md` is a router only. `playbooks/<topic>.md` is a step list to follow. `references/<topic>.md` is facts to look up. The infra-ops router says "Playbooks are step lists to follow. References are facts to look up." Evidence `~/.omp/agent/managed-skills/infra-ops/SKILL.md`.
- Every file must be routed from `SKILL.md` by one line shaped like `- [topic](playbooks/topic.md) — what it covers`.
- Hard rules and `scripts/` change behavior, so the layout rule says to propose them, not add them unasked. Evidence `~/.omp/agent/rules/managed-skill-layout.md`.
- Why one skill per domain. The rule file says a lesson goes into the matching area skill, and a new area needs the user's agreement. [INFERENCE] The split keeps unrelated work (a Dokploy deploy, a WhatsApp template, a thesis cluster) out of each other's context, and each router stays short. A task reads one router, then one playbook or reference.
- His stated preference is in a reference file. "Zahid prefers one skill with nested `references/*.md` files over multiple flat sibling skills when building skill pipelines." He rejected a flat layout on 2026-09-17. Evidence `~/.omp/agent/managed-skills/omp-ops/references/zahid-skill-structure-preference.md`.
- Sizes vary a lot. `infra-ops` has about 40 playbooks and about 30 references. `git-pr-workflow` has about 40 playbooks. `nimbly-ops` has none. [UNVERIFIED] These counts came from glob listings that were capped, and the notes say to re-run `grep -c` per skill before putting numbers on a slide.
- Lint script `~/work/labs/omp-skills/scripts/skills_lint.py`, run with `uv run skills_lint.py [skill-dir ...]`. Default target is every non-hidden folder in `~/.omp/agent/managed-skills`. It exits 1 on errors.
- Checks, each an error unless noted.
  1. `SKILL.md` exists.
  2. Frontmatter parses, `name` equals the folder name and is kebab-case.
  3. `description` is present and at most 1024 characters.
  4. No extra frontmatter keys beyond `name` and `description`, because "omp drops them on update".
  5. `SKILL.md` is at most 500 lines.
  6. Root entries are limited to `SKILL.md`, `playbooks`, `references`, `scripts`, `assets`, `evals`.
  7. No directories nested below the first level.
  8. Every file is linked from `SKILL.md`.
  9. Every path mentioned in `SKILL.md` exists. The same check covers `playbooks/` and `references/` paths mentioned inside other `.md` files.
  10. Warning only. A reference over 100 lines with no Contents heading.
- Pre-commit hook. `~/.omp/agent/managed-skills/.pre-commit-config.yaml` runs the lint as a local hook named `skills-lint`.
- The lint has not been run for this digest. Run it before the talk and keep the output.

### Story/example

The lint exists because skills grow without anyone noticing. A playbook of omp-ops says autolearn "mints continuously" and the skill index "regrows past ~15", so a human cannot keep the layout tidy by hand. The rule file ends with a command. "Afterwards run `uv run -q ~/work/labs/omp-skills/scripts/skills_lint.py` and fix every error." That is the Encode Lessons in Structure principle in practice, since the layout rule became a script and a hook instead of a longer instruction. [INFERENCE] The principle link is mine. The notes do not say he chose it for that reason.

### Show on screen

- `ls ~/.omp/agent/managed-skills/` (14 folders).
- `head -40 ~/.omp/agent/managed-skills/infra-ops/SKILL.md`.
- `ls ~/.omp/agent/managed-skills/infra-ops/playbooks | head` then the same for `references`.
- `cat ~/.omp/agent/rules/managed-skill-layout.md`.
- `cat ~/.omp/agent/managed-skills/.pre-commit-config.yaml`.
- `uv run -q ~/work/labs/omp-skills/scripts/skills_lint.py` (live, after a dry check).

### Quotable

```
Playbooks are step lists to follow. References are facts to look up.
```
```
Put it in the matching area skill. Use `manage_skill create` only for a genuinely new area, and only after the user agrees.
```
```
if (n := text.count("\n")) > 500: errors.append(f"{skill.name}: SKILL.md has {n} lines (max 500)")
```
```
errors.append(f"{skill.name}: extra frontmatter {...} (omp drops them on update)")
```
```
Zahid prefers one skill with nested `references/*.md` files over multiple flat sibling skills
```

## Topic 3c: omp config for memory, autolearn, autoskills, and skill discovery

### Key facts: memory with Hindsight

- Live config sets `memory.backend: hindsight` and `memories.enabled: true`. The Hindsight block uses `retainMode: last-turn`, `retainEveryNTurns: 10`, `retainOverlapTurns: 2`. Evidence live `~/.omp/agent/config.yml`. The API token key exists in that block. Never show its value.
- The service runs as a Docker image of Hindsight 0.8.3 on a local port. Its extraction model is a GLM model reached through an OpenAI-style endpoint. Evidence `~/.omp/agent/managed-skills/omp-ops/playbooks/omp-hindsight-memory-backend.md`.
- Migration from the old Mnemopi backend. 249 items retained from 5,633 raw rows (4.4 percent pass rate), 945 memory units, 0 failures, about 8 minutes. Evidence the same playbook, which is dated 2026-06-28.
- Rollback is one flip. The old data stays untouched under `~/.omp/agent/memories/mnemopi/`, so setting `memory.backend: mnemopi` reverts.
- Retain triggers, from the retain-triggers reference. Session startup (watermark-gated), before compaction, and an explicit tool call. The payload is distilled conclusions only, from assistant text blocks. Evidence `~/.omp/agent/managed-skills/omp-ops/references/omp-memory-retain-triggers.md`.
- Cost reasoning. "Per-run auto-retain is the most expensive option. Each retain runs an LLM structured-output extraction per chunk." Retaining every 10 turns is the budget version.
- Config backup tagged `config.yml.bak-pre-hindsight-20260918` records the switch date in the filename. Evidence `~/.omp/agent/`.
- This talk's own session context contains recalled memories from earlier sessions, which makes a good live demo of the backend.

### Key facts: autolearn

- Live config sets `autolearn: { enabled: true, autoContinue: false }`. Autolearn mints skills from sessions. `autoContinue: false` means it does not chain into further work by itself. The older dotfiles copy has `autoContinue: true`. Evidence live and dotfiles `config.yml`.
- A `auto-capture-triage.md` reference decides which session output is worth capturing. Evidence `~/.omp/agent/managed-skills/omp-ops/references/`.
- The consolidation playbook classifies a minted skill by name prefix, not by session folder, because autolearn mints skills from meta-sessions where the working folder is misleading. Evidence `~/.omp/agent/managed-skills/omp-ops/playbooks/omp-skill-consolidate-domain-scope.md`.

### Key facts: autoskills injection is off

- The evidence has three parts. The extension file is renamed to `autoskills.ts.disabled`. A kill-switch file `~/.omp/agent/autoskills.off` exists. `autoskills.json` has `maxSkills: 1`, empty `always`, empty `keywords`, empty `perCwd`, so even if enabled it has no triggers. Evidence `~/.omp/agent/extensions/`, `~/.omp/agent/autoskills.json`.
- [INFERENCE] The talk point is "I tried auto-selected skills, then turned them off in favor of explicit routing through router skills and the poteto keyword". The notes say to confirm this with Zahid. The reasoning is not written in any file that was read.

### Key facts: Claude skill discovery is disabled

- Live `skills:` has `enableAgentsUser: true`, `enableClaudeUser: false`, `enableClaudeProject: false`. Commands have the same two Claude flags set to false. Evidence `~/.omp/agent/managed-skills/omp-ops/references/omp-skill-source-binding.md`, fix dated 2026-08-31.
- Reason. Claude Code's discovery has priority 80 and the `.agents` directory has priority 70. With a same-named skill, the Claude copy wins. Turning Claude discovery off makes `~/.agents/skills` the source of truth.
- A backup named `config.yml.bak-disable-claude-skills` is the matching snapshot.

### Story/example

Every config change gets a dated backup before the edit. The folder `~/.omp/agent/` reads like a log. `config.yml.bak-pre-glm-flash-20260826`, `config.yml.bak-pre-hindsight-20260918`, `config.yml.bak-pre-2rail-20261004`, `config.yml.bak-pre-cc-deepseek-20261025`. The notes read this as model routing changing every two to four weeks, with the memory backend moving on 2026-09-18 and skill discovery moving off Claude around 2026-08-31. The skill-source fix has a concrete cause. Two skills with the same name loaded from two places, and the wrong one won.

### Show on screen

- `ls ~/.omp/agent/ | grep bak` for the dated backups.
- The `memory` and `hindsight` block of `~/.omp/agent/config.yml`, with the token line masked or cropped out. Do not `cat` the whole file.
- `cat ~/.omp/agent/autoskills.json`, `ls ~/.omp/agent/autoskills.off`, `ls ~/.omp/agent/extensions/`.
- The `skills:` block of the live config.
- `~/.omp/agent/managed-skills/omp-ops/references/omp-skill-source-binding.md`.
- `~/.omp/agent/managed-skills/omp-ops/references/omp-memory-retain-triggers.md` (triggers table).

### Quotable

```
memory:
  backend: hindsight
hindsight:
  retainMode: last-turn
  retainEveryNTurns: 10
  retainOverlapTurns: 2
```
```
Per-run auto-retain is the most expensive option. Each retain runs an LLM structured-output extraction per chunk.
```
```
Claude Code is 80; Agent Dirs (`.agents`) is 70. Same skill name: Claude wins.
```
```
autolearn: { enabled: true, autoContinue: false }
```

## Check before the talk

These are drift items found while researching. Resolve each before showing it on stage.

- Domain-skill parking playbook is stale. `omp-skill-consolidate-domain-scope.md` describes a 2026-09-13 layout with 7 global skills in `managed-skills/`, 8 domain skills parked in `managed-skills-disabled/`, and a `domain-skills.ts` extension that surfaces them by working folder. Today all 14 domain skills sit in `managed-skills/`, `domain-skills.ts` is not in `extensions/`, and `managed-skills-disabled/` holds only seven `luvus-*` folders. [INFERENCE] Either the parking was undone or the playbook is stale. Do not describe the parking mechanism as working. Describe the current layout.
- `bankId` is missing from the live Hindsight block. The setup playbook calls `bankId: omp` required, because omp otherwise names the memory bank after the working folder basename. The older dotfiles copy sets `bankId: omp`, `scoping: global`, and `mentalModelAutoSeed: true`. Check whether memory is really shared across projects before saying so.
- Date mismatch on the Hindsight migration. The playbook is dated 2026-06-28, while the pre-Hindsight config backup is dated 2026-09-18. Confirm which date to quote.
- Live and dotfiles `config.yml` differ. The omp-ops playbook says the live file is a symlink to the dotfiles copy. The two files now differ, so [INFERENCE] the symlink was replaced. Verify before showing any dotfiles diff as "the same file".
- Plaintext token. The Hindsight API token is stored as a plain value in the live config and in the version-controlled dotfiles copy (a private repo). Treat it as a rotation item. Crop it out of every screen.
- Prompt history keeps pasted secrets. A client-integration credential was pasted into a prompt on 2026-11-05, and secret obfuscation does not cover local history. This is a talk point and a rotation item. Do not show the history file.
- PR rules disagree on drafts. `opening-a-pr.md` says to open every PR ready. `pr-body-shape.md` says GinaV2 PRs open as drafts. The `pr-body` rule routes to the second. Pick the GinaV2 rule if the slide covers it.
- Autoskills reasoning is [INFERENCE]. Ask Zahid why it is off before stating a reason.
- Skill counts are partial. Router-entry and playbook counts came from capped globs. Re-run `grep -c` per skill and `ls -d ~/.agents/skills/principle-* | wc -l` before slides carry numbers. The reflog count of 14 commits for `omp-skills` is also [INFERENCE] until `git log --oneline | wc -l` is run.
- `skills_lint.py` has not been run. Run it and capture the summary line.
- `jam-proof` was not found under `~/.agents/skills` or `managed-skills`, though it is installed as a skill. It sits under `~/.omp/agent/skills/`, so the PR-proof step works, but check the path before showing it.
- The `domain-skills.off` kill switch named in the stale playbook does not exist. Skip it on stage.
