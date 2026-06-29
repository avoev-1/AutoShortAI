# AutoShortAI ZIP14 — Device Farm Deployment

ZIP14 defines the architecture for deploying AutoShortAI workloads across multiple devices, machines, workers, and future phone-farm setups.

It does **not** implement a real mobile app, device control stack, publishing bot, cloud backend, or platform bypass. It defines contracts, models, routing, device health, secure communication, restricted platform handling, examples, templates, hooks, and verification tests that Claude must follow later.

## What ZIP14 Adds

- Device Farm Core
- Device Registry
- Device Node and Capability Contracts
- Worker Deployment Contracts
- Phone Farm Readiness
- Task Routing and Assignment
- Device Health Monitoring
- Secure Communication Contracts
- Platform-Agnostic Device Requirements
- Restricted / Adult Creator Device Workflows
- Dashboard and Queue Integration
- Device Farm Hooks
- Structure tests and examples

## Why ZIP14 Exists

AutoShortAI is designed to become a serious automation studio. Over time, users may want to run parts of the workload on:

- the local workstation
- a secondary laptop
- a home server
- a VM
- an Android phone
- an iPhone later
- a rack of phones
- a render node
- a publishing node
- an analytics node
- a manual review node

ZIP14 makes that possible without turning the core into a heavy distributed system or a platform-specific bot.

## Platform Strategy

ZIP14 is not YouTube-only.

The device farm must support future workflows for:

- YouTube Shorts
- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- X / Twitter video
- adult / X creator platforms through restricted adapters
- future networks

The core speaks through platform capability contracts and device requirements, not through hard-coded platform logic.

## Adult / X Creator Mode Readiness

The user wants AutoShortAI to support creators who publish on adult / 18+ platforms because these workflows can be financially important.

ZIP14 therefore treats adult / X creator support as a **dedicated restricted creator workflow**, not just a vague future note.

Rules:

- opt-in only
- isolated from general content workflows
- age-gated
- adults-only
- consent metadata required
- manual review required by default
- credential isolation required later through security ZIPs
- restricted storage and logs required later
- no illegal content
- no non-consensual content
- no content involving minors
- no automatic unsafe publishing

## Integration With Existing ZIPs

- ZIP08 schedules jobs that may be routed to devices.
- ZIP11 will display device health and worker state in the dashboard.
- ZIP12 may use render nodes for video rendering.
- ZIP13 may use device nodes for AI worker execution or review workflows.
- ZIP16 will later define publishing runtime adapters.
- ZIP18 will later define credential vault and private media isolation.

## Non-Goals

- no real mobile app implementation
- no Android/iOS bypass
- no scraping or platform abuse
- no spam automation
- no automatic unsafe publication
- no cloud backend requirement
- no SaaS conversion
- no mandatory database
- no Guardian Engine implementation
- no full dashboard implementation
- no forced support for one platform only

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The whole software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to YouTube, TikTok, Instagram, OnlyFans, Android, iOS, one OS, one device type, one cloud, or one database.
- Device support must be adapter-based, capability-based, and opt-in.
- Phone farm support is for legitimate management of owned devices and owned/authorized accounts.
- No spam automation, no platform bypass, no credential theft, no security circumvention, and no abusive bot behavior.
- Adult / X creator workflows are a dedicated restricted creator mode, not the core. They are opt-in, isolated, adults-only, consent-based, policy-gated, and manual-review-first.
- ZIP14 must remain compatible with ZIP01 through ZIP13.
