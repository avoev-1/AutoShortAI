# ROADMAP ZIP14 — Device Farm Deployment

## Phase 1 — Architecture Contracts

- Define device farm models.
- Define device registry contracts.
- Define device capability and health contracts.
- Define device task and assignment contracts.
- Define secure communication primitives.
- Define restricted creator workflow contracts.

## Phase 2 — Local Machine Support

- Register local machine as a device node.
- Run lightweight local health checks.
- Route basic tasks to local worker nodes.
- Keep all behavior local-first.

## Phase 3 — Remote Node Support

- Add remote machine profiles.
- Add heartbeat contracts.
- Add worker availability status.
- Add failure reporting and retry metadata.

## Phase 4 — Mobile Device Readiness

- Prepare Android device profiles.
- Prepare iOS device profiles for later.
- Prepare phone rack and phone slot definitions.
- Prepare platform account binding policies.

## Phase 5 — Restricted Creator Mode Readiness

- Add dedicated Adult / X Creator Mode device profiles.
- Enforce opt-in restricted workflows.
- Require consent and age metadata.
- Require manual review by default.
- Prepare credential isolation integration with ZIP18.

## Phase 6 — Future Implementation

Claude may later implement real device agents, but only after respecting:

- platform policies
- user ownership / authorization
- credential isolation
- local-first design
- no abusive automation
- no security bypass
