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

> Timeline dimulai Juli 2026. Foundation baseline masih WIP (Zahid, target done end Jul). Tim part-time (~10 jam/orang/2-minggu).

| Year | Theme | Key Deliverables | Headcount |
| --- | --- | --- | --- |
| **2026 H2** | Build Basics | Foundation baseline; majlis management (CRUD, RSVP, maktab, undangan); org management | Current team |
| **2027** | Expand & Explore | Eksplorasi kebutuhan org; SK docs; signing; keuangan module; ZIS donasi dari hexa | Current team |
| **2028** | Design & Polish | Hire UI/UX designer; design review & improvement; app-wide redesign | Current team + 1 designer (hire 2028) |

- **2026 H2 (Build Basics)**: Foundation baseline (Zahid, done Jul). Majlis management basics: CRUD, RSVP, committee, maktab, undangan, food distribution, checkin. Org management basics: struktur pengurus, data jamaah. H-3 HAF checkpoint Okt. HAF launch Jan 2027.
- **2027 H1 (Expand)**: Stabilisasi pasca-HAF. Eksplorasi kebutuhan org — riset prioritas. SK (Surat Keputusan) document management. Digital signing.
- **2027 H2 (Explore)**: Keuangan module (domain terpisah). ZIS donasi dari hexa (Stream C). Domain coverage mengikuti prioritas org.
- **2028 (Design & Polish)**: Hire UI/UX designer. Design review & improvement berdasarkan feedback 2026–2027. App-wide redesign. Sisa fitur mengikuti prioritas org.
