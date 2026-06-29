# API Cost Optimizer

The API Cost Optimizer protects AutoShortAI from uncontrolled paid or rate-limited provider usage.

## Responsibilities

- Estimate operation cost before execution.
- Decide whether an operation is allowed under current policy.
- Record actual or estimated usage after execution.
- Expose budget and usage metadata for diagnostics.

## Non-responsibilities

- It does not call provider APIs directly.
- It does not replace user-defined strategy.
- It does not hide costs from the workflow layer.

## Default philosophy

The default future implementation should be conservative. Unknown cost should require explicit allow logic or a safe zero-cost provider.
