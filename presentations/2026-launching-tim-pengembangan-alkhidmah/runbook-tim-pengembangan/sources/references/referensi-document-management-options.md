# Referensi — Opsi Manajemen Dokumen & Signing

> Sumber: `docs/prd/organization/document-management-options.md`, web research (Google Workspace, Nextcloud, ONLYOFFICE, Paperless-ngx). Status: opsi under decision — **belum ada provider/CMS/tenant/signing engine yang diimplementasi**.

## Scope

Manajemen dokumen organisasi mencakup:

- **Persuratan** (surat masuk/keluar, disposisi)
- **SK (Surat Keputusan)** docs
- **Arsip** (template, dokumen historis)
- **Approval metadata** & access policy
- **Signing orchestration** (alur tanda tangan)

> **Keuangan = domain terpisah.** Tidak di-scope di manajemen dokumen org. App **tidak menduplikasi** binary storage Google/Nextcloud kecuali sebuah opsi eksplisit mengharuskan.

**Boundary yang direkomendasikan:** office suite (Google Workspace/alternatif) memiliki kolaborasi/storage; app Alkhidmah memiliki metadata dokumen, workflow state, regional scope, dan links. Signing = adapter/workflow terpisah, **bukan** implementasi kriptografi ad-hoc.

## Option 1 — Google Workspace (evaluasi pertama yang direkomendasikan)

Docs/Sheets/Drive/Gmail sebagai sistem kolaborasi; app Alkhidmah menyimpan metadata organisasi/dokumen, links, workflow state, dan ABAC scope.

### Topologi default

- **Satu Workspace tenant** di bawah `alkhidmah.or.id`.
- **Shared Drive per unit**: `PP`, `PW/<unit>`, `PC/<unit>`, `PD/<unit>`.
- **Access groups**:
  - `pp-doc-admins@alkhidmah.or.id` — eksplisit **Manager/Content Manager** di semua child drives.
  - Tiap child punya local group sendiri (Content Manager/Contributor di drive-nya).
  - Hindari direct per-user sharing kecuali break-glass account.

### Fakta penting: Shared Drive access

- **OU (Organizational Unit) mengontrol policy/settings, BUKAN membership Drive.** Shared-drive membership **tidak diwariskan** dari OU — harus di-grant eksplisit ke user atau Google Group.
- **PP access ke child drives = eksplisit via group**, bukan warisan OU. Tidak ada asumsi inheritance otomatis dari parent drive ke child drive.
- **Folder/file permissions diwariskan ke bawah di dalam satu drive** — tidak otomatis menyeberang dari parent drive ke child drive.

### Model biaya — USD reference (quote required)

> ⚠️ **Angka di bawah adalah USD reference dari harga resmi Google, sebelum pajak/FX/quote reseller. BUKAN invoice Indonesia.** Biaya IDR final butuh quote Google/reseller, verifikasi nonprofit, pajak/FX, dan konfirmasi user mana yang butuh akun berbayar.

Rumus:

- Nonprofit free: `N × $0 × 12` — jika eligible Google for Nonprofits (verifikasi fitur wajib).
- Business Standard annual: `N × $3.50 × 12`; monthly: `N × $4.20 × 12`.
- Business Plus annual: `N × $6.16 × 12`; monthly: `N × $7.40 × 12`.

| Licensed users | Nonprofit free | Standard annual | Standard monthly | Plus annual | Plus monthly |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | $0/year if eligible | $2,100/year | $2,520/year | $3,696/year | $4,440/year |
| 100 | $0/year if eligible | $4,200/year | $5,040/year | $7,392/year | $8,880/year |
| 300 | $0/year if eligible | $12,600/year | $15,120/year | $22,176/year | $26,640/year |

- Standard: 2 TB/user; Plus: 5 TB/user; **100 TB pooled storage** di nonprofit free.
- Business Standard/Plus include **Google eSignature** — availability eSignature di free nonprofit tier **wajib diverifikasi** sebelum diandalkan.
- Biaya eksisting (Biznet Gio VPS / kirimdev / Cloudflare R2-later) **terpisah** dari license cost Workspace.

### Provider-lobby checklist

Sebelum komit, lobi/klarifikasi ke Google/reseller Indonesia:

- Verifikasi nonprofit & eligibility plan donated/free.
- Quote nonprofit Business Standard/Plus.
- Billing dalam IDR.
- Diskon annual commitment.
- Jumlah akun aktif vs kontributor sesekali.
- Pooled storage & quota.
- Shared Drive & eSignature availability per plan.
- Migration assistance.
- Admin/support SLA.
- Data export/retention policy.
- Training atau partner credits.

## Option 2 — Nextcloud Stack (self-hosted)

Nextcloud + Nextcloud Office (Collabora) + LibreSign/DocuSeal.

**Kelebihan:** kontrol penuh, tidak ada per-user SaaS cost, ekosistem office + signing dalam satu platform self-hosted.

**Kekurangan:**

- **Beban VPS**: office editing, backup, dan concurrent use butuh resource — **tidak ada klaim kapasitas tanpa ukur**. Wajib load test apakah Biznet Gio VPS saat ini cukup.
- Beban operasional: upgrade, security patching, backup, fidelity office.
- Training burden untuk pengurus.

## Option 3 — ONLYOFFICE + Nextcloud

Self-hosted collaborative editor dengan kompatibilitas Microsoft Office yang kuat.

**Tradeoff:** kompatibilitas & integration baik, tapi **licensing/support dan resource needs wajib di-quote** sebelum dipilih.

## Option 4 — Paperless-ngx (complement)

Strong self-hosted OCR/archive/search/workflow.

> **Bukan** pengganti lengkap untuk real-time office collaboration/signing. Posisikan sebagai **complement** arsip/OCR/search, dipasangkan dengan office suite terpisah.

## WPS WebOffice — catatan penting

**WPS WebOffice adalah hosted integration/API platform — BUKAN open-source self-hosted equivalent.** Jangan dipresentasikan sebagai opsi zero-license self-hosted. Jika dikejar, minta quote provider dan terms integrasi terpisah.

## Signing — terpisah dari storage/kolaborasi

Signing adalah workflow/adapter terpisah, bukan bagian dari office suite. Tiga path:

### Path 1 — Google Workspace eSignature

- Tersedia di plan Standard/Plus eligible.
- **Up to 10 signers / 200 fields** per request.
- Evaluasi tercepat, **tapi** wajib validasi formal/legal requirement.

### Path 2 — App workflow + licensed/certified provider

- App Alkhidmah memiliki approval state/audit/integration; provider signature menangani evidence/certificate.
- **Jangan implementasi cryptographic signing ad-hoc.**

### Path 3 — Self-host LibreSign/DocuSeal

- Kontrol & integrasi tinggi, **tapi** wajib validasi: legal acceptance, identity assurance, audit trail, dan operasional.

> **Decision gate:** Imam/Dzaky harus **mendefinisikan apa yang dimaksud "official signing"** (signer identity, approval authority, audit evidence, certificate/PSrE, document retention) **sebelum** memilih implementasi.

## Rollout sequence

1. Provider/nonprofit quote + access proof.
2. Satu PP/PW pilot drive.
3. Document/index workflow.
4. Signing proof-of-concept.
5. Scale ke child units.

> **Edge case:** jika child units pakai Workspace tenant terpisah, dokumentasikan governance external-sharing/group dan perlakukan sebagai fallback dengan biaya operasional lebih tinggi. Model one-tenant tetap target yang direkomendasikan.

## Referensi resmi

- Google — [Workspace for Nonprofits compare](https://www.google.com/nonprofits/workspace/compare/)
- Google — [Indonesia pricing](https://workspace.google.com/intl/en_id/pricing.html)
- Google — [Set up shared drives](https://support.google.com/a/answer/7337469)
- Google — [Shared-drive policies](https://support.google.com/a/answer/7337635)
- Google — [eSignature availability](https://support.google.com/docs/answer/16704506)
- Google — [eSignature limits](https://support.google.com/docs/answer/12315692)
- Nextcloud — [Nextcloud Office](https://nextcloud.com/office/)
- Nextcloud — [File access control](https://docs.nextcloud.com/server/latest/admin_manual/file_workflows/access_control.html)
- Nextcloud — [Office apps](https://apps.nextcloud.com/categories/office)
- Nextcloud — [LibreSign](https://apps.nextcloud.com/apps/libresign)
- ONLYOFFICE — [ONLYOFFICE for Nextcloud](https://www.onlyoffice.com/office-for-nextcloud)
- Paperless-ngx — [docs](https://docs.paperless-ngx.com/)
