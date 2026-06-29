# ZIP15 Architecture — Guardian Engine Foundation

## Purpose

ZIP15 defines an independent Guardian Engine that protects AutoShortAI during future implementation and maintenance.

Guardian must answer:

```text
Did this change preserve the architecture?
Did this change break older ZIP contracts?
Did this change couple the core to one platform/provider/UI/DB?
Did this change violate lightweight constraints?
Did this change ignore restricted workflow rules?
Did this change remove required docs/scripts/tests/hooks?
```

## High-Level Flow

```text
New ZIP / New Feature / Claude Implementation
        ↓
Guardian Engine
        ↓
Architecture Rules
        ↓
Compatibility Rules
        ↓
Platform / Provider / Performance / Safety Rules
        ↓
Guardian Report
        ↓
Warnings / Violations / Recommendations
```

## Guardian Boundary

Guardian does not own product behavior.

It does not generate videos, publish content, manage analytics, run AI workers, schedule jobs, control devices, or render UI.

It validates that those modules keep their intended boundaries.

## Core Contracts

- `GuardianEngine`
- `GuardianRule`
- `GuardianCheck`
- `GuardianContext`
- `GuardianResult`
- `GuardianReport`
- `GuardianViolation`
- `GuardianSeverity`
- `GuardianScope`

## Architecture Integrity Checker

Guardian must verify:

- core independence
- plugin-first architecture
- strict module boundaries
- no unnecessary coupling
- no hard-coded platform dependency
- no mandatory cloud
- no mandatory heavy database
- no mandatory heavy UI
- no provider lock-in
- no SaaS drift

## ZIP Compatibility Guard

Guardian must protect ZIP01 through ZIP14 and all future ZIPs.

It should detect:

- deleted public contracts
- renamed modules without adapters
- removed hooks
- missing release docs
- missing tests
- broken install/verify scripts
- incompatible import paths
- cross-module ownership violations

## Module Boundary Rules

Expected ownership:

- ZIP06 owns assets, fingerprints, cache, storage, checkpoints.
- ZIP07 owns strategy, profiles, blueprints, rules, variants.
- ZIP08 owns queue, scheduler, jobs, workers, retries.
- ZIP09 owns analytics, metrics, feedback reports.
- ZIP10 owns learning insights and adaptation suggestions.
- ZIP11 owns lightweight dashboard contracts and view models.
- ZIP12 owns rendering pipeline contracts.
- ZIP13 owns AI worker runtime contracts.
- ZIP14 owns device farm deployment contracts.
- ZIP15 owns architecture protection.

Guardian should flag modules doing another module's job.

## Platform-Agnostic Guard

AutoShortAI must never become YouTube-only.

Guardian must validate that platform logic stays adapter-based for:

- YouTube Shorts
- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- X / Twitter video
- adult / X creator platforms through restricted adapters
- future platforms

Core modules should use platform capability contracts, not direct platform assumptions.

## Provider-Agnostic Guard

AutoShortAI must not become OpenAI-only, ElevenLabs-only, FFmpeg-only, SQLite-only, or cloud-only.

Guardian should prefer:

- providers behind adapters
- optional dependencies
- local-first defaults
- capability-based routing
- fallback readiness

## Restricted / Adult Creator Mode Guard

The future Adult / X Creator Mode is a dedicated opt-in module/category. It must remain isolated and compliant.

Guardian must enforce architectural readiness for:

- opt-in activation
- adult-only requirements
- age-gating
- consent metadata
- maturity ratings
- manual review by default
- restricted asset isolation
- restricted logs
- credential isolation
- policy checks
- blocked unsafe categories

Guardian must flag:

- non-consensual content workflow support
- minor-related content workflow support
- adult workflows mixed into general mode
- unrestricted auto-publishing for restricted content
- restricted assets stored in general folders
- restricted credentials mixed with general credentials

## Performance & Lightweight Guard

Guardian must protect the lightweight philosophy:

- lazy loading when possible
- optional heavy dependencies
- no permanent workers unless required
- CPU/RAM budgets
- bounded queues
- no mandatory cloud runtime
- no mandatory web dashboard
- no mandatory database service

## Security & Secrets Guard

Before ZIP18, Guardian already prepares baseline checks:

- no API keys in code
- no tokens in examples
- no secrets in logs
- no credentials committed
- no private media in examples
- no unsafe export paths

## Guardian Reports

Reports should be readable by humans and tools:

- `guardian_report.json`
- `guardian_report.md`
- architecture score
- compatibility score
- platform neutrality score
- lightweight score
- restricted workflow score
- security risk score
- violations
- warnings
- recommendations

## Guardian Hooks

Plugin-first hooks:

- `before_guardian_run`
- `after_guardian_run`
- `before_rule_checked`
- `after_rule_checked`
- `before_violation_reported`
- `after_violation_reported`
- `before_report_written`
- `after_report_written`

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The whole software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian is not a product feature; it is an independent development and quality layer.
- Adult / X creator workflows are opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
