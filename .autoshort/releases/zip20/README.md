# AutoShortAI ZIP20 — Beta Stabilization & Release Governance

ZIP20 defines the **Beta Stabilization & Release Governance** architecture for AutoShortAI.

This release closes the first full architecture cycle and establishes the **AutoShortAI v1 Architecture Baseline** across ZIP01-ZIP20.

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

## What ZIP20 Adds

- beta release governance contracts
- release candidate contracts
- release gate contracts
- architecture freeze v1 documentation
- full-system verification contracts
- official release checklist contracts
- module stability matrix contracts
- risk management contracts
- backward compatibility policy contracts
- platform-agnostic governance policy
- restricted Adult / X creator governance policy
- post-ZIP20 roadmap governance
- Guardian-compatible release gates
- templates, examples, docs, and structure tests

## Why ZIP20 Exists

AutoShortAI now has architecture for production foundations, modular core, plugins, mission workflows, distribution, asset pipeline, strategy, queues, analytics, learning, dashboard, rendering, AI workers, device farms, Guardian, publishing runtime, workspace, vault, and packaging.

ZIP20 turns these releases into a stable beta architecture baseline so implementation can begin without drift.

## Non-Goals

ZIP20 does not add a new product feature, final UI, SaaS deployment, cloud service, mandatory database, mandatory heavy dependency, auto-publisher, or complete implementation.

ZIP20 defines governance and stabilization architecture only.
