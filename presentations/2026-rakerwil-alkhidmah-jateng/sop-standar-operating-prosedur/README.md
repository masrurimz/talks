# SOP Kegiatan Al Khidmah

## Standar Operating Prosedur Kegiatan Al Khidmah
**RAKERWIL II Al Khidmah dan Ath Thoriqoh Jawa Tengah**  
**Jumat, 15 Mei 2026 (27 Dzul Qo'dah 1447 H) | Semarang**

---

## Status
📋 Draft — Source files & prompts ready for NotebookLM

## Konteks
Presentasi **SOP Kegiatan Al Khidmah** untuk RAKERWIL II PW Al Khidmah & Ath Thoriqoh Jawa Tengah 2026. Disajikan **setelah** paparan Bidang Pembinaan Majlis dalam sesi yang sama.

Materi ini berisi pedoman lengkap pelaksanaan majlis dan kegiatan Al Khidmah, mulai dari:
- Pengertian Majlis Dzikir Al Khidmah dan Jama'ah Al Khidmah
- Kriteria Imam Majlis (status, suara, kemampuan bacaan)
- Adab (etika) peserta majlis
- Prosedur pelaksanaan tiap bagian bacaan (tawassul, istighatsah, Yasin, manaqib, maulid, doa, talqin, tahlil, iklil)
- Pra Majlis, Pelaksanaan, dan Pasca Majlis
- Evaluasi dan catatan penting untuk istiqomah

**Presenter**: **Ustadz Hasyim**

## Highlight Konten
- **15 slide asli** dari dokumen SOP resmi
- **3 Kriteria Imam Majlis**: khususi/kyai/ustadz/sesepuh, suara lantang, fasih kitab
- **8 Adab** peserta majlis
- **12 Prosedur bacaan** dari tawassul sampai sambutan
- **Pra–Pelaksanaan–Pasca** majlis
- **6 Catatan evaluasi** untuk perbaikan berkelanjutan

## Workflow
```
sources/ → Upload ke NotebookLM → Paste prompts → Generate slides → Save ke output/
```

## File Structure
```
sop-standar-operating-prosedur/
├── sources/
│   ├── context/
│   │   ├── brief.md                    — Identitas acara, presenter Ustadz Hasyim, audiens, tujuan
│   │   └── structure.md                — Arc narasi: "Standar yang Menyatukan — Adab yang Mengangkat"
│   ├── outlines/
│   │   ├── presenter.md                — Outline 12 slide (ringkas, visual)
│   │   └── detailed.md                 — Outline 15 slide (data-rich, detail lengkap)
│   └── references/
│       ├── sop-kegiatan-al-khidmah.md       — Clean structured Markdown dari PPT (primary source)
│       └── STANDAR OPERATING PROSEDUR (SOP).pptx — File asli
├── prompts/
│   ├── generate-presenter.md           — Prompt untuk deck presenter (12 slide)
│   ├── generate-detailed.md            — Prompt untuk deck detailed (15 slide)
│   └── revise.md                       — Prompt revisi
├── output/                             — Hasil NotebookLM (belum ada)
└── README.md
```

## Penamaan yang Distandarkan
- **Jama'ah Al Khidmah** (dengan apostrof)
- **Majlis Dzikir Al Khidmah**
- **Imam Khususi** / **Imam Majlis**
- **Istighatsah** (bukan istighosah)
- **Manaqib** (As Syaikh Abdul Qadir al-Jilany RA)
- **Maulid** Nabi besar Muhammad SAW
- **Iklil**
- **Tawassul**
- **Talqin**
- **Tahlil**
- **Tuma'ninah**, **Khusyu'**, **Istiqomah**
- **Wadhifah**
- **Adab**

## Catatan Data
- Semua prosedur dari dokumen SOP resmi Al Khidmah
- Imam khususi diharapkan terus belajar dan memperbaiki diri
- Evaluasi dilakukan setelah setiap majlis
- Dokumen ini disampaikan setelah paparan Bidang Majlis dalam sesi yang sama

## Langkah Setelah Generate di NotebookLM
1. Review output di PowerPoint / Google Slides
2. Sesuaikan visual (logo Al Khidmah, warna hijau brand)
3. Untuk slide adab: pastikan icon ✓ dan ✗ jelas
4. Untuk slide prosedur: pertimbangkan flowchart jika teks terlalu panjang
5. Gunakan `prompts/revise.md` untuk iterasi berdasarkan feedback
6. Simpan final ke folder `output/`

## Penanggung Jawab
- **Presenter**: Ustadz Hasyim
- Presentasi ini adalah bagian dari sesi RAKERWIL II 2026, disampaikan setelah paparan Bidang Pembinaan Majlis

---

**Siap untuk NotebookLM.**  
Upload seluruh isi `sources/` (context/, outlines/, dan references/).  
Paste prompt yang sesuai (`generate-presenter.md` atau `generate-detailed.md`).

Catatan: File PPTX asli tetap tersimpan di references/ jika suatu saat butuh referensi layout asli.  
File .md di references/ sudah dibersihkan dan diformat ulang menjadi Markdown yang rapi — ini yang sebaiknya di-upload ke NotebookLM.
