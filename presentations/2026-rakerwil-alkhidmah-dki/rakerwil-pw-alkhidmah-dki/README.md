# RAKERWIL PW Jama'ah Al Khidmah DKI Jakarta

## Presentasi Rapat Kerja Wilayah
**Masa Bakti 2023–2027**
**Minggu, 12 April 2026 | Amanaia Green Terrace TMII**

---

## Status
📋 Draft — Source files & prompts ready for NotebookLM

## Konteks
Presentasi laporan kepengurusan, keuangan, perkembangan majlis, dan program kewirausahaan untuk RAKERWIL PW Jama'ah Al Khidmah DKI Jakarta.

## Highlight
- 📊 Laporan keuangan total saldo Rp 494.773.712
- 🏗️ Progress Masjid Al Fithrah: 81.6% terbayar
- 🆕 Peluncuran Sarung "NDALEM AL KHIDMAH" oleh Gus Vaiq
- 💡 Strategi kolaborasi & kewirausahaan

## Workflow
```
sources/ → Upload ke NotebookLM → Paste prompts → Generate slides → Save ke output/
```

## File Structure
```
sources/
├── context/
│   ├── brief.md          — Identitas acara, speaker, audiens
│   └── structure.md      — Arc narasi dan sekuens
├── outlines/
│   ├── presenter.md       — Outline 16 slide presenter-style
│   └── detailed.md        — Outline 20 slide detailed-style
└── references/
    ├── laporan-keuangan.md
    ├── pembebasan-lahan-masjid-al-fithrah.md
    ├── perkembangan-majlis.md
    ├── sarung-ndalem-al-khidmah.md
    ├── tantangan-dan-strategi.md
    ├── profil-organisasi.md
    ├── inventaris-visual.md
    ├── poster-masjid-al-fithrah.jpeg       — Poster donasi Masjid Al Fithrah
    ├── peta-jabodetabek.png                 — Peta JABODETABEK
    ├── portrait-kh-achmad-asrori.png        — ⚠️ Upload MANUAL ke PowerPoint (wajah)
    ├── chart-cashflow-koperasi.jpeg         — Grafik tren cashflow
    ├── sarung-motif-1.jpeg                  — Motif 1 sarung NDALEM AL KHIDMAH
    ├── sarung-motif-2.jpeg                  — Motif 2 sarung NDALEM AL KHIDMAH
    └── sarung-motif-3.jpeg                  — Motif 3 sarung NDALEM AL KHIDMAH
prompts/
├── generate-presenter.md  — Prompt untuk presenter deck
├── generate-detailed.md   — Prompt untuk detailed deck
└── revise.md             — Prompt untuk revisi
output/                    — Hasil NotebookLM (belum ada)
```

## Gambar yang Perlu Ditambahkan

Setelah generate deck di NotebookLM, tambahkan gambar berikut:

1. **Foto KH. Achmad Asrori Al-Ishaqy RA** — pada slide Landasan/Kutipan Hadrotusyeikh
   - ⚠️ **Tambahkan manual** setelah generate (NotebookLM membatasi gambar dengan wajah)
   - File: `sources/references/portrait-kh-achmad-asrori.png`
2. **Poster Masjid Al Fithrah** — pada slide Pembebasan Lahan
   - File: `sources/references/poster-masjid-al-fithrah.jpeg`
3. **Peta JABODETABEK** — pada slide Peta Majlis dan Tantangan Kewilayahan
   - File: `sources/references/peta-jabodetabek.png`
4. **Grafik Cashflow** — pada slide Laporan Koperasi
   - File: `sources/references/chart-cashflow-koperasi.jpeg`
5. **Sarung NDALEM AL KHIDMAH** (3 motif) — pada slide peluncuran sarung
   - File: `sources/references/sarung-motif-{1,2,3}.jpeg`

Lihat detail lengkap di `sources/references/inventaris-visual.md`.

## Penamaan yang Distandarkan

Untuk konsistensi, gunakan penamaan berikut di semua slide:
- **KH. Achmad Asrori Al-Ishaqy** (bukan Asrory, Asrori saja, atau Al Ishaqi)
- **Masjid Al Fithrah** (dengan 'h')
- **Jama'ah Al Khidmah** (dengan apostrof)
- **Al Munawwarah** (dobel 'w')
- **At Taqwa** (dengan spasi)
- **JABODETABEK** untuk wilayah cakupan

## Catatan Data

- Data keuangan: per **11 April 2026** (saldo kegiatan), per **Maret 2026** (koperasi)
- Progress tanah: per **April 2026**
- Sarung: HPP Rp 65.000 sudah termasuk royalti Rp 2.000/pcs