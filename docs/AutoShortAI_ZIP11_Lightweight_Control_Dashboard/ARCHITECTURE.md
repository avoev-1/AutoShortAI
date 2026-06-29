# ZIP11 Architecture — Lightweight Control Dashboard

## Purpose

ZIP11 introduces a dashboard architecture that can evolve into the future AutoShortAI Studio interface while preserving strict modularity.

The dashboard is intentionally split into four layers:

1. **Source modules** — existing AutoShortAI modules expose state and actions through contracts.
2. **Control API contracts** — safe commands such as pause, resume, cancel, retry, refresh metrics, and approve adaptation.
3. **Dashboard view models** — lightweight normalized objects made for display.
4. **UI adapters** — CLI, local web, desktop wrapper, or future mobile companion.

The dashboard never bypasses module boundaries.

## Core Rule

The dashboard reads state and sends commands. It does not own the business logic.

```text
AutoShortAI modules
        ↓
Control API Contracts
        ↓
Dashboard View Models
        ↓
UI Adapter Layer
```

## Dashboard Areas

ZIP11 defines the following dashboard areas:

- Overview
- Production Queue
- Job Details
- Assets
- Analytics
- Learning Suggestions
- Costs
- System Health
- Logs
- Platform Status
- Project Activity

## Platform-Agnostic Design

The dashboard core never imports a YouTube-only implementation directly. It uses platform status and metric adapters.

```text
PlatformDashboardAdapter
        ↓
PlatformStatusView
PlatformMetricView
PlatformCapabilityView
```

This keeps YouTube Shorts as the first target while preserving future support for TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, and future networks.

## Local-First Design

ZIP11 assumes a local/private dashboard by default.

- Default host should be local-only when a web adapter exists.
- No public dashboard is introduced.
- No SaaS authentication model is introduced.
- Secrets must never be exposed in dashboard view models.
- API keys must be represented only as masked metadata.

## Relationship With Previous ZIPs

- ZIP06 provides asset and storage views.
- ZIP07 provides creative strategy context.
- ZIP08 provides queue, job, worker, and resource usage views.
- ZIP09 provides metrics, reporting, and performance views.
- ZIP10 provides learning suggestion and confidence views.

## Relationship With Future ZIPs

- ZIP12 Video Rendering Pipeline can expose render state to ZIP11.
- ZIP13 AI Worker Runtime can expose worker/provider status to ZIP11.
- ZIP14 Device Farm Deployment can expose device health to ZIP11.
- ZIP15 Guardian Engine can expose architecture health and regression status to ZIP11.

## Compatibility

ZIP11 is additive. It must not rename, remove, or rewrite previous module namespaces.

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The core must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- Every platform integration must pass through adapters, providers, or capability contracts.
- The dashboard must not become the business logic layer.
- The dashboard must stay lightweight and optional.
- No mandatory cloud service, account system, database, or heavy frontend framework is introduced in ZIP11.
- ZIP11 must remain compatible with ZIP01 through ZIP10.
