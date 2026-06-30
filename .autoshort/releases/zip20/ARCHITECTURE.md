# ZIP20 Architecture — Beta Stabilization & Release Governance

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The complete software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, one renderer, one app store, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian Engine rules from ZIP15 must be used as an implementation checklist before and after future work.
- Secrets and credentials are protected by ZIP18 and must never be packaged, logged, committed, or exported in clear text.
- Adult / X creator workflows are dedicated opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
- Heavy dependencies must be optional and module-scoped, never forced globally.
- ZIP20 declares the AutoShortAI v1 Architecture Baseline.

## Architectural Position

ZIP20 is the release governance, stabilization, and baseline declaration layer.

It does not own product runtime behavior. It defines the rules and contracts that decide whether AutoShortAI is ready for beta and whether future changes preserve the architecture.

```text
Architecture ZIPs
        ↓
Guardian Verification
        ↓
Security Verification
        ↓
Packaging Verification
        ↓
Beta Release Checklist
        ↓
AutoShortAI v1 Architecture Baseline
```

## 1. Beta Release Governance

Core contracts:

- `BetaRelease`
- `ReleaseCandidate`
- `ReleaseStatus`
- `ReleaseChecklist`
- `ReleaseGate`
- `ReleaseApproval`
- `ReleaseRisk`
- `ReleaseNote`

Release statuses:

- `draft`
- `candidate`
- `validated`
- `blocked`
- `released`
- `deprecated`

A beta release must be checklist-driven and auditable. Claude must not treat a release as beta-ready just because code runs locally.

## 2. Architecture Freeze v1

ZIP20 declares:

```text
AutoShortAI v1 Architecture Baseline = ZIP01-ZIP20
```

Meaning:

- ZIP01-ZIP20 are the official baseline.
- Future ZIPs may extend but not break this baseline.
- Existing contracts must not be removed without replacement and migration.
- Existing modules must not be re-scoped without governance review.
- Optional dependencies must not become global requirements.
- Platform adapters must remain adapters, not core dependencies.

## 3. Full System Verification

ZIP20 prepares a full verification layer that checks:

- project structure
- release metadata
- installed modules
- Python imports
- root docs
- roadmaps
- hooks
- structure tests
- install scripts
- verify scripts
- platform-agnostic policies
- restricted workflow isolation
- secret hygiene
- packaging readiness
- Guardian rules

## 4. Release Checklist

Official beta checklist categories:

- Guardian check passed
- VERIFY passed
- no secret in Git
- no broken module boundary
- no single-platform lock-in
- no mandatory heavy dependency
- no adult / restricted mode enabled by default
- docs updated
- roadmap updated
- structure tests passed
- backward compatibility preserved

## 5. Module Stability Matrix

Modules tracked by ZIP20:

- production foundation
- modular core
- SDK plugin system
- mission workflow orchestrator
- intelligent distribution platform
- smart asset pipeline
- creative strategy engine
- production queue scheduler
- analytics feedback loop
- auto-learning adaptation engine
- lightweight control dashboard
- video rendering pipeline
- AI worker runtime
- device farm deployment
- Guardian Engine foundation
- multi-platform publishing runtime
- local workspace media library
- security secrets credentials vault
- cross-platform packaging installer
- beta stabilization release governance

Stability statuses:

- `planned`
- `architecture_ready`
- `implementation_ready`
- `experimental`
- `stable`
- `restricted`
- `blocked`

## 6. Risk Management

Risk contracts:

- `ReleaseRisk`
- `RiskLevel`
- `RiskCategory`
- `RiskMitigation`
- `KnownIssue`
- `RegressionRisk`
- `BreakingChangeWarning`

Risk categories:

- architecture
- security
- performance
- platform
- adult_restricted_mode
- publishing
- storage
- credentials
- rendering
- ai_provider
- packaging
- compatibility

## 7. Backward Compatibility Policy

Official rules:

- never break previous ZIPs
- do not delete contracts without replacement
- do not rename modules without migration
- do not move files without migration
- do not make optional dependencies mandatory
- do not turn AutoShortAI into SaaS
- do not couple the core to YouTube or any single platform
- do not activate restricted workflows by default
- do not store secrets in examples, templates, or logs

## 8. Restricted / Adult Creator Governance

Adult / X Creator Mode is a real product direction, but restricted and opt-in.

Rules:

- disabled by default
- explicit opt-in only
- isolated workspace
- isolated credentials
- isolated logs
- isolated device/account bindings
- manual review by default
- maturity rating required
- consent metadata required
- all participants 18+ required
- platform policy checks required
- no illegal content
- no non-consensual content
- no minors
- no mixing with general content

The restricted creator workflow must never contaminate the general core.

## 9. Platform-Agnostic Governance

AutoShortAI is not YouTube-only.

Supported direction:

- YouTube Shorts first
- TikTok later
- Instagram Reels later
- Facebook Reels later
- Snapchat Spotlight later
- X / Twitter video later
- adult / restricted creator platforms later
- future platforms via adapters

Required architecture mechanisms:

- platform adapters
- provider abstractions
- capability contracts
- platform profiles
- manual review gates
- normalized analytics models
- platform-aware rendering profiles

## 10. Post-ZIP20 Roadmap

After ZIP20, architecture work shifts from foundation ZIPs to targeted extension ZIPs, implementation guidance, platform adapter packs, UI polish, optimized local AI, restricted creator studio extensions, and production readiness.

Potential future ZIPs:

- ZIP21 — Adult Creator Studio Extension
- ZIP22 — Studio UI Polish Pack
- ZIP23 — Advanced Video Template Pack
- ZIP24 — Platform Adapter Pack
- ZIP25 — Local AI Optimization Pack

## Guardrail for Claude

Before implementing future work, Claude must check:

1. Does the change preserve ZIP01-ZIP20?
2. Does it respect Guardian rules?
3. Does it avoid platform lock-in?
4. Does it avoid provider lock-in?
5. Does it keep heavy dependencies optional?
6. Does it preserve restricted workflow isolation?
7. Does it avoid secrets in code/logs/examples?
8. Does it document migration and rollback if needed?
