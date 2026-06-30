from __future__ import annotations

from .models import ReleaseRisk, RiskCategory, RiskLevel


def default_beta_risk_register() -> tuple[ReleaseRisk, ...]:
    return (
        ReleaseRisk(
            id="platform_lock_in",
            title="Core becomes tied to one platform",
            category=RiskCategory.PLATFORM,
            level=RiskLevel.HIGH,
            mitigation="Use platform adapters and capability contracts only.",
            blocks_release=True,
        ),
        ReleaseRisk(
            id="secret_leak",
            title="Secret appears in code, logs, templates, examples, or package",
            category=RiskCategory.SECURITY,
            level=RiskLevel.BLOCKER,
            mitigation="Use ZIP18 vault, redaction, and packaging checks.",
            blocks_release=True,
        ),
        ReleaseRisk(
            id="restricted_mode_default",
            title="Restricted creator mode enabled by default",
            category=RiskCategory.ADULT_RESTRICTED_MODE,
            level=RiskLevel.BLOCKER,
            mitigation="Keep restricted mode opt-in and isolated.",
            blocks_release=True,
        ),
    )
