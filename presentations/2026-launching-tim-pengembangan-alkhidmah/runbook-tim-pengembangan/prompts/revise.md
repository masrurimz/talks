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
- To-be: 1 super app (`my.alkhidmah.id`) + 1 thin landing (`alkhidmah.id`).
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

---

## Prioritas sumber untuk revisi:
1. `sources/context/brief.md` — cek audiens dan gaya.
2. `sources/context/structure.md` — cek proporsi dan urutan.
3. `sources/outlines/presenter.md` atau `detailed.md` — cek slide-by-slide.
4. `sources/references/referensi-tim-dan-raci.md` — cek tim & RACI.
5. `sources/references/referensi-milestone.md` — cek milestone.

---

## Catatan khusus:
- Revisi ringan, bukan rewrite total.
- Fokus pada ketidaksesuaian dengan arahan.
- Kalau ada slide terlalu padat, pisahkan.
- Kalau ada slide terlalu singkat, tambahkan substansi.
- **Faiz adalah developer ke-4** — pastikan muncul di slide tim dan peran. Dia mantan tim jamaah app, relevan untuk Stream A.
