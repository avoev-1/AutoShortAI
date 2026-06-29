# SAFETY — ZIP16 Multi-Platform Publishing Runtime

## Publishing Safety Principles

Publishing is high-impact because it can make generated content public.

ZIP16 therefore requires architecture for:

- manual review gates
- platform capability validation
- content maturity classification
- restricted workflow handling
- credential isolation readiness
- normalized errors
- no automatic risky publishing by default

## Platform Rules

AutoShortAI must respect target platform rules.

ZIP16 explicitly forbids architecture that depends on:

- bypassing platform security
- spam automation
- evading rate limits
- hiding automation against policy
- publishing to accounts without permission

## Adult / X Creator Workflows

Adult creator workflows are allowed only as restricted opt-in architecture.

Mandatory restrictions:

- all participants must be adults
- consent metadata must exist
- age gate metadata must exist
- content maturity rating must exist
- credentials must be isolated
- restricted storage/log handling must be supported
- manual review must be required by default
- no illegal content
- no non-consensual content
- no content involving minors

## Secrets

ZIP16 does not store secrets. Future ZIP18 must define the vault layer.

Until then:

- no API keys in source files
- no tokens in templates
- no real credentials in examples
- no secrets in logs

## Guardian Checks

ZIP15 Guardian should flag any implementation that removes manual review, hard-codes a platform, bypasses rules, leaks credentials, or enables restricted workflows by default.
