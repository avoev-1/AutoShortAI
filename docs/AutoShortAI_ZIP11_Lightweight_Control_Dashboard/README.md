# AutoShortAI ZIP11 — Lightweight Control Dashboard

ZIP11 defines the architecture for a lightweight local control dashboard for AutoShortAI.

The goal is to prepare the future polished **AutoShortAI Studio** experience without turning the project into a heavy web application or SaaS product.

The dashboard is a control and visualization layer. It shows the state of the system and sends safe commands through contracts. It does not own production logic, analytics logic, learning logic, rendering logic, distribution logic, or asset logic.

## What ZIP11 Adds

- Dashboard Core
- Control API Contracts
- Dashboard View Models
- Queue Monitoring
- Analytics Monitoring
- Learning Monitoring
- Asset Monitoring
- Platform-Agnostic Dashboard Contracts
- Lightweight UI Adapter Layer
- Dashboard Hooks
- Local-first dashboard safety rules
- Structure tests and example dashboard snapshots

## Long-Term Product Vision

The final product can evolve toward a polished local studio/dashboard interface with:

- sidebar navigation
- overview cards
- generated video previews
- production pipeline status
- recent activity
- projects
- calendar
- analytics
- workers
- storage
- API key panels
- logs
- health monitoring
- system performance panels

ZIP11 does not implement that full interface. It defines the contracts that allow that interface to be built later without coupling the UI to the core.

## Integration With Existing ZIPs

- ZIP06 provides asset, storage, cache, provider-cost, checkpoint, and integrity state.
- ZIP07 provides creative strategy and content blueprint state.
- ZIP08 provides queue, jobs, workers, scheduling, retry, and resource budget state.
- ZIP09 provides analytics and feedback state.
- ZIP10 provides learning suggestions, confidence, policies, and adaptation state.
- ZIP11 visualizes and controls these systems through lightweight contracts.

## Platform Strategy

The dashboard must never be YouTube-only. YouTube Shorts can be the first platform displayed, but the dashboard core must support TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, and future networks through adapters.

## Non-Goals

- no complete heavy UI implementation
- no mandatory React/Vue/Svelte app
- no SaaS conversion
- no cloud dashboard
- no public dashboard
- no authentication system as a required dependency
- no mandatory database
- no direct platform-specific coupling
- no video rendering implementation
- no phone farm implementation
- no Guardian Engine implementation

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The core must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- Every platform integration must pass through adapters, providers, or capability contracts.
- The dashboard must not become the business logic layer.
- The dashboard must stay lightweight and optional.
- No mandatory cloud service, account system, database, or heavy frontend framework is introduced in ZIP11.
- ZIP11 must remain compatible with ZIP01 through ZIP10.
