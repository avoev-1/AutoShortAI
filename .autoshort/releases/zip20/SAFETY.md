# SAFETY — ZIP20 Beta Stabilization & Release Governance

ZIP20 is a governance release. Its safety purpose is to prevent AutoShortAI from drifting away from the architecture defined by ZIP01-ZIP20.

## Safety Rules

- No secrets in Git, docs, examples, reports, logs, or templates.
- No platform lock-in.
- No provider lock-in.
- No SaaS drift.
- No mandatory heavy dependency drift.
- No unrestricted adult automation.
- No restricted creator mode enabled by default.
- No publishing without review gates during early implementation.
- No breaking change without migration and rollback plan.

## Restricted / Adult Creator Governance

Adult / X creator workflows are valid product workflows only as restricted opt-in modules.

Required constraints:

- all participants 18+
- consent metadata required
- maturity rating required
- isolated credentials
- isolated workspace
- isolated logs
- manual review by default
- no illegal content
- no non-consensual content
- no minors
- no mixing with general content

## Guardian Position

Guardian remains an independent development-quality layer. It does not become the product core and must not automatically rewrite code without explicit review.
