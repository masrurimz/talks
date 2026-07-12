# Referensi — Engineering Process

> Sumber: `docs/ops/engineering/trunk-based-development.md`, `code-review-policy.md`, `meeting-cadence.md`.

## Trunk-Based Development

### Principle

Semua orang integrate ke `master` (trunk) **setidaknya harian**. Branch fitur berumur pendek (< 2 hari) → PR → review → merge. `master` selalu deployable.

### Branch model

| Branch | Lifetime | Purpose | Merge to |
| --- | --- | --- | --- |
| `master` | Permanent | Always deployable | — |
| `<type>/<scope>-<desc>` | < 2 hari | Satu PR worth of work | `master` via squash-merge |
| `release/*` (rare) | Jam | Production release tag only | Tag, jangan merge back |

### Branch naming

- `feat/<scope>-<desc>` — fitur baru (cth: `feat/majlis-rsvp`)
- `fix/<scope>-<desc>` — bug fix
- `docs/<scope>-<desc>` — dokumentasi
- `chore/<scope>-<desc>` — tooling, deps, config
- `refactor/<scope>-<desc>` — refactor tanpa behavior change

### Worktree model

Setiap branch fitur punya lazyworktree sendiri: `lazyworktree create <branch-name>`. File `.wt` auto-bootstrap (env symlinks, `mise trust -y`, `bun install`, `bun run env:setup`). Setiap worktree punya **Postgres container terisolasi** per-branch.

### Pre-PR checklist

Sebelum buka PR, jalankan dari root repo:

```bash
bun run check          # oxlint + oxfmt
bun run check-types    # tsc --noEmit across all packages
bun run test           # turbo runs Vitest (server) + Jest (native)
```

### Anti-patterns

- NEVER branch fitur berumur > 2 hari → split PR.
- NEVER merge commit dari `master` ke branch fitur → **rebase** saja.
- NEVER push langsung ke `master` → selalu lewat PR dengan review.
- NEVER pakai `--no-verify` saat commit (kecuali spurious `.wt`-only error).

## Code Review Policy

### Aturan inti

**Setiap PR butuh setidaknya 2 reviewers + 1 local retest oleh orang ketiga sebelum merge.**

Tidak ada exception untuk "PR kecil" atau "fix typo". Aturan ini berlaku universal — ini adalah cara tim memastikan setiap perubahan terverifikasi oleh tiga pasang mata berbeda.

### Reviewer model

| Slot | Who | Responsibility |
| --- | --- | --- |
| **Reviewer 1 (architectural)** | Tech Lead (Zahid) atau delegate | Scope, design, contracts (Zod shapes untuk `packages/api`), cross-cutting impact |
| **Reviewer 2 (domain)** | Domain owner per RACI | Implementation correctness, domain conventions |
| **Retester (third person)** | QA Engineer (Anaz) atau reviewer non-author manapun | Pull branch locally, jalankan app, exercise behavior yang berubah, konfirmasi acceptance criteria |

Reviewer 1 dan 2 boleh approved paralel. Retester baru aktif setelah kedua reviewer approved.

### Local retest procedure

1. Setup worktree — `lazyworktree create <pr-branch>`.
2. Bootstrap pertama kali — `bun run bootstrap`.
3. Jalankan app — `bun run dev`.
4. Exercise acceptance criteria — ikuti setiap langkah "how to verify" di PR description.
5. Jalankan checks — `bun run check && bun run check-types && bun run test`.
6. Comment hasil di PR — PASS / FAIL dengan alasan.

### What reviewers check

- API contracts — Zod shapes di `packages/api/src/contracts/` benar & konsisten.
- Type safety — no `any`, no `as any`, no `@ts-ignore`.
- No `enum` — pakai `const` objects `as const`.
- No `console.log` di luar seeders/tests.
- No array index as React `key`.
- No `shadow-*` / `elevation` — pakai glassmorphism (`backdrop-blur-md` + translucent borders).
- Typed errors — pakai `baseErrors` di `packages/api/src/contracts/errors.ts`.
- Cross-domain impact — perubahan di `packages/api` mempengaruhi `apps/native` dan `apps/web`.
- Test coverage — pada behavior baru, bukan plumbing.

### PR size & squash-merge

- Target: **< 400 lines diff**. PR lebih besar split by behavior.
- Squash-merge ke `master`. Commit message: `<type>(<scope>): <imperative description>`.
- Breaking change → tambahkan `BREAKING CHANGE:` footer.

### Escalation

PR blocked > 24 jam → escalate ke Tech Lead di weekly Dev Sync. Tech Lead memutuskan: unblock dengan decision, reassign reviewer, atau split PR.

## Cadence Pertemuan

| Meeting | Frequency | Duration | Owner | Attendees | Output |
| --- | --- | --- | --- | --- | --- |
| **Product Meeting** | Bulanan (minggu pertama) | 90 min | Tech Lead + stakeholder | Full dev team + stakeholder rep | Prioritized backlog, milestone progress, decisions log |
| **Dev Sync** | Mingguan (Senin) | 30 min | Tech Lead | Full dev team | Blockers, PR queue, trunk health |
| **PR Review sync** | Ad-hoc | 15 min | Reviewer on duty | PR author + reviewers | Unblock stuck PRs |
| **Retrospective** | Bulanan (setelah Product Meeting) | 45 min | Tech Lead | Full dev team | Process improvements → update `docs/ops/engineering/` |

### Aturan output meeting

Output setiap meeting **committed ke `docs/ops/` dalam 48 jam**:

- **Decisions** → update doc strategi/milestone yang relevan.
- **Process changes** → update doc engineering.
- **Backlog changes** → update milestone workstreams.

**Tidak ada meeting notes yang hidup di luar repo.** Catatan mentah boleh di medium apa saja, tapi output final harus di `docs/ops/` agar discoverable dan version-controlled.
