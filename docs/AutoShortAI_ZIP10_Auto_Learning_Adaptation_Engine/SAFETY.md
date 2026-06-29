# ZIP10 Safety — Controlled Learning Rules

ZIP10 introduces learning and adaptation contracts. This creates risk if future implementations mutate behavior without review.

## Required safeguards

- Default policy must be `suggestion_only`.
- All adaptations must include confidence and risk metadata.
- Low sample size must require manual review.
- High-risk adaptations must require manual review.
- Rollback metadata must be preserved when a profile change is proposed.
- Learning memory must be inspectable and local-first.
- Platform-specific assumptions must be explicit.

## Forbidden behavior

- No hidden automatic profile mutation.
- No destructive optimization without rollback.
- No platform-only hardcoding.
- No scraping-based learning by default.
- No mandatory cloud dependency.
- No SaaS user/account model.

## Recommended first implementation

Claude should initially implement ZIP10 as a suggestion engine, not an autonomous mutation system.
