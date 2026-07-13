# Prompt untuk Revisi Deck

## Instruksi untuk NotebookLM

Revisi deck presentasi yang sudah dihasilkan untuk materi:

**Launching Tim Pengembangan IT**

### Arahan revisi:

#### 1. Cek tim aktual + nama
- Dev: **Zahid** (Tech Lead), **Dzaky** (developer, dual role Sekretaris), **Anaz** (developer + QA automation), **Faiz** (developer, mantan tim jamaah app).
- Product: **Shofi, Taufik, Tahzan** (PM + per-product QA).
- Leadership: **Imam** (Ketua Bidang).
- Tim = 7 orang total. Pastikan semua nama muncul dan tidak ada placeholder `[TODO]`.

#### 2. Cek milestone
- **Milestone terdekat = H-3 bulan HAF (Oktober 2026)** — readiness checkpoint.
- **HAF = Januari 2027** — wide-usage launch.
- **Haul Metesh TIDAK boleh muncul sebagai milestone aktif.** Kalau ada, ganti dengan H-3 HAF.
- Timeline: Launch 14 Jul → Build Jul–Okt → H-3 Okt → Final sprint → HAF Jan'27.

#### 3. Cek proporsi
- Landasan + pembuka: 10%.
- Strategi + roadmap: 25% (terbesar).
- Milestone: 15%.
- Tim & peran & RACI: 20%.
- Cara kerja: 20%.
- Langkah berikutnya + penutup: 10%.

#### 4. Cek RACI
- Architecture decisions: Zahid A/R.
- Feature development: Dev (Dzaky/Anaz/Faiz) R.
- Product requirements & design: PM (Shofi/Taufik/Tahzan) A/R.
- QA & retest: Anaz lead + PM per-product.
- Production deploy: Zahid A.

#### 5. Cek strategi super app
- As-is: 3 app terpisah (jamaah mobile, web, ekhidmah store).
- To-be: 1 super app (`my.alkhidmah.or.id`) + 1 thin landing (`alkhidmah.or.id`).
- Stream A target: H-3 HAF (Okt 2026), bukan Haul Metesh.

#### 6. Cek cara kerja
- Code review: **2 reviewer + 1 local retest oleh orang ketiga** — tanpa exception.
- Trunk-based: integrate ke master harian, branch < 2 hari.
- Cadence: product meeting bulanan, dev sync mingguan.

#### 7. Cek gaya bahasa
- Bahasa Indonesia sederhana, formal-hangat.
- Bukan korporat/kaku — organisasi keagamaan.
- Istilah teknis dengan penjelasan singkat.
- Satu pesan utama per slide.

#### 8. Cek kapasitas tim
- **Kapasitas: ~10 jam/orang/2-minggu (part-time)** — pastikan disebut, bukan full-time.
- Sprint 2-mingguan, bukan 1-mingguan.

#### 9. Cek tooling & infra
- **Tooling: GitHub Issues (bugs) + GitHub Projects (sprint) + markdown docs** — tidak pakai Jira/Trello/Notion.
- **Infra: Biznet Gio VPS** (self-hosted Postgres + API + app, no managed cloud) — jangan implikasikan biaya cloud mahal.
- **OTP: kirimdev.com** (WhatsApp, Rp 25K/mo). Customer-initiated = gratis dalam 24h window.

#### 10. Cek URL & Stream C
- Semua URL pakai **`.or.id`** — tidak boleh ada `alkhidmah.id` (harus `alkhidmah.or.id`).
- **Stream C = ZIS donasi dari hexa** (bukan ekhidmah store).
- **Keuangan bukan bagian dari org/majlis** — domain terpisah.
- **Desktop-first** (bukan mobile-first).
- **Monorepo shared packages only** — per-feature packages deferred.

#### 11. Cek portal options
- **Tiga opsi portal muncul**: separate deployment, custom CMS + ABAC, one WordPress.
- **Option B (CMS+ABAC) = rekomendasi**, bukan final approval. Option C = pilot fallback. Option A = autonomy-only.
- Decision matrix (9 dimensions) present.

#### 12. Cek document management & signing
- **Google Workspace cost = USD reference** — jangan fabricate IDR. Label "quote required" present.
- **PP→child Drive: explicit Google Groups** — OU policy ≠ Drive membership inheritance.
- **Signing = open question** — jangan portray satu path sebagai sudah dipilih.
- **WPS = hosted integration, BUKAN open-source self-hosted**.
- Deck = **22 slide** (3 slide decision baru di posisi 9, 12, 13).

---

## Prioritas sumber untuk revisi:
1. `sources/context/brief.md` — cek audiens dan gaya.
2. `sources/context/structure.md` — cek proporsi dan urutan.
3. `sources/outlines/presenter.md` atau `detailed.md` — cek slide-by-slide.
4. `sources/references/referensi-tim-dan-raci.md` — cek tim & RACI.
5. `sources/references/referensi-milestone.md` — cek milestone.
6. `sources/references/referensi-arsitektur-dan-auth.md` — cek arsitektur, auth, kapasitas, tooling, infra.
7. `sources/references/referensi-public-portal-options.md` — cek portal options.
8. `sources/references/referensi-document-management-options.md` — cek document management, signing, cost.

---

## Catatan khusus:
- Revisi ringan, bukan rewrite total.
- Fokus pada ketidaksesuaian dengan arahan.
- Kalau ada slide terlalu padat, pisahkan.
- Kalau ada slide terlalu singkat, tambahkan substansi.
- **Faiz adalah developer ke-4** — pastikan muncul di slide tim dan peran. Dia mantan tim jamaah app, relevan untuk Stream A.
