# 2026 RAKERWIL — PW Jama'ah Al Khidmah & Ath Thoriqoh Jawa Tengah

Event series: Rapat Kerja Wilayah (RAKERWIL) II Al Khidmah dan Ath Thoriqoh Jawa Tengah Tahun 2026.

## Event details

- **Tanggal**: Jumat, 15 Mei 2026 (27 Dzul Qo'dah 1447 H)
- **Waktu**: 07.00 – selesai (full day)
- **Lokasi**: Semarang, Jawa Tengah
- **Format**: Rapat kerja wilayah dengan sidang pleno dan sidang komisi bidang-bidang
- **Penyelenggara**: Pengurus Wilayah (PW) Jama'ah Al Khidmah Jawa Tengah & Ath Thoriqoh Jawa Tengah

## Presentations

| Folder          | Title                                      | Status | Presenter |
|-----------------|--------------------------------------------|--------|-----------|
| `bidang-majlis/` | Bidang Majlis — Target Kegiatan Majlis Jawa Tengah 2026 | Draft | H. Syakroni, S.Pd. |
| `sop-standar-operating-prosedur/` | SOP Kegiatan Al Khidmah | Draft | Ustadz Hasyim |

## Structure

Event series ini berisi **dua presentasi** yang disampaikan dalam sesi yang sama:

1. **Bidang Majlis** (H. Syakroni, S.Pd.) — paparan target kegiatan majlis 2026
2. **SOP Kegiatan Al Khidmah** (Ustadz Hasyim) — pedoman standar pelaksanaan majlis dan kegiatan Al Khidmah, disampaikan setelah paparan Bidang Majlis

Setiap presentasi mengikuti struktur standar repo:
```
presentation-folder/
├── sources/
│   ├── context/
│   │   ├── brief.md
│   │   └── structure.md
│   ├── outlines/
│   │   ├── presenter.md
│   │   └── detailed.md
│   └── references/          # clean, structured .md (reformatted for readability)
├── prompts/
│   ├── generate-presenter.md
│   ├── generate-detailed.md
│   └── revise.md
├── output/
└── README.md
```

## Workflow

Lihat README presentasi individual untuk detail NotebookLM.

## Catatan

- Kedua presentasi disiapkan untuk keperluan **Sidang Komisi** dan paparan hasilnya di Sidang Pleno II.
- **Bidang Majlis**: fokus pada target HAF Surabaya & HAF Meteseh 2026, skema pembiayaan, perubahan pengelolaan Majlis 11an, skema Tuan Rumah Mandiri, serta program Qiyamullail dan majlis rutin zonasi.
- **SOP**: fokus pada pedoman pelaksanaan majlis, kriteria imam, adab, prosedur bacaan, pra/pasca majlis, dan evaluasi.
- Data per 15 Mei 2026 (dokumen Rakerwil).
- File asli (PDF dan PPTX) tetap ada di root repo jika suatu saat dibutuhkan untuk referensi layout.  
  File .md di references/ sudah dibersihkan dan diformat ulang menjadi Markdown yang rapi dan terstruktur (semua data asli tetap lengkap dan akurat). Ini yang digunakan untuk NotebookLM.
