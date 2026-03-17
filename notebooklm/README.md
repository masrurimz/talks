# Paket Kerja NotebookLM untuk Persiapan Slide

Dokumen ini merangkum apa yang perlu Anda unggah ke NotebookLM, pengaturan yang saya rekomendasikan, prompt yang siap ditempel, dan best practices yang saya konfirmasi lewat dokumentasi Google.

## 1. File yang sudah siap dipakai

### Sumber utama materi
Unggah file berikut sebagai sumber utama isi presentasi:
- `og-reference/bahan-bacaan-ramadhan-medsos-game-judol-roblox-revisi-v2.md`
- `og-reference/lampiran-data-statistik-ramadhan-medsos-game-judol-v2.md`

### Sumber tambahan untuk membentuk gaya dan target deck
Unggah juga file berikut agar NotebookLM memahami siapa pembicara, siapa audiens, dan gaya deck yang diinginkan:
- `notebooklm/upload-01-brief-pembicara-audiens.md`
- `notebooklm/upload-02-arahan-struktur-presentasi.md`

## 2. Urutan kerja yang disarankan di NotebookLM
1. Buat notebook baru.
2. Unggah 4 file di atas.
3. Pastikan hanya 4 source itu yang aktif/terpilih saat generate deck.
4. Buat deck pertama dengan format **Slide Presenter**.
5. Gunakan prompt dari `paste-03-prompt-slide-presenter.md`.
6. Jika hasilnya terlalu ringkas atau Anda ingin versi handout, buat deck kedua dengan prompt dari `paste-04-prompt-presentasi-mendetail.md`.
7. Jika ada bagian yang perlu dipoles, gunakan prompt revisi dari `paste-05-prompt-revisi-deck.md`.

## 3. Konfigurasi yang direkomendasikan

### Untuk acara presentasi langsung
- Format: **Slide Presenter**
- Bahasa: **Indonesia**
- Panjang: **Default**
- Alasan: format ini paling cocok untuk pembicara yang akan menjelaskan dengan lisan. Deck lebih bersih dan tidak terlalu penuh teks.

### Untuk versi bagikan setelah acara
- Format: **Presentasi Mendetail**
- Bahasa: **Indonesia**
- Panjang: **Default** atau **Long**
- Alasan: lebih nyaman dibaca sendiri atau dibagikan lewat PDF.

## 4. Best practices yang sebaiknya Anda ikuti

### A. Gunakan source yang bersih dan terarah
NotebookLM mendukung Markdown, PDF, Google Docs, Google Slides, web URL, YouTube, audio, dan beberapa format lain. Setiap source dapat mencapai sampai 500.000 kata atau 200 MB, dan satu notebook bisa memuat hingga 50 source. Namun untuk hasil deck yang fokus, lebih baik gunakan sedikit source yang benar-benar relevan daripada terlalu banyak source bercampur.[1]

### B. Tambahkan source khusus untuk audiens dan gaya
Google juga menekankan bahwa rough notes atau outline bisa dipakai sebagai source untuk membentuk deck. Karena itu saya buat dua file tambahan khusus untuk pembicara, audiens, struktur, dan gaya presentasi. Ini membantu deck lebih cocok dengan konteks desa Indonesia dan audiens lintas usia.[2]

### C. Pilih format sesuai fungsi
Menurut bantuan resmi Google, **Detailed Deck** cocok untuk dibaca sendiri atau dibagikan, sedangkan **Presenter Slides** cocok untuk membantu Anda berbicara langsung.[3]

### D. Jangan terlalu mengandalkan revisi berat
Dokumentasi resmi Google menyebut bahwa saat melakukan revisi slide, **sources tidak dipertimbangkan**. Jadi bila hasil deck awal melenceng secara isi atau struktur, lebih aman generate deck baru dari awal dengan prompt yang lebih tegas daripada merevisi besar-besaran.[3]

### E. Verifikasi slide penting sebelum dipakai
Google juga mengingatkan bahwa Slide Deck bersifat AI-generated dan bisa mengandung ketidakakuratan visual maupun fakta. Karena itu, cek kembali terutama:
- angka statistik;
- istilah Roblox dan kontrol usia;
- kutipan ayat atau pesan agama;
- slide yang terlalu indah tetapi kurang tepat isi.

### F. Fokus pada satu pesan per slide
Blog resmi Google tentang Slide Decks menonjolkan penggunaan NotebookLM untuk mengubah riset padat menjadi cerita visual, rough notes menjadi deck, dan data menjadi visual yang lebih mudah dipahami. Untuk audiens Anda, prinsip yang paling aman adalah: satu slide, satu pesan utama, dengan contoh sehari-hari.[2]

## 5. Strategi deck yang saya rekomendasikan

### Opsi terbaik: buat 2 deck
1. **Deck utama**: Slide Presenter, dipakai saat tampil.
2. **Deck pendamping**: Presentasi Mendetail, dipakai untuk dibagikan atau dijadikan PDF setelah acara.

Keuntungannya:
- deck presenter tetap rapi dan tidak penuh tulisan;
- deck detail bisa jadi bahan panitia, moderator, atau jamaah yang ingin membaca ulang.

## 6. Checklist cepat sebelum klik Generate
- Apakah hanya 4 source yang relevan sedang aktif?
- Apakah bahasa output sudah Indonesia?
- Apakah format deck sesuai tujuan: presenter vs handout?
- Apakah prompt sudah menyebut audiens desa, lintas usia, dan bahasa sederhana?
- Apakah prompt sudah menegaskan bahwa judol harus dibahas tegas, sementara medsos dan game dibahas seimbang?

## 7. Jika hasil pertama belum memuaskan
Urutan perbaikannya:
1. Perbaiki prompt generasi awal.
2. Generate ulang deck baru.
3. Baru gunakan prompt revisi untuk penyempurnaan lokal.

Jangan mulai dari revisi besar kalau arah awal deck sudah salah.

## 8. Sumber web yang saya pakai untuk konfirmasi
1. Google NotebookLM Help — Add or discover new sources for your notebook: https://support.google.com/notebooklm/answer/16215270
2. Google Blog — 8 ways to make the most out of Slide Decks in NotebookLM: https://blog.google/innovation-and-ai/models-and-research/google-labs/8-ways-to-make-the-most-out-of-slide-decks-in-notebooklm/
3. Google NotebookLM Help — Generate a Slide Deck in NotebookLM: https://support.google.com/notebooklm/answer/16757456
4. Google Blog — NotebookLM goes global with Slides support and better ways to fact-check: https://blog.google/innovation-and-ai/products/notebooklm-goes-global-support-for-websites-slides-fact-check/
