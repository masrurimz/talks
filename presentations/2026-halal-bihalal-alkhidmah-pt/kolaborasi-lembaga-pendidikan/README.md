# 2026 Halal Bi Halal — Kolaborasi Al Khidmah di Lembaga Pendidikan

Presentasi untuk Halal Bi Halal Bidang Pemuda dan Pelajar Pengurus Pusat Jama'ah Al Khidmah dengan tema **Kolaborasi Al Khidmah di Lembaga Pendidikan (PERGUNU atau lainnya)**.

## Konteks

- **Acara**: Halal Bi Halal Bidang Pemuda dan Pelajar Pengurus Pusat Jama'ah Al Khidmah
- **Tanggal**: 1 April 2026
- **Posisi**: Materi ke-3 (sebelum materi Strategi Pengembangan Al Khidmah di Perguruan Tinggi oleh Mas Deda)
- **Durasi**: ~30 menit
- **Pembicara**: Dr. Aris Adi Laksono
- **Audiens**: Pengurus pusat-daerah dan mahasiswa-mahasiswi

## Struktur folder

```
├── sources/              # File untuk diunggah ke NotebookLM
│   ├── context/          # Brief pembicara, audiens, dan arahan struktur
│   │   ├── brief.md
│   │   ├── structure.md
│   ├── outlines/         # Outline slide (presenter dan detailed)
│   │   ├── presenter.md
│   │   ├── detailed.md
│   └── references/       # Bahan utama dan data statistik
│       ├── bahan-utama.md
│       ├── data-statistik.md
├── prompts/              # Prompt untuk dipaste ke NotebookLM
│   ├── generate-presenter.md
│   ├── generate-detailed.md
│   ├── revise.md
├── output/               # Hasil generate dari NotebookLM
└── README.md
```

## Workflow NotebookLM

### 1. Unggah sources

Unggah file berikut ke NotebookLM:
- `sources/context/brief.md`
- `sources/context/structure.md`
- `sources/outlines/presenter.md` atau `sources/outlines/detailed.md`
- `sources/references/bahan-utama.md`
- `sources/references/data-statistik.md`

### 2. Paste prompt

Gunakan prompt dari folder `prompts/`:
- `prompts/generate-presenter.md` — untuk deck presenter (12–15 slide)
- `prompts/generate-detailed.md` — untuk deck lengkap (16–20 slide)
- `prompts/revise.md` — untuk revisi ringan

### 3. Pengaturan

**Presenter deck**:
- Format: Slide Presenter
- Bahasa: Indonesia
- Panjang: Long

**Detailed deck**:
- Format: Presentasi Mendetail
- Bahasa: Indonesia
- Panjang: Long

## Prinsip penting

- Kutipan dari Hadrotusyeikh KH. Achmad Asrori Al-Ishaqy RA harus ditampilkan dengan respek dan lengkap.
- 4 teladan pendiri (Majlis di Akademisi, di Pemerintah, Pembimbingan Anak Muda, Organisasi Profesional) adalah inspirasi konkret.
- Data perkembangan wilayah/daerah/luar negeri harus akurat dan mendukung narasi.
- Strategi kolaborasi harus terasa aplikatif, bukan hanya teori.
- **GAMBAR** (peta Indonesia, peta global, foto KH. Achmad Asrori) akan ditambahkan manual setelah generate.

## Catatan data

Data statistik telah **✅ DIVERIFIKASI** dari presentasi asli:
- **Sumber**: "Strategi Pengembangan alkhidmah pada lingkugan pendidikan.pptx"
- **Metode**: python-pptx (library Python untuk membaca file PPTX)
- **Data yang diekstrak**: 4 chart pada Slide 7 (COLUMN_STACKED)
- **Tanggal ekstraksi**: 1 April 2026

Lihat detail data di `sources/references/data-statistik.md`.

## Gambar yang perlu ditambahkan

Setelah generate deck di NotebookLM, tambahkan gambar berikut:

1. **Foto KH. Achmad Asrori Al-Ishaqy RA** — pada slide Landasan Utama
   - File: `sources/references/gambar-kh-achmad-asrori.png` (foto utama)
   - File: `sources/references/gambar-kh-achmad-asrori-2.png` (foto alternatif)
2. **Peta Indonesia** — pada slide Pengembangan Wilayah Indonesia (opsional)
   - File: `sources/references/peta-indonesia.png`
3. **Peta Global** — pada slide Pengembangan Wilayah Luar Negeri (opsional)
   - File: `sources/references/peta-global.png`

Semua gambar sudah dalam format PNG dan siap digunakan di NotebookLM.

## Keterkaitan dengan presentasi lain

- **Materi ini (Materi 3)**: Kolaborasi Al Khidmah di Lembaga Pendidikan (PERGUNU atau lainnya)
- **Materi berikutnya (Materi 4)**: Strategi Pengembangan Al Khidmah di Perguruan Tinggi oleh Mas Deda
- Ada keterkaitan antara kolaborasi dengan PERGUNU dan strategi pengembangan di PT
