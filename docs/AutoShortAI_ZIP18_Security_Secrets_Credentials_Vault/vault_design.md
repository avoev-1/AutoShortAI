# Vault Design

The vault is an abstraction. The core stores and retrieves secrets through `SecretReference`, not raw strings.

## Flow

```text
Module
  -> AccessRequest
  -> SecretsVault
  -> AccessPolicy
  -> SecretProvider
  -> SecretEntry
  -> AuditEvent
```

## Provider Strategy

Default implementations should start with memory-only and environment variables for development. Persistent encrypted providers must use proven libraries and avoid home-made crypto.
