# ROADMAP ZIP13 — AI Worker Runtime

## Phase 1 — Architecture Contracts

- Define AI task, result, worker, provider, and capability contracts.
- Define runtime routing boundaries.
- Define safety and manual review contracts.
- Define restricted / adult platform readiness contracts.
- Add templates, examples, docs, and structure tests.

## Phase 2 — Claude Implementation Later

Claude may implement simple no-op or mock workers first:

- mock script worker
- mock title worker
- mock hashtag worker
- mock moderation worker
- mock provider selector

No provider-specific API integration should be added unless it respects the contracts.

## Phase 3 — Provider Expansion Later

Add providers as plugins/adapters:

- cloud LLM providers
- cloud voice providers
- cloud image providers
- cloud video providers
- local models
- manual workers

## Phase 4 — Restricted Platform Expansion Later

Adult / 18+ creator platform workflows may be added later only with:

- separated adapters
- manual review
- consent metadata
- age gate metadata
- secure credentials
- explicit user-controlled publishing

## Phase 5 — Future ZIP Connections

- ZIP14 device farm deployment may run workers across machines/devices.
- ZIP15 Guardian may validate AI runtime regressions.
- ZIP16 multi-platform publishing may consume AI outputs.
- ZIP18 security vault must isolate credentials and private media.
- ZIP20 stabilization will define release gates.
