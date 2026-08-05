# PWA Demo — MAS Precast

Intro + referensi slides untuk **pilot/demo** Production Line Ops (companion GinaV2) bersama mitra PT MAS Precast. Bukan presentasi penjualan.

| Item | Detail |
|---|---|
| Event | PWA Demo to MAS Precast |
| Tanggal | Rabu, 5 Agustus 2026 · 15:00–16:30 |
| Sifat | Pilot / riset bersama mitra |
| Status | Draft (sources + prompts siap) |
| Bahasa | Indonesia |
| Format | Presenter + Detailed |

## Narasi deck
1. **Peran sederhana** dulu (Operator / Supervisor / Admin)
2. **Gambar besar proses**: mesin → sensor GinaV2 + app → diteliti bareng
3. Alur satu hari
4. Install PWA Android Chrome (Vysor untuk mirroring)
5. Transisi: penempatan orang→mesin dilakukan bareng saat sesi

> Penempatan peran/mesin/PIN **tidak** di deck — dilakukan saat sesi live.

## Isi folder
```
sources/
  context/     brief.md, structure.md
  outlines/    presenter.md, detailed.md
  references/  konteks produk, peran/agenda, install PWA, screenshot list, praktik demo
prompts/       generate-presenter.md, generate-detailed.md, revise.md
output/        (hasil NotebookLM — Anda yang isi)
```

## Cara pakai dengan NotebookLM
1. Buat notebook baru.
2. Upload semua file di `sources/`.
3. Paste `prompts/generate-presenter.md` → deck live.
4. Paste `prompts/generate-detailed.md` → handout/referensi.
5. Simpan hasil ke `output/`.
6. Rapikan dengan `prompts/revise.md` bila perlu.

AI assistant **tidak** menjalankan NotebookLM / tidak menghasilkan slide final di sini.

## Screenshot
Lihat `sources/references/screenshot-checklist.md` — ambil setelah dry-run.
