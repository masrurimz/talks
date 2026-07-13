# Referensi — Opsi Portal Public & Per-Region

> Sumber: `docs/prd/15-public-portal.md`, web research (WordPress official docs). Status: opsi under decision — **belum ada yang diimplementasi**.

## Konteks & Domain Boundary

Alkhidmah punya dua surface yang sudah didefinisikan:

| Surface | URL | Sifat | Auth |
| --- | --- | --- | --- |
| **Public Portal** | `alkhidmah.or.id` (+ `<unit>.alkhidmah.or.id`) | Read-only, SEO, konten public | None |
| **Authenticated App** | `my.alkhidmah.or.id` (+ iOS/Android) | Manajemen org/majlis | Required (Better Auth) |

Pertanyaan yang belum terjawab: **bagaimana arsitektur portal public per-region (PP/PW/PC/PD)?** Apakah tiap unit deploy sendiri, satu CMS custom, atau satu WordPress?

> Hostname `<unit>.alkhidmah.or.id` hanya **contoh netral** — belum di-freeze sampai pilot menentukan skema naming PW/PD/PC.

## Kebutuhan bersama (berlaku untuk semua opsi)

Setiap opsi portal public harus memenuhi:

- **Central portal + identitas per-unit**: satu pintu public plus identitas PW/PD/PC masing-masing.
- **Konten SEO/read-only public**: jadwal majlis, berita, galeri, profil unit.
- **Link ke app terautentikasi**: konten interaktif (RSVP, login) mengarah ke `my.alkhidmah.or.id`.
- **Workflow approval/publishing**: kontributor → editor → publisher.
- **Contributor access organization-scoped**: akses berdasarkan scope unit (PP/PW/PC/PD), bukan sharing ad-hoc.
- **Konvensi SEO/analytics bersama**: metadata, sitemap, tracking konsisten lintas unit.
- **Security updates & backup**: portal tetap harus di-patch dan di-backup.
- **Future markdown/app publishing**: kemampuan menerbitkan konten (markdown) dari app di masa depan.

## Option A — Separate Deployment per PW/PD/PC

Tiap unit punya deployment/database/content sendiri-sendiri.

**Kelebihan:**

- **Otonomi & kontrol penuh** per unit — tiap PW/PD/PC bebas menentukan stack, konten, dan jadwal update.
- **Isolasi security blast radius** per unit (insiden di satu unit tidak menyentuh unit lain).

**Kekurangan:**

- **Operasional berlipat**: hosting, backup, security patching, monitoring, integrasi — dikali jumlah unit.
- **UX/konten tidak konsisten** lintas unit tanpa enforcement manual.
- **Integrasi diduplikasi** (auth, analytics, app links) untuk setiap deployment.
- **Central publishing sulit** — publikasi konten lintas-portal atau standar tunggal menjadi mahal.

> Cocok **hanya** ketika sebuah unit secara hukum/operasional butuh independensi dan ada maintainer yang ditunjuk. Bukan default.

## Option B — Custom CMS + ABAC (REKOMENDASI strategis)

Satu deployment, satu model konten; setiap portal di-resolve berdasarkan unit scope. Otorisasi kontributor/editor/publisher memakai **existing organization hierarchy + Permix ABAC** — bukan model otorisasi kedua yang baru.

**Kelebihan:**

- **Auth terintegrasi** — tidak ada model otorisasi paralel; ABAC organisasi yang sudah ada dipakai ulang (`docs/prd/organization/README.md`, `docs/tdd/architecture/`).
- **UX & standar konten konsisten** lintas unit.
- **Central publishing** — satu pipeline publish, region scoping via ABAC.
- **Future super-app reuse** — konten, API, dan publishing bisa dipakai ulang oleh app.

**Kekurangan:**

- **Build time lebih panjang** ke portal pertama.
- **Editorial UX harus didesain** (bukan out-of-the-box seperti WordPress).
- **ABAC/content workflow harus diuji** sebelum pilot.
- **Satu deployment = shared operational dependency** — outage memengaruhi semua portal.

> **Rekomendasi arah strategis jangka panjang.** Bukan final approval — tetap keputusan Imam/Dzaky malam ini.

## Option C — One WordPress (fallback pilot)

Satu deployment WordPress; konten regional direpresentasikan via categories/custom post types/taxonomies dan roles/plugins yang di-scope.

**Kelebihan:**

- **Pilot tercepat** — editor matang, ekosistem plugin/theme besar, engineering awal rendah.
- **SEO & CMS matang** out-of-the-box.

**Kekurangan:**

- **Regional ABAC/isolation tidak native** untuk hierarki PP→PW→PC→PD — butuh custom post types, capabilities, atau plugin yang ditangani hati-hati.
- **Plugin/theme security risk** — satu kerentanan/update buruk punya blast radius single-site.
- **Integrasi/auth butuh custom code** — tidak terintegrasi dengan Better Auth/ABAC yang sudah ada.
- **Future app publishing butuh API/content contract** — bukan otomatis.

**WordPress Multisite (varian):** centralized Super Admin/plugin/theme management, tapi tetap sharing network-level operational/security blast radius dan menambah kompleksitas network-admin. Multisite **bukan** sama dengan deployment independen penuh (Option A).

> Cocok sebagai **time-boxed pilot** hanya jika portal dibutuhkan sebelum CMS custom siap.

## Decision Matrix

| Dimension | A: separate deployment | B: custom CMS + ABAC | C: one WordPress |
| --- | --- | --- | --- |
| Build effort to first portal | Medium | High | Low |
| Unit autonomy | High | Medium | Low |
| Security blast radius | Low per unit / high ops variance | Medium shared | High shared |
| Regional access control | High isolation | High (existing ABAC) | Medium/Low (custom roles/plugins) |
| Shared UX/content standards | Low | High | Medium |
| Initial integration effort | High × unit | High once | Medium |
| Ongoing maintenance | High × unit | Medium | Low/Medium |
| Future app/markdown publishing | Low/duplicated | High | Medium |
| Cost shape | High × unit | Medium upfront, low incremental | Low initial, plugin/ops variable |

## Rekomendasi & Keputusan malam ini

- **Option B — Custom CMS + ABAC**: target strategis jangka panjang.
- **Option C — One WordPress**: pilot time-boxed **hanya** jika portal dibutuhkan sebelum CMS custom siap.
- **Option A — Separate deployment**: hanya untuk unit yang eksplisit butuh otonomi/independensi.

> **Keputusan malam ini = arah + pilot, bukan komitmen membangun semua opsi.** Implementer tidak membangun ketiganya. Boundary konten: metadata/approval/index bisa dimiliki app/CMS, sementara portal public mengonsumsi konten yang sudah dipublikasikan — tidak ada opsi yang sudah diimplementasi.

## Referensi resmi

- WordPress — [Tools Network screen (Multisite)](https://wordpress.org/documentation/article/tools-network-screen/)
- WordPress — [Roles and Capabilities](https://wordpress.org/documentation/article/roles-and-capabilities/)
