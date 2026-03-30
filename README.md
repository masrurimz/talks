# Presentations Repository

Repositori untuk menyimpan semua slide deck dan material presentasi.

## Struktur

```
presentations/
├── YYYY-event-title/       # Presentasi berdasarkan event
│   ├── sources/            # File untuk NotebookLM
│   ├── prompts/            # Prompt untuk NotebookLM
│   ├── output/             # Hasil generate
│   └── README.md
├── _template/              # Template untuk presentasi baru
└── README.md
```

## Workflow NotebookLM

Setiap presentasi menggunakan workflow NotebookLM:

1. **Upload sources** — semua file di `sources/` diunggah ke NotebookLM
2. **Paste prompt** — gunakan prompt dari `prompts/` untuk generate
3. **Save output** — simpan hasil ke `output/`

## Cara membuat presentasi baru

1. Salin `_template/` ke `YYYY-event-title/`
2. Isi brief dan struktur di `sources/context/`
3. Buat outline di `sources/outlines/`
4. Tambahkan referensi di `sources/references/`
5. Siapkan prompt di `prompts/`
6. Generate via NotebookLM
7. Simpan hasil ke `output/`

## Daftar presentasi

| Folder | Event | Status |
|--------|-------|--------|
| 2026-ramadhan-digital-challenges | Refleksi Nuzulul Qur'an | Draft |