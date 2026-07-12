# Launching Tim Pengembangan IT — Runbook & Workflow

> **Status**: Active
> **Tanggal**: Selasa, 14 Juli 2026
> **Pembicara**: Zahid (Koordinator Pengembangan / Tech Lead)

## Tujuan

Deck kickoff untuk launching **Tim Pengembangan IT**, Bidang Media & IT PP Jama'ah Al Khidmah. Menyatukan pemahaman tim tentang visi, strategi, milestone, struktur peran, dan cara kerja sebelum eksekusi dimulai.

## Dua sesi pemakaian

| Sesi | Kapan | Audiens | Tujuan |
| --- | --- | --- | --- |
| **Review kepemimpinan** | Minggu 12 Jul 2026 (malam) | Imam (Ketua Bidang) + Dzaky (Sekretaris) | Sign-off framework sebelum diluncurkan ke tim |
| **Launch tim** | Selasa 14 Jul 2026 | Tim Pengembangan penuh | Onboarding: visi, strategi, milestone, peran, cara kerja |

## Struktur folder

```
sources/
├── context/
│   ├── brief.md        # Identitas pembicara, audiens, tujuan
│   └── structure.md    # Arahan struktur + urutan slide
├── outlines/
│   ├── presenter.md    # Outline presenter-style (slide-by-slide + coaching)
│   └── detailed.md     # Outline detailed-style (slide-by-slide, self-reading)
└── references/
    ├── referensi-strategi-dan-roadmap.md
    ├── referensi-milestone.md
    ├── referensi-tim-dan-raci.md
    └── referensi-engineering-process.md
prompts/
├── generate-presenter.md
├── generate-detailed.md
└── revise.md
```

## Workflow NotebookLM

1. Upload semua file di `sources/` ke NotebookLM.
2. Paste salah satu prompt di `prompts/` (`generate-presenter.md` atau `generate-detailed.md`).
3. Hasil slide disimpan ke `output/`.
4. Untuk revisi, paste `prompts/revise.md`.

AI assistant menyiapkan materials — user menjalankan NotebookLM.

## Referensi konvensi

Struktur dan gaya mengikuti: [`../../2026-halal-bihalal-alkhidmah-pt/pengembangan-pt/`](../../2026-halal-bihalal-alkhidmah-pt/pengembangan-pt/).
