# 2026 RAKERWIL — PW Jama'ah Al Khidmah & Ath Thoriqoh Jawa Tengah

Event series: Rapat Kerja Wilayah (RAKERWIL) II Al Khidmah dan Ath Thoriqoh Jawa Tengah Tahun 2026.

## Event details

- **Tanggal**: Jumat, 15 Mei 2026 (27 Dzul Qo'dah 1447 H)
- **Waktu**: 07.00 – selesai (full day)
- **Lokasi**: Semarang, Jawa Tengah
- **Format**: Rapat kerja wilayah dengan sidang pleno dan sidang komisi bidang-bidang
- **Penyelenggara**: Pengurus Wilayah (PW) Jama'ah Al Khidmah Jawa Tengah & Ath Thoriqoh Jawa Tengah

## Presentations

| Folder          | Title                                      | Status |
|-----------------|--------------------------------------------|--------|
| `bidang-majlis/` | Bidang Majlis — Target Kegiatan Majlis Jawa Tengah 2026 | Draft |

## Structure

Presentasi ini difokuskan pada **Bidang Pembinaan Majlis** (salah satu dari 4 komisi di Sidang Komisi Rakerwil).

Sumber utama:
- `bidang-majlis-target-2026.md` (target data kegiatan Bidang Majlis — clean structured Markdown)
- `rundown-rakerwil-2026.md` (konteks acara & penanggung jawab komisi — clean schedule)

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

- Presentasi ini disiapkan untuk keperluan **Sidang Komisi Bidang Pembinaan Majlis** dan paparan hasilnya di Sidang Pleno.
- Fokus utama: target HAF Surabaya & HAF Meteseh 2026, skema pembiayaan (Pagu Daerah + donatur), perubahan pengelolaan Majlis 11an, skema Tuan Rumah Mandiri, serta program Qiyamullail dan majlis rutin zonasi.
- Data per 15 Mei 2026 (dokumen Rakerwil).
- File PDF asli tetap ada di folder `rakerwil/` di root repo jika suatu saat dibutuhkan untuk referensi format/layout.  
  File .md di references/ sudah dibersihkan dan diformat ulang menjadi Markdown yang rapi dan terstruktur (semua data asli tetap lengkap dan akurat). Ini yang digunakan untuk NotebookLM.
