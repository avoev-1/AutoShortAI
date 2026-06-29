# SAFETY — ZIP11 Lightweight Control Dashboard

## Dashboard Safety Rules

The dashboard is a control surface. It must not become a privileged logic bypass.

## Secrets

- Never expose raw API keys.
- Never expose raw credentials.
- Only display masked secret references.
- Secret editing belongs to a future secure credentials module.

## Local-First Access

- A future web dashboard must default to local-only access.
- Public network exposure must be explicit and protected.
- No cloud account system is introduced by ZIP11.

## Action Safety

Control actions must be explicit, auditable, and reversible when possible.

Examples:

- pause job
- resume job
- cancel job
- retry job
- approve learning suggestion
- reject learning suggestion
- refresh metrics

## Learning Safety

ZIP11 may display ZIP10 suggestions, confidence, risk, and policy status. It must not silently apply risky adaptations.

## Platform Safety

Platform dashboards must use normalized adapters. No platform-specific dashboard code should hard-code YouTube-only assumptions into the core.

## Performance Safety

The dashboard must be lightweight:

- no mandatory heavy frontend
- no mandatory database
- no mandatory cloud service
- no polling loop that burns CPU
- no unbounded logs or metrics kept in memory
