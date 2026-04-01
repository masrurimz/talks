# 2026 Ramadhan - Digital Challenges

Presentasi sesi 1 acara refleksi Nuzulul Qur'an dengan tema **Al-Qur'an menjawab problematika zaman**.

## Konteks

- **Acara**: Refleksi Nuzulul Qur'an
- **Tema besar**: Al-Qur'an menjawab problematika zaman
- **Posisi**: Sesi 1 (pembuka fenomena dari sudut pandang praktisi/akademisi Geomatika)
- **Durasi**: ~30 menit
- **Fokus utama**: Media sosial (game online dan judi online disentuh secukupnya)

## Struktur folder

```
├── sources/              # File untuk diunggah ke NotebookLM
│   ├── context/          # Brief pembicara, audiens, dan arahan struktur
│   ├── outlines/         # Outline slide (presenter dan detailed)
│   └── references/       # Bahan bacaan dan data statistik
├── prompts/              # Prompt untuk dipaste ke NotebookLM
├── output/               # Hasil generate dari NotebookLM
└── README.md
```

## Workflow NotebookLM

### 1. Unggah sources

Unggah file berikut ke NotebookLM:
- `sources/context/brief.md`
- `sources/context/structure.md`
- `sources/outlines/presenter.md` atau `sources/outlines/detailed.md`
- `sources/references/bahan-bacaan.md`
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
- Panjang: Default atau Long

**Detailed deck**:
- Format: Presentasi Mendetail
- Bahasa: Indonesia
- Panjang: Long

## Prinsip penting

- Media sosial harus menjadi fokus utama
- Game online dan judi online hanya secukupnya
- Penjelasan teknis harus sederhana dan membumi
- Penutup harus menjembatani ke sesi 2