# Prompt Revisi — Dana Organisasi Mandiri

Gunakan prompt ini setelah NotebookLM menghasilkan deck pertama. Revisi deck tanpa mengubah fakta, angka, atau status usulan.

## Tujuan revisi

Buat deck lebih:

- mudah dipahami dalam sekali lihat;
- jujur membedakan fakta, usulan, contoh, dan keputusan;
- kuat secara visual tanpa menjadi pitch bisnis;
- fokus pada musyawarah dan tindak lanjut.

## Pemeriksaan wajib sebelum revisi

Periksa dan koreksi bila salah:

1. **750 × Rp300.000 = Rp225.000.000 per tahun**.
2. **Rp300.000 per tahun = Rp25.000 per bulan**.
3. Alokasi total:
   - Kedinding Rp37.500.000;
   - Meteseh Rp37.500.000;
   - Haul Kabupaten Rp75.000.000;
   - haul kecamatan/PC Rp52.500.000;
   - organisasi PD Rp22.500.000.
4. Jumlah lima alokasi harus tepat Rp225.000.000.
5. Jangan gunakan typo Rp52.500.500.
6. Jika 13 PC dipakai sebagai contoh pembagian rata, gunakan ± Rp4.038.462 per PC per tahun.
7. Jelaskan bahwa undangan mencantumkan 9 PC, sedangkan 13 PC berasal dari contoh draft dan perlu diverifikasi.
8. Haul Kabupaten Rp75 juta adalah sekitar 21,43% dari RAB minimum Rp350 juta.
9. Selisih alokasi model terhadap setoran/pagu 2026 harus diberi label **belum diputuskan**.

## Revisi struktur

- Pertahankan alur: masalah → model → manfaat → tata kelola → pilot → keputusan.
- Pastikan masalah “banyak cara, lingkar yang sama” muncul sebelum angka.
- Pastikan manfaat PC muncul segera setelah alokasi total.
- Jangan menaruh KTA sebelum tata kelola keuangan; KTA adalah tahap lanjut.
- Akhiri dengan keputusan, penanggung jawab, dan tenggat—bukan hanya doa umum.

## Revisi isi

- Ubah judul label menjadi judul pesan. Contoh:
  - “Permasalahan” → “Cara Sudah Banyak, Lingkar Masih Sama”
  - “Pondasi” → “Dari Rp25.000 Menjadi Rp225 Juta Setahun”
  - “Support Kecamatan” → “PC Menjadi Ujung Tombak Sekaligus Penerima Manfaat”
- Pendekkan paragraf menjadi maksimal 3–4 poin untuk presenter deck.
- Detailed deck boleh memiliki tabel dan penjelasan lebih lengkap, tetapi hindari dinding teks.
- Gunakan istilah **dukungan PC**, bukan “support kecamatan”, agar konsisten.
- Ganti klaim pasti seperti “akan menghilangkan tarikan” menjadi “ditujukan untuk mengurangi tarikan berulang, sesuai keputusan dan hasil pelaksanaan”.
- Ganti “wajib” pada kontribusi anggota menjadi “komitmen yang dipahami dan disetujui anggota”, kecuali rapat memang telah menghasilkan keputusan dan deck sedang direvisi berdasarkan notulen.

## Revisi visual

- Gunakan satu stacked bar atau lima kartu untuk Rp225 juta.
- Pastikan chart menggunakan skala dan label nominal yang terbaca.
- Gunakan tiga kolom untuk Rata / Proporsional / Hibrida.
- Gunakan timeline 30–60–90 hari.
- Gunakan checklist keputusan pada bagian akhir.
- Kurangi ornamen, foto uang, gradient berlebihan, dan ikon generik.
- Pertahankan nuansa hijau tua–gading–emas yang khidmat.

## Hal yang tidak boleh diubah

- Jangan mengarang jumlah anggota aktif atau PC final.
- Jangan mengubah program usulan menjadi keputusan.
- Jangan menambahkan dalil atau mengatribusikan kutipan draft kepada Hadrotusy Syaikh.
- Jangan menghapus risiko, tata kelola, atau kebutuhan persetujuan anggota.
- Jangan menampilkan KTA/database global/super aplikasi sebagai sudah tersedia.
- Jangan menambahkan denda, bunga, penalti, investasi, atau detail teknis pembayaran yang tidak ada di sumber.

## Bila hasil awal terlalu jauh dari outline

Jangan memaksa revisi parsial. Generate ulang menggunakan:

- `prompts/generate-presenter.md` untuk deck rapat; atau
- `prompts/generate-detailed.md` untuk bahan baca.

Revisi dianggap berhasil bila peserta dapat menjawab lima pertanyaan ini hanya dari deck:

1. Masalah apa yang ingin diselesaikan?
2. Bagaimana Rp225 juta dihitung dan dialokasikan?
3. Apa manfaat langsung bagi PC?
4. Kontrol apa yang mencegah salah kelola?
5. Keputusan apa yang harus dibuat setelah presentasi?