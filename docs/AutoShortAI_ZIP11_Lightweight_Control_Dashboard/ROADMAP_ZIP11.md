# ROADMAP ZIP11 — Lightweight Control Dashboard

## Phase 1 — Architecture Contracts

- Define dashboard models.
- Define safe control actions.
- Define panel contracts.
- Define UI adapter boundaries.
- Define platform dashboard adapters.

## Phase 2 — Local CLI Prototype

- Implement a basic CLI/status view later.
- Read queue state from ZIP08 contracts.
- Read analytics state from ZIP09 contracts.
- Read learning suggestions from ZIP10 contracts.
- Display only masked secrets and safe metadata.

## Phase 3 — Local Web Prototype

- Add a local-only web adapter later.
- Keep it optional.
- Avoid direct coupling between UI routes and business modules.
- Keep API contracts stable.

## Phase 4 — Studio UI Evolution

- Build a polished local studio interface.
- Add overview cards, preview panels, activity feed, project navigation, and system health.
- Keep platform support adapter-based.

## Phase 5 — Future Integration

- Add rendering status after ZIP12.
- Add AI worker/provider status after ZIP13.
- Add device farm health after ZIP14.
- Add Guardian health after ZIP15.

## Done Criteria

ZIP11 is complete when future implementations can build CLI, local web, desktop, or mobile companion dashboards without embedding business logic inside the dashboard layer.
