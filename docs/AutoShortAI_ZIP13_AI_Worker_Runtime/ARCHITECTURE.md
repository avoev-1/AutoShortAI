# ZIP13 Architecture — AI Worker Runtime

## Purpose

ZIP13 defines the AI Worker Runtime for AutoShortAI.

It creates a clean boundary between:

1. creative strategy from ZIP07,
2. scheduled production jobs from ZIP08,
3. assets and storage from ZIP06,
4. rendering inputs for ZIP12,
5. analytics and learning from ZIP09 and ZIP10,
6. dashboard control from ZIP11,
7. future publishing adapters and security vaults.

## Runtime Overview

```text
Production Job / Creative Strategy
        ↓
AI Worker Task
        ↓
Capability-Based Worker Routing
        ↓
Provider or Local Worker Execution
        ↓
Safety / Validation / Manual Review Gate
        ↓
Normalized AI Worker Result
        ↓
Asset Pipeline / Rendering Pipeline / Distribution Pipeline
```

## Core Boundary

The AI runtime defines task and result contracts. It must not directly own:

- platform account credentials
- publishing state
- video rendering internals
- analytics collection
- dashboard UI
- Guardian validation
- device farm deployment
- billing infrastructure

## Worker Types

ZIP13 defines contracts for these worker families:

- script generation
- voice generation
- image generation
- video generation
- subtitle generation
- title generation
- description generation
- hashtag generation
- classification
- optimization
- moderation / policy review
- manual review handoff

Each worker is replaceable by plugin, provider, local implementation, or manual workflow.

## Provider Abstraction

Provider-specific logic must be isolated behind provider contracts.

Future providers may include:

- OpenAI
- Anthropic
- Mistral
- Google
- ElevenLabs
- Runway
- Pika
- Stability
- local models
- custom providers
- manual workers

The core must select providers by capability, not by hard-coded name.

## Capability-Based Routing

A task declares what it needs:

- task type
- language
- target platform context
- maturity rating
- quality target
- latency target
- budget limit
- output modality
- manual review requirement

The runtime chooses a compatible worker/provider based on declared capabilities, cost, availability, policy, and quotas.

## Platform-Agnostic Output Context

ZIP13 must never assume that all content goes to YouTube.

Every AI task can carry a `PlatformContext` describing:

- platform family
- content format
- duration target
- aspect ratio
- language
- caption style
- policy category
- restricted / 18+ flag
- capability requirements

## Restricted / Adult Platform Readiness

Adult / 18+ creator platforms are supported as a restricted platform category, not as a core identity.

The architecture introduces:

- maturity ratings
- restricted platform contexts
- adult platform policy flags
- consent requirements
- age gate requirements
- manual review gates
- policy adapter hooks
- blocked unsafe category markers

Publishing support is deferred to future platform runtime ZIPs. Credential isolation is deferred to the security vault ZIP.

## Safety Defaults

Default behavior must be conservative:

- restricted adult platform tasks require manual review
- missing consent metadata blocks restricted content tasks
- underage or ambiguous-age content must be blocked
- illegal or non-consensual content categories must be blocked
- provider outputs must be validated before storage, rendering, or publishing

## Integration Points

```text
ZIP07 Creative Strategy
        ↓
ZIP08 Production Queue
        ↓
ZIP13 AI Worker Runtime
        ↓
ZIP06 Asset Pipeline
        ↓
ZIP12 Video Rendering
        ↓
ZIP05 / ZIP16 Publishing
        ↓
ZIP09 Analytics
        ↓
ZIP10 Learning
```

## Non-Goals

ZIP13 does not implement real cloud calls, local model inference, video rendering, publishing, account credentials, or dashboard screens.

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
