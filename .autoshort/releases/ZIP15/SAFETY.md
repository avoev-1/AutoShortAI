# SAFETY — ZIP15 Guardian Engine Foundation

## Guardian Safety Position

Guardian is a validation and reporting layer. It must not silently rewrite code, publish content, rotate credentials, or alter user data.

## Restricted / Adult Creator Protection

Guardian must treat adult / X creator workflows as restricted, opt-in, isolated workflows.

Required architecture principles:

- adults-only workflows
- consent metadata
- age-gating
- maturity rating
- manual review by default
- restricted assets separated from general assets
- restricted logs separated from general logs
- restricted credentials isolated in future vault architecture
- no illegal content
- no non-consensual content
- no content involving minors
- no unsafe automatic publication

## Platform Safety

Guardian must flag any architecture that becomes tied to one platform.

AutoShortAI must remain open to YouTube Shorts, TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, adult creator platforms through restricted adapters, and future networks.

## Security Baseline

Guardian must flag:

- API keys in source code
- credentials in examples
- tokens in logs
- private assets in fixtures
- secrets in repository files
- unrestricted credential access

## Lightweight Safety

Guardian must flag heavy mandatory dependencies and background services that violate the local-first lightweight philosophy.
