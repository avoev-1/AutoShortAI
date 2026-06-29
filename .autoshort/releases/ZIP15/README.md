# AutoShortAI ZIP15 — Guardian Engine Foundation

ZIP15 defines the **Guardian Engine Foundation** for AutoShortAI.

The Guardian Engine is not the software product itself. It is the independent architecture and quality layer that protects AutoShortAI while Claude and future contributors implement the real system.

ZIP15 is intentionally placed now, after ZIP01-ZIP14 and before the next heavy runtime/publishing/security/packaging ZIPs, so the project gets guardrails before implementation becomes too large.

## What ZIP15 Adds

- Guardian Engine core contracts
- Architecture integrity checks
- ZIP backward-compatibility guard
- Module boundary rules
- Platform-agnostic guard
- Restricted / Adult Creator Mode guard
- Performance and lightweight guard
- Security and secrets pre-guard
- Guardian report models
- Rule packs and templates
- Guardian hooks
- Structure tests and examples

## Why ZIP15 Exists

AutoShortAI now has many architectural areas:

- foundation and core
- plugins
- mission orchestration
- distribution
- assets/cache/storage
- creative strategy
- production queue
- analytics
- auto-learning
- dashboard
- rendering
- AI workers
- device farm
- restricted creator workflows

Without a Guardian layer, future implementation can easily become coupled, heavy, platform-specific, or incompatible with earlier ZIPs.

Guardian gives Claude a reference and checklist before and after implementation:

- verify module boundaries
- verify backward compatibility
- verify platform neutrality
- verify lightweight constraints
- verify safety and restricted-mode rules
- verify docs/scripts/tests remain present
- detect architecture drift

## Position in the Project

```text
ZIP01-ZIP14  = product architecture foundations
ZIP15        = independent Guardian guardrail layer
ZIP16-ZIP20  = heavy final architecture protected by Guardian
```

Guardian must stay outside the runtime core.

```text
AutoShortAI Product Core
    ├── assets
    ├── strategy
    ├── queue
    ├── analytics
    ├── learning
    ├── dashboard
    ├── rendering
    ├── AI workers
    └── device farm

Guardian Engine
    └── checks the product architecture from the outside
```

## Non-Goals

- no autonomous code rewriting
- no forced CI/CD integration
- no cloud service
- no SaaS
- no heavy dashboard
- no mandatory database
- no provider-specific enforcement
- no platform-specific enforcement
- no adult-content generation
- no replacement for human review

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
