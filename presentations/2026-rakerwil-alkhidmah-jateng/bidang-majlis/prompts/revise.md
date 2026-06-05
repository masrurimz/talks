# Prompt Revisi — Bidang Majlis RAKERWIL 2026 (Jawa Tengah)

## Instruksi untuk NotebookLM

Gunakan prompt ini untuk **merevisi** slide deck yang sudah dihasilkan sebelumnya (baik presenter maupun detailed).

### Langkah-langkah Revisi
1. Baca ulang seluruh file di `sources/` (brief.md, structure.md, outlines, dan semua referensi di references/).
2. Identifikasi bagian yang perlu diperbaiki berdasarkan feedback user atau inkonsistensi dengan sumber.
3. Pertahankan arc narasi: **"Dari Amanat Munas ke Tanggung Jawab Daerah — Istiqomah Membangun Majlis Jawa Tengah"**.
4. Pastikan semua data (angka, nama daerah, ketentuan) tetap akurat persis seperti di `bidang-majlis-target-2026.md`.

### Hal yang Sering Perlu Direvisi
- Perbaikan data angka atau tabel yang salah/kurang lengkap
- Penambahan atau pengurangan slide sesuai durasi presentasi aktual
- Penyesuaian tone (lebih mengajak / lebih formal)
- Perbaikan urutan agar alur narasi lebih kuat
- Penambahan highlight pada 8 daerah Tuan Rumah Mandiri atau jadwal kerja bakti
- Penyesuaian visual hint (jika user memberikan feedback setelah generate)
- Penambahan catatan "data akan ditetapkan di Rapat PW" pada bagian yang masih terbuka

### Format Output Revisi
- Sebutkan nomor slide yang direvisi
- Jelaskan perubahan yang dilakukan
- Berikan versi slide yang sudah diperbaiki
- Jika ada data baru yang perlu ditambahkan, minta konfirmasi terlebih dahulu sebelum mengarang

### Batasan
- **JANGAN** mengubah nama daerah, urutan, atau angka target kecuali ada sumber baru yang valid
- **JANGAN** menghapus bagian [Wajib] di outline kecuali diminta secara eksplisit
- Pertahankan konsistensi penamaan: "Jama'ah Al Khidmah", "Majlis Sewelasan", "Tuan Rumah Mandiri", "Pagu Daerah", "PP Assalafi Al Fithrah Meteseh", dll.

Setelah revisi, sarankan user untuk menguji kembali di NotebookLM dan memberikan feedback lanjutan.
