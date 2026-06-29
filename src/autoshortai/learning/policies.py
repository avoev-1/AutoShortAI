from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence

from .models import ConfidenceLevel, RiskLevel


class AdaptationPolicyMode(str, Enum):
    MANUAL_ONLY = "manual_only"
    SUGGESTION_ONLY = "suggestion_only"
    SEMI_AUTOMATIC = "semi_automatic"
    AUTOMATIC_SAFE = "automatic_safe"
    LOCKED = "locked"


@dataclass(frozen=True)
class AdaptationPolicy:
    mode: AdaptationPolicyMode = AdaptationPolicyMode.SUGGESTION_ONLY
    min_confidence: ConfidenceLevel = ConfidenceLevel.MEDIUM
    max_risk: RiskLevel = RiskLevel.MEDIUM
    min_sample_size: int = 3
    locked_targets: Sequence[str] = field(default_factory=tuple)


DEFAULT_ADAPTATION_POLICY = AdaptationPolicy()


def requires_manual_review(policy: AdaptationPolicy, confidence: ConfidenceLevel, risk: RiskLevel, sample_size: int) -> bool:
    if policy.mode in {AdaptationPolicyMode.MANUAL_ONLY, AdaptationPolicyMode.SUGGESTION_ONLY, AdaptationPolicyMode.LOCKED}:
        return True
    if sample_size < policy.min_sample_size:
        return True
    risk_rank = [RiskLevel.LOW, RiskLevel.MEDIUM, RiskLevel.HIGH, RiskLevel.CRITICAL]
    confidence_rank = [ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW, ConfidenceLevel.MEDIUM, ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH]
    return risk_rank.index(risk) > risk_rank.index(policy.max_risk) or confidence_rank.index(confidence) < confidence_rank.index(policy.min_confidence)
