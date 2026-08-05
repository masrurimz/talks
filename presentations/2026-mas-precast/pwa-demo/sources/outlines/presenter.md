# Outline Presenter — PWA Demo MAS Precast

**Judul:** Production Line Ops — Companion App untuk GinaV2  
**Event:** PWA Demo to MAS Precast · Rabu, 5 Agustus 2026 · 15:00–16:30  
**Pembicara:** Zahid (Groundup)  
**Bahasa:** Indonesia · **Target:** ~14–16 slide · intro bicara ~10–15 menit

## Catatan penggunaan
- Sifat sesi: **pilot/riset bersama mitra** — bukan presentasi penjualan.
- Urutan: **peran dulu → gambar besar proses → alur → install → live demo**.
- Penempatan orang ke mesin/PIN dilakukan **saat sesi**, bukan di deck.
- **[Wajib]** jangan dipotong; **[Opsional]** boleh dipotong.
- PIN tidak ditampilkan di slide.

## Urutan potong jika mepet
1. Slide 11 (admin singkat)
2. Slide 7 (prinsip data) — gabung ke slide alur
3. Slide 8 (mengapa install) — gabung ke slide langkah install

---

## Slide 1 [Wajib] — Judul
**Ritme bicara:** 30–45 dtk
- Production Line Ops
- Companion app untuk **GinaV2**
- Pilot bersama PT MAS Precast · Zahid · 5 Agustus 2026

**Arah bicara:** Salam singkat. Konteks: kita uji bareng di lantai, bukan presentasi penjualan.

**Pesan utama:** Hari ini kita lihat cara kerja app, pasang, lalu coba bareng.

---

## Slide 2 [Wajib] — Agenda
**Ritme bicara:** 45 dtk
1. Peran (siapa ngapain)
2. Gambar besar proses
3. Alur satu hari
4. Cara **install** ke HP
5. Live demo → penempatan + praktik

**Arah bicara:** HP diam dulu saat intro + demo. Penempatan mesin kita lakukan bareng nanti.

**Pesan utama:** Bukan hari chart — hari mulai kebiasaan catat.

---

## Slide 3 [Wajib] — Tiga peran (sederhana)
**Ritme bicara:** 1,5–2 mnt

| Peran | Tugas dasar |
|---|---|
| **Operator** | Catat Made / Reject / issue + break; minta end shift |
| **Supervisor** | Plan mesin + jawab **Needs you** |
| **Admin** | People + Activity; bantu jika macet |

**Arah bicara:** Jelaskan tugas dasar saja. Jangan bahas siapa di mesin mana — itu nanti.

**Pesan utama:** Tiga peran sederhana. Siapa di mana → bareng saat sesi.

**Visual:** Tiga kartu besar, satu per peran.

---

## Slide 4 [Wajib] — Login: peran sudah terikat PIN
**Ritme bicara:** 45 dtk
- Masuk dengan PIN 4 digit
- App sudah tahu Anda Operator / SPV / Admin — tidak memilih role
- Bahasa **Indonesia**

**Visual:** Placeholder `01-login.png`.

---

## Slide 5 [Wajib] — Gambar besar: bagaimana kita bekerja dengan app
**Ritme bicara:** 2–3 mnt [SLIDE TERPENTING]
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

**Arah bicara:** Telusuri diagram pelan-pelan. Sensor sudah ada; app mencatat kejadian + waktu. Keduanya bercerita setelah log terkumpul.

**Pesan utama:** App duduk **di samping** GinaV2. Bukan pengganti, bukan dashboard analisis hari ini.

**Visual:** Diagram besar, terbaca dari jauh.

---

## Slide 6 [Wajib] — Yang kita teliti bareng
**Ritme bicara:** 1 mnt
- Kapan produksi **lambat**?
- Kapan **kualitas** turun?
- Break vs mesin bermasalah?
- Hari ini: kumpulkan log dulu — analisis datang setelahnya

**Arah bicara:** Jangan janji chart. Ini riset bareng.

**Pesan utama:** Hasilnya belum hari ini — fondasinya dimulai hari ini.

---

## Slide 7 [Wajib] — Prinsip: kosong boleh, menebak tidak
**Ritme bicara:** 45 dtk
| Baik | Buruk |
|---|---|
| Angka nyata | Dibulatkan "biar rapi" |
| Kosong jika belum yakin | Mengarang agar selesai |
| Tandai issue/break nyata | Sembunyikan stop |

**Pesan utama:** Log salah menyesatkan riset; kosong terlihat, tebakan tidak.

---

## Slide 8 [Wajib] — Alur satu hari
**Ritme bicara:** 1–1,5 mnt
```text
Plan → Cek sensor → Log Made/Reject/Issue
     → Break → Needs you (SPV) → End shift
```
- Cek sensor penting: log dibaca bersama GinaV2

**Visual:** Flow horizontal (WAJIB).

---

## Slide 9 [Wajib] — Install = bagian dari sesi
**Ritme bicara:** 45 dtk
- App di **Home Screen** = kebiasaan kerja, bukan tab sekali buka
- Sesi ini mengajarkan **cara pasang**
- Layar HP dipantulkan via **Vysor**

**Visual:** Ikon browser vs ikon Home Screen.

---

## Slide 10 [Wajib] — Langkah install Android Chrome
**Ritme bicara:** 1,5–2 mnt
1. Buka URL **HTTPS** di **Chrome**
2. Menu ⋮ → **Install app** / **Add to Home Screen**
3. Buka dari **ikon Home Screen**
4. Login PIN 4 digit · bahasa **Indonesia**

**Arah bicara:** Idealnya lakukan live di Vysor di sini.

**Visual:** 4 langkah bernomor + placeholder `09-install-pwa.png`, `10-home-icon.png`.

---

## Slide 11 [Opsional] — Operator & Supervisor: singkat
**Ritme bicara:** 45 dtk
- **Operator:** produk biasanya sudah terpilih; angka via +/−; satu Save; Break menjeda
- **Supervisor:** plan pagi; Needs you hanya saat perlu; antrean kosong = bagus

**Visual:** Placeholder `05-log-entry.png`, `02-supervisor-board.png`, `06-needs-you.png`.

---

## Slide 12 [Wajib] — Aturan sesi
**Ritme bicara:** 45 dtk
1. Bahasa app = Indonesia
2. Ikuti kartu PIN
3. Macet → angkat tangan, jangan lawan HP
4. Log jujur — akan dibaca bersama data sensor

**Visual:** Checklist 4 poin besar.

---

## Slide 13 [Wajib] — Mari mulai (penempatan dilakukan bareng)
**Ritme bicara:** 45–60 dtk
- Penempatan orang ke mesin → kita lakukan **bareng** sekarang
- Lalu: satu cerita utuh di satu mesin (Vysor)
- Framing: log sekarang → dibaca bersama sensor nanti
- Tonton dulu, lalu praktik

**Arah bicara:** Tutup slide, pindah ke HP.

**Pesan utama:** Penempatan + alur nyata sekarang — bareng.
