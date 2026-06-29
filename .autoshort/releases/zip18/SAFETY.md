# SAFETY — ZIP18 Security, Secrets & Credentials Vault

## Security Rules

- never commit secrets
- never hard-code tokens
- never print raw credentials
- never place real secrets in examples
- never place tokens in templates
- never include secrets in Guardian reports
- never expose restricted credentials in dashboard views
- never mix restricted creator credentials with general credentials

## Cryptography Rule

ZIP18 does not authorize custom cryptography. Future implementation must use proven libraries and OS keychains where appropriate.

## Restricted / Adult Creator Rules

Restricted creator workflows are opt-in and isolated.

Required safety metadata:

- maturity rating
- consent metadata
- all participants 18+ flag
- manual review status
- restricted workspace reference
- restricted credential reference

Blocked:

- underage content
- non-consensual content
- illegal content
- publication without manual review by default
- credential sharing between general and restricted workflows

## Logging Rules

Logs and reports must show only redacted values or status-level values.
