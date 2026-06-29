from __future__ import annotations

from typing import Iterable, Protocol, Sequence

from .models import AdaptationSuggestion, LearningInsight, LearningSignal, StrategyRecommendation
from .policies import AdaptationPolicy


class LearningSignalExtractor(Protocol):
    def extract_signals(self, evidence: object) -> Sequence[LearningSignal]:
        """Extract learning signals from analytics, jobs, strategy or distribution evidence."""


class LearningInsightGenerator(Protocol):
    def generate_insights(self, signals: Iterable[LearningSignal]) -> Sequence[LearningInsight]:
        """Convert signals into reviewable insights."""


class AdaptationPlanner(Protocol):
    def plan_adaptations(self, insights: Iterable[LearningInsight], policy: AdaptationPolicy) -> Sequence[AdaptationSuggestion]:
        """Create safe adaptation suggestions from insights."""


class StrategyRecommendationBuilder(Protocol):
    def build_recommendations(self, suggestions: Iterable[AdaptationSuggestion]) -> Sequence[StrategyRecommendation]:
        """Group suggestions into strategy-level recommendations."""


class LearningMemoryStore(Protocol):
    def save_insight(self, insight: LearningInsight) -> None:
        """Persist an insight."""

    def list_insights(self) -> Sequence[LearningInsight]:
        """Return known insights."""
