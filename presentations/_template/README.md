# Template Presentasi

Salin folder ini untuk membuat presentasi baru.

## Struktur

```
├── sources/
│   ├── context/
│   │   ├── brief.md        # Brief pembicara dan audiens
│   │   ├── structure.md    # Arahan struktur presentasi
│   ├── outlines/
│   │   ├── presenter.md    # Outline presenter-style
│   │   ├── detailed.md     # Outline detailed
│   ├── references/         # Bahan referensi/research
├── prompts/
│   ├── generate-presenter.md  # Prompt generate presenter deck
│   ├── generate-detailed.md   # Prompt generate detailed deck
│   ├── revise.md              # Prompt revisi
├── output/                  # Hasil NotebookLM
└── README.md
```

## Workflow

1. Isi `sources/context/` dengan brief dan arahan
2. Buat outline di `sources/outlines/`
3. Tambahkan referensi di `sources/references/`
4. Siapkan prompt di `prompts/`
5. Unggah semua dari `sources/` ke NotebookLM
6. Paste prompt yang sesuai
7. Simpan hasil ke `output/`