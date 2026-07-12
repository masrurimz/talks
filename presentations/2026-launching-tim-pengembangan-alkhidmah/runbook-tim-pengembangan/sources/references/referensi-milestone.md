# Referensi — Milestone

> Sumber: `docs/ops/milestones/h-3-haf-2026.md`, `haf-2027.md`. `haul-metesh-2026.md` = historis (superseded).

## Konteks pergeseran milestone

**Haul Metesh (September 2026) bukan lagi sprint target aktif.** Tim baru launching 14 Juli 2026 — jendela ~2 bulan terlalu sempit untuk sprint produksi. Haul Metesh ditandai **superseded** (catatan historis disimpan; kriteria DoD-nya diwariskan).

**Milestone terdekat sekarang = H-3 bulan HAF (Oktober 2026)** — internal readiness checkpoint 3 bulan sebelum HAF wide-usage launch.

Timeline tim:
**Launch 14 Jul → Build (Zahid baseline + tim) Jul–Okt → H-3 checkpoint Okt → Final sprint Okt–Jan → HAF launch Jan 2027.**

## H-3 bulan HAF (Oktober 2026) — milestone terdekat

Internal readiness checkpoint 3 bulan sebelum HAF. Pada milestone ini super app harus feature-complete dan testable.

### Signifikansi

Milestone ini memvalidasi arsitektur dan membuka jalan untuk final sprint menuju wide-usage launch di HAF. Stream A (migrasi jamaah app → super app) harus selesai di sini.

### Definition of Done

- Stream A (jamaah app → super app) migration lengkap.
- Majlis MVP production-ready: CRUD + RSVP + committee flows end-to-end di staging & production.
- Khidmah Hub + organization governance production-ready.
- Auth + cross-subdomain cookie verified end-to-end di `my.alkhidmah.id`.
- Quality gates: crash rate < 1%, load time < 3s.

### Workstreams

| Workstream | Domain |
| --- | --- |
| Stream A migration | cross-cutting |
| Majlis CRUD + RSVP + committee | `prd/majlis/` |
| Khidmah Hub + org governance | `prd/organization/` |
| Auth + cookie cross-subdomain | `prd/04-authentication.md` |
| Production infra provisioning | ops |

### Dependencies

- Expo EAS production builds (iOS/Android).
- PostgreSQL production provisioning.
- API server hosting (`api.alkhidmah.id` live).
- App Store + Play Store submissions (akun ready, review time).
- SSL certificates untuk `my.alkhidmah.id` dan `alkhidmah.id`.

### Risks

| Risk | Mitigation |
| --- | --- |
| Scope creep Stream A | Parity audit frozen sebelum porting. Fitur baru deferred pasca-HAF. |
| Native module crashes di Expo web | Viability check per-app. Feature-flag komponen bermasalah. |
| App Store review delay | Submit 2 minggu sebelum target. Fallback PWA jika reject. |

## HAF (Januari 2027) — wide-usage launch

Setelah HAF, super app menjadi pengganti resmi jamaah app untuk semua pengguna. Public landing live dengan redirect ke super app.

### Definition of Done

- Super app live di 3 platform: iOS App Store + Google Play + `my.alkhidmah.id` web.
- Public landing page (`alkhidmah.id`) shipped — semua route interaktif redirect ke super app (Stream B).
- Ekhidmah store embedding design finalized (Stream C scope dikunci; eksekusi post-HAF).
- Adoption: 1.000+ registered users, 100+ majlis, 70% RSVP rate.
- Trunk-based dev + PR review policy operating at scale.
- Designer onboard (target Q4 2026 atau awal Q1 2027).

### Dependencies

- H-3 HAF 2026 tercapai (prediktor kesiapan).
- App Store + Play Store production approvals.
- Production monitoring aktif (error tracking).
- Designer hired (Q4 2026).

### Risks

| Risk | Mitigation |
| --- | --- |
| H-3 HAF slip → HAF bergeser | Buffer 3 bulan antara H-3 dan HAF. Komunikasi early ke stakeholder. |
| App Store/Play Store reject | Submit 3 minggu sebelum target. Demo account + review notes siap. |
| Adoption rendah | Komunikasi masif 1 bulan sebelum sunset jamaah app. In-app migration wizard. |

## Hubungan antar milestone

- **H-3 HAF = prediktor kesiapan HAF.** Kalau H-3 slip, HAF bergeser.
- Buffer 3 bulan antara H-3 (Okt) dan HAF (Jan) untuk polish + app store submission + adoption push.
- Haul Metesh (Sep 2026) dilewati — tidak lagi relevant sebagai milestone aktif.
