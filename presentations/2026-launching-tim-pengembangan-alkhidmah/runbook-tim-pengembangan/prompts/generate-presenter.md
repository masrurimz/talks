# Prompt untuk Generate Presenter Deck

## Instruksi untuk NotebookLM

Buat deck presentasi dengan format **Slide Presenter** untuk materi:

**Launching Tim Pengembangan IT**
**Visi, Strategi, dan Cara Kerja Menuju Super App Al Khidmah**

### Pengaturan:
- **Format**: Slide Presenter.
- **Bahasa**: Indonesia.
- **Panjang**: Long (untuk coverage lebih baik).

---

## Arahan isi:

### Judul dan pembuka:
- Judul utama: "Launching Tim Pengembangan IT".
- Subjudul: "Visi, Strategi, dan Cara Kerja Menuju Super App Al Khidmah".
- Nama pembicara: Zahid (Koordinator Pengembangan / Tech Lead).
- Konteks: Bidang Media & IT PP Jama'ah Al Khidmah, Selasa 14 Juli 2026.

### Fokus utama:
1. **Landasan spiritual** — visi Al Khidmah Oase Dunia, digitalisasi sebagai enabler.
2. **Strategi konsolidasi super app** — 3 app terpisah → 1 super app (`my.alkhidmah.or.id`) + 1 thin landing (`alkhidmah.or.id`). Kenapa Expo Web (shared codebase, responsive, satu auth cookie).
3. **Tiga stream migrasi** — A: jamaah→super app (H-3 HAF Okt'26); B: web→thin landing (HAF Jan'27); C: ZIS donasi→embedded dari hexa (Q2'27).
4. **Milestone terdekat: H-3 bulan HAF (Oktober 2026)** — readiness checkpoint, Stream A selesai, majlis MVP production-ready. HAF Januari 2027 = wide-usage launch.
5. **Tim aktual** — dev: Zahid (Tech Lead), Dzaky, Anaz (+ QA automation), Faiz (ex-jamaah app); product: Shofi, Taufik, Tahzan (PM + per-product QA); leadership: Imam (Ketua Bidang).
6. **Cara kerja engineering** — trunk-based development, code review (2 reviewer + 1 retest), cadence pertemuan.

### Proporsi yang diinginkan:
- Landasan + pembuka: 10%.
- Strategi + roadmap: 25% (bagian terbesar).
- Milestone: 15%.
- Tim & peran & RACI: 20%.
- Cara kerja engineering: 20%.
- Langkah berikutnya + penutup: 10%.

### Tim aktual (WAJIB pakai nama-nama ini):
- **Dev**: Zahid (Tech Lead, bangun baseline), Dzaky (developer, dual role Sekretaris), Anaz (developer + QA automation), Faiz (developer, mantan tim jamaah app).
- **Product**: Shofi, Taufik, Tahzan (Product Manager + per-product QA).
- **Leadership**: Imam (Ketua Bidang, Accountable).

### Milestone (WAJIB):
- **Milestone terdekat = H-3 bulan HAF (Oktober 2026)** — readiness checkpoint 3 bulan sebelum HAF.
- **HAF = Januari 2027** — wide-usage launch.
- **Haul Metesh sudah superseded** — JANGAN sebut sebagai milestone aktif.

### Gaya yang diinginkan:
- Jelas, terstruktur, formal namun hangat.
- Bahasa Indonesia sederhana. Istilah teknis (trunk-based, PR, RACI) dengan penjelasan singkat.
- Bukan korporat/kaku — ini organisasi keagamaan.
- Bukan seminar akademik, bukan ceramah motivasi tanpa substansi.
- Satu pesan utama per slide.

### Jumlah slide target:
- 16–18 slide untuk presenter-style.
- Durasi target: 30 menit.

### Visual yang diharapkan:
- Rapi, bersih, mudah dibaca.
- Tabel untuk tim, RACI, stream migrasi.
- Timeline untuk roadmap dan milestone.
- Tidak terlalu korporat.

---

## Prioritas sumber:
1. `sources/context/brief.md` — konteks, audiens, tujuan.
2. `sources/context/structure.md` — struktur narasi + urutan slide.
3. `sources/outlines/presenter.md` — slide-by-slide breakdown.
4. `sources/references/referensi-strategi-dan-roadmap.md` — strategi & roadmap.
5. `sources/references/referensi-milestone.md` — milestone detail.
6. `sources/references/referensi-tim-dan-raci.md` — tim & RACI.
7. `sources/references/referensi-engineering-process.md` — cara kerja.
8. `sources/references/referensi-arsitektur-dan-auth.md` — arsitektur, auth/OTP, kapasitas, tooling, infra.
9. `sources/references/referensi-public-portal-options.md` — portal options (separate, CMS+ABAC, WordPress).
10. `sources/references/referensi-document-management-options.md` — Google Workspace, self-hosted alternatives, signing options.

---

## Catatan khusus:
- Materi ini dipakai dua kali: review kepemimpinan (Minggu 12 Jul, Imam + Dzaky) dan launch tim (Selasa 14 Jul).
- **Haul Metesh (Sep 2026) sudah superseded** — milestone terdekat adalah H-3 bulan HAF (Oktober 2026).
- Tim adalah 7 orang: 4 developer + 3 product manager. Pakai nama asli, bukan placeholder.
- Audiens campuran teknis (dev) dan non-teknis (PM) — jangan terlalu jargon-heavy.
- **Desktop-first adaptive mobile** (bukan mobile-first) — info density lebih baik untuk dashboard/admin.
- **URL pakai `.or.id`** — `my.alkhidmah.or.id` dan `alkhidmah.or.id`, bukan `.id`.
- **Monorepo shared packages only** — per-feature packages deferred (Expo typed routes + client-server splitting belum stabil).
- **OTP via kirimdev.com** (WhatsApp, Rp 25K/mo). Customer-initiated messages untuk registrasi murah (free dalam 24h window).
- **ZIS donasi dari hexa** (embedded dengan shared auth), bukan ekhidmah store. Stream C = hexa.
- **Keuangan bukan bagian dari org/majlis** — domain terpisah.
- **Kapasitas ~10 jam/orang/2-minggu** (part-time, bukan full-time). Sprint 2-mingguan.
- **Tooling: GitHub Issues + Projects + markdown** (tidak pakai Jira/Trello/Notion).
- **Infra: Biznet Gio VPS** (self-hosted, no managed cloud) + kirimdev Rp 25K/mo.
- Deck menjadi **22 slide** (3 slide baru: Portal Options #9, Document Management Options #12, Signing & Parent→Child Access #13). Slide-slide decision `[Wajib — tonight]` untuk review Imam & Dzaky.
- **Portal: tampilkan OPSI, bukan satu keputusan** — Option B (CMS+ABAC) adalah rekomendasi, bukan final approval. Option C (WordPress) = pilot fallback. Option A = autonomy-only.
- **Document management: Google Workspace cost = USD reference** — jangan fabricate harga IDR. Tampilkan label "quote required".
- **Signing: open question** — tanyakan Imam/Dzaky apa definisi "official signing" untuk SK/surat. Jangan portray satu signing path sebagai sudah dipilih.
- **PP→child Drive: explicit Google Groups, bukan OU inheritance** — OU policy ≠ Drive membership inheritance. Folder/file permissions inherit within a drive only.
- **WPS = hosted integration platform, BUKAN open-source self-hosted** — jangan label sebagai self-hosted alternative.
- **Foundation baseline WIP** — Zahid target done end July. Folder structure: shared packages only.
