# AutoShortAI ZIP19 — Cross-Platform Packaging & Installer

ZIP19 defines the **Cross-Platform Packaging & Installer** architecture for AutoShortAI.

This release prepares AutoShortAI to become a real installable local application across Windows, Linux, and macOS while preserving modularity, local-first operation, platform-agnostic design, optional dependencies, and Guardian-compatible checks.

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The complete software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, one renderer, one app store, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian Engine rules from ZIP15 must be used as an implementation checklist before and after future work.
- Secrets and credentials are protected by ZIP18 and must never be packaged or written into installers.
- Adult / X creator workflows are dedicated opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
- Heavy dependencies must be optional and module-scoped, never forced globally.

## What ZIP19 Adds

- packaging core contracts
- installer architecture contracts
- dependency manager contracts
- OS platform profile contracts
- local app launcher contracts
- module installation profile contracts
- restricted Adult / X creator pack packaging readiness
- update and migration readiness contracts
- build profile contracts
- packaging verification contracts
- Guardian-compatible packaging checks
- templates, examples, docs, and structure tests

## Why ZIP19 Exists

AutoShortAI now has architecture for strategy, assets, production queues, analytics, learning, dashboard, rendering, AI workers, devices, Guardian, publishing, workspaces, and security.

Before beta stabilization, AutoShortAI needs packaging architecture so implementation can support:

- developer installs
- local user installs
- portable CLI mode
- desktop Studio launcher mode
- headless worker nodes
- device node packages
- optional module packs
- restricted creator pack isolation
- Windows, Linux, and macOS profile differences

## Non-Goals

ZIP19 does not implement a store release, Electron app, auto-updater, cloud deployment, SaaS packaging, mandatory FFmpeg, mandatory database, mandatory Node runtime, or real installer binary.

ZIP19 defines architecture only.
