# Dashboard Core

The Dashboard Core coordinates dashboard panels and view-model generation.

It must not run production jobs, generate videos, collect analytics directly, or adapt strategies directly. It delegates to contracts exposed by the correct modules.

## Responsibilities

- register panels
- aggregate dashboard snapshots
- expose safe dashboard status
- normalize module state for display
- dispatch user actions through Control API contracts

## Non-Responsibilities

- rendering videos
- generating scripts
- collecting platform metrics directly
- storing API secrets
- running auto-learning directly
