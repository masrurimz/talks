# Arahan Struktur — PWA Demo MAS Precast

## Tujuan Deck

Deck intro + referensi untuk sesi **PWA Demo to MAS Precast** (Rabu 5 Agustus 2026, 15:00–16:30).

Deck membantu audiens paham **bagaimana mereka bekerja dengan app** — mulai dari **peran sederhana**, lalu **gambar besar proses** (mesin → sensor + app → yang diteliti bareng), lalu **alur satu hari**, lalu **cara install PWA**.

## Sifat: pilot/riset bersama, BUKAN menjual

MAS Precast mitra yang menguji app ini. Tidak ada arus penjualan. Korelasi kecepatan/kualitas = **yang sedang diteliti bersama**, bukan janji/ROI.

---

## Proporsi Isi

| Bagian | Proporsi | Durasi bicara (intro) |
|--------|----------|------------------------|
| Pembuka + konteks pilot | ~5% | ~1 mnt |
| **Peran sederhana** | ~20% | ~2–3 mnt |
| **Big-picture process diagram** | ~25% | ~3–4 mnt |
| Alur satu hari | ~15% | ~2 mnt |
| Install PWA (Android) | ~15% | ~2–3 mnt |
| Referensi layar / aturan | ~15% | ~1–2 mnt |
| Transisi ke live demo | ~5% | ~1 mnt |

---

## Struktur Narasi

### 1. Pembuka (Slide 1–2)
- Judul: Production Line Ops — companion GinaV2.
- Konteks: ini sesi pilot/riset bersama mitra, bukan presentasi penjualan.
- Agenda: peran → gambar besar → alur → install → live demo → praktik.

**Poin:** kita coba bareng di lantai; lihat apa yang jalan.

---

### 2. Peran sederhana (Slide 3–4) [DI MUKA]

Tiga peran, hanya tugas dasar — **tanpa penempatan mesin**:

| Peran | Tugas dasar |
|-------|-------------|
| Operator | Catat Made/Reject/issue + break, minta end shift |
| Supervisor | Plan mesin + jawab Needs you |
| Admin | People + Activity, bantu jika macet |

**Catatan:** siapa di mesin mana → dilakukan **saat sesi**, bukan di deck.

---

### 3. Big-picture process diagram (Slide 5–6) [KRUSIAL]

Diagram besar **bagaimana mereka bekerja dengan app**:

```text
   Mesin Anda (Pipe / Wiremesh / Paving)
        │
   ┌────┴──────────────────────┐
   │                           │
GINAV2 (sensor)         PRODUCTION LINE OPS (app)
getaran / kondisi       catat Made / Reject / break
mesin                   + siapa + kapan
   │                           │
   └─────────────┬─────────────┘
                 v
        Diteliti bareng (pilot):
     kapan lambat / kualitas turun
```

**Pesan:** app duduk di samping sensor GinaV2. Keduanya baru bercerita setelah log nyata terkumpul. Hari ini = mulai bangun kebiasaan catat.

**Jangan** jadikan ini janji hasil/chart.

---

### 4. Alur satu hari (Slide 7–8)

```text
Plan shift → Cek sensor → Log Made/Reject/Issue
     → Break → Needs you (SPV) → End shift
```
- Satu cerita utuh di satu mesin.
- Cek sensor penting: log akan dibaca bersama data GinaV2.

---

### 5. Install PWA Android / Chrome (Slide 9–10) [WAJIB]

1. URL HTTPS di Chrome
2. Menu ⋮ → Install app / Add to Home Screen
3. Buka dari ikon Home Screen
4. Login PIN 4 digit · bahasa Indonesia

Presenter pakai **Vysor** agar HP terlihat. Fokus Android.

---

### 6. Referensi singkat + aturan (Slide 11–12)
- Login PIN — peran terikat akun.
- Operator: +/−, satu Save.
- Supervisor: plan pagi; Needs you hanya saat perlu.
- Aturan: bahasa ID, ikuti kartu PIN, angkat tangan jika macet, log jujur (kosong boleh, menebak tidak).

---

### 7. Transisi live demo (Slide 13)
- Penempatan mesin dilakukan bareng.
- Framing: log sekarang → dibaca bersama sensor nanti.
- Next: HP via Vysor → tonton → praktik.

---

## Aturan Isi Slide
- Satu slide, satu gagasan.
- Peran + big picture = **diagram/kartu**, bukan paragraf.
- Bahasa lantai.
- Presenter ringkas; detailed boleh tabel referensi lebih lengkap.
- Label **[Wajib]** / **[Opsional]**.

## Aturan Nada
- **Tidak menjual.** Mitra pilot, bukan prospek.
- Praktis, hormati waktu lantai.
- Tidak overpromise chart.

## Hal yang WAJIB Ada
- Tiga peran (sederhana) di muka.
- Diagram big-picture process (mesin → sensor+app → riset bareng).
- Diagram alur satu hari.
- Slide install PWA Android Chrome.
- Transisi ke live demo + penempatan dilakukan bareng.
- Pengingat: kosong OK, menebak tidak.

## Hal yang JANGAN Dicantumkan
- Arus penjualan / ROI / nilai bisnis sebagai pitch.
- Arsitektur, database, tech stack.
- Chart/hasil analisis sebagai janji.
- Penempatan orang→mesin / PIN di deck (dilakukan live).
- Detail iOS sebagai jalur utama.

## Screenshot / Aset (daftar untuk nanti)
| Aset | Isi |
|------|-----|
| `01-login.png` | Layar PIN |
| `02-supervisor-board.png` | Board SPV |
| `03-assign.png` | Form plan/assign |
| `04-sensor-check.png` | Cek sensor |
| `05-log-entry.png` | Kartu log Made +/− |
| `06-needs-you.png` | Antrean Needs you |
| `07-end-shift.png` | End / shift ditutup |
| `08-people.png` | Admin People |
| `09-install-pwa.png` | Chrome Install / Add to Home Screen |
| `10-home-icon.png` | Ikon Home Screen |
