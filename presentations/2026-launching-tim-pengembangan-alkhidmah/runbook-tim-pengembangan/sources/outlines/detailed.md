# Launching Tim Pengembangan IT
## Visi, Strategi, dan Cara Kerja Menuju Super App Al Khidmah

**Bidang Media & IT PP Jama'ah Al Khidmah**
**14 Juli 2026**
**Zahid — Koordinator Pengembangan / Tech Lead**

---

## Slide 1 — Judul
- Launching Tim Pengembangan IT.
- Bidang Media & IT PP Jama'ah Al Khidmah.
- Selasa, 14 Juli 2026.
- Pembicara: Zahid, Koordinator Pengembangan / Tech Lead.
- Subjudul: Visi, Strategi, dan Cara Kerja Menuju Super App Al Khidmah.

---

## Slide 2 — Selamat Datang & Kenapa Kita Berkumpul
- Tim baru — hari ini adalah hari pertama kita berkumpul sebagai satu kesatuan.
- Tujuan meeting: menyatukan arah sebelum eksekusi dimulai.
- Agenda: visi → strategi → milestone → tim & peran → cara kerja → langkah berikutnya.
- Bukan presentasi satu arah — pertanyaan kapan saja diterima.

---

## Slide 3 — Landasan: Al Khidmah Oase Dunia
- Visi besar Jama'ah Al Khidmah: Al Khidmah sebagai Oase Dunia.
- Cita-cita Hadratusy Syaikh r.a. — mensyiarkan nilai Al Khidmah seluas-luasnya.
- Digitalisasi adalah kolaborator, akselerator, dan alat pendukung visi ini.
- Empat tujuan digitalisasi:
  1. Tata kelola keorganisasian yang profesional dan berkelanjutan.
  2. Manajemen penyelenggaraan majlis yang terkelola.
  3. Mensyiarkan majlis dan nilai jama'ah seluas-luasnya.
  4. Menuju Al Khidmah Oase Dunia.
- Kita tidak membangun teknologi untuk teknologi — kita membangun alat yang melayani jamaah.

---

## Slide 4 — Konteks Organisasi
- Bidang Media & IT PP Jama'ah Al Khidmah punya dua sub-tim: Pengembangan dan Multimedia.
- Departemen Pengembangan IT = sub-tim development. Itu kita.
- Struktur kepemimpinan:
  - **Ketua Bidang**: Imam — Accountable untuk seluruh bidang, signs off direction/scope/releases.
  - **Sekretaris Bidang**: Dzaky — administrasi, dokumentasi, koordinasi antar-bidang.
  - **Koordinator Pengembangan**: Zahid — Tech Lead, punya technical roadmap, arsitektur, delivery.
- Multimedia di luar scope development kita.

---

## Slide 5 — Program Kerja Bidang Media & IT
- 7 item Program Kerja dari roadmap visioner 2025.
- **Scope Departemen Pengembangan IT (item 1–3)**:
  1. Sistem database (organisasi, jama'ah, majlis) — pemetaan, pembinaan, pengembangan.
  2. IT tools (organisasi & kemajlisan — administratif, dokumentasi, pendanaan).
  3. Web Portal Jama'ah Al Khidmah.
- Item 4 (kanal media sosial) = scope Multimedia.
- Item 5–7 (kapabilitas tim, masterplan, rekrutasi) = shared bidang.

---

## Slide 6 — Strategi: Konsolidasi Super App
- **Saat ini (As-Is)**: 3 app terpisah.
  - Jamaah app — mobile, separate codebase. Active, sunsetting pasca-migrasi.
  - Web app — `alkhidmah.or.id` (TanStack Start). Active, refactor jadi thin landing.
  - Ekhidmah store — mobile, separate codebase. Active, embedding TBD.
- Masalah: 3 codebase = beban maintenance tinggi, auth/data/UX terpisah, release train pecah.
- **Target (To-Be)**: 1 super app + 1 thin landing.
  - Super App — `my.alkhidmah.or.id` (+ iOS/Android). Expo Router universal. Auth required (Better Auth).
  - Public Landing — `alkhidmah.or.id`. `apps/web` SSG-first. Auth none.
- Kenapa Expo Web:
  - Shared codebase — satu pipeline fitur untuk semua platform.
  - `apps/native` desktop-first adaptive mobile — info density lebih baik untuk dashboard/admin flows.
  - Satu auth cookie cross-subdomain — login di `alkhidmah.or.id` berlaku di `my.alkhidmah.or.id`.

---

## Slide 7 — Tiga Stream Migrasi
- **Stream A — Jamaah app → Super App** (paling kritis).
  - Target: **H-3 bulan HAF (Oktober 2026)**.
  - Scope: parity audit → port missing features → data migration → sunset jamaah app.
  - Faiz membawa knowledge dari jamaah app lama — langsung relevan.
- **Stream B — Web app → Thin Landing**.
  - Target: **HAF (Januari 2027)**.
  - Scope: strip `apps/web` jadi landing, redirect route interaktif ke `my.alkhidmah.or.id`.
- **Stream C — ZIS donasi → Embedded dari hexa**.
  - Target: **post-HAF** (2027).
  - Scope: ZIS + donasi jadi embedded app dari hexa dengan shared auth (Better Auth session).

---

## Slide 8 — Roadmap 2026–2028
> Timeline dimulai Juli 2026. Foundation baseline masih WIP. Tim part-time.

| Year | Theme | Key Deliverables | Headcount |
| --- | --- | --- | --- |
| 2026 H2 | Build Basics | Foundation baseline; majlis management (CRUD, RSVP, maktab, undangan); org management | Current team |
| 2027 | Expand & Explore | SK docs; signing; keuangan module; ZIS donasi dari hexa; eksplorasi kebutuhan org | Current team |
| 2028 | Design & Polish | Hire UI/UX designer; design review; app-wide redesign | + 1 designer (hire 2028) |

- Q3 2026: Foundation baseline (Zahid, done Jul). Majlis management basics: CRUD, RSVP, committee, maktab, undangan, food distribution, checkin. Org management basics. H-3 HAF milestone Okt.
- Q4 2026: Polish pasca-H-3 HAF. Stabilisasi majlis + org. HAF launch Jan 2027.
- 2027 H1: Stabilisasi pasca-HAF. Eksplorasi kebutuhan org. SK (Surat Keputusan) docs. Digital signing.
- 2027 H2: Keuangan module (domain terpisah). ZIS donasi dari hexa (Stream C).
- 2028: Hire UI/UX designer. Design review & improvement. App-wide redesign. Sisa fitur mengikuti prioritas org.

---

## Slide 9 — Portal Options [Wajib — tonight; Opsional — Tuesday]
- Tiga opsi untuk portal public per-region (PW/PD/PC), mengikuti kebutuhan identitas tiap wilayah.
- **Shared requirements (semua opsi)**: portal public terpusat + identitas per-unit; konten public SEO/read-only (jadwal majlis, berita, galeri, profil); link ke authenticated app (`my.alkhidmah.or.id`); workflow approval/publishing konten; akses kontributor scoped per organisasi; konvensi SEO/analytics; security update & backup; kemampuan publish markdown/konten lewat app di masa depan.
- **Option A — Separate deployment per PW/PD/PC**: setiap unit punya deployment/database/content sendiri.
  - Pro: autonomy penuh, full control, isolation per unit.
  - Con: hosting/backup/security/monitoring berlipat ganda, UX tidak konsisten, integrasi terduplikasi, central publishing sulit.
  - Cocok hanya untuk unit yang secara eksplisit otonom (legal/operasional) dan punya maintainer yang ditunjuk.
- **Option B — Custom CMS + ABAC (RECOMMENDED)**: satu deployment, satu content model, setiap portal di-resolve berdasarkan unit scope. Reuses existing org hierarchy + Permix ABAC untuk role contributor/editor/publisher.
  - Pro: integrated auth, UX konsisten, central publishing, reuse di app/API di masa depan.
  - Con: build time lebih lama, editorial UX harus didesain, ABAC/content workflow harus diuji, satu deployment = shared operational dependency.
  - Long-term strategic target, bukan final approval.
- **Option C — One WordPress**: satu deployment, konten regional direpresentasikan via categories/custom post types/taxonomy + scoped roles/plugins.
  - Pro: pilot tercepat, editor matang, initial engineering rendah.
  - Con: regional ABAC/isolation tidak cukup native untuk hierarchy org kita, risiko security plugin/theme update, integrasi butuh custom code.
  - Multisite variant: centralized network admin (Super Admin/plugin/theme), tapi operational/security blast radius tetap shared network-level.
- Decision matrix (9 dimensi × 3 opsi, nilai kualitatif Low/Medium/High): build effort to first portal, unit autonomy, security blast radius, regional access control, shared UX/content standards, initial integration effort, ongoing maintenance, future app/markdown publishing, cost shape.
- Malam ini: pilih arah/pilot — bukan build semua opsi. Option B = strategic target; Option C = pilot fallback kalau portal dibutuhkan sebelum custom CMS siap; Option A = autonomy-only.

---

## Slide 10 — Milestone: H-3 bulan HAF (Oktober 2026)
- **Milestone terdekat.** Internal readiness checkpoint 3 bulan sebelum HAF.
- Super app harus feature-complete dan testable pada titik ini.
- Definition of Done:
  - Stream A (jamaah app → super app) migration lengkap.
  - Majlis MVP production-ready: CRUD + RSVP + committee flows end-to-end.
  - Khidmah Hub + organization governance production-ready.
  - Auth + cross-subdomain cookie verified di `my.alkhidmah.or.id`.
  - Quality gates: crash rate < 1%, load time < 3s.
  - Foundation baseline selesai (Zahid, target end July 2026).
- Dependencies: Expo EAS builds, PostgreSQL prod, API server, app store submissions, SSL.
- Kenapa bukan Haul Metesh: tim launching 14 Jul, jendela 2 bulan ke Haul Metesh (Sep) terlalu sempit. Haul Metesh dilewati.

---

## Slide 11 — Milestone: HAF (Januari 2027)
- **Wide-usage launch.** Super app jadi pengganti resmi jamaah app.
- Definition of Done:
  - Super app live di 3 platform: iOS App Store + Google Play + `my.alkhidmah.or.id` web.
  - Public landing page (`alkhidmah.or.id`) shipped — route interaktif redirect ke super app.
  - Ekhidmah store embedding design finalized (Stream C scope dikunci).
  - Adoption: 1.000+ registered users, 100+ majlis, 70% RSVP rate.
  - Trunk-based dev + PR review policy operating at scale.
  - Designer onboard (Q4 2026 atau awal Q1 2027).
- Buffer 3 bulan antara H-3 (Okt) dan HAF (Jan): polish + app store submission + adoption push.
- H-3 HAF = prediktor kesiapan HAF. Kalau H-3 slip, HAF bergeser.

---

## Slide 12 — Document Management Options [Wajib — tonight; Opsional — Tuesday]
- **Scope**: manajemen dokumen organisasi — persuratan, SK docs, archive, templates, approval metadata, access policy, signing orchestration. Keuangan = domain terpisah. App tidak menduplikasi binary storage Google/Nextcloud.
- **Option 1 — Google Workspace** (Drive/Docs/Sheets/Gmail) — recommended first evaluation.
  - App owns: organization/document metadata, links, workflow state, ABAC scope.
  - Google owns: document collaboration & storage (Docs/Sheets/Drive/Gmail).
  - Satu tenant under `alkhidmah.or.id`. Shared drives per PP/PW/PC/PD.
- **Access model**: `pp-doc-admins@alkhidmah.or.id` = Manager/Content Manager di semua child drives. Local group tiap child unit = Content Manager/Contributor di drive sendiri. Hindari direct per-user sharing (kecuali break-glass). OUs configure policy; Groups grant membership.
- **Cost** (USD reference, before tax/FX/reseller; **quote required**):

| Licensed users | Nonprofit free | Standard annual | Standard monthly | Plus annual | Plus monthly |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | $0/yr if eligible | $2,100/yr | $2,520/yr | $3,696/yr | $4,440/yr |
| 100 | $0/yr if eligible | $4,200/yr | $5,040/yr | $7,392/yr | $8,880/yr |
| 300 | $0/yr if eligible | $12,600/yr | $15,120/yr | $22,176/yr | $26,640/yr |

  - Final IDR cost butuh Google/reseller quote, nonprofit verification, taxes/FX, konfirmasi user mana yang butuh paid account.
- **Provider-lobby checklist**: nonprofit verification; donated/free plan eligibility; Business Standard/Plus nonprofit quote; billing IDR; annual commitment discount; jumlah active accounts vs occasional contributors; pooled storage; Shared Drive/eSignature availability; migration assistance; admin/support SLA; data/export/retention; training/partner credits.
- **Self-hosted alternatives**:
  - **Nextcloud + Nextcloud Office (Collabora) + LibreSign/DocuSeal**: control tinggi, no per-user SaaS cost. Con: VPS capacity, backup, upgrade, security, office-fidelity, training burden. Current VPS capacity perlu diukur — no capacity claim tanpa pilot.
  - **ONLYOFFICE Docs + Nextcloud**: MS Office compatibility kuat. Con: licensing/support & resource perlu di-quote.
  - **Paperless-ngx**: archive/OCR/search/workflow complement — bukan full office collaboration/signing replacement.
- **WPS WebOffice**: hosted integration/API platform — **NOT** open-source self-hosted. Kalau dipakai, request provider quote & integration terms terpisah.
- Keuangan = domain terpisah, tidak termasuk document management scope ini.

---

## Slide 13 — Signing & Parent→Child Access [Wajib — tonight; Opsional — Tuesday]
- **Signing options** (dipisah dari collaboration/storage):
  - **(1) Google eSignature** pada eligible Standard/Plus plans: evaluasi tercepat, up to 10 signers/200 fields per request. Tapi validasi formal/legal requirements — availability ≠ acceptance.
  - **(2) App workflow + licensed/certified provider**: app owns approval state/audit/integration; provider handles signature evidence/certificates. **Jangan implementasikan cryptographic signing ad hoc.**
  - **(3) Self-host LibreSign/DocuSeal**: control + integration, tapi validasi legal acceptance, identity assurance, audit trail, dan operations.
- **Decision gate**: Imam/Dzaky define apa yang dimaksud "official signing" (signer identity, approval authority, audit evidence, certificate/PSrE, document retention) sebelum memilih implementation.
- **PP → child Drive access model**:
  - Explicit Google Groups membership. `pp-doc-admins@alkhidmah.or.id` = Manager/Content Manager di child drives.
  - **OU policy inheritance is NOT Drive membership inheritance.** OUs control policy/settings; akses drive diberikan explicit ke users/groups.
  - Folder/file permissions inherit **within** a shared drive only; tidak otomatis cross dari parent drive ke child drive.
  - Fallback (children pakai separate Workspace tenants): external sharing/groups, dengan governance & support cost lebih tinggi.
- Boundary: Google Workspace/alternative office suite = document collaboration/storage; Alkhidmah app = document metadata, workflow state, regional scope, links.

---

## Slide 14 — Tim Kita
- **Development** (4 orang):
  - **Zahid** — Tech Lead / Koordinator Pengembangan. Bangun core baseline arsitektur, lalu development. Release authority.
  - **Dzaky** — Developer. Dual role: juga Sekretaris Bidang. Development di atas baseline Zahid.
  - **Anaz** — Developer + QA Automation. Development + automated test/QA infrastructure.
  - **Faiz** — Developer. Mantan tim jamaah app. Knowledge transfer untuk Stream A migration.
- **Product** (3 orang):
  - **Shofi** — Product Manager + per-product QA. Kumpul kebutuhan, desain produk, QA.
  - **Taufik** — Product Manager + per-product QA. Kumpul kebutuhan, desain produk, QA.
  - **Tahzan** — Product Manager + per-product QA. Kumpul kebutuhan, desain produk, QA.
- **Leadership**: Imam — Ketua Bidang, Accountable.

---

## Slide 15 — Peran & Tanggung Jawab
- **Zahid (Tech Lead)**: architecture decisions, trunk keeper, release authority, stakeholder bridge ke Pengurus. Menetapkan core baseline agar developer lain bisa build di atasnya.
- **Dzaky, Anaz, Faiz (Developer)**: fitur di `apps/*` + `packages/api`. Cross-cutting feature work. Build di atas baseline Zahid.
- **Anaz (QA Automation)**: automated test infrastructure, regression suites, release verification. Double duty: dev + QA.
- **Shofi, Taufik, Tahzan (Product Manager)**: mengumpulkan kebutuhan produk, mendesain UX/flow, handoff ke developer, per-product QA.
- Alur kerja: Zahid baseline → Dzaky/Anaz/Faiz kembangkan fitur → PM feed kebutuhan & desain.

---

## Slide 16 — RACI: Siapa Pegang Apa
- **R** = Responsible (mengerjakan) · **A** = Accountable (tanggung jawab akhir) · **C** = Consulted · **I** = Informed.

| Workstream | Zahid (TL) | Dev (Dzaky/Anaz/Faiz) | PM (Shofi/Taufik/Tahzan) | Imam (KB) |
| --- | :---: | :---: | :---: | :---: |
| Architecture decisions | A/R | C | C | I |
| Feature development | C | R | C | I |
| Product requirements & design | C | C | A/R | I |
| QA & local retest | C | R (Anaz lead) | R (per-product) | — |
| Production deploy | A | R | — | I |

- Ketua Bidang (Imam) = A untuk scope bidang, I untuk operasional dev harian.
- RACI dipakai saat PR review — Reviewer 2 (domain) ditentukan dari kolom workstream yang cocok.

---

## Slide 17 — Cara Kerja: Trunk-Based Development
- Semua orang integrate ke `master` (trunk) setidaknya harian.
- Branch fitur berumur pendek (< 2 hari) → PR → review → merge.
- `master` selalu deployable — tidak ada branch release lama.
- Branch naming: `feat/`, `fix/`, `docs/`, `chore/`, `refactor/` + `<scope>-<desc>`.
- Setiap branch punya worktree sendiri (lazyworktree) + Postgres container terisolasi per-branch.
- Pre-PR checklist wajib:
  - `bun run check` (oxlint + oxfmt)
  - `bun run check-types` (tsc --noEmit)
  - `bun run test` (Vitest + Jest)
- Anti-pattern: branch > 2 hari, push langsung ke master, merge-commit dari master (pakai rebase).
- Monorepo: shared packages only (DB, API contracts, config, auth, UI). Per-feature packages deferred — Expo typed routes (beta) + client-server splitting (experimental) belum stabil. Riset lanjutan diperlukan.

---

## Slide 18 — Code Review Policy
- **Aturan inti: setiap PR butuh 2 reviewers + 1 local retest oleh orang ketiga sebelum merge.**
- Tidak ada exception — berlaku universal, termasuk "PR kecil" dan "fix typo".

| Slot | Who | Responsibility |
| --- | --- | --- |
| Reviewer 1 (architectural) | Zahid atau delegate | Scope, design, contracts, cross-cutting impact |
| Reviewer 2 (domain) | Domain owner per RACI | Implementation correctness, domain conventions |
| Retester (third person) | Anaz (QA) atau reviewer non-author | Pull branch, jalankan app, exercise behavior, konfirmasi criteria |

- Local retest procedure: setup worktree → bootstrap → run app → exercise acceptance criteria → run checks → comment PASS/FAIL.
- PR target < 400 lines diff. Squash-merge ke master.
- PR stuck > 24 jam → escalate ke Tech Lead di Dev Sync.

---

## Slide 19 — Auth, OTP & Infrastruktur
- **OTP provider**: kirimdev.com — WhatsApp Business API, Indonesia. Rp 25K/mo starter. Meta-approved AUTHENTICATION templates (auto-approved). Single REST endpoint, TypeScript SDK, webhooks.
- **Cost optimization — customer-initiated messages**: registrasi via WhatsApp di mana user menginisiasi chat (klik link → kirim trigger → sistem balas OTP). Free within 24h window (up to 1.000/bulan per WABA). Business-initiated auth template ~$0.003/msg.
- **WhatsApp fallback — OPEN DESIGN ITEM**: current approach tidak disukai. Flag untuk diskusi dengan Imam & Dzaky. Belum ada keputusan.
- **Infrastruktur**: Biznet Gio VPS (self-hosted PostgreSQL + API server Elysia + app). No managed cloud (no RDS, no Vercel/Render, no managed Redis). Maybe Cloudflare R2 for object storage later. SSL via reverse proxy (Caddy/nginx + Let's Encrypt).
- **Total cost**: VPS + Rp 25K/mo (kirimdev).

---

## Slide 20 — Cadence Pertemuan
| Meeting | Frequency | Duration | Output |
| --- | --- | --- | --- |
| Product Meeting | Bulanan (minggu pertama) | 90 min | Prioritized backlog, milestone progress, decisions log |
| Dev Sync | Mingguan (Senin) | 30 min | Blockers, PR queue, trunk health |
| PR Review sync | Ad-hoc | 15 min | Unblock stuck PRs |
| Retrospective | Bulanan | 45 min | Process improvements → update docs/ops/engineering/ |

- Output setiap meeting committed ke `docs/ops/` dalam 48 jam.
- Tidak ada meeting notes di luar repo — catatan mentah boleh di mana saja, output final harus di repo.
- Tooling: GitHub Issues (bugs) + GitHub Projects (sprint kanban, 2-mingguan). Dokumentasi markdown di docs/ops/ — bisa di-publish via super app nanti. Tidak pakai Jira/Trello/Notion.

---

## Slide 21 — Langkah Berikutnya
- **Minggu 1 — Onboarding**:
  - Setup environment, worktree, akses repo untuk semua.
  - Baca `docs/ops/` — mulai dari roadmap, roster, engineering process.
- **Zahid**: core baseline WIP, target done end of July. Folder structure: shared packages only — lalu Dzaky/Anaz/Faiz build di atasnya.
- **PM (Shofi/Taufik/Tahzan)**: mulai audit kebutuhan produk — parity audit jamaah app, domain MVP scope.
- **Dev (Dzaky/Anaz/Faiz)**: familiarisasi codebase (`apps/native`, `packages/api`, `apps/server`, `packages/db`).
- **Dev Sync pertama**: Senin depan.
- **Kapasitas tim**: ~10 jam/orang/2-minggu (part-time, ~5 jam/minggu). Total ~35 jam/minggu ≈ <1 FTE. Sprint 2-mingguan, realistis terhadap milestone.

---

## Slide 22 — Penutup
- Tim ini punya peran strategis: mewujudkan Al Khidmah Oase Dunia lewat teknologi.
- Kita bukan sekadar ngoding — kita membangun alat yang melayani jamaah dan mensyiarkan nilai Al Khidmah.
- Setiap orang di tim ini penting — dev, PM, leadership.
- Arah jelas: H-3 HAF Oktober 2026 (readiness checkpoint) → HAF Januari 2027 (wide-usage launch).
- Mari mulai — Dev Sync Senin depan.
