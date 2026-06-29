# ZIP06 Roadmap — Smart Asset Pipeline

## Phase 1 — Contracts and structure

- Install ZIP06 package namespace.
- Validate all public contracts import correctly.
- Confirm documentation is installed under `docs/AutoShortAI_ZIP06_Smart_Asset_Pipeline`.
- Keep all files additive and backwards compatible.

## Phase 2 — Minimal reference implementation

Claude may later implement lightweight in-memory and local-disk adapters behind the contracts:

- In-memory asset registry
- SHA-256 fingerprint adapter
- Local dependency graph adapter
- Local disk cache adapter
- JSON checkpoint store
- Filesystem storage provider
- No-op performance profiler
- Static API cost estimator

## Phase 3 — Production-ready internal pipeline

- Add incremental rebuild planner.
- Add cache invalidation policies.
- Add resumable workflow integration with ZIP04 missions.
- Add integrity verification after each asset write.
- Add structured metrics output.

## Phase 4 — Provider ecosystem

- Add provider plugins through ZIP03 SDK rules.
- Support filesystem, cloud object storage, local database metadata, and future remote providers.
- Keep provider SDKs out of the core package.

## Phase 5 — Optimization and maintenance

- Add cache compaction.
- Add API budget guardrails.
- Add performance regression snapshots.
- Prepare later Guardian Engine validation rules without implementing Guardian here.

## Hard rules

- Do not convert AutoShortAI into SaaS.
- Do not create heavy background services.
- Do not couple asset logic to one video platform.
- Do not break ZIP01-ZIP05.
- Do not implement full business logic in this ZIP.
