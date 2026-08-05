# Konteks Produk: Production Line Ops dan GinaV2

## Mengapa aplikasi ini dibutuhkan

Di lantai MAS Precast, kecepatan produksi dan kualitas belum selalu stabil. Total harian saja terlalu kasar: kita belum tentu tahu **bagian hari mana** yang melambat, kapan terjadi Reject, atau apakah perubahan terjadi saat mesin sedang berjalan, istirahat, atau ada masalah.

GinaV2 sudah membantu dengan sensor getaran pada mesin. Sensor memberi gambaran tentang bagaimana mesin bergetar atau berjalan. Namun sensor saja tidak mengetahui:

- produk yang sedang dibuat (Made);
- produk yang ditolak (Reject);
- masalah yang sedang terjadi (issue);
- kapan dan berapa lama break;
- siapa yang sedang bertugas di mesin; atau
- apakah shift sudah selesai.

## Peran PWA ini

**Production Line Ops** adalah companion app untuk GinaV2. PWA ini mencatat kejadian produksi beserta waktunya, supaya catatan lantai punya konteks saat dibaca bersama data sensor:

```text
GinaV2                         Production Line Ops (PWA)
Bagaimana mesin                Apa yang diproduksi,
bergetar / berjalan             kapan, dan oleh siapa
             \                         /
              \                       /
               v                     v
             Digabung nanti untuk memahami
             kapan produksi melambat atau kualitas turun
```

PWA ini bukan pengganti sensor dan bukan dashboard analisis. Sensor tetap mengukur kondisi mesin; PWA mencatat kejadian produksi dan waktu. Keduanya baru bisa dipakai bersama setelah log produksi cukup rapi dan jujur.

## Apa yang dicatat

Operator mencatat Made, Reject, issue, dan break sesuai kejadian di lapangan. Supervisor menyiapkan plan mesin dan menjawab **Needs you** jika ada permintaan. Catatan ini duduk di samping data getaran GinaV2 sehingga, pada tahap berikutnya, tim dapat melihat hubungan waktu antara jalannya mesin, kecepatan, dan kualitas.

## Fokus sesi hari ini

Hari ini **bukan hari chart** dan bukan sesi menjanjikan hasil analisis yang belum tersedia. Fokusnya adalah membangun kebiasaan logging:

1. plan shift pada mesin yang benar;
2. cek sensor;
3. catat Made / Reject / issue saat kejadian;
4. catat break;
5. tangani Needs you; dan
6. tutup shift dengan benar.

Prinsipnya: **kosong boleh, menebak tidak**. Jika belum ada kejadian atau datanya belum diketahui, biarkan kosong sesuai alur aplikasi. Jangan mengisi angka atau alasan berdasarkan perkiraan, karena log yang salah dapat menyesatkan pembacaan sensor nanti.

## Cerita demo

Cerita penuh dijalankan di **Pipe No.5**, karena mesin ini paling cocok untuk demo sensor. Alur yang sama berlaku untuk Wiremesh dan Paving; yang berubah adalah mesin dan akun yang digunakan.

Sesudah demo, setiap SPV mencoba alurnya di mesin masing-masing. Catatan hari ini adalah fondasi kebiasaan logging; penggabungan dengan data GinaV2 untuk membaca kecepatan dan kualitas dilakukan kemudian, setelah log nyata terkumpul.
