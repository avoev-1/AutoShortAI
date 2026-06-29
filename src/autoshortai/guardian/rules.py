"""Baseline Guardian rule definitions for ZIP15."""

from __future__ import annotations

from .models import GuardianRule, GuardianScope, GuardianSeverity

BASELINE_RULES: tuple[GuardianRule, ...] = (
    GuardianRule(
        id="guardian.architecture.core_independent",
        name="Core remains independent",
        scope=GuardianScope.ARCHITECTURE,
        severity=GuardianSeverity.ERROR,
        description="Core modules must not depend on platform-specific, provider-specific, UI-specific, or cloud-specific implementations.",
        recommendation="Move specific behavior behind adapters/providers/contracts.",
        tags=("core", "architecture"),
    ),
    GuardianRule(
        id="guardian.compatibility.previous_zips",
        name="Previous ZIP compatibility",
        scope=GuardianScope.ZIP_COMPATIBILITY,
        severity=GuardianSeverity.ERROR,
        description="New changes must not remove or break contracts introduced by previous ZIP releases.",
        recommendation="Keep backward-compatible aliases, adapters, or migrations.",
        tags=("zip", "compatibility"),
    ),
    GuardianRule(
        id="guardian.platform.not_youtube_only",
        name="Not YouTube-only",
        scope=GuardianScope.PLATFORM_AGNOSTIC,
        severity=GuardianSeverity.ERROR,
        description="AutoShortAI must stay platform-agnostic and must not hard-code YouTube as the only supported platform.",
        recommendation="Use platform capability contracts and adapters.",
        tags=("platform", "multi-platform"),
    ),
    GuardianRule(
        id="guardian.provider.no_provider_lockin",
        name="No provider lock-in",
        scope=GuardianScope.PROVIDER_AGNOSTIC,
        severity=GuardianSeverity.WARNING,
        description="No module should require one AI, video, storage, UI, or cloud provider as a core dependency.",
        recommendation="Use provider abstractions and optional dependencies.",
        tags=("provider", "adapter"),
    ),
    GuardianRule(
        id="guardian.restricted.adult_mode_isolated",
        name="Restricted creator mode isolation",
        scope=GuardianScope.RESTRICTED_CREATOR,
        severity=GuardianSeverity.CRITICAL,
        description="Adult / X Creator Mode must be opt-in, isolated, adults-only, consent-based, and manual-review-first.",
        recommendation="Separate restricted assets, logs, credentials, maturity ratings, consent metadata, and review gates.",
        tags=("restricted", "adult", "safety"),
    ),
    GuardianRule(
        id="guardian.security.no_secrets_committed",
        name="No secrets committed",
        scope=GuardianScope.SECURITY,
        severity=GuardianSeverity.CRITICAL,
        description="API keys, tokens, credentials, and private media must not be committed to the repository.",
        recommendation="Use future ZIP18 vault contracts and sanitized fixtures.",
        tags=("security", "secrets"),
    ),
)
