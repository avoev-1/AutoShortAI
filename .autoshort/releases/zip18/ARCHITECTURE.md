# ZIP18 Architecture — Security, Secrets & Credentials Vault

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

## Architectural Position

ZIP18 is a cross-cutting security layer. It is not a product feature and it is not a platform adapter. It provides secure contracts for every module that needs sensitive data.

```text
Module requests credential
        ↓
Secrets Vault
        ↓
Access Policy
        ↓
Secret Provider
        ↓
Redacted Result / Secure Access
        ↓
Audit Event
```

## 1. Secrets Vault Core

Core contracts:

- `SecretsVault`
- `SecretEntry`
- `SecretReference`
- `SecretScope`
- `SecretKind`
- `SecretProviderKind`
- `SecretAccessPolicy`
- `SecretRotationPolicy`
- `SecretAuditEvent`

Rules:

- modules never hard-code secrets
- modules request secrets by reference
- raw secret values are never printed
- vault implementations must be replaceable
- local-first is default, external vault is optional

## 2. Credential Manager

Credential contracts cover:

- platform credentials
- provider credentials
- publishing credentials
- device credentials
- workspace credentials
- restricted creator credentials

Examples:

```text
YouTube API token
TikTok credential/session reference
Instagram credential reference
OpenAI API key reference
ElevenLabs API key reference
restricted adult creator credential reference
device auth token reference
```

No example in this ZIP contains a real secret.

## 3. Secret Storage Providers

Provider-first architecture:

- `LocalEncryptedFileProvider`
- `EnvironmentVariableProvider`
- `OSKeychainProvider`
- `ExternalVaultProvider`
- `MemoryOnlyProvider`

Future OS targets:

- Windows Credential Manager
- macOS Keychain
- Linux Secret Service / keyring
- secure `.env` style local development references
- optional external vaults

The core must not depend on exactly one provider.

## 4. Access Control Contracts

Contracts:

- `AccessPolicy`
- `AccessRequest`
- `AccessResult`
- `PermissionScope`
- `ModulePermission`
- `CredentialPermission`

Examples:

- publishing runtime can request platform publishing credentials
- analytics can request read-only metrics credentials
- AI workers can request only their provider credentials
- dashboard can show configured / missing / expired states, but never raw secrets
- restricted workflows require restricted scope

## 5. Secret Redaction

Secrets must be redacted from:

- logs
- exceptions
- debug output
- dashboard panels
- Guardian reports
- exports
- examples
- templates

Contracts:

- `SecretRedactor`
- `RedactionRule`
- `SafeLogRecord`
- `SensitiveValueDetector`

Default redaction display:

```text
secret_reference: configured
****REDACTED****
configured: true
```

## 6. Adult / X Creator Secure Isolation

Restricted creator workflows are dedicated, opt-in, and isolated. ZIP18 prepares security contracts for future adult/X creator features without making the core adult-only.

Contracts:

- `RestrictedCredentialVault`
- `RestrictedCredentialPolicy`
- `AdultPlatformCredentialReference`
- `RestrictedWorkspaceSecret`
- `ConsentDocumentReference`
- `AgeVerificationReference`
- `RestrictedExportPolicy`

Rules:

- disabled by default
- opt-in only
- credentials isolated from general workflows
- restricted workspaces isolated from general workspaces
- restricted logs isolated and redacted
- maturity rating required
- consent metadata required
- all participants must be 18+
- manual review required by default
- no illegal, non-consensual, or underage content

## 7. Security Policy Engine

The security policy engine defines checks that Guardian can also enforce.

Policy examples:

- no secrets in code
- no secrets in Git
- no secrets in README files
- no tokens in logs
- no credentials in examples
- no sensitive export without explicit policy
- no restricted credential access from non-restricted modules

## 8. API Key Lifecycle

Lifecycle contracts:

- create
- store
- access
- rotate
- disable
- delete
- audit
- health check
- expiry check

## 9. Dashboard Security View

The dashboard may show status only:

```text
OpenAI: configured
YouTube: expired
TikTok: missing
Restricted Platform: locked
Device Token: configured
```

It must never show raw secrets.

## 10. Hooks

ZIP18 defines plugin-first hooks:

- `before_secret_saved`
- `after_secret_saved`
- `before_secret_accessed`
- `after_secret_accessed`
- `before_credential_rotated`
- `after_credential_rotated`
- `before_sensitive_log_written`
- `after_security_violation_detected`

## Integration with Previous ZIPs

```text
ZIP06 = storage / cache / integrity
ZIP11 = dashboard
ZIP13 = AI providers
ZIP14 = devices / phone farm
ZIP15 = Guardian checks
ZIP16 = multi-platform publishing
ZIP17 = local workspace / media library
ZIP18 = secrets, credentials, redaction, access policies
```
