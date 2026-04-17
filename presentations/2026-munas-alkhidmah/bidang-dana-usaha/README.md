# Laporan Pertanggungjawaban Bidang Dana dan Usaha — MUNAS Al Khidmah 2026

Presentasi laporan pertanggungjawaban Bidang Dana dan Usaha Pengurus Pusat Jama'ah Al Khidmah untuk MUNAS 24-25 April 2026.

## Konteks

- **Acara**: Musyawarah Nasional (MUNAS) Jama'ah Al Khidmah
- **Tanggal**: 24-25 April 2026
- **Lokasi**: Royal Orchid Garden Hotel, Batu Malang
- **Periode LPJ**: Masa Khidmat 2022-2026
- **Arah proyeksi**: Masa Khidmat 2026-2029
- **Ketua Bidang**: Pak Yaumi Azhar (Almarhum)
- **Penyampai laporan**: Ketua Umum PP Jama'ah Al Khidmah

## Prinsip Paket Sumber

- `sources/context/brief.md` dipertahankan sebagai pengarah tone, audiens, tujuan, dan konteks emosional.
- File lain ditulis ulang berdasarkan dokumen final `DRAFT BIDANG DANA USAHA (1).docx`.
- Presentasi mengikuti alur: **landasan → kinerja 2022-2026 → proyeksi 2026-2029 → kesimpulan & tantangan**.
- Nada harus **spiritual, akuntabel, strategis, dan tetap rendah hati**.

## Struktur Folder

```text
sources/
├── context/
│   ├── brief.md
│   └── structure.md
├── outlines/
│   ├── presenter.md
│   └── detailed.md
└── references/
    ├── laporan-akhir.md
    ├── data-chart.md
    └── images/
prompts/
├── generate-presenter.md
├── generate-detailed.md
└── revise.md
output/
```

## Workflow NotebookLM

### 1. Upload ke NotebookLM

Upload minimal:
- `sources/context/brief.md`
- `sources/context/structure.md`
- `sources/outlines/presenter.md` atau `sources/outlines/detailed.md`
- `sources/references/laporan-akhir.md`
- `sources/references/data-chart.md`
- gambar yang relevan di `sources/references/images/`

### 2. Generate

Gunakan prompt:
- `prompts/generate-presenter.md` — deck presenter, ringkas, untuk penyampaian lisan
- `prompts/generate-detailed.md` — deck lebih lengkap, dapat dibaca mandiri
- `prompts/revise.md` — revisi ringan setelah generate

### 3. Setelah Generate

- Tambahkan manual foto **KH. Achmad Asrori Al-Ishaqi RA** pada slide landasan bila diperlukan.
- Tinjau kembali akurasi angka agar tetap sesuai `sources/references/laporan-akhir.md`.
- Gunakan revisi ringan untuk wording/layout; untuk perubahan struktur besar, generate ulang dari prompt utama.

## Aset Visual

Folder `sources/references/images/` tetap dipakai sebagai inventaris visual lokal untuk:
- kandang PT Dujaj Berkah Lestari
- tiga motif sarung tenun gloyor
- budidaya lele
- menu PPOB
- foto KH. Achmad Asrori Al-Ishaqi RA (tambahkan manual setelah generate)

## Catatan Penting

- Jangan menambah fakta baru di luar DOCX final.
- Jangan mengubah capaian yang belum maksimal menjadi seolah-olah sudah berhasil penuh.
- Presentasi ini adalah **LPJ**, bukan pitch deck bisnis murni.
