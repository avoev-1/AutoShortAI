# Guardian Compliance for ZIP16

ZIP15 Guardian should check ZIP16 implementations for:

- platform-agnostic core
- separate platform adapters
- no hard-coded platform API calls in core
- no credential leakage
- no bypass or spam logic
- manual review gate present
- adult / X creator workflows isolated and disabled by default
- no content or publication flow that skips required restricted compliance metadata
- no mandatory cloud or heavy database dependency
