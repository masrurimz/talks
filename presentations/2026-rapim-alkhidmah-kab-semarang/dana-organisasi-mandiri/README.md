# Dana Organisasi Mandiri — Rapim Al Khidmah Kabupaten Semarang

Bahan sumber dan prompt NotebookLM untuk membahas usulan **Pondasi Khidmah Organisasi** dalam Rapat Pimpinan PD–PC Al Khidmah Kabupaten Semarang.

| Item | Detail |
|---|---|
| **Acara** | Rapat Pimpinan Al Khidmah se-Kabupaten Semarang |
| **Tanggal** | Rabu malam Kamis, 5 Agustus 2026 · mulai 20.00 WIB |
| **Tempat** | Kediaman Kyai Suuri, Reksosari, Suruh |
| **Topik** | Dana Organisasi Mandiri / Pondasi Khidmah Organisasi |
| **Status** | Draft musyawarah — sources dan prompts siap |
| **Bahasa** | Bahasa Indonesia |
| **Format** | Presenter + Detailed |

## Narasi deck

1. Kegiatan besar memerlukan pondasi dana yang terencana.
2. Cara penghimpunan sudah banyak, tetapi lingkar orang yang diminta sering sama.
3. Usulan: 750 anggota × Rp300.000/tahun = Rp225 juta/tahun.
4. Dana dialokasikan ke Kedinding, Meteseh, Haul Kabupaten, PC/haul kecamatan, dan organisasi PD.
5. Manfaat hanya dapat dipercaya bila formula PC, pencairan, pencatatan, dan laporan disepakati.
6. Mulai dengan pilot 30–60–90 hari; KTA menjadi tahap lanjut.
7. Presentasi berakhir pada keputusan, pemilik tugas, dan tenggat.

## Isi folder

```text
sources/
  context/
    brief.md
    structure.md
  outlines/
    presenter.md
    detailed.md
  references/
    undangan-rapim.md
    draft-program-dana-organisasi.md
    model-keuangan.md
    rencana-implementasi-dan-keputusan.md
prompts/
  generate-presenter.md
  generate-detailed.md
  revise.md
output/
  (simpan hasil NotebookLM di sini)
```

## Pilihan deck

### Presenter deck

- 19 slide
- 25–30 menit sebelum diskusi
- Visual ringkas dan pesan utama besar
- Gunakan `prompts/generate-presenter.md`

### Detailed deck

- 24 slide
- Dapat dibaca mandiri sebagai bahan rapat
- Memuat tabel angka, pilihan formula, tata kelola, dan implementasi
- Gunakan `prompts/generate-detailed.md`

## Cara pakai dengan NotebookLM

1. Buat notebook baru.
2. Upload seluruh file dari folder `sources/`.
3. Paste `prompts/generate-presenter.md` untuk deck utama Rapim.
4. Generate kembali dengan `prompts/generate-detailed.md` untuk bahan baca.
5. Periksa angka terhadap `sources/references/model-keuangan.md`.
6. Gunakan `prompts/revise.md` hanya untuk penyempurnaan ringan.
7. Simpan hasil ke folder `output/`.

AI assistant tidak menjalankan NotebookLM dan tidak membuat slide final di repository ini.

## Pemeriksaan wajib sebelum dipresentasikan

- [ ] Nama penandatangan kedua pada surat diverifikasi dari scan asli bila ingin ditampilkan.
- [ ] Ejaan Kecamatan Bringin dikonfirmasi.
- [ ] Daftar 9 PC undangan dan klaim 13 PC aktif dijelaskan sebagai konteks berbeda.
- [ ] Dukungan PC tertulis Rp52.500.000, bukan Rp52.500.500.
- [ ] Formula pembagian PC masih diberi label “perlu diputuskan”.
- [ ] Kontribusi anggota tidak disebut wajib sebelum keputusan rapat.
- [ ] KTA/super aplikasi tidak digambarkan sebagai sistem yang sudah tersedia.
- [ ] Deck menyediakan ruang untuk mencatat keputusan, penanggung jawab, dan tenggat.