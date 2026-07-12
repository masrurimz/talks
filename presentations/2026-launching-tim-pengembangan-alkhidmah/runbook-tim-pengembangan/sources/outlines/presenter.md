# Launching Tim Pengembangan IT
## Visi, Strategi, dan Cara Kerja Menuju Super App Al Khidmah

**Bidang Media & IT PP Jama'ah Al Khidmah**
**14 Juli 2026**
**Zahid — Koordinator Pengembangan / Tech Lead**

## Catatan penggunaan untuk presenter
- Target durasi total: sekitar **30 menit**.
- Tanda **[Wajib]** berarti sebaiknya tetap dipakai.
- Tanda **[Opsional]** berarti bisa dipotong jika waktu mepet.
- Kolom **Ritme bicara** membantu memperkirakan durasi per slide.

## Urutan potong jika waktu mepet
Potong dalam urutan ini:
1. Slide 5 (Program Kerja 7 item — ringkas jadi 1 kalimat).
2. Slide 16 (Cadence pertemuan — sebut cepat).
3. Slide 8 (Roadmap detail — tunjukkan tabel saja, skip detail per-tahun).

Dengan begitu, inti besar masih aman: strategi, milestone, tim, dan cara kerja masih utuh.

---

## Slide 1 [Wajib] — Judul
**Ritme bicara:** 1 menit
- Launching Tim Pengembangan IT.
- Bidang Media & IT PP Jama'ah Al Khidmah.
- 14 Juli 2026.
- Pembicara: Zahid, Koordinator Pengembangan / Tech Lead.

**Arah bicara:**
Buka dengan hangat. Sampaikan bahwa hari ini adalah hari pertama tim ini berkumpul sebagai satu kesatuan. Jangan langsung ke substansi.

**Pesan utama:**
Hari ini kita memulai perjalanan bersama sebagai Tim Pengembangan IT.

---

## Slide 2 [Wajib] — Selamat Datang & Kenapa Kita Berkumpul
**Ritme bicara:** 2 menit
- Tim baru — beberapa dari kalian sudah kenal, beberapa baru.
- Tujuan hari ini: menyatukan arah sebelum kita mulai eksekusi.
- Kita akan bahas: ke mana platform ini menuju, siapa mengerjakan apa, dan bagaimana cara kerja kita.
- Bukan presentasi satu arah — silakan bertanya kapan saja.

**Arah bicara:**
Bangun rasa tim. Akui bahwa ini awal baru. Jelaskan struktur meeting: visi → strategi → milestone → tim → cara kerja → langkah berikutnya.

**Pesan utama:**
Kita berkumpul untuk menyatukan arah — bukan sekadar update, tapi alignment.

---

## Slide 3 [Wajib] — Landasan: Al Khidmah Oase Dunia
**Ritme bicara:** 2–3 menit
- Visi besar: Al Khidmah sebagai Oase Dunia — cita-cita Hadratusy Syaikh r.a.
- Digitalisasi adalah kolaborator, akselerator, alat pendukung visi ini.
- Kita tidak membangun teknologi untuk teknologi — kita membangun alat yang melayani jamaah dan mensyiarkan nilai Al Khidmah.
- Empat tujuan digitalisasi: tata kelola profesional, manajemen majlis terkelola, syiar seluas-luasnya, menuju Oase Dunia.

**Arah bicara:**
Ini adalah akar spiritual dari semua yang akan dibahas. Jangan lewati cepat. Tekankan bahwa pekerjaan tim ini punya makna — bukan sekadar ngoding.

**Pesan utama:**
Pekerjaan kita berakar pada visi Al Khidmah Oase Dunia — teknologi sebagai alat melayani jamaah.

---

## Slide 4 [Wajib] — Konteks Organisasi
**Ritme bicara:** 1–2 menit
- Bidang Media & IT PP Jama'ah Al Khidmah punya dua sub-tim: Pengembangan dan Multimedia.
- Kita adalah **Departemen Pengembangan IT** — sub-tim development.
- Ketua Bidang: Imam (Accountable). Sekretaris: Dzaky.
- Koordinator Pengembangan: Zahid (Tech Lead).
- Multimedia di luar scope kita — fokus kita adalah platform digital.

**Arah bicara:**
Jelaskan posisi tim dalam struktur. Imam sebagai Ketua Bidang menandatangani arah. Dzaky dual-role: Sekretaris sekaligus developer di tim kita.

**Pesan utama:**
Kita adalah Departemen Pengembangan IT di bawah Bidang Media & IT — punya tempat dan peran yang jelas.

---

## Slide 5 [Opsional] — Program Kerja Bidang Media & IT
**Ritme bicara:** 2 menit
- 7 item Program Kerja dari roadmap visioner 2025.
- **Scope kita (item 1–3)**: sistem database (org, jama'ah, majlis), IT tools (org & majlis management), Web Portal.
- Item 4 (media sosial) = scope Multimedia.
- Item 5–7 (kapabilitas tim, masterplan, rekrutasi) = shared.

**Arah bicara:**
Ringkas — tunjukkan bahwa tim kita punya scope yang terdefinisi. Jangan bahas tiap item detail; fokus bahwa item 1–3 adalah domain kita.

**Pesan utama:**
Scope Departemen Pengembangan IT adalah database, IT tools, dan web portal — item 1–3 Program Kerja.

---

## Slide 6 [Wajib] — Strategi: Konsolidasi Super App
**Ritme bicara:** 3–4 menit
- **Saat ini**: 3 app terpisah — jamaah app (mobile), web app (`alkhidmah.id`), ekhidmah store (mobile).
- Masalah: maintenance 3 codebase, auth/data/UX terpisah, release train pecah.
- **Target**: 1 super app (`my.alkhidmah.id`, Expo Router untuk iOS/Android/Web) + 1 thin landing (`alkhidmah.id`, konten publik read-only).
- Kenapa Expo Web: satu codebase, sudah responsive, satu auth cookie cross-subdomain.

**Arah bicara:**
Ini adalah slide strategis terpenting. Jelaskan masalah dulu (3 app = beban), lalu solusi (konsolidasi). Pakai tabel as-is vs to-be kalau bisa. Tekankan: satu pipeline fitur untuk semua platform.

**Pesan utama:**
Kita mengkonsolidasi 3 app terpisah menjadi 1 super app + 1 thin landing — satu codebase, satu auth, satu release train.

---

## Slide 7 [Wajib] — Tiga Stream Migrasi
**Ritme bicara:** 2–3 menit
- **Stream A** (paling kritis): jamaah app → super app. Target **H-3 HAF (Okt 2026)**. Faiz bawa knowledge dari jamaah app lama — langsung relevan.
- **Stream B**: web app → thin landing. Target **HAF (Jan 2027)**.
- **Stream C**: ekhidmah store → embedded di super app. Target **Q2 2027** (post-HAF).

**Arah bicara:**
Tiga stream paralel dengan target berbeda. Stream A paling kritis — mengaktifkan super app untuk pengguna nyata. Sebut Faiz sebagai knowledge bridge untuk Stream A.

**Pesan utama:**
Tiga stream migrasi: A (jamaah→super app, Okt'26), B (web→thin landing, HAF), C (store→embedded, Q2'27).

---

## Slide 8 [Opsional] — Roadmap 2026–2028
**Ritme bicara:** 2 menit
- **2026 H2**: Build + Migrate + Launch (H-3 HAF Okt, HAF Jan'27).
- **2027**: Functionality Coverage — semua PRD domain MVP parity; ekhidmah embedded.
- **2028**: Redesign + UX Maturity — app-wide redesign, riset usability.
- Hiring: designer Q4 2026.

**Arah bicara:**
Tunjukkan tabel roadmap. Jangan bahas detail per-tahun — fokus pada tema: build dulu, lalu coverage, lalu redesign.

**Pesan utama:**
Tiga tahun: build (2026) → coverage (2027) → redesign (2028).

---

## Slide 9 [Wajib] — Milestone: H-3 bulan HAF (Oktober 2026)
**Ritme bicara:** 3–4 menit
- **Milestone terdekat kita.** Internal readiness checkpoint 3 bulan sebelum HAF.
- Definition of Done:
  - Stream A (jamaah→super app) migrasi selesai.
  - Majlis MVP production-ready (CRUD + RSVP + committee).
  - Khidmah Hub + org governance production-ready.
  - Auth + cross-subdomain cookie verified.
  - Quality gates: crash < 1%, load < 3s.
- Kenapa bukan Haul Metesh: tim baru launching Jul, jendela 2 bulan terlalu sempit. Haul Metesh dilewati.

**Arah bicara:**
Ini adalah target konkret pertama kita. Jelaskan setiap DoD point. Tekankan: H-3 HAF adalah prediktor — kalau slip, HAF bergeser. Tim punya ~3 bulan dari launch ke checkpoint ini.

**Pesan utama:**
Target pertama kita: H-3 bulan HAF (Okt 2026) — super app feature-complete dan testable, Stream A selesai.

---

## Slide 10 [Wajib] — Milestone: HAF (Januari 2027)
**Ritme bicara:** 2–3 menit
- **Wide-usage launch.** Super app jadi pengganti resmi jamaah app.
- Definition of Done:
  - Live di 3 platform: iOS + Play Store + web `my.alkhidmah.id`.
  - Thin landing (`alkhidmah.id`) ship.
  - Ekhidmah store embed design finalized.
  - Adoption: 1.000+ users, 100+ majlis, 70% RSVP rate.
  - Engineering process at scale.
- Buffer 3 bulan antara H-3 (Okt) dan HAF (Jan) untuk polish + submission + adoption.

**Arah bicara:**
Ini adalah target besar. HAF = super app resmi menggantikan jamaah app. Buffer 3 bulan adalah ruang untuk app store review dan adoption push.

**Pesan utama:**
HAF Januari 2027 = wide-usage launch — super app resmi menggantikan jamaah app untuk semua pengguna.

---

## Slide 11 [Wajib] — Tim Kita
**Ritme bicara:** 3–4 menit
- **Development** (4 orang):
  - **Zahid** — Tech Lead. Bangun core baseline arsitektur, lalu development.
  - **Dzaky** — Developer. Dual role: juga Sekretaris Bidang.
  - **Anaz** — Developer + QA Automation. Development + test infrastructure.
  - **Faiz** — Developer. Mantan tim jamaah app — knowledge transfer untuk Stream A.
- **Product** (3 orang):
  - **Shofi, Taufik, Tahzan** — Product Manager. Kumpul kebutuhan, desain produk, per-product QA.
- **Leadership**: Imam (Ketua Bidang, Accountable).

**Arah bicara:**
Perkenalkan setiap orang dan perannya. Tekankan pembagian dev vs product. Zahid bangun baseline dulu, lalu Dzaky/Anaz/Faiz kembangkan. PM kumpul kebutuhan dan desain. Faiz penting untuk Stream A karena dia kenal jamaah app lama.

**Pesan utama:**
Tim kita: 4 developer (Zahid lead + Dzaky/Anaz/Faiz) + 3 product manager (Shofi/Taufik/Tahzan) + Imam sebagai Ketua Bidang.

---

## Slide 12 [Wajib] — Peran & Tanggung Jawab
**Ritme bicara:** 2–3 menit
- **Zahid (Tech Lead)**: architecture, trunk keeper, release authority, stakeholder bridge. Bangun baseline agar tim lain bisa build.
- **Dzaky, Anaz, Faiz (Developer)**: fitur di `apps/*` + `packages/api`. Build di atas baseline Zahid.
- **Anaz (QA Automation)**: automated test infrastructure, regression suites, release verification.
- **Shofi, Taufik, Tahzan (PM)**: kumpul kebutuhan produk, desain UX/flow, handoff ke dev, per-product QA.

**Arah bicara:**
Jelaskan apa yang dimiliki tiap peran. Kuncinya: Zahid menetapkan baseline dulu, lalu Dzaky/Anaz/Faiz bebas kembangkan fitur. PM feed kebutuhan dan desain ke dev. Anaz double duty: dev + QA automation.

**Pesan utama:**
Zahid bangun baseline → Dzaky, Anaz & Faiz kembangkan fitur → PM kumpul kebutuhan & desain → semua punya peran yang jelas.

---

## Slide 13 [Wajib] — RACI: Siapa Pegang Apa
**Ritme bicara:** 2–3 menit
- RACI = siapa **R**esponsible (mengerjakan), **A**ccountable (tanggung jawab akhir), **C**onsulted, **I**nformed.
- Architecture decisions: Zahid A/R.
- Feature development: Dev R (Dzaky/Anaz/Faiz).
- Product requirements & design: PM A/R (Shofi/Taufik/Tahzan).
- QA & local retest: Anaz lead + PM per-product.
- Production deploy: Zahid A.
- Ketua Bidang (Imam): A untuk scope bidang, I untuk operasional dev.

**Arah bicara:**
Jangan baca seluruh tabel. Ambil 3–4 contoh: architecture, feature dev, product design, deploy. Tekankan: Imam Accountable untuk bidang, Zahid Accountable untuk dev operasional.

**Pesan utama:**
Setiap workstream punya R/A/C/I yang jelas — tidak ada yang ambiguity tentang siapa mengerjakan apa.

---

## Slide 14 [Wajib] — Cara Kerja: Trunk-Based Development
**Ritme bicara:** 2–3 menit
- Semua integrate ke `master` **setidaknya harian**.
- Branch fitur pendek (< 2 hari) → PR → review → merge.
- `master` selalu deployable.
- Branch naming: `feat/`, `fix/`, `docs/`, `chore/`, `refactor/`.
- Setiap branch punya worktree sendiri (lazyworktree) + Postgres terisolasi.
- Pre-PR: `bun run check`, `check-types`, `test`.

**Arah bicara:**
Jelaskan untuk PM juga — mereka perlu tahu alurnya walau tidak ngoding. Tekankan: branch pendek, sering merge, tidak ada branch lama. Pre-PR checklist wajib sebelum buka PR.

**Pesan utama:**
Kita bekerja trunk-based: integrate harian, branch pendek, PR dengan review — master selalu deployable.

---

## Slide 15 [Wajib] — Code Review Policy
**Ritme bicara:** 3 menit
- **Aturan inti: 2 reviewers + 1 local retest oleh orang ketiga sebelum merge.**
- Tidak ada exception untuk "PR kecil" atau "fix typo".
- Reviewer 1 (architectural): Zahid atau delegate — scope, design, contracts.
- Reviewer 2 (domain): domain owner per RACI — implementation correctness.
- Retester (third person): pull branch, jalankan app, exercise behavior, konfirmasi criteria.
- PR target < 400 lines. Squash-merge ke master.

**Arah bicara:**
Ini adalah aturan paling penting untuk kualitas. Jelaskan kenapa 3 pasang mata: 2 reviewer + 1 retester. Tidak ada shortcut. Kalau PR stuck > 24 jam, escalate ke Tech Lead.

**Pesan utama:**
Setiap PR diverifikasi oleh 3 orang: 2 reviewer + 1 retester — tanpa exception.

---

## Slide 16 [Opsional] — Cadence Pertemuan
**Ritme bicara:** 1–2 menit
- **Product Meeting**: bulanan, 90 min — prioritized backlog, milestone progress.
- **Dev Sync**: mingguan (Senin), 30 min — blockers, PR queue.
- **Retrospective**: bulanan — process improvements.
- Output meeting committed ke `docs/ops/` dalam 48 jam — tidak ada notes di luar repo.

**Arah bicara:**
Ringkas. Tekankan: output meeting selalu di repo, bukan di Slack/Notion terpisah.

**Pesan utama:**
Kita punya ritme: product meeting bulanan, dev sync mingguan — output selalu di repo.

---

## Slide 17 [Wajib] — Langkah Berikutnya
**Ritme bicara:** 2–3 menit
- **Minggu 1**: Onboarding — setup environment, worktree, akses repo.
- **Zahid**: selesaikan core baseline arsitektur agar Dzaky/Anaz/Faiz bisa mulai build.
- **PM (Shofi/Taufik/Tahzan)**: mulai audit kebutuhan produk — parity audit jamaah app, domain MVP scope.
- **Dev (Dzaky/Anaz/Faiz)**: familiarisasi codebase (`apps/native`, `packages/api`, `apps/server`).
- **Semua**: baca `docs/ops/` — mulai dari roadmap, roster, engineering process.
- Dev Sync pertama: Senin depan.

**Arah bicara:**
Ini adalah call to action konkret. Setiap orang tahu apa yang dilakukan minggu pertama. Tekankan: Zahid bangun baseline dulu, PM mulai audit, dev familiarisasi.

**Pesan utama:**
Minggu pertama: onboarding + Zahid selesaikan baseline + PM mulai audit kebutuhan + dev familiarisasi codebase.

---

## Slide 18 [Wajib] — Penutup
**Ritme bicara:** 2–3 menit
- Tim ini punya peran strategis: mewujudkan Al Khidmah Oase Dunia lewat teknologi.
- Kita bukan sekadar ngoding — kita membangun alat yang melayani jamaah dan mensyiarkan nilai Al Khidmah.
- Setiap orang di tim ini penting — dev, PM, leadership.
- Kita punya arah yang jelas: H-3 HAF Okt 2026, HAF Jan 2027.
- Mari mulai.

**Arah bicara:**
Penutup harus membangun rasa kepemilikan dan tekad. Sampaikan dengan hangat. Akhiri dengan ajakan konkret: Dev Sync Senin depan, baca docs/ops/. Tim harus merasa siap memulai.

**Pesan utama:**
Kita adalah tim yang mewujudkan Al Khidmah Oase Dunia lewat teknologi — mari mulai.

---

## Jumlah slide: 18
## Estimasi total waktu: 30–35 menit
