# Prompt NotebookLM: Generate Detailed Deck

## Instruksi

Buatkan slide deck detailed-style untuk laporan pertanggungjawaban Bidang Dana dan Usaha Pengurus Pusat Jama'ah Al Khidmah, masa khidmat 2022-2026, yang disampaikan di MUNAS 24-25 April 2026 di Hotel Royal Orchid, Batu Malang.

## Format

- **Bahasa**: Bahasa Indonesia
- **Gaya**: Detailed-style — konten lengkap di setiap slide, bisa berdiri sendiri tanpa pembicara
- **Jumlah slide**: 22-26 slide
- **Target durasi**: ±25-30 menit (jika dipresentasikan) atau dokumen mandiri

## Konteks Penting

- Ketua Bidang Dana dan Usaha, **Pak Yaumi Azhar, telah Almarhum**. Penyampaian LPJ di MUNAS ini diwakilkan oleh Ketua Umum PP Al Khidmah; cukup dicantumkan singkat di cover atau disampaikan lisan.
- Audiens: Pengurus Pusat, PW, PD, PC, dan jama'ah Al Khidmah se-Indonesia
- Versi detailed ini bisa digunakan sebagai dokumen pendukung yang dibagikan ke peserta setelah MUNAS

## Sumber yang Diprioritaskan

1. **`sources/references/laporan-akhir.md`** — Sumber kebenaran, semua angka dan data dari sini
2. **`sources/context/brief.md`** — Konteks event, pembicara, audiens
3. **`sources/context/structure.md`** — Narasi dan alur presentasi
4. **`sources/outlines/detailed.md`** — Outline slide-by-slide (IKUTI INI)
5. **`sources/references/data-chart.md`** — Data siap visual untuk grafik
6. **`sources/references/images/`** — Aset gambar untuk visual slide

## Alur Narasi

Ikuti alur LPJ (bukan pitch deck), namun setiap slide memiliki konten yang lebih lengkap:

1. **Pembukaan spiritual** — Dawuh + AD/ART + Visi (lebih detail)
2. **Laporan kinerja** — Semua pencapaian dengan data lengkap dan narasi
3. **Proyeksi masa depan** — Program 2026-2029 dengan detail implementasi
4. **Penutup** — Kesimpulan LPJ dan tantangan utama

## Hal-hal yang HARUS Ada

- Semua yang ada di presenter deck, PLUS:
- Kutipan lengkap dawuh Hadrotusyaikh RA (bukan ringkasan)
- Cantumkan *in memoriam* secara kecil dan sopan di cover (tanpa membuat slide khusus)
- Detail skema bisnis sarung (harga produksi, jual, margin, royalti)
- 3 motif sarung dengan nama dan varian warna lengkap
- Catatan evaluasi pemanfaatan QRIS (gunakan redaksi netral sesuai LPJ; jangan framing konflik)
- 5 tahapan implementasi budidaya lele
- Konsep dan fungsi Khidmah Connect (cukup ringkas sesuai outline)
- Tabel investasi Khidmah Connect (3 modul vs 11 modul)
- Visi "The Next Generation of Al Khidmah"
- Gunakan gambar langsung dari `sources/references/images/` di slide yang sesuai
- Untuk slide Dawuh: gunakan placeholder (tanpa foto manusia) `sources/references/images/placeholder-dawuh-hadrotussyaikh.png` dan tambahkan foto asli secara manual di luar NotebookLM bila dibutuhkan.
- Wajib buat chart data berikut (bar chart sederhana, clean):
  - Bar chart kontribusi PT DBL (modal vs dividen)
  - Bar chart skema bisnis sarung (harga produksi vs harga jual vs margin)
  - Bar chart target vs realisasi Modal Abadi + (opsional) chart nilai CSR (boleh digabung atau dipisah)
  - Bar chart investasi Khidmah Connect (3 modul vs 11 modul)
  - (Opsional) Bar chart perbandingan angka acuan per kelompok program

## Penutup

- Akhiri dengan penutup yang human: apresiasi, mohon doa/masukan, dan ajakan sinergi yang rendah hati (bukan promosi)

## Hal-hal yang TIDAK BOLEH

- Jangan buat slide yang terlalu ringkas — ini detailed deck, konten harus cukup untuk dibaca mandiri
- Jangan gunakan jargon bisnis berlebihan
- Jangan abaikan konteks spiritual dan penghormatan almarhum
- Jangan tambahkan informasi yang tidak ada di sumber referensi
- Jangan gunakan pie chart jika data bukan bagian dari satu total yang sama

## Tone & Nuansa

- Akuntabel, dokumentatif, profesional, hangat, dan rendah hati
- Tapi lebih informatif dan dokumentatif — cocok sebagai bahan bacaan
- Setiap slide harus bisa dipahami tanpa penjelasan lisan

## Perbedaan dari Presenter Deck

| Aspek | Presenter | Detailed |
|-------|-----------|----------|
| Teks per slide | Ringkas, poin | Lengkap, naratif |
| Jumlah slide | 22-25 | 22-26 |
| Penggunaan | Presentasi lisan | Dokumen mandiri |
| Angka/data | Highlight utama | Detail lengkap |
