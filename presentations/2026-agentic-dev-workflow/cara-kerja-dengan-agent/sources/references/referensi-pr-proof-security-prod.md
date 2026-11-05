# Reference digest: PR standard and proof, secrets and security, AI in production

Summary. Three topics from Zahid's omp setup. Every PR body is a one-minute briefing with proof beside each claim, and it ends with an honest "Not verified:" list. Secrets are handled by layers (placeholder obfuscation, damage-control rules, a secret manager), and he says openly that obfuscation is not secret management. Production work is read-only by default, and every write follows dry run, backup, guarded apply, verify.
Evidence comes from research notes taken on 2026-11-05. Paths starting with `MS/` mean `~/.omp/agent/managed-skills/`. Markers [INFERENCE] and [UNVERIFIED] are kept from the source notes. No secret values appear in this file.

---

## 1. PR standard and proof

### Key facts

- **One template for every repo.** The sections, in order, are Why, How, What changed, Scope, Tradeoffs, Blast Radius, Verification, then a `Ticket:` line. `MS/git-pr-workflow/references/pr-body-shape.md`
- **The body is a briefing.** It is written for a reviewer who already has the diff and has one minute. It says why the change exists, how a person sees or runs it, what it leaves out, what it could break, and the proof. `pr-body-shape.md`
- **Title rule.** `type(scope): imperative subject`, at most 72 characters, no trailing period. `pr-body-shape.md`
- **Section rules.** `pr-body-shape.md`
  - Why is 1 to 3 sentences and is the summary.
  - How describes what a person does and sees. With two or more actors it uses a mermaid diagram plus bullets. With one straight line it is one sentence. If nothing is user-visible, it says so and names the proving command.
  - What changed has 1 to 5 bullets and ends with a reading order.
  - Scope has 1 to 3 items covering what is in and what is left out.
  - Tradeoffs is optional and only appears when a real choice existed.
  - Blast Radius is 1 to 2 sentences and ends with the rollback command.
  - Verification has one bullet per claim, proof inline, and ends with `Not verified:` plus the list, or `Not verified: none`.
- **Length budget.** The text above the first `<details>` block is about 40 lines, because it becomes the squash commit. One `<details>` at the end holds CVE tables, full verification and extra tradeoffs. `pr-body-shape.md`
- **A runnable check for the budget.** `gh pr view <N> --json body --jq '.body | split("<details>")[0] | split("\n") | length'` should print about 40. `pr-body-shape.md`
- **Proof ladder.** Take the first rung that shows the claim. `pr-body-shape.md`
  1. UI or visible behavior: a recording. For a bug fix, before and after.
  2. API or CLI: the command and its real output, or a run link.
  3. CI or infra: the Actions run link and the one output line that carries the claim.
  4. Nothing visible: the test command and its result.
- **Jam for GroundUp repos.** In `groundup-ai/*` repos he records a Jam per `skill://jam-proof`. In other repos he uses a screenshot or video uploaded per `skill://gh-attach`. `pr-body-shape.md`. Where jam-proof is installed is [INFERENCE]; check before the demo.
- **Honesty rule.** "Every proof link is one you produced or opened this session." `pr-body-shape.md`
- **The rule file that binds it.** `~/.omp/agent/rules/pr-body.md` tells the main agent and task agents that PR text follows `pr-body-shape` and beats poteto's own description shape.
- **No literal `poteto validate` command exists.** The notes searched the poteto-mode tree, git-pr-workflow, omp-skills and the omp agent dir and found none. The only "validate" is a manual step in `~/.agents/skills/poteto-mode/playbooks/authoring-a-skill.md`. Proof comes from poteto-mode's "Prove It Works" principle (verify against the real artifact, not "it compiles") plus the PR shape above. Do not say "I run poteto validate" on stage.
- **Alkhidmah has its own proof gate.** `~/work/alkhidmah/main_digital-platform/AGENTS.md` says a user-facing change needs a proof written under `.agents/skills/verify-alkhidmah/`, driven red before the change and green after. The agent must obtain a PROVEN verdict (or GREEN ONLY with a reason) from `verify.ts verdict` at desktop and 390px width, with zero console errors.
- **The same vocabulary shows up in the coordinator's reports.** `~/work/alkhidmah/coord/2026-11-05-review-580.md` freezes a verdict at one commit: `verify.ts verdict` PROVEN, red run on master, green on head, desktop 1280 and mobile 390, then a gates table (merge-tree clean, check-types, unit and e2e counts on a throwaway database removed afterward).
- **Drift to admit (draft vs ready).** `~/.agents/skills/poteto-mode/playbooks/opening-a-pr.md` says "Open every PR ready, never as a draft." `pr-body-shape.md` says that for GinaV2, PRs open as drafts and the body ends with `Ticket:`. Because `rules/pr-body.md` routes to pr-body-shape, the GinaV2 draft rule wins in that repo.
- **More drift.** `MS/git-pr-workflow/playbooks/pr-description-from-diff.md` and the poteto opening-a-pr playbook list six sections with no How section. They are older and defer to pr-body-shape. Older GinaV2 bodies (#574, #609) use `Problem`, `Reviewer focus` and `Known tradeoffs` instead of the strict order.
- **No `## Proof` heading exists anywhere.** Proof lives inside each Verification bullet. The notes found no GinaV2 PR by him with a literal Proof heading.

### Story/example

PR #804 in `groundup-ai/GinaV2` came from a QA message pasted into a session on 2026-10-26, with the instruction to test on the shared dev box so the PR could carry proof screenshots or recordings. The body has a Why with six numbered issues, and Verification gives a before and after table with videos for each one. The agent reproduced each issue on the base first, then checked it on the branch, with the same recording method. The next morning QA posted one low-priority finding on the PR, a draft sensor opening the edit modal on click. From a phone, Zahid pasted it and asked the agent to fix it, prove it and update the PR. In about four minutes the agent committed the fix, recorded a "before" video on the dev stack, applied the fix, recorded "after", uploaded both and edited the body. QA marked the finding resolved 65 minutes after posting it. The PR carries the label "Tested - Pass". `local://talk-extra-facts.md` section on #804.

PR #760 is the cleanest example of the shape. Its title is "feat(deploy): build, vulnerability scan images in CI and deploy them by digest". How is a mermaid diagram plus bullets. Verification cites a staging deploy run by link and says the first scan found 16 CRITICAL findings in three packages, all fixed. It ends with a Not verified list that names an auth deploy on staging and a password-reset email with the mounted template. The `<details>` block says CI built, scanned and pushed all nine images in 6 minutes, down from 38.

### Show on screen

- `cat ~/.omp/agent/managed-skills/git-pr-workflow/references/pr-body-shape.md` (the template and the proof ladder).
- `cat ~/.omp/agent/rules/pr-body.md` (the rule that routes to it).
- `gh pr view 760 --repo groundup-ai/GinaV2 --json body --jq '.body'` (read-only, live body with mermaid).
- `gh pr view 760 --repo groundup-ai/GinaV2 --json body --jq '.body | split("<details>")[0] | split("\n") | length'` (the 40-line check).
- https://github.com/groundup-ai/GinaV2/pull/804 (before and after per issue) and https://github.com/groundup-ai/GinaV2/pull/760 (How diagram, run links).
- `~/work/alkhidmah/coord/2026-11-05-review-580.md` gates table. Check it for customer data before showing.
- Side by side, the draft-vs-ready conflict: `grep -n "draft" ~/.agents/skills/poteto-mode/playbooks/opening-a-pr.md` and the same grep on `pr-body-shape.md`.

### Quotable

> A PR body is a **briefing**: one minute for a reviewer who already has the diff.

> Proof sits beside the claim it proves. Take the first rung that shows the claim.

> Verification ... Ends with `Not verified:` and the list, or `Not verified: none`.

> **Live proof backs a user-facing change.** ... drive it red before the change and green after ... PROVEN ... at desktop and 390px with zero console errors.

> "Not verified: an auth deploy on staging, and a password-reset email with the mounted template." (PR #760)

> go stack and ship all include proof also in pr (real prompt, 2026-11-05)

---

## 2. Secrets and security

### Key facts

- **Obfuscation is switched on.** The live config has `secrets: { enabled: true }`. A key file sits at `~/.omp/agent/secret-placeholder.key`. The notes did not read it, and it should stay off screen. `~/.omp/agent/config.yml`
- **What the model sees.** Tool output carries opaque tokens shaped `$$HASH$$` or `$$HASH:CASE$$`. The system rule is to copy them byte for byte. [INFERENCE] The real value is swapped in at tool execution and the model only sees the placeholder. The notes say to confirm with Zahid how the key file is used before claiming this on stage.
- **Example of the placeholder form.** `~/.omp/agent/managed-skills/omp-ops/playbooks/reset-amp-cliapi-proxy-integration.md` line 16 shows a stored key as a `$$...$$` token. Show only that line, never the secrets file it describes.
- **Damage-control rules.** `~/dotfiles/omp/agent/damage-control-rules.yaml` is version controlled and declares four lists.
  - Blocked bash patterns include `rm -r/-rf`, `git reset --hard`, `git clean -fd`, `git push --force` (not `--force-with-lease`, which asks), `DROP TABLE|DATABASE`, `TRUNCATE`, `chmod 777`, `eas update --force` and `eas build --clear-cache`.
  - `zeroAccessPaths` is `~/.ssh/`.
  - `readOnlyPaths` are `.env`, `.env.local`, `.env.production`, `.npmrc`, `google-services.json` and `GoogleService-Info.plist`.
  - `noDeletePaths` are `.git/` and `node_modules/`.
- **Enforcement caveat.** The notes found the rules file but not the loader that enforces it. [INFERENCE] The switches to point at are `security: { enabled: true }` and `bashInterceptor: { enabled: true }` in the live config.
- **Credential-path redaction in an extension.** `~/.omp/agent/extensions/orca-agent-status.ts` lines 413 to 416 (`statusInputReferencesCredentialPath()`) refuse status payloads that mention `.ssh`, `.ssh-mcp`, `.mcp-secrets.env` or the omp backup keyfile path. Lines 423 to 463 (`sanitizeStatusToolInput()`) deep-copy tool input under limits (4096 nodes, 262144 chars, depth 64). A violation returns `{ redacted: true }`.
- **Two secret managers by the hard rule.** `MS/infra-ops/SKILL.md` Hard rules say "Secrets from Infisical (machines) or Bitwarden (humans). Never print them." A self-hosted Infisical stack lives in `~/dotfiles/dev-server/infisical/` (compose with backend, redis, db and a tunnel, a backup script with 14-day retention, a watchdog). Values were not read.
- **Per-worktree `.env` handling.** `tern-wt create` with `worktree.clone` copies ignored files such as `.env` into a new worktree. Damage control marks `.env*` read-only. GinaV2 checkouts symlink `.env` to one shared file, so a backup comes before any edit. `MS/groundup-ops/references/ginav2-tailnet-dev-stack.md`
- **Rules about output.** Playbooks say "Redact API keys in user-visible output" (`verify-premzone-pricing.md` line 64) and "Redact keys when displaying" (`wire-vscode-byok-reseller-into-omp.md` line 26).
- **His own framing.** On 2026-10-21 he wrote "go enable those obfuscate secrets", then, while evaluating a credential manager, "omp just doing obfuscation but not manage secrets". `local://talk-extra-facts.md`, prompting style section.
- **Finding 1, to rotate.** Prompt history contains a pasted client secret for a client-integration project (2026-11-05). Obfuscation does not cover what already sits in local history. Talk point plus a rotation item. No value is recorded.
- **Finding 2, to move or rotate.** The memory backend token is a plain value in the live omp config and in the git-tracked dotfiles copy of it. The dotfiles repo is private. A literal tenant token also appears in a memory-setup playbook. Action is to move it into the secret manager and rotate it. No value is recorded.
- **Other credentials at rest.** The omp agent DB has an `auth_credentials` table (19 rows, not read). Provider API keys are exported in the shell env file as variables, and the notes recorded names only.
- **Browser relay is on.** The live config has `browser: { headless: true, relay: true }`. Confirm what that exposes before showing it.

### Story/example

On 2026-10-21 he turned on omp's secret obfuscation, and the same day he wrote that omp "just doing obfuscation but not manage secrets". Two weeks later the research for this talk found exactly the gap that sentence predicts. Obfuscation hides values from the model in tool output. It does not clean the local prompt history where he once pasted a client secret, and it does not move a plain-text memory token out of a config file that is also tracked in a private dotfiles repo. Both became rotation items instead of slides with values. The fix path is the rule already in infra-ops, machines get Infisical and humans get Bitwarden.

### Show on screen

- `~/dotfiles/omp/agent/damage-control-rules.yaml` (whole file, safe).
- `~/.omp/agent/extensions/orca-agent-status.ts:413-463` (redaction guard).
- `grep -n "secrets" ~/.omp/agent/config.yml` (shows `enabled: true` only). Do not open the whole file, because the memory token is in it.
- `~/.omp/agent/managed-skills/omp-ops/playbooks/reset-amp-cliapi-proxy-integration.md:16` (the `$$...$$` form).
- `~/.omp/agent/managed-skills/infra-ops/SKILL.md` lines 8 to 16 (Hard rules).
- `~/dotfiles/dev-server/infisical/docker-compose.yml`, service names only.
- Never show `secret-placeholder.key`, `~/.config/tern/` files, `agent.db`, or prompt history.

### Quotable

> Secrets come from Infisical (machines) or Bitwarden (humans). Never print them.

> omp just doing obfuscation but not manage secrets (his prompt, 2026-10-21)

> zeroAccessPaths: ["~/.ssh/"]

> readOnlyPaths: [".env", ".env.local", ".env.production", ".npmrc", ...]

> Redact API keys in user-visible output

---

## 3. AI in production

### Key facts

- **Prod is read-only by default.** "Owner rule: prod is read-only by default; no writes without explicit approval; show the plan before running anything heavy." `MS/groundup-ops/references/prod-readonly-access-playbook.md`
- **Show the exact queries first.** Guardrail 1 in that file is "**Show the exact queries first** for anything beyond a handful of cheap reads."
- **How the read-only access is built.** Tunnels via `ssh -fN -L`, `SET default_transaction_read_only=on`, and a 5 second statement timeout. `MS/groundup-ops/playbooks/prod-readonly-access-playbook.md`
- **Dry-run contract for correction scripts.** Default to dry-run. Print a preview table and counts. Commit only with `--apply`. Print `Dry-run complete. Pass --apply to commit the changes.` when not applying. The code shape is `conn.autocommit = False`, then rollback if dry run, commit otherwise. `MS/groundup-ops/references/dry-run-db-correction-script.md`
- **The 7-step VA cleanup runbook** (`MS/groundup-ops/playbooks/ginav2-unmonitored-va-cleanup.md`).
  - Step 2 shows the user a per-machine table plus a timeline SVG.
  - Step 3 records decisions the user confirmed, with "Never hard-delete; machine stays an asset."
  - Step 4 dry-runs the cleanup script, which runs the real UPDATEs in a transaction, rolls back, and writes ID backups.
  - Step 5 takes a Cloud SQL backup with a `pre-<slug>` description before apply.
  - Step 6 applies with `--apply --expect wo,drafts,reports` from the reviewed dry run, and a count mismatch rolls back.
  - Step 7 verifies per machine, for example open work orders 0 and drafts 0.
- **Backfill variant.** "Dry-run every write first, show the user, apply only after 'go'." The script asserts the expected row count in a `DO` block that raises on mismatch before `COMMIT`. `MS/groundup-ops/playbooks/ginav2-va-backfill-missed-weeks.md`
- **Alkhidmah prod-init is dry-run by default.** Every subcommand is a dry run without `--apply`, applying to the real database also needs `--allow-main`, and passwords are masked in every printed line. `~/work/alkhidmah/main_digital-platform/packages/devkit/README.md`
- **Threshold migrator has three modes.** `validate` is a full-pipeline dry run, `preview` shows the planned inserts, and `migrate ... [--apply]` writes. `MS/groundup-ops/playbooks/run-threshold-migrator.md`
- **Version-gated deploy.** `application.deploy` "is an acceptance receipt, not a rollout receipt." It enqueues a job and returns before touching the host, and a refused update can still show green while the old container serves. The playbook saves the image digest, deploys, polls, then verifies out of band with a baked build marker under a bounded timeout. "`done` plus a stale marker is a failed deploy." `MS/infra-ops/playbooks/dokploy-version-gated-deploy.md`
- **Backup proven by restore.** The prod deploy sequence checks that a dump's table of contents contains TABLE entries (82 means schema present), not only TABLE DATA, and keeps the previous image digest as the rollback. `MS/infra-ops/playbooks/prod-deploy-safety-sequence.md`
- **Infra hard rules.** Back up before any mutating change to a live service, DB or DNS record. A deploy is done only when the running version is verified. Stop and ask before DNS changes, payment actions, data deletion or live WhatsApp numbers. `MS/infra-ops/SKILL.md`
- **Gap to be honest about.** The notes found no explicit dry-run wording in infra-ops playbooks. Infra safety there rests on backup plus verify. Dry-run discipline lives in the groundup-ops and alkhidmah data scripts. [INFERENCE]
- **Agentic feature guardrails** (GinaV2 agentic reasoning).
  - Kill switch: `AGENTIC_REASONING_ENABLED=0` must mean zero claims, and the live-verify playbook has a kill-switch drill. `ginav2-agentic-live-verify-and-cron-test.md` line 48
  - Auth matrix: "no token and wrong token MUST 401 before any run starts". `deploy-ginav2-agentic-groundup-dev.md` line 38
  - Read gate: an internal user sees the completed report, and a customer sees all-null. Same file, line 41
  - Scheduler budget: at exactly 1800s the run ends `failed`, which the playbook calls "the designed isolation path, not a bug".
- **Deploys go to the shared dev box first.** The agentic stack runs on `groundup-dev` under its own compose project, and the deploy rsyncs scoped source trees only, because the dataset directory there is huge. `deploy-ginav2-agentic-groundup-dev.md`

### Story/example

On 2026-11-04 he told an agent "update db directly also fine, dry run first and show me the list so i can confirm with [a colleague]". The next day, on a GinaV2 task, he wrote "dry run first then show me what will be changed". Both prompts ask for the same contract the runbooks encode. The agent runs the real UPDATEs inside a transaction that rolls back, prints the preview table and counts, and stops. A colleague confirms the list. Only then does `--apply --expect ...` run, after a Cloud SQL backup, and a wrong row count rolls the whole transaction back. The VA cleanup playbook is the worked example. The version-gated deploy is the same instinct applied to releases, where a green job is not proof that the new container serves.

### Show on screen

- `~/.omp/agent/managed-skills/groundup-ops/playbooks/ginav2-unmonitored-va-cleanup.md` as one screen of seven steps.
- `~/.omp/agent/managed-skills/groundup-ops/references/dry-run-db-correction-script.md`, the "CLI contract" section.
- `~/.omp/agent/managed-skills/infra-ops/playbooks/dokploy-version-gated-deploy.md`.
- `alkhidmah prod-init build` without `--apply` (dry-run table). Never run it with `--apply` on stage.
- `~/.omp/agent/managed-skills/groundup-ops/references/prod-readonly-access-playbook.md`, guardrail list.
- The 2026-11-04 prompt in session history names a colleague. Keep the bracketed placeholder if you quote it.

### Quotable

> Owner rule: prod is read-only by default; no writes without explicit approval; show the plan before running anything heavy.

> Default to dry-run.
> Print a preview table and counts.
> Commit only with --apply.

> Apply with `--apply --expect wo,drafts,reports` from the reviewed dry run; mismatch rolls back.

> `application.deploy` is an acceptance receipt, not a rollout receipt.

> A deploy is done only when the running version is verified, not when the job is green.

> dry run first then show me what will be changed (real prompt, 2026-11-05)
