# ROADMAP ZIP18 — Security, Secrets & Credentials Vault

## ZIP18 Scope

- define vault contracts
- define credential contracts
- define provider abstraction
- define redaction contracts
- define access control contracts
- define restricted credential isolation
- define lifecycle and audit contracts
- define Guardian-compatible security checks

## Implementation Guidance for Claude

Claude must implement ZIP18 gradually and safely:

1. Add data models without real credential storage.
2. Add memory-only provider for tests.
3. Add environment variable provider.
4. Add local encrypted provider only with proven libraries, never custom crypto.
5. Add OS keychain providers per OS later.
6. Add redaction before adding verbose logging.
7. Add Guardian checks for accidental secrets.
8. Add restricted credential isolation before enabling Adult / X creator workflows.

## Future ZIPs

- ZIP19 — Cross-Platform Packaging & Installer
- ZIP20 — Beta Stabilization & Release Governance

## Long-Term Extensions

- optional external vault provider
- OS-native credential providers
- security health dashboard
- credential expiry notifications
- automated token rotation where providers support it
- restricted creator compliance export reports
