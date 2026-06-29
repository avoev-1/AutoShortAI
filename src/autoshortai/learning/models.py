from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Optional, Sequence


class LearningSignalType(str, Enum):
    HOOK_PATTERN = "hook_pattern"
    RETENTION_PATTERN = "retention_pattern"
    ENGAGEMENT_PATTERN = "engagement_pattern"
    FORMAT_PATTERN = "format_pattern"
    TIMING_PATTERN = "timing_pattern"
    COST_EFFICIENCY_PATTERN = "cost_efficiency_pattern"
    PLATFORM_FIT_PATTERN = "platform_fit_pattern"


class ConfidenceLevel(str, Enum):
    VERY_LOW = "very_low"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AdaptationAction(str, Enum):
    INCREASE_WEIGHT = "increase_weight"
    DECREASE_WEIGHT = "decrease_weight"
    LOCK_PATTERN = "lock_pattern"
    AVOID_PATTERN = "avoid_pattern"
    TEST_MORE = "test_more"
    REQUIRE_REVIEW = "require_review"
    NO_CHANGE = "no_change"


@dataclass(frozen=True)
class LearningSignal:
    signal_id: str
    signal_type: LearningSignalType
    source_ids: Sequence[str] = field(default_factory=tuple)
    platforms: Sequence[str] = field(default_factory=lambda: ("generic",))
    strength: float = 0.0
    sample_size: int = 0
    metadata: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class ConfidenceReport:
    score: float
    level: ConfidenceLevel
    sample_size: int
    risk_level: RiskLevel
    manual_review_required: bool = True
    rollback_available: bool = True
    reasons: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class LearningInsight:
    insight_id: str
    title: str
    summary: str
    signals: Sequence[LearningSignal] = field(default_factory=tuple)
    platforms: Sequence[str] = field(default_factory=lambda: ("generic",))
    confidence: ConfidenceReport = field(default_factory=lambda: ConfidenceReport(
        score=0.0,
        level=ConfidenceLevel.VERY_LOW,
        sample_size=0,
        risk_level=RiskLevel.MEDIUM,
        manual_review_required=True,
    ))
    tags: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class AdaptationSuggestion:
    suggestion_id: str
    target_ref: str
    action: AdaptationAction
    rationale: str
    platforms: Sequence[str] = field(default_factory=lambda: ("generic",))
    confidence: Optional[ConfidenceReport] = None
    proposed_delta: Mapping[str, object] = field(default_factory=dict)
    reversible: bool = True


@dataclass(frozen=True)
class StrategyRecommendation:
    recommendation_id: str
    strategy_ref: str
    suggestions: Sequence[AdaptationSuggestion] = field(default_factory=tuple)
    summary: str = ""
    requires_manual_review: bool = True


@dataclass(frozen=True)
class PlatformLearningProfile:
    platform: str
    supported_metric_names: Sequence[str] = field(default_factory=tuple)
    known_constraints: Mapping[str, object] = field(default_factory=dict)
    learning_enabled: bool = True


@dataclass(frozen=True)
class CrossPlatformInsight:
    insight_id: str
    generic_summary: str
    platform_notes: Mapping[str, str] = field(default_factory=dict)
    confidence_by_platform: Mapping[str, ConfidenceLevel] = field(default_factory=dict)
