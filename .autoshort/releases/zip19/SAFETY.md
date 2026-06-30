# SAFETY — ZIP19 Cross-Platform Packaging & Installer

## Packaging Safety Rules

- never package real credentials
- never package local secrets
- never package tokens
- never package restricted private media by default
- never make optional heavy tools globally mandatory
- never enable restricted creator pack by default
- never use installers to bypass platform policies
- never couple the package to one platform or provider

## Dependency Rules

Dependencies must be declared as required only when needed by the selected module profile.

Examples:

- rendering pack may require a renderer provider later
- AI worker pack may require selected provider dependencies later
- device farm pack may require device tools later
- restricted creator pack requires policy and isolation checks

## Restricted / Adult Creator Pack Rules

The restricted creator pack is opt-in and disabled by default.

Required:

- maturity rating
- consent metadata
- all participants 18+ requirement
- isolated workspace
- isolated credentials
- isolated logs
- manual review by default

Blocked:

- underage content
- non-consensual content
- illegal content
- publication without manual review by default
- mixing restricted workspace with general workspace
- shipping real restricted credentials or media in packages

## Security Rules

ZIP18 is authoritative for secrets and credentials. ZIP19 must package references, templates, and checks only.
