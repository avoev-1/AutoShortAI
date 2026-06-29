from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence

from .models import ConfidenceReport


class VariantLearningStatus(str, Enum):
    WINNER = "winner"
    WEAK = "weak"
    INCONCLUSIVE = "inconclusive"
    NEEDS_MORE_DATA = "needs_more_data"


@dataclass(frozen=True)
class LearningExperiment:
    experiment_id: str
    strategy_ref: str
    variant_ids: Sequence[str] = field(default_factory=tuple)
    platforms: Sequence[str] = field(default_factory=lambda: ("generic",))


@dataclass(frozen=True)
class VariantLearningResult:
    variant_id: str
    status: VariantLearningStatus
    confidence: ConfidenceReport
    notes: str = ""
    metrics_summary: Mapping[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class ExperimentLearningResult:
    experiment_id: str
    results: Sequence[VariantLearningResult] = field(default_factory=tuple)
    platform: str = "generic"
    summary: str = ""
