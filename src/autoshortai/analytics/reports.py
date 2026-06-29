"""Reporting contracts and template identifiers."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class AnalyticsReportType(str, Enum):
    DAILY = "daily_report"
    WEEKLY = "weekly_report"
    PLATFORM = "platform_report"
    CONTENT = "content_report"
    EXPERIMENT = "experiment_report"
    COST_PERFORMANCE = "cost_performance_report"


@dataclass(frozen=True)
class AnalyticsReportRequest:
    report_type: AnalyticsReportType | str
    platforms: tuple[str, ...] = field(default_factory=tuple)
    content_ids: tuple[str, ...] = field(default_factory=tuple)
    experiment_ids: tuple[str, ...] = field(default_factory=tuple)
    metadata: Mapping[str, str] = field(default_factory=dict)
