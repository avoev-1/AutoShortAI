# Integrity, Storage, and Provider Abstraction

## Integrity Checker

The Integrity Checker validates assets after storage, before reuse, and before resume. It must check expected fingerprints, required metadata, and provider-reported state when available.

## Storage Manager

The Storage Manager persists and loads assets through provider contracts. It should not care whether the provider is local filesystem, cloud object storage, or another future backend.

## Provider Abstraction Layer

Providers expose capabilities through a descriptor. The core pipeline asks what a provider supports instead of importing provider-specific SDKs.

## Required provider rules

- Providers must declare capabilities.
- Providers must expose read and write operations through contracts.
- Provider-specific dependencies stay outside the core.
- Provider configuration must be serializable.
