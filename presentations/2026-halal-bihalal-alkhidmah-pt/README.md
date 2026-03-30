# 2026 Halal Bi Halal — Strategi Pengembangan Al Khidmah di Perguruan Tinggi

Presentasi untuk Halal Bi Halal Bidang Pemuda dan Pelajar Pengurus Pusat Jama'ah Al Khidmah dengan tema **Strategi Pengembangan Al Khidmah di Perguruan Tinggi**.

## Konteks

- **Acara**: Halal Bi Halal Bidang Pemuda dan Pelajar Pengurus Pusat Jama'ah Al Khidmah
- **Tanggal**: 1 April 2026
- **Posisi**: Materi ke-4 (setelah materi Kolaborasi dengan PERGUNU)
- **Durasi**: ~30 menit
- **Pembicara**: Mas Deda
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
- `prompts/generate-detailed.md` — untuk deck lengkap (14–18 slide)
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

- Kutipan dari Hadrotusyeikh KH. Achmad Asori Al Ishaqi RA harus ditampilkan dengan respek dan lengkap.
- Tiga alasan mengapa Al Khidmah di PT sangat perlu adalah bagian terpenting.
- Data statistik harus mendukung pesan, bukan menguasai — fokus pada makna.
- Ekosistem pemuda pelajar (TPQ → PT) harus jelas.
- Penutup harus membangun tekad — "Al Khidmah adalah kebutuhan".

## Catatan data

Data statistik telah **✅ DIVERIFIKASI** dengan sumber resmi (Maret 2026):
- BPS (Badan Pusat Statistik) — https://www.bps.go.id/
- Kemendikdasmen — https://data.kemendikdasmen.go.id/
- Kemenag — https://satudata.kemenag.go.id/

Lihat detail verifikasi di `sources/references/data-statistik.md`.