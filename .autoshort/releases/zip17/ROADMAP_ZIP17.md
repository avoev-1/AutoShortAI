# ZIP17 Roadmap — Local Workspace & Media Library

## Phase 1 — Architecture Contracts

- Define workspace manifests.
- Define project structure contracts.
- Define media library models.
- Define import/export contracts.
- Define versioning contracts.
- Define restricted workspace isolation contracts.

## Phase 2 — Lightweight Local Implementation

Claude may later implement:

- JSON manifests
- filesystem-based project registry
- local media index
- basic tag index
- import/export helpers
- integrity links with ZIP06

No database is required at this stage.

## Phase 3 — Dashboard Integration

Expose data for ZIP11:

- projects list
- recent media
- storage usage
- broken references
- restricted workspace status
- latest exports

## Phase 4 — Publishing Package Integration

Prepare ZIP16 packages:

- per-platform export bundles
- metadata attachments
- review status
- maturity rating
- publishing targets

## Phase 5 — Future Enhancements

Potential later extensions:

- optional SQLite index
- optional cloud sync provider
- optional desktop file watcher
- optional media previews
- optional duplicate detection
- optional archive compression
- optional restricted workspace encryption after ZIP18
