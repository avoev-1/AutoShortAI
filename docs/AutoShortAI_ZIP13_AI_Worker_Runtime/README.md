# AutoShortAI ZIP13 — AI Worker Runtime

ZIP13 defines the architecture for AI workers inside AutoShortAI.

It does **not** implement real AI provider calls. It defines contracts, models, workers, provider abstractions, routing, safety gates, prompt templates, hooks, and verification tests that Claude must later follow when implementing the real AI runtime.

## What ZIP13 Adds

- AI Worker Core
- AI Worker Runtime Contracts
- Worker Task and Result Models
- Provider Abstraction Layer
- Capability-Based Routing
- Cost and Quota Guards
- Prompt and Task Templates
- Multi-Platform Output Awareness
- Local-First / Cloud-Optional Worker Strategy
- Worker Queue Integration
- Rendering Integration
- Restricted / Adult Platform Readiness
- Safety and Manual Review Layer
- AI Worker Hooks
- Structure tests and examples

## Why ZIP13 Exists

AutoShortAI needs AI-capable workers for scripts, voices, images, videos, titles, descriptions, hashtags, classifications, moderation checks, and optimization tasks.

ZIP13 makes those workers modular and replaceable so the project does not become locked to OpenAI, Anthropic, ElevenLabs, Runway, Pika, Stability, a local model, or any future provider.

## Platform Strategy

ZIP13 is not YouTube-only.

The AI runtime must support future output contexts for:

- YouTube Shorts
- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- X / Twitter video
- adult / 18+ creator platforms through restricted adapters
- future platforms

The core speaks through platform contexts and capability contracts, never through hard-coded platform logic.

## Restricted / Adult Platform Readiness

ZIP13 prepares optional support for adult / 18+ creator platform workflows. This is architecture readiness only.

The rules are strict:

- restricted platforms are opt-in
- manual review is required by default
- age gate metadata is required
- consent requirements must be represented
- unsafe or illegal content must be blocked
- credentials and media must be isolated later through security ZIPs
- the core must not become adult-specific

## Integration With Existing ZIPs

- ZIP06 supplies assets, cache, storage, checkpoints, provider cost tracking, and integrity checks.
- ZIP07 supplies creative strategies, content profiles, and script blueprints.
- ZIP08 schedules AI tasks and controls workers through the production queue.
- ZIP09 measures performance after publication.
- ZIP10 learns from performance and proposes adaptations.
- ZIP11 visualizes AI jobs, errors, costs, and review gates.
- ZIP12 consumes generated scripts, audio, subtitles, images, and clips for rendering.

## Non-Goals

- no real API call implementation
- no mandatory OpenAI dependency
- no mandatory ElevenLabs dependency
- no mandatory video generation provider
- no mandatory local model
- no complete rendering implementation
- no dashboard implementation
- no Guardian Engine implementation
- no phone farm implementation
- no SaaS conversion
- no mandatory database
- no automatic publication without explicit downstream approval
- no unrestricted adult-content automation

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The whole software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- AI providers must be interchangeable through contracts, capabilities, and adapters.
- No single provider, API, platform, model, database, cloud service, or dashboard UI is mandatory.
- The AI runtime must stay lightweight, queue-aware, budget-aware, cache-aware, and compatible with previous ZIP releases.
- Adult / 18+ creator platform readiness is supported only as a restricted, opt-in platform category with manual review, consent requirements, policy gates, and credential isolation.
- The core must never become adult-only, OnlyFans-only, or platform-specific.
- ZIP13 must remain compatible with ZIP01 through ZIP12.
