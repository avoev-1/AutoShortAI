from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .models import DashboardMetric, DashboardPanel, DashboardPanelType, DashboardStatus


@dataclass(frozen=True)
class MonitoringSource:
    id: str
    label: str
    module_ref: str
    panel_type: DashboardPanelType
    enabled: bool = True


DEFAULT_MONITORING_SOURCES = (
    MonitoringSource("zip06_assets", "Assets", "autoshortai.asset_pipeline", DashboardPanelType.ASSETS),
    MonitoringSource("zip08_queue", "Production Queue", "autoshortai.production", DashboardPanelType.QUEUE),
    MonitoringSource("zip09_analytics", "Analytics", "autoshortai.analytics", DashboardPanelType.ANALYTICS),
    MonitoringSource("zip10_learning", "Learning", "autoshortai.learning", DashboardPanelType.LEARNING),
)


def monitoring_panel(source: MonitoringSource, metrics: Sequence[DashboardMetric] = ()) -> DashboardPanel:
    return DashboardPanel(
        id=source.id,
        title=source.label,
        panel_type=source.panel_type,
        status=DashboardStatus.OK if source.enabled else DashboardStatus.OFFLINE,
        metrics=tuple(metrics),
        payload={"module_ref": source.module_ref},
    )
