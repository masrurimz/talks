# Prompt revisi Renstra Bidang Pemuda

Gunakan prompt ini setelah NotebookLM menghasilkan deck pertama. Revisi deck tanpa mengubah isi sumber atau mengarang status pengesahan dan fakta yang belum diketahui.

## Tujuan revisi

Buat deck lebih mudah dipahami, mudah disampaikan dalam 15 menit, dan setia pada sumber. Deck harus membedakan arah, pointer, hasil yang diharapkan, usulan tambahan, dan informasi yang belum diketahui.

## Pemeriksaan wajib

Periksa dan koreksi setiap butir berikut:

1. Tujuan dan sasaran sesuai `sources/references/renstra-bidang-pemuda.md`.
2. Seluruh lima fokus strategis tampil dan berurutan.
3. Pointer dan hasil yang diharapkan sesuai sumber dan tidak diganti dengan daftar tugas final.
4. Tujuh prioritas program unggulan tampil dengan penamaan yang konsisten.
5. Tiga tahapan tampil tanpa rentang tahun atau tenggat tambahan.
6. Rumus IKU persis berikut:

   **IKU = (Jumlah program prioritas yang mencapai target outcome tahunan ÷ Jumlah seluruh program prioritas yang ditetapkan dalam Renstra) × 100%**

7. Lima indikator pendukung dan cara ukur sesuai sumber.
8. Tahun acara tidak ditegaskan. Tahun folder 2026 hanya label pengarsipan.
9. Jabatan, kredensial, tanggal, tempat, jumlah peserta, anggaran, dan status pengesahan tidak diarang.
10. Waktu presenter tetap tepat 15 menit.

## Revisi struktur

- Pertahankan alur: tujuan → masalah → lima fokus → program → prioritas → tahapan → IKU → ukuran keberhasilan.
- Bila slide terlalu padat, ringkas penjelasan lisan. Jangan menghapus pointer atau hasil yang diharapkan dari detailed deck.
- Bila presenter deck perlu dipadatkan, gabungkan dua bagian masalah. Jangan menghapus lima fokus, tujuh prioritas, tiga tahapan, rumus IKU, atau lima indikator.
- Ganti judul label menjadi judul pesan. Contoh:
  - “Pointer” menjadi “Jaringan yang Harus Dipetakan”;
  - “Program” menjadi “Komunitas Menjadi Wadah Pembinaan”;
  - “Indikator” menjadi “Program Prioritas yang Mencapai Target Outcome Tahunan”.

## Revisi isi

- Ubah klaim pasti menjadi redaksi yang setia pada sumber. Gunakan “hasil yang diharapkan”, bukan “hasil yang sudah tercapai”.
- Ubah daftar tugas final menjadi “pointer kegiatan” atau “usulan untuk dibahas”.
- Hapus target numerik, tanggal, tenggat, anggaran, penanggung jawab, data, jumlah kader, dan keputusan yang tidak ada dalam sumber.
- Beri label **tidak diketahui** bila mengingatkan informasi acara atau target outcome yang belum tersedia.
- Jangan menyajikan Renstra sebagai keputusan Rakernas.
- Jangan mengatribusikan quote baru kepada Dida atau tokoh lain.
- Buat istilah konsisten: jejaring pendidikan, komunitas, karakter dan amaliah, keterampilan dan kapasitas, kaderisasi dan regenerasi.

## Revisi visual

- Gunakan lima kolom untuk lima fokus.
- Gunakan tujuh kartu untuk tujuh prioritas.
- Gunakan tiga jenjang untuk tiga tahapan.
- Gunakan rumus besar untuk IKU.
- Kurangi ornamen dan dekorasi generik.
- Jangan menambahkan foto, logo, grafik, angka, atau ilustrasi yang tidak tersedia dalam sumber.
- Pertahankan nuansa hijau tua, gading, dan aksen emas.

## Hal yang tidak boleh diubah

- Jangan memadatkan deck dengan menghapus isi sumber secara permanen.
- Jangan mengarang target outcome tahunan, nilai dasar, tanggal, anggaran, jabatan, kredensial, atau keputusan.
- Jangan menambahkan dalil, kutipan tokoh, atau penjelasan teologis yang tidak ada dalam sumber.
- Jangan mengubah pointer menjadi kewajiban final.
- Jangan menghapus rumus IKU atau lima indikator pendukung.

## Bila hasil awal menyimpang

Jangan memaksa revisi parsial. Generate ulang menggunakan:

- `prompts/generate-presenter.md` untuk presentasi 15 menit; atau
- `prompts/generate-detailed.md` untuk bahan pembahasan dan penelaahan mandiri.

Revisi berhasil bila peserta dapat menjawab lima pertanyaan berikut dari deck:

1. Apa arah dan sasaran Bidang Pemuda?
2. Masalah apa yang diidentifikasi sumber?
3. Apa lima kelompok program dan tujuh prioritasnya?
4. Bagaimana IKU dihitung dan apa lima cara ukurnya?
5. Apa yang masih perlu diputuskan dalam Rakernas?
