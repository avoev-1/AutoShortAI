"""Minimal ZIP09 contract usage example."""

from autoshortai.analytics.models import (
    MetricSource,
    MetricTimeWindow,
    MetricValue,
    NormalizedMetricName,
    PlatformPerformance,
)
from autoshortai.analytics.feedback import FeedbackItem, FeedbackReport, FeedbackSeverity

performance = PlatformPerformance(
    platform="generic",
    platform_content_id="content-on-platform",
    time_window=MetricTimeWindow.TWENTY_FOUR_HOURS,
    metrics=(
        MetricValue(NormalizedMetricName.VIEWS, 12000, source=MetricSource.SIMULATED),
        MetricValue(NormalizedMetricName.COMPLETION_RATE, 0.74, unit="ratio", source=MetricSource.SIMULATED),
    ),
)

feedback = FeedbackReport(
    report_id="feedback-example",
    content_id="content-001",
    summary="Example feedback generated from normalized metrics.",
    items=(
        FeedbackItem(
            message="Completion rate is strong for the 24h window.",
            severity=FeedbackSeverity.OPPORTUNITY,
            platform="generic",
            metric="completion_rate",
        ),
    ),
)

print(performance.platform, feedback.summary)
