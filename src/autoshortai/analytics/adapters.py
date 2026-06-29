"""Adapter base classes and placeholders.

ZIP09 does not implement real platform API clients. Concrete adapters must
remain isolated from the analytics core.
"""

from __future__ import annotations

from dataclasses import dataclass

from .models import AnalyticsContext, MetricSource, MetricTimeWindow, PlatformPerformance


@dataclass
class BasePlatformMetricsAdapter:
    platform_name: str

    def supports_platform(self, platform: str) -> bool:
        return platform == self.platform_name

    def collect_metrics(self, content_id: str, context: AnalyticsContext) -> PlatformPerformance:
        return PlatformPerformance(
            platform=self.platform_name,
            platform_content_id=content_id,
            time_window=context.time_windows[0] if context.time_windows else MetricTimeWindow.TWENTY_FOUR_HOURS,
            metrics=(),
            additional_metrics={"status": "placeholder", "source": MetricSource.SIMULATED.value},
        )


class GenericPlatformMetricsAdapter(BasePlatformMetricsAdapter):
    def __init__(self) -> None:
        super().__init__(platform_name="generic")
