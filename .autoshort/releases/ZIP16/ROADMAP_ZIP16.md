# ROADMAP ZIP16 — Multi-Platform Publishing Runtime

## Phase 1 — Contracts

- Add normalized publishing models.
- Add platform capability contracts.
- Add adapter protocols.
- Add manual review gate contracts.
- Add restricted adult creator publishing contracts.

## Phase 2 — Dry-Run Runtime

- Implement a dry-run publishing runtime.
- Validate rendered media manifests from ZIP12.
- Validate metadata without calling real platform APIs.
- Generate publishing reports.

## Phase 3 — Adapter Skeletons

- Add adapter skeletons for YouTube Shorts, TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, and generic platforms.
- Keep every adapter optional.
- Keep the core independent.

## Phase 4 — Account and Channel Profiles

- Add account/channel profile loading.
- Add account health models.
- Add permission and review state models.
- Integrate with future ZIP18 credentials vault.

## Phase 5 — Restricted Creator Readiness

- Add opt-in restricted publishing profiles.
- Add isolated adult creator account binding contracts.
- Add consent, age-gate, maturity rating, and review checklist enforcement.
- Keep publication blocked unless compliance data is present.

## Phase 6 — Future Runtime Implementation

- Claude may implement real platform publishing only after credentials, safety, rate limits, and manual review flows are defined.
- No implementation may bypass platform rules.
- No implementation may make adult workflows default.

## Next ZIPs

- ZIP17 — Local Workspace & Media Library
- ZIP18 — Security, Secrets & Credentials Vault
- ZIP19 — Cross-Platform Packaging & Installer
- ZIP20 — Beta Stabilization & Release Governance
