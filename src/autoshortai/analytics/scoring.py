"""Performance scoring contracts for ZIP09."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class ScoreValue:
    name: str
    value: float
    confidence: float = 1.0
    explanation: str | None = None


@dataclass(frozen=True)
class PerformanceScorecard:
    content_id: str
    platform_scores: Mapping[str, tuple[ScoreValue, ...]] = field(default_factory=dict)
    overall_scores: tuple[ScoreValue, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)


ZIP09_SCORE_NAMES = (
    "visibility_score",
    "retention_score",
    "engagement_score",
    "growth_score",
    "platform_fit_score",
    "cost_efficiency_score",
    "overall_performance_score",
)
