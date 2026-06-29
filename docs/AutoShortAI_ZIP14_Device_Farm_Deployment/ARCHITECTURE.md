# ZIP14 Architecture — Device Farm Deployment

## Purpose

ZIP14 defines the architecture that lets AutoShortAI distribute selected workloads across local machines, remote machines, and future mobile device farms.

It creates a clean boundary between:

1. scheduled production jobs from ZIP08,
2. render tasks from ZIP12,
3. AI worker tasks from ZIP13,
4. distribution and publishing capabilities from ZIP05 and future ZIP16,
5. dashboard monitoring from ZIP11,
6. future credential isolation from ZIP18.

## High-Level Flow

```text
Production Queue / Runtime Task
        ↓
Device Farm Router
        ↓
Capability + Platform + Safety Matching
        ↓
Device Assignment
        ↓
Device Worker Execution
        ↓
Result / Heartbeat / Failure Report
        ↓
Dashboard / Queue / Analytics / Learning
```

## Core Boundary

The Device Farm module does not own:

- creative strategy
- rendering internals
- AI provider logic
- platform account credentials
- platform publishing policies
- dashboard UI rendering
- analytics scoring
- Guardian validation

It only defines device registration, capabilities, routing, assignment, secure commands, heartbeats, and restricted workflow constraints.

## Device Types

Supported architectural categories:

- local machine
- remote machine
- home server
- VM
- Android device
- iOS device later
- emulator
- browser node
- render node
- AI worker node
- publishing node
- analytics node
- monitoring node
- manual review node

## Capability-Based Deployment

A task must declare what it needs. A device declares what it can safely do.

Routing decisions can consider:

- task type
- platform family
- content maturity
- required device type
- account binding
- CPU/RAM/storage
- online state
- battery state
- network status
- current load
- manual review requirement
- restricted creator mode requirement
- platform policy requirement

## Phone Farm Readiness

Phone farms are represented through neutral contracts:

- PhoneFarmProfile
- PhoneRack
- MobileDeviceSlot
- DeviceRotationPolicy
- AccountBindingPolicy
- PlatformAccountAssignment

The architecture supports legitimate creator workflows, not abusive bot automation.

## Restricted Creator Workflows

Adult / X creator mode is represented as a restricted device workflow category.

A restricted creator task must be able to require:

- isolated device assignment
- isolated platform account binding
- content maturity rating
- creator consent metadata
- all-participants-18-plus metadata
- manual review before dispatch
- manual review before upload
- restricted logs
- credential isolation later via ZIP18
- policy adapter checks later via ZIP16

## Secure Communication

ZIP14 defines communication contracts without forcing one protocol:

- DeviceMessage
- DeviceCommand
- DeviceResponse
- Heartbeat
- DeviceAuthToken
- SecureChannel

Future implementations may use local network, SSH, HTTP local, WebSocket local, desktop agents, or mobile agents.

## Compatibility

ZIP14 is additive. It must not modify the public contracts of ZIP01 through ZIP13.

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
