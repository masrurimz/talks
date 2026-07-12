# Referensi — Arsitektur, Auth, & Keputusan Teknis

> Sumber: keputusan tim Juli 2026 + web research.

## Pendekatan Development — Desktop-First Adaptive Mobile

- **Desktop-first, adaptive ke mobile.** Bukan mobile-first.
- Alasan: mobile-first tidak memberikan info density yang cukup untuk dashboard/admin flows. Pengurus dan panitia butuh tampilan padat informasi (tabel, list, form kompleks) yang terbaik di desktop.
- `apps/native` dibangun desktop-first dengan adaptive breakpoint ke mobile (bukan sebaliknya).
- Semua fitur tetap harus jalan di mobile — tapi layout utama dioptimalkan untuk desktop.

## Arsitektur Monorepo — Shared Packages Only

- Pakai **shared packages** (DB schema, API contracts, config, auth, env, UI components) — bukan per-feature packages.
- Per-feature packages di-defer karena:
  - Expo typed routes masih beta (auto-generated, gitignored) — belum stabil untuk cross-package typing.
  - Client-server splitting via React Server Components masih experimental — "ongoing work to stabilize routing features and full client-server division in monorepos" ([Expo Server Components docs](https://docs.expo.dev/guides/server-components/)).
- Perlu riset lanjutan untuk ensure web+mobile compatibility sebelum adopt per-feature packages.
- **Foundation** (core baseline by Zahid): folder structure dengan shared packages. **Status: WIP, expected done end of July 2026.** Zahid menetapkan baseline agar Dzaky, Anaz & Faiz bisa langsung build fitur di atasnya.

## Auth & OTP Strategy

### OTP Provider — kirimdev.com

- [kirimdev.com](https://kirimdev.com/) — WhatsApp Business API platform, Indonesia.
- Rp 25K/mo starter (2.000 broadcast, 200K messages).
- Meta-approved AUTHENTICATION templates (auto-approved, no 24h marketing review).
- Single REST endpoint compatible dengan Meta WhatsApp Cloud API. TypeScript SDK. Webhooks dengan HMAC-SHA256 verification.
- OTP via WhatsApp punya delivery rate lebih tinggi dan biaya lebih rendah vs SMS.

### Cost Optimization — Customer-Initiated Messages

- Strategi: registration via WhatsApp di mana **user menginisiasi chat** (klik link WhatsApp → user kirim trigger message → sistem balas dengan OTP).
- Customer-initiated conversations dalam **24-hour window = gratis** (up to 1.000/bulan per WABA).
- Business-initiated authentication template = ~$0.003/msg (~Rp 50).
- Sumber: [MessageCentral pricing](https://www.messagecentral.com/en-in/blog/whatsapp-business-api-pricing), [WhatsBizAPI](https://whatsbizapi.com/blog/whatsapp-business-api-pricing-2026).
- **Hasil: registrasi user baru nyaris gratis** selama dalam free tier.

### WhatsApp Fallback — OPEN DESIGN ITEM

- Current WhatsApp fallback approach tidak disukai. Perlu didesain ulang.
- Pertanyaan terbuka: bagaimana feedback/feel-back flow bekerja kalau OTP via WhatsApp gagal? Apakah fallback ke SMS? Apakah retry? Apakah user pilih channel?
- **Flag untuk diskusi malam ini dengan Imam & Dzaky.** Belum ada keputusan.

## Domain Boundary — Keuangan

- Keuangan (finance) **bukan bagian dari organization dan majlis management**. Domain terpisah.
- Organization management: struktur pengurus, data jamaah, persuratan, arsip.
- Majlis management: jadwal, kepanitiaan, maktab, RSVP, food distribution, checkin.
- Keuangan: terpisah dari keduanya — tidak di-scope di org/majlis management.

## ZIS & Donasi — Embedded dari Hexa

- ZIS (Zakat, Infaq, Sedekah) + donasi akan menjadi **embedded app dari "hexa"** dengan shared auth (Better Auth session).
- Bukan built-from-scratch di super app — embed aplikasi hexa yang sudah ada, dengan SSO/shared session.
- Menggantikan/melengkapi Stream C (sebelumnya: ekhidmah store → embedded). Sekarang: ZIS donasi dari hexa → embedded dengan shared auth. Post-HAF.

## Kapasitas Tim — 10 Jam/Orang/2-Minggu

- Setiap anggota tim berkontribusi **~10 jam per 2 minggu** (~5 jam/minggu, part-time). Bukan full-time.
- Total: 7 orang × ~5 jam/minggu = ~35 jam/minggu ≈ **kurang dari 1 FTE**.
- Implikasi: milestone harus realistis terhadap kapasitas ini. H-3 HAF (Okt 2026) punya ~3 bulan dari launch (14 Jul) = ~6 sprint 2-mingguan = ~420 jam total tim.
- Sprint cadence: **2-mingguan**, bukan 1-mingguan. GitHub Projects untuk sprint board.

## Tooling & Tracking — Markdown + GitHub Issues + GitHub Projects

- **Dokumentasi**: markdown di `docs/ops/` (sudah berjalan, version-controlled). Bisa di-render/publikasikan via super app nanti sebagai knowledge base in-app.
- **Bug tracking**: GitHub Issues — terintegrasi langsung dengan repo, PR, dan commit.
- **Task/sprint tracking**: GitHub Projects (kanban board) — terintegrasi dengan Issues dan PR. Sprint 2-mingguan.
- **Tidak ada tooling terpisah** (tidak pakai Jira, Trello, Notion untuk tracking). Semua di GitHub ecosystem.

## Infrastruktur & Biaya — Biznet Gio VPS

- **Saat ini**: single **Biznet Gio VPS** — self-hosted PostgreSQL + API server (Elysia) + app, semua di satu box.
- **Mungkin nanti**: **Cloudflare R2** untuk object storage (file/image uploads).
- **WhatsApp OTP**: **kirimdev.com** Rp 25K/mo.
- **Tidak ada managed cloud** (tidak pakai RDS, tidak pakai Vercel/Render terpisah, tidak pakai managed Redis).
- SSL via reverse proxy di VPS (Caddy/nginx + Let's Encrypt).
- Total infra cost: VPS + Rp 25K/mo kirimdev. Sangat hemat.
