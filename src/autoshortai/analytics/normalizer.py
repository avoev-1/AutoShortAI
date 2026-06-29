"""Metric normalization contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .models import MetricSource, MetricValue, NormalizedMetricName


@dataclass(frozen=True)
class NormalizationRule:
    raw_name: str
    normalized_name: NormalizedMetricName | str
    unit: str = "count"


DEFAULT_NORMALIZATION_RULES = (
    NormalizationRule("views", NormalizedMetricName.VIEWS),
    NormalizationRule("likes", NormalizedMetricName.LIKES),
    NormalizationRule("comments", NormalizedMetricName.COMMENTS),
    NormalizationRule("shares", NormalizedMetricName.SHARES),
    NormalizationRule("saves", NormalizedMetricName.SAVES),
    NormalizationRule("completion_rate", NormalizedMetricName.COMPLETION_RATE, unit="ratio"),
    NormalizationRule("retention_rate", NormalizedMetricName.RETENTION_RATE, unit="ratio"),
)


def build_metric_value(rule: NormalizationRule, raw_metrics: Mapping[str, Any], source: MetricSource) -> MetricValue:
    return MetricValue(
        name=rule.normalized_name,
        value=raw_metrics.get(rule.raw_name),
        unit=rule.unit,
        source=source,
        raw_name=rule.raw_name,
    )
