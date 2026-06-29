"""Protocol contracts for ZIP09 analytics components."""

from __future__ import annotations

from typing import Protocol, Sequence

from .models import AnalyticsContext, ContentPerformance, PerformanceSnapshot, PlatformPerformance
from .scoring import PerformanceScorecard
from .feedback import FeedbackReport


class PlatformMetricsAdapter(Protocol):
    """Adapter contract for platform-specific metrics retrieval."""

    platform_name: str

    def supports_platform(self, platform: str) -> bool:
        ...

    def collect_metrics(self, content_id: str, context: AnalyticsContext) -> PlatformPerformance:
        ...


class MetricsNormalizer(Protocol):
    """Converts raw provider metrics into normalized ZIP09 metrics."""

    def normalize(self, platform: str, raw_metrics: dict) -> PlatformPerformance:
        ...


class AnalyticsStorage(Protocol):
    """Persistence contract for analytics snapshots."""

    def save_snapshot(self, snapshot: PerformanceSnapshot) -> None:
        ...

    def load_content_performance(self, content_id: str) -> ContentPerformance | None:
        ...


class PerformanceScorer(Protocol):
    """Scores normalized content performance."""

    def score(self, performance: ContentPerformance) -> PerformanceScorecard:
        ...


class FeedbackGenerator(Protocol):
    """Produces feedback without mutating production or strategy state."""

    def generate_feedback(self, scorecard: PerformanceScorecard) -> FeedbackReport:
        ...


class AnalyticsReporter(Protocol):
    """Renders analytics information to reports."""

    def render_report(self, performances: Sequence[ContentPerformance]) -> str:
        ...
