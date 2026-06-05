# Bidang Majlis — Target Kegiatan Majlis Jawa Tengah 2026

## Presentasi Rapat Kerja Wilayah (RAKERWIL) II
**Al Khidmah dan Ath Thoriqoh Jawa Tengah**  
**Jumat, 15 Mei 2026 (27 Dzul Qo'dah 1447 H) | Semarang**

---

## Status
📋 Draft — Source files & prompts ready for NotebookLM

## Konteks
Presentasi **Bidang Pembinaan Majlis** untuk RAKERWIL II PW Al Khidmah & Ath Thoriqoh Jawa Tengah 2026. Difokuskan pada target data kegiatan majlis tahun 2026, dengan penekanan pada:
- Persiapan HAF Surabaya (sebagai icon per amanat Munas 2026) + Posko PW Jateng
- HAF Meteseh 2026 (target dana Rp 1,4 Miliar + skema pembiayaan + kerja bakti)
- Perubahan pengelolaan Majlis Sewelasan (11an) dan skema Tuan Rumah Mandiri
- Program pendukung: Haul Akbar Jateng, Qiyamullail, dan Majlis Rutin untuk daerah zonasi

Sumber utama: dokumen resmi "Rakerwil 2026 Bidang Majlis" yang disiapkan untuk Sidang Komisi.

## Highlight Angka & Skema Penting
- **HAF Meteseh 2026**: Ahad 02 Agustus 2026, target total **Rp 1.400.000.000**
- **Pagu Daerah utama**: Rp 515.000.000 (31 daerah/korda)
  - Tertinggi: Kota Semarang **Rp 45.000.000**
  - Besar: Kab. Demak & Grobogan **Rp 65.000.000** masing-masing
- **Tiga sumber besar lain**: Donatur Khusus (250 jt), Amplop Arwah Jamak (250 jt), Kotak Amal (150 jt)
- **Tuan Rumah Mandiri 11an** (8 daerah @ Rp 15.000.000 cash):
  - Kota Semarang, Kab. Pemalang, Kab. Grobogan, Kab. Demak, Kab. Kudus, Kab. Kendal, Kab. Semarang, Kab. Jepara
- **Kerja Bakti HAF**: Juni (minggu 4) + Juli (minggu 1–5)
- **7 daerah zonasi** untuk Majlis Rutin bulanan (Temanggung, Kebumen, Banjarnegara, Cilacap, Banyumas, Korda Klaten, Korda Wonosobo)
- Kebutuhan cash minimal per Majlis 11an: **Rp 15.000.000**

## Workflow
```
sources/ → Upload ke NotebookLM → Paste prompts → Generate slides → Save ke output/
```

## File Structure
```
bidang-majlis/
├── sources/
│   ├── context/
│   │   ├── brief.md                    — Identitas acara, speaker H. Syakroni S.Pd., audiens PD se-Jateng, tujuan
│   │   └── structure.md                — Arc narasi + 8 sekuens section + batasan konten
│   ├── outlines/
│   │   ├── presenter.md                — Outline 14–15 slide (ringkas, visual)
│   │   └── detailed.md                 — Outline 15–18 slide (data-rich + tabel lengkap)
│   └── references/
│       ├── bidang-majlis-target-2026.md      — Clean, structured Markdown version of "Rakerwil 2026 Bidang Majlis" (primary data source)
│       └── rundown-rakerwil-2026.md          — Clean schedule version of the Master Rundown (context for komisi & timing)
├── prompts/
│   ├── generate-presenter.md           — Prompt untuk deck presenter (14–16 slide)
│   ├── generate-detailed.md            — Prompt untuk deck detailed (data lengkap)
│   └── revise.md                       — Prompt revisi
├── output/                             — Hasil NotebookLM (belum ada)
└── README.md
```

## Penamaan yang Distandarkan (untuk konsistensi slide)
- **Jama'ah Al Khidmah** (dengan apostrof)
- **Ath Thoriqoh** (bukan Thoriqoh saja di konteks formal)
- **Majlis Sewelasan** atau **Majlis 11an**
- **Tuan Rumah Mandiri** (bukan "mandiri" kecil)
- **Pagu Daerah** (bukan "pagu daerah")
- **PP Assalafi Al Fithrah Meteseh** (nama lengkap pondok)
- **Masjid Agung Jawa Tengah (MAJT)**
- **HAF Surabaya** dan **HAF Meteseh 2026** (bedakan jelas)
- Daftar daerah: gunakan persis "Kab. Grobogan", "Pekalongan Raya", "Tegal Raya", "Korda. Klaten", "Korda. Wonosobo"

## Catatan Data
- Semua target 2026 vs realisasi 2025 diambil dari dokumen resmi Rakerwil 2026 Bidang Majlis (per Mei 2026)
- Angka pembiayaan dalam Rupiah penuh (tidak dibulatkan)
- 8 daerah Tuan Rumah Mandiri dan daftar gabungan adalah usulan yang akan difinalisasi di Rapat PW
- Jadwal kerja bakti Juni–Juli 2026 bersifat tentatif, finalisasi via Rapat Pengurus Wilayah

## Langkah Setelah Generate di NotebookLM
1. Review output di PowerPoint / Google Slides
2. Sesuaikan visual (logo Al Khidmah, warna hijau brand)
3. Jika ada slide dengan wajah atau foto sensitif, tambahkan manual (NotebookLM sering membatasi)
4. Gunakan `prompts/revise.md` untuk iterasi berdasarkan feedback
5. Simpan final ke folder `output/`

## Penanggung Jawab Komisi (dari Rundown)
- **Ketua Sidang Komisi Bidang Pembinaan Majlis**: H. Syakroni, S.Pd. (Waket II PW Al Khidmah)
- **Notulen**: Muhammad Ghozali (Korbid Penataan Majlis)
- Hasil komisi akan dipaparkan di Sidang Pleno II dan diserahkan kepada Ketua PW Al Khidmah & Ketua PW Ath Thoriqoh

---

**Siap untuk NotebookLM.**  
Upload seluruh isi `sources/` (context/, outlines/, dan references/ — kedua file .md extracted sudah berisi teks lengkap).  
Paste prompt yang sesuai (`generate-presenter.md` atau `generate-detailed.md`).

Catatan: File PDF asli tetap tersimpan di `rakerwil/` (root repo) jika suatu saat butuh referensi layout asli.  
File .md di references/ sudah dibersihkan dan diformat ulang menjadi Markdown yang rapi (semua data asli 100% dipertahankan) — ini yang sebaiknya di-upload ke NotebookLM.
