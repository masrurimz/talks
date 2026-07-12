# Referensi — Strategi & Roadmap

> Sumber: `docs/ops/strategy/super-app-consolidation.md`, `roadmap-2026-2028.md`, `docs/og-roadmap-digitalisasi.md` §01+§05.

## Tujuan utama digitalisasi (OG roadmap §01)

1. Mewujudkan tata kelola keorganisasian yang profesional dan berkelanjutan.
2. Memfasilitasi manajemen penyelenggaraan majlis yang terkelola.
3. Mensyiarkan seluas-luasnya majlis dan nilai jama'ah Al Khidmah.
4. Menuju cita-cita mulia: **Al Khidmah sebagai Oase Dunia**.

Landasan spiritual: digitalisasi adalah kolaborator, akselerator, dan alat pendukung visi besar Hadratusy Syaikh r.a. menuju Al Khidmah Oase Dunia.

## Program Kerja Bidang Media & IT (OG roadmap §05)

7 item Program Kerja:

1. Pengembangan sistem database organisasi, jama'ah, dan majlis — fungsi pemetaan, pembinaan, pengembangan.
2. Pengembangan IT tools untuk pengelolaan organisasi dan kemajlisan (administratif, dokumentasi, pendanaan).
3. Pengembangan Web Portal Jama'ah Al Khidmah.
4. Pengembangan kanal media sosial official untuk komunikasi dan syiar.
5. Pembentukan media komunikasi dan peningkatan kapabilitas tim pengelola media.
6. Pembuatan Masterplan Media dan IT.
7. Rekrutasi dan pengembangan Tim Media dan IT.

> **Item 1–3 adalah scope Departemen Pengembangan IT** (database, IT tools, web portal). Item 4 adalah scope Multimedia. Item 5–7 shared.

## Strategi konsolidasi super app

### As-Is (3 app terpisah)

| App | Platform | Status |
| --- | --- | --- |
| Jamaah app | Mobile (separate codebase) | Active, sunsetting pasca-migrasi |
| Web app | `alkhidmah.or.id` (TanStack Start) | Active, refactor jadi thin landing |
| Ekhidmah store | Mobile (separate codebase) | Active, embedding TBD pasca-HAF |

### To-Be (1 super app + 1 thin landing)

| Surface | URL | Tech | Auth |
| --- | --- | --- | --- |
| **Super App** | `my.alkhidmah.or.id` (+ iOS/Android) | Expo Router universal (`apps/native`) | Required (Better Auth) |
| **Public Landing** | `alkhidmah.or.id` | `apps/web` (TanStack Start, SSG-first) | None |

### Kenapa Expo Web (bukan web app terpisah)

1. **Shared codebase** = satu pipeline fitur. Fitur ditulis sekali di `apps/native`, jalan di iOS/Android/Web.
2. **`apps/native` desktop-first adaptive mobile** — dibangun desktop-first dengan adaptive breakpoint ke mobile. Info density lebih baik untuk dashboard/admin flows. SidebarTabBar tablet/desktop, FloatingTabBar mobile.
3. **Satu auth cookie domain** — cross-subdomain cookie (`sameSite: "none"`, `secure: true`). Login di `alkhidmah.or.id` berlaku di `my.alkhidmah.or.id`.

## Tiga stream migrasi

| Stream | Dari → Ke | Target | Scope |
| --- | --- | --- | --- |
| **A** | Jamaah app → Super App | **H-3 HAF (Okt 2026)** | Parity audit → port missing features → data migration → sunset jamaah app |
| **B** | Web app → Thin Landing | **HAF (Jan 2027)** | Strip `apps/web` jadi landing; redirect route interaktif ke `my.alkhidmah.or.id` |
| **C** | ZIS donasi → Embedded dari hexa | **Q2 2027** | ZIS + donasi embedded app dari hexa dengan shared auth (Better Auth). Post-HAF |

> Stream A paling kritis — mengaktifkan super app untuk pengguna nyata.

### Risks & mitigations

| Risk | Mitigation |
| --- | --- |
| Scope creep Stream A | Parity audit dibekukan sebelum porting. Fitur baru masuk backlog pasca-H-3 HAF. |
| Web-parity gaps di Expo web | Viability check per-app sebelum redirect aktif. Komponen yang crash di-feature-flag. |
| Data migration integrity | Dual-run period selama migrasi. Rollback plan jika mismatch. |

### Domain Boundary — Keuangan

Keuangan (finance) **bukan bagian dari organization dan majlis management**. Domain terpisah. Org management: struktur pengurus, data jamaah, persuratan, arsip. Majlis management: jadwal, kepanitiaan, maktab, RSVP. Keuangan: terpisah dari keduanya.

## Roadmap 2026–2028

| Year | Theme | Key Milestones | Headcount |
| --- | --- | --- | --- |
| **2026 H2** | Build + Migrate + Launch | H-3 HAF (Okt 2026), HAF launch (Jan 2027) | Current team |
| **2027** | Functionality Coverage | Semua PRD domain MVP parity; ZIS donasi dari hexa | Current team + 1 designer (hire Q4 2026) |
| **2028** | Redesign + UX Maturity | App-wide redesign; riset usability | + designer full-time |

- **2026 H2**: Stream A aktif (parity audit Jul → porting Aug–Sep → data migration Okt). H-3 HAF milestone Okt. Backend stabil (auth + cross-subdomain). Stream B dimulai Q4 (strip web ke thin landing). Polish pasca-H-3 HAF. Designer hiring mulai. HAF launch Jan 2027.
- **2027 H1**: Stabilisasi pasca-HAF (monitoring, performance, crash < 1%). PRD domain coverage sprint (content, zis, spiritual, notification).
- **2027 H2**: Stream C (ZIS donasi dari hexa embedding). Domain coverage lanjutan (store, organization). Designer onboard.
- **2028**: App-wide redesign. Usability research. Designer full-time.
