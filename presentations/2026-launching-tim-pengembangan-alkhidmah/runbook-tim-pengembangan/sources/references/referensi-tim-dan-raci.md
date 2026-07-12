# Referensi — Tim & RACI

> Sumber: `docs/ops/team/roster.md`, `raci.md`, plus konfigurasi tim aktual.

## Struktur Bidang Media & IT

Departemen Pengembangan IT adalah sub-tim di bawah **Bidang Media & IT PP Jama'ah Al Khidmah**.

| Role Title | Responsibility | Scope |
| --- | --- | --- |
| **Ketua Bidang** | Accountable untuk seluruh divisi Media & IT; menandatangani arah, scope, rilis. | Whole bidang |
| **Sekretaris Bidang** | Administrasi, dokumentasi, progress reporting, koordinasi antar-bidang. | Whole bidang |
| **Koordinator Pengembangan** | Memimpin software development; punya technical roadmap, arsitektur, delivery. Maps ke Tech Lead. | Development sub-team |
| **Koordinator Multimedia** | Memimpin kanal social media / multimedia. **Outside dev scope.** | Multimedia sub-team |

## Tim aktual (Departemen Pengembangan IT)

| Person | Role | Scope |
| --- | --- | --- |
| **Imam** | Ketua Bidang (Accountable) | Signs off direction, scope, releases — leadership/stakeholder |
| **Dzaky** | Developer (dual role: Sekretaris Bidang) | Development on top of Zahid's baseline; admin bidang |
| **Zahid** | Tech Lead / Koordinator Pengembangan | Core baseline arsitektur → development; release authority; stakeholder bridge |
| **Anaz** | Developer + QA Automation | Development + automated test / QA infrastructure |
| **Faiz** | Developer (mantan tim jamaah app) | Development; knowledge transfer dari jamaah app lama (Stream A migration) |
| **Shofi** | Product Manager + per-product QA | Mengumpulkan kebutuhan, desain produk, QA pada product yang dipegang |
| **Taufik** | Product Manager + per-product QA | Mengumpulkan kebutuhan, desain produk, QA pada product yang dipegang |
| **Tahzan** | Product Manager + per-product QA | Mengumpulkan kebutuhan, desain produk, QA pada product yang dipegang |

### Pembagian: Development vs Product

- **Development** (4 orang): Zahid (lead, bangun core baseline) → Dzaky, Anaz & Faiz kembangkan fitur di atasnya. Faiz membawa knowledge dari jamaah app lama — langsung relevan untuk Stream A (migrasi jamaah app → super app).
- **Product** (3 orang): Shofi, Taufik & Tahzan mengumpulkan kebutuhan produk, mendesain UX/flow, dan melakukan QA per-product sendiri.
- **Leadership**: Imam sebagai Ketua Bidang (Accountable), Dzaky dual-role sebagai Sekretaris.

> Catatan: `roster.md` di repo punya slot generik (Full-stack/Mobile/Backend/QA/Designer, tanpa role PM) yang merupakan **target structure**. Tim aktual di atas adalah konfigurasi nyata. Update roster formal adalah PR terpisah di masa depan.

## Role definitions

| Role | Deskripsi |
| --- | --- |
| **Tech Lead / Ketua Departemen** | Architecture decisions, trunk keeper, release authority, stakeholder bridge ke Pengurus. Zahid menetapkan core baseline agar developer lain bisa build di atasnya. |
| **Developer** | Memegang `apps/*` + `packages/api`. Cross-cutting feature work. Dzaky, Anaz & Faiz. |
| **QA Automation** | Automated test infrastructure, regression suites, release verification. Anaz memegang ini + development. |
| **Product Manager** | Mengumpulkan kebutuhan produk, mendesain UX/flow, handoff ke developer, per-product QA. Shofi, Taufik & Tahzan. |

## RACI Bidang Delivery (Program Kerja)

Accountability per Program Kerja item (per role title, bukan nama orang):

| Program Kerja Item | Ketua Bidang | Sekretaris Bidang | Koord. Pengembangan | Koord. Multimedia |
| --- | :---: | :---: | :---: | :---: |
| 1. Sistem database (org, jama'ah, majlis) | A | C | R | I |
| 2. IT Tools (org & majlis management) | A | C | R | I |
| 3. Web Portal Al Khidmah | A | C | R | C |
| 4. Kanal Media Sosial Official | A | C | I | R |
| 5. Kapabilitas tim Pengelola Media | A | R | C | R |
| 6. Masterplan Media & IT | A/R | C | R | C |
| 7. Rekrutasi & pengembangan Tim | A | R | R | R |

> Items 1–3 = scope Koord. Pengembangan (Departemen Pengembangan IT). Item 4 = Multimedia. Items 5–7 shared.

Legend: **R** = Responsible (mengerjakan) · **A** = Accountable (tanggung jawab akhir, satu orang) · **C** = Consulted · **I** = Informed.

## RACI workstream (adaptasi ke tim aktual)

| Workstream | Zahid (TL) | Dzaky/Anaz/Faiz (Dev) | Shofi/Taufik/Tahzan (PM) | Imam (KB) |
| --- | :---: | :---: | :---: | :---: |
| Architecture decisions | A/R | C | C | I |
| Feature development | C | R | C | I |
| Product requirements & design | C | C | A/R | I |
| QA & local retest | C | R (Anaz lead) | R (per-product) | — |
| Production deploy | A | R | — | I |
| Product meeting agenda | A | C | C | C |

> Konvensi: kalau peran tidak tercantum, dianggap tidak involved. Hanya tulis I kalau informed secara eksplisit.
