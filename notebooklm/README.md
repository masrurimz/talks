# Paket Kerja NotebookLM untuk Persiapan Slide

Dokumen ini merangkum file yang perlu Anda unggah ke NotebookLM untuk **sesi 1** acara refleksi Nuzulul Qur'an bertema **Al-Qur'an menjawab problematika zaman**.

Arah yang dipakai sekarang sudah disesuaikan dengan brief asli:
- sesi 1 dari sudut pandang praktisi IT;
- durasi sekitar 30 menit;
- fokus utama pada media sosial;
- game online dan judi online hanya disentuh secukupnya;
- pembatasan usia dan pengawasan pengguna muda dibahas dari alasan perlindungannya dulu;
- penutup harus menjadi jembatan ke sesi 2.

## 1. Daftar file di folder `notebooklm/`
- `notebooklm/README.md`
- `notebooklm/upload-01-brief-pembicara-audiens.md`
- `notebooklm/upload-02-arahan-struktur-presentasi.md`
- `notebooklm/upload-03-outline-slide-presenter.md`
- `notebooklm/upload-04-outline-slide-mendetail.md`
- `notebooklm/paste-03-prompt-slide-presenter.md`
- `notebooklm/paste-04-prompt-presentasi-mendetail.md`
- `notebooklm/paste-05-prompt-revisi-deck.md`

## 2. File yang disarankan untuk diunggah ke NotebookLM

### Referensi isi utama
- `og-reference/bahan-bacaan-ramadhan-medsos-game-judol-roblox-revisi-v2.md`
- `og-reference/lampiran-data-statistik-ramadhan-medsos-game-judol-v2.md`

### Pengarah konteks dan audiens
- `notebooklm/upload-01-brief-pembicara-audiens.md`
- `notebooklm/upload-02-arahan-struktur-presentasi.md`

### Sumber slide yang paling langsung
- `notebooklm/upload-03-outline-slide-presenter.md`
- `notebooklm/upload-04-outline-slide-mendetail.md`

## 3. Cara pakai yang paling aman

### Untuk deck presentasi utama
Gunakan:
- `upload-03-outline-slide-presenter.md` sebagai sumber slide utama;
- `upload-01-brief-pembicara-audiens.md`;
- `upload-02-arahan-struktur-presentasi.md`;
- dua file dari `og-reference/` sebagai referensi isi dan data.

Pengaturan yang direkomendasikan:
- Format: **Slide Presenter**
- Bahasa: **Indonesia**
- Panjang: **Default**

### Untuk deck yang lebih lengkap / handout
Gunakan:
- `upload-04-outline-slide-mendetail.md` sebagai sumber slide utama;
- `upload-01-brief-pembicara-audiens.md`;
- `upload-02-arahan-struktur-presentasi.md`;
- dua file dari `og-reference/` sebagai referensi isi dan data.

Pengaturan yang direkomendasikan:
- Format: **Presentasi Mendetail**
- Bahasa: **Indonesia**
- Panjang: **Default**

## 4. Prompt yang dipakai
- Untuk deck presenter: buka `notebooklm/paste-03-prompt-slide-presenter.md`
- Untuk deck mendetail: buka `notebooklm/paste-04-prompt-presentasi-mendetail.md`
- Untuk revisi ringan: buka `notebooklm/paste-05-prompt-revisi-deck.md`

## 5. Prinsip penting supaya NotebookLM tidak salah arah
- Jangan biarkan game online menjadi topik dominan.
- Jangan biarkan judi online mengambil porsi terbesar.
- Jangan jadikan contoh platform sebagai fokus utama.
- Pastikan media sosial tetap menjadi bahasan paling besar.
- Pastikan penutup mengarah ke sesi 2, bukan menutup semua jawaban di sesi 1.

## 6. Checklist sebelum klik Generate
- Apakah deck ini jelas untuk **sesi 1**, bukan materi gabungan dua pemateri?
- Apakah media sosial mendapat porsi terbesar?
- Apakah game online dan judol hanya disebut secukupnya?
- Apakah pembatasan usia dibahas dari alasan perlindungannya dulu?
- Apakah penutup menjadi jembatan ke sesi 2?
- Apakah bahasa sudah sederhana dan cocok untuk audiens umum di desa?

## 7. Catatan NotebookLM yang tetap berlaku
- NotebookLM mendukung Markdown, PDF, Google Docs, Google Slides, URL web, YouTube, audio, dan format lain; satu notebook bisa memuat hingga 50 source dan tiap source bisa sampai 500.000 kata atau 200MB. Sumber yang sedikit tetapi terarah biasanya memberi hasil deck yang lebih baik.
- NotebookLM menyediakan mode **Presenter Slides** dan **Detailed Deck**.
- Revisi deck tidak lagi memakai sources sebagai dasar. Jadi jika arah deck awal salah, lebih aman generate ulang dari prompt yang benar daripada merevisi besar-besaran.

## 8. Sumber web yang dipakai untuk konfirmasi NotebookLM
1. Google NotebookLM Help — Add or discover new sources for your notebook: https://support.google.com/notebooklm/answer/16215270
2. Google NotebookLM Help — Generate a Slide Deck in NotebookLM: https://support.google.com/notebooklm/answer/16757456
3. Google Blog — 8 ways to make the most out of Slide Decks in NotebookLM: https://blog.google/innovation-and-ai/models-and-research/google-labs/8-ways-to-make-the-most-out-of-slide-decks-in-notebooklm/
4. Google Blog — NotebookLM goes global with Slides support and better ways to fact-check: https://blog.google/innovation-and-ai/products/notebooklm-goes-global-support-for-websites-slides-fact-check/
