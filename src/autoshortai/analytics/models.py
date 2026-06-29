"""Normalized analytics models for ZIP09.

These models are intentionally lightweight. They define contracts and data
shapes only; provider/API logic belongs behind adapters.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Mapping


class NormalizedMetricName(str, Enum):
    VIEWS = "views"
    LIKES = "likes"
    COMMENTS = "comments"
    SHARES = "shares"
    SAVES = "saves"
    SUBSCRIBERS_GAINED = "subscribers_gained"
    WATCH_TIME_SECONDS = "watch_time_seconds"
    AVERAGE_VIEW_DURATION_SECONDS = "average_view_duration_seconds"
    RETENTION_RATE = "retention_rate"
    COMPLETION_RATE = "completion_rate"
    CLICK_THROUGH_RATE = "click_through_rate"
    ENGAGEMENT_RATE = "engagement_rate"
    IMPRESSION_COUNT = "impression_count"
    COST_UNITS = "cost_units"


class MetricTimeWindow(str, Enum):
    ONE_HOUR = "1h"
    SIX_HOURS = "6h"
    TWENTY_FOUR_HOURS = "24h"
    SEVEN_DAYS = "7d"
    TWENTY_EIGHT_DAYS = "28d"
    LIFETIME = "lifetime"


class MetricSource(str, Enum):
    PLATFORM_API = "platform_api"
    EXPORT_FILE = "export_file"
    MANUAL_ENTRY = "manual_entry"
    SIMULATED = "simulated"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class MetricValue:
    name: NormalizedMetricName | str
    value: float | int | None
    unit: str = "count"
    confidence: float = 1.0
    source: MetricSource = MetricSource.UNKNOWN
    raw_name: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PlatformPerformance:
    platform: str
    platform_content_id: str | None
    time_window: MetricTimeWindow | str
    collected_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metrics: tuple[MetricValue, ...] = field(default_factory=tuple)
    additional_metrics: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PerformanceSnapshot:
    snapshot_id: str
    content_id: str
    platform_performances: tuple[PlatformPerformance, ...]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    production_job_id: str | None = None
    distribution_id: str | None = None
    creative_profile_id: str | None = None
    experiment_id: str | None = None
    variant_id: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ContentPerformance:
    content_id: str
    snapshots: tuple[PerformanceSnapshot, ...] = field(default_factory=tuple)
    title: str | None = None
    content_type: str | None = None
    primary_platform: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AnalyticsContext:
    run_id: str
    requested_platforms: tuple[str, ...] = field(default_factory=tuple)
    time_windows: tuple[MetricTimeWindow | str, ...] = field(default_factory=tuple)
    dry_run: bool = True
    metadata: Mapping[str, Any] = field(default_factory=dict)
