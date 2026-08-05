# Prompt untuk Generate Presenter Deck

## Instruksi untuk NotebookLM

Buat deck **Slide Presenter** untuk materi:

**Production Line Ops — Companion App untuk GinaV2**  
**Pilot bersama PT MAS Precast · 5 Agustus 2026**

### Pengaturan
- **Format**: Slide Presenter (sedikit teks, dibicarakan).
- **Bahasa**: Indonesia.
- **Panjang**: target **14–16 slide**.
- **Durasi intro**: ~10–15 menit bicara.

### Sifat — PENTING
- **Bukan presentasi penjualan.** Ini pilot/riset bersama mitra. Tidak ada arus "masalah → solusi → nilai/ROI".
- Korelasi kecepatan/kualitas = **yang sedang diteliti bersama**, bukan janji hasil.
- **Penempatan orang ke mesin/PIN TIDAK boleh di slide** — dilakukan saat sesi.

### Urutan wajib
1. Judul + agenda.
2. **Tiga peran sederhana** (Operator/Supervisor/Admin + tugas dasar) — tanpa penempatan mesin.
3. Login: peran terikat PIN.
4. **Diagram big-picture process**: mesin mereka → (sensor GinaV2 + app) → diteliti bareng.
5. Yang diteliti bareng (bukan janji chart).
6. Prinsip: kosong boleh, menebak tidak.
7. Alur satu hari (diagram).
8. Mengapa install + langkah install Android Chrome + Vysor.
9. Referensi operator/supervisor singkat.
10. Aturan sesi + transisi live demo (penempatan dilakukan bareng).

### Gaya
- Bahasa lantai pabrik; praktis.
- Satu slide satu gagasan; diagram lebih penting dari paragraf.
- Jangan jargon ("correlation", "provenance").
- Jangan tampilkan PIN.
- Jangan janji chart analisis hari ini.

### Visual
- Diagram big-picture besar & terbaca jauh.
- Flow alur horizontal.
- Langkah install bernomor.

### Prioritas sumber
1. `sources/context/brief.md`
2. `sources/context/structure.md`
3. `sources/outlines/presenter.md`
4. `sources/references/konteks-produk-ginav2.md`
5. `sources/references/peran-dan-agenda-sesi.md`
6. `sources/references/install-pwa-android.md`
7. `sources/references/praktik-terbaik-demo-pelatihan.md`

### Batas
- Tidak arsitektur/backend/tech stack.
- Tidak feature laundry list.
- Tidak penempatan orang→mesin.
- iOS hanya FAQ, bukan jalur utama.
