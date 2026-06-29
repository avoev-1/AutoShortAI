from __future__ import annotations

from .models import ConfidenceLevel, ConfidenceReport, RiskLevel


def confidence_level_from_score(score: float) -> ConfidenceLevel:
    if score >= 0.9:
        return ConfidenceLevel.VERY_HIGH
    if score >= 0.75:
        return ConfidenceLevel.HIGH
    if score >= 0.5:
        return ConfidenceLevel.MEDIUM
    if score >= 0.25:
        return ConfidenceLevel.LOW
    return ConfidenceLevel.VERY_LOW


def build_confidence_report(score: float, sample_size: int, risk_level: RiskLevel = RiskLevel.MEDIUM) -> ConfidenceReport:
    level = confidence_level_from_score(score)
    manual = sample_size < 3 or risk_level in {RiskLevel.HIGH, RiskLevel.CRITICAL} or level in {ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW}
    reasons = []
    if sample_size < 3:
        reasons.append("sample_size_below_default_threshold")
    if manual:
        reasons.append("manual_review_recommended")
    return ConfidenceReport(
        score=score,
        level=level,
        sample_size=sample_size,
        risk_level=risk_level,
        manual_review_required=manual,
        rollback_available=True,
        reasons=tuple(reasons),
    )
