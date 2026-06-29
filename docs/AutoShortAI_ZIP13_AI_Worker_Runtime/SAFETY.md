# SAFETY — ZIP13 AI Worker Runtime

ZIP13 introduces AI runtime contracts, so safety boundaries are mandatory.

## Provider Safety

- Provider errors must be isolated.
- Provider costs must be tracked before and after execution.
- Provider outputs must be validated before use.
- No provider may bypass task policy or manual review requirements.

## Restricted / Adult Platform Safety

Adult / 18+ creator platform workflows are allowed only as restricted, opt-in architecture paths.

Mandatory safeguards:

- manual review required by default
- explicit maturity rating
- consent metadata required
- age gate metadata required
- no minors or ambiguous-age content
- no non-consensual content
- no illegal content categories
- no hidden auto-publication
- credentials isolated in a later security vault
- platform policy checks before publishing

## Platform Safety

The core must remain platform-agnostic.

No worker may hard-code YouTube, TikTok, Instagram, OnlyFans, or any other platform into the core runtime.

## Operational Safety

- API budgets must be enforceable.
- Quotas must be respected.
- Retry loops must be bounded.
- Outputs must be traceable to task and prompt versions.
- Unsafe outputs must not enter rendering or publishing pipelines.
