# AutoShortAI ZIP18 — Security, Secrets & Credentials Vault

ZIP18 defines the **Security, Secrets & Credentials Vault** architecture for AutoShortAI.

This release introduces the contracts and documentation required to protect API keys, platform credentials, provider credentials, device credentials, restricted creator credentials, sensitive logs, and private configuration.

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
- Secrets, credentials, tokens, session data, account identifiers, restricted workspace data, and private provider configuration must never be committed, logged, displayed, or exported in clear text.

## What ZIP18 Adds

- Secrets Vault core contracts
- credential manager contracts
- secret storage provider abstractions
- access control contracts
- secret redaction contracts
- security policy engine contracts
- credential lifecycle contracts
- dashboard security view contracts
- restricted Adult / X creator secure isolation contracts
- Guardian-compatible security checks
- templates, examples, docs, and structure tests

## Why ZIP18 Exists

AutoShortAI now has architecture for strategy, assets, production queues, analytics, learning, rendering, AI workers, devices, publishing, workspaces, and Guardian checks.

Before packaging and stabilizing the software, AutoShortAI needs a security foundation so implementation can safely handle:

- API keys
- AI provider tokens
- publishing platform credentials
- session data
- device auth tokens
- restricted workspace secrets
- adult creator platform credentials
- private project configuration

## Non-Goals

ZIP18 does not implement a full encryption system, a SaaS authentication system, a cloud vault, a heavy multi-user permission platform, or platform bypass logic.

ZIP18 defines architecture only.
