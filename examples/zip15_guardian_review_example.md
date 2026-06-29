# Example Guardian Review

## Scenario

Claude adds a YouTube analytics implementation.

## Expected Guardian Behavior

Guardian should allow:

- a YouTube adapter
- YouTube-specific capability metadata
- YouTube-specific API implementation behind a provider boundary

Guardian should flag:

- core analytics importing YouTube directly
- dashboard assuming every video has YouTube metrics
- learning engine using YouTube-only fields without normalized metrics
- publishing runtime treating YouTube as the only platform
