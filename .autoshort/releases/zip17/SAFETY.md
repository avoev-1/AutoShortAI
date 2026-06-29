# ZIP17 Safety

## General safety principles

- Keep workspace data local-first.
- Do not store secrets in workspace manifests.
- Do not log credentials.
- Do not require cloud storage.
- Do not require a database.
- Do not mix platform-specific implementation with core workspace logic.

## Restricted / Adult Creator Mode

Restricted creator workspace support is opt-in and disabled by default.

Required safeguards:

- all participants must be verified 18+
- consent metadata must be tracked
- content maturity rating must be present
- manual review must be required by default
- restricted assets must not mix with general assets
- restricted exports must remain isolated
- restricted logs must be separated
- unsafe publishing must be blocked

Forbidden:

- illegal content
- non-consensual content
- underage content
- publishing without review in restricted mode
- bypassing platform rules
- leaking restricted media to general folders
