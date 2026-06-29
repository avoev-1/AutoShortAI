# AutoShortAI ZIP16 — Multi-Platform Publishing Runtime

ZIP16 defines the **Multi-Platform Publishing Runtime** for AutoShortAI.

ZIP05 introduced intelligent distribution architecture. ZIP16 defines the runtime contracts that will eventually prepare, validate, schedule, and publish rendered content across multiple platforms through adapters.

YouTube Shorts remains the first practical target, but ZIP16 is not YouTube-only. The runtime is designed for:

- YouTube Shorts
- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- X / Twitter video
- generic future video platforms
- optional Adult / X creator platforms in a restricted opt-in category

## What ZIP16 Adds

- Publishing Runtime core contracts
- Platform adapter layer
- Platform capability contracts
- account and channel targeting contracts
- scheduled publishing contracts
- metadata builder contracts
- manual review gate contracts
- adult / X creator platform readiness
- publishing error and retry policy contracts
- publishing hooks
- examples, templates, docs, and structure tests

## Why ZIP16 Exists

AutoShortAI can now define strategy, queue jobs, manage assets, render videos, run AI workers, monitor devices, analyze performance, learn from feedback, and guard its architecture.

The next missing runtime layer is publication:

```text
Rendered Video
    ↓
Publishing Runtime
    ↓
Platform Adapter
    ↓
Manual Review Gate
    ↓
Publish / Schedule
    ↓
Analytics Feedback Loop
```

ZIP16 does not implement real platform API calls. It defines the contracts and boundaries Claude must follow later.

## Non-Goals

- no real API keys
- no real platform login automation
- no bypass of platform rules
- no spam automation
- no dangerous automatic publishing by default
- no SaaS
- no cloud requirement
- no mandatory database
- no YouTube-only logic
- no adult platform activation by default

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The complete software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian Engine rules from ZIP15 must be used as an implementation checklist before and after future work.
- Adult / X creator workflows are dedicated opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
