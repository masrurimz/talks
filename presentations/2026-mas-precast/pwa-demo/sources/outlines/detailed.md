# Outline Detailed — PWA Demo MAS Precast

**Judul:** Production Line Ops — Companion App untuk GinaV2  
**Event:** PWA Demo to MAS Precast · Rabu, 5 Agustus 2026 · 15:00–16:30  
**Pembicara:** Zahid (Groundup)  
**Bahasa:** Indonesia · **Target:** 16–18 slide · handout/referensi

## Catatan penggunaan
- **Pilot/riset bersama mitra** — bukan penjualan.
- Urutan: **peran → gambar besar proses → alur → install → referensi → live**.
- Penempatan orang ke mesin/PIN dilakukan **saat sesi** — tidak tertulis di deck.
- Cocok sebagai leave-behind saat praktik. PIN tidak ditulis di slide.

---

## Slide 1 [Wajib] — Sampul
- Production Line Ops — companion app GinaV2
- Pilot bersama PT MAS Precast · 5 Agustus 2026 · Zahid (Groundup)

---

## Slide 2 [Wajib] — Sesi ini (90 menit)
| Blok | Isi | Waktu |
|---|---|---|
| Intro slides | Peran, gambar besar, alur, install | ~10–15 mnt |
| Live demo | Satu cerita di satu mesin (Vysor) | ~25–30 mnt |
| Penempatan + praktik | Pasang orang ke mesin, lalu coba | ~30–40 mnt |
| Buffer / Q&A | Admin singkat, stuck cases | sisa |

**Sifat:** pilot/riset bareng, bukan presentasi penjualan.

---

## Slide 3 [Wajib] — Tiga peran (sederhana)
| Peran | Tugas dasar |
|---|---|
| Operator | Catat Made/Reject/issue + break; minta end shift |
| Supervisor | Plan mesin + jawab Needs you |
| Admin | People + Activity; bantu jika macet |

**Catatan:** siapa di mesin mana → dilakukan **saat sesi**.

---

## Slide 4 [Wajib] — Tugas per peran (referensi)
**Operator**
- Cek sensor jika diminta
- Catat Made/Reject/issue via +/−
- Break saat perlu
- Minta end shift (tidak bisa tutup sendiri)

**Supervisor**
- Assign orang ke mesin (plan)
- Jawab antrean **Needs you** (target, issue, sensor, permintaan end)
- Antrean kosong = sukses

**Admin / owner**
- Lihat Activity (siapa, kapan)
- Kelola People (aktif, reset PIN)
- Bantu jika macet

---

## Slide 5 [Wajib] — Login & bahasa
- PIN 4 digit; peran terikat akun
- Tidak memilih role di layar
- Bahasa **Indonesia**
- Salah berkali-kali → minta admin reset
- **Visual:** `01-login.png`

---

## Slide 6 [Wajib] — Gambar besar: bagaimana kita bekerja dengan app
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
- App = companion, bukan pengganti sensor
- Bukan dashboard analisis hari ini

---

## Slide 7 [Wajib] — Yang kita teliti bareng
- Kapan produksi lambat?
- Kapan kualitas turun?
- Break vs mesin bermasalah?
- Hari ini: kumpulkan log jujur; analisis setelahnya

---

## Slide 8 [Wajib] — Prinsip data: kosong boleh, menebak tidak
| Baik | Buruk |
|---|---|
| Angka nyata | Dibulatkan "rapi" |
| Kosong jika belum yakin | Mengarang |
| Tandai issue/break nyata | Sembunyikan stop |

Log salah menyesatkan riset sensor nanti.

---

## Slide 9 [Wajib] — Alur satu hari
```text
Plan shift → Cek sensor → Log Made/Reject/Issue
         → Break → Needs you (SPV) → End shift
```
Cek sensor menjaga kualitas pembacaan bersama GinaV2.

---

## Slide 10 [Wajib] — Arti tiap langkah
| Langkah | Siapa | Kenapa |
|---|---|---|
| Plan | SPV | Orang + target ke mesin |
| Cek sensor | Op | Sensor hilang melemahkan riset |
| Log | Op | Made/Reject + waktu = setengah cerita |
| Break | Op | Break ≠ mesin tiba-tiba lambat |
| Needs you | SPV | Keputusan hanya saat perlu |
| End | Op minta, SPV setuju | Tidak bisa tutup sendiri |

---

## Slide 11 [Wajib] — Mengapa install sebagai PWA
- Home Screen = kebiasaan kerja, bukan tab sekali buka
- Lebih cepat dibuka di lantai
- Sesi ini mengajarkan **cara pasang**
- Vysor memantulkan HP Android ke Mac

---

## Slide 12 [Wajib] — Checklist install Android Chrome
1. URL **HTTPS** di **Chrome**
2. Menu **⋮**
3. **Install app** / **Tambahkan ke layar utama**
4. Konfirmasi
5. Buka dari **ikon Home Screen**
6. Bahasa = **Indonesia**
7. Login PIN 4 digit dari kartu

**FAQ singkat:** iPhone pakai Safari → Share → Add to Home Screen. Fokus sesi = Android.

**Visual:** `09-install-pwa.png`, `10-home-icon.png`

---

## Slide 13 [Wajib] — Referensi layar operator
- Produk biasanya sudah terisi
- Angka via +/−
- Jalur normal: Made → Save sekali
- Bisa tambah Reject/Issue bila nyata
- Break menjeda countdown
- **Visual:** `05-log-entry.png`, `04-sensor-check.png`

---

## Slide 14 [Wajib] — Referensi layar supervisor
- Board: siapa di mesin mana
- Plan/Assign: mesin + operator + durasi + target
- Needs you: target, issue, sensor, permintaan end
- End shift: SPV yang menutup
- **Visual:** `02-supervisor-board.png`, `03-assign.png`, `06-needs-you.png`, `07-end-shift.png`

---

## Slide 15 [Opsional] — Referensi admin
- People: daftar aktif
- Activity: jejak siapa/kapan
- Jangan nonaktifkan orang live tanpa alasan
- **Visual:** `08-people.png`

---

## Slide 16 [Wajib] — Aturan sesi + stuck cases
**Aturan**
1. Bahasa Indonesia
2. Ikuti kartu PIN
3. Angkat tangan jika macet
4. Log jujur

**Jika macet**
| Gejala | Tindakan |
|---|---|
| "No shift planned" | SPV belum assign / salah Op |
| Tidak bisa login | PIN salah / nonaktif → admin |
| UI English | Account → Language → ID |
| Panic | Logout → login lagi dari kartu |

---

## Slide 17 [Wajib] — Transisi live demo
- Penempatan orang ke mesin → dilakukan **bareng** sekarang
- Satu cerita utuh di satu mesin (Vysor)
- Framing: log sekarang → dibaca bersama sensor nanti
- Tonton dulu, lalu praktik
