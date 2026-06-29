# Migration Notes — ZIP06 to ZIP07

ZIP07 is additive.

It adds:

- `docs/AutoShortAI_ZIP07_Creative_Strategy_Engine/`
- `src/autoshortai/creative_strategy/`
- `templates/zip07_creative_strategy/`
- `examples/zip07_creative_strategy/`
- ZIP07 structure tests and fixtures.

It does not modify or replace ZIP06 asset pipeline contracts.

Future implementation should connect the two by passing asset requirements from strategy plans into ZIP06 asset pipeline abstractions.
