# SAFETY — ZIP14 Device Farm Deployment

ZIP14 introduces device farm and phone farm readiness. This requires strict boundaries.

## Allowed Architectural Goals

- Manage owned or authorized devices.
- Route legitimate production tasks.
- Monitor health, status, and failures.
- Prepare multi-machine and mobile workflows.
- Support restricted creator workflows with safety gates.

## Not Allowed

- platform bypass
- credential theft
- anti-bot evasion
- spam automation
- fake engagement farming
- unauthorized account access
- device compromise
- illegal content workflows
- non-consensual content workflows
- content involving minors

## Adult / X Creator Mode Safety

Adult / X Creator Mode must be:

- opt-in
- isolated from general workflows
- adults-only
- consent-based
- manually reviewed by default
- credential-isolated later through ZIP18
- policy-checked later through ZIP16
- storage-isolated for private media
- never enabled as a hidden default

## Manual Review Principle

Restricted creator workflows should default to manual review before device dispatch and before upload/publishing.
