# ROADMAP ZIP19 — Cross-Platform Packaging & Installer

## ZIP19 Scope

- define packaging contracts
- define installer contracts
- define dependency manager contracts
- define OS platform profiles
- define local launcher contracts
- define module pack profiles
- define restricted creator pack packaging readiness
- define update and migration readiness
- define build profile contracts
- define packaging verification contracts

## Implementation Guidance for Claude

Claude must implement ZIP19 gradually:

1. Add packaging models and manifests only.
2. Add developer-mode install checks.
3. Add local CLI launcher profile.
4. Add optional dependency checks.
5. Add Guardian packaging verification.
6. Add OS profile path resolution.
7. Add build profile metadata.
8. Add restricted creator pack as disabled-by-default metadata only.
9. Add portable mode once core paths are stable.
10. Add desktop launcher integration later, after the lightweight dashboard stabilizes.

## Future ZIP

- ZIP20 — Beta Stabilization & Release Governance

## Long-Term Extensions

- Windows installer profile
- Linux AppImage / deb / rpm profile candidates
- macOS app bundle profile candidate
- portable folder distribution
- local Studio launcher
- worker node installer
- optional external updater
- signed artifacts later
- module marketplace later only if it does not turn AutoShortAI into SaaS
