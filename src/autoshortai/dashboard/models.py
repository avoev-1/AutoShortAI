from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class DashboardStatus(str, Enum):
    OK = "ok"
    WARNING = "warning"
    DEGRADED = "degraded"
    ERROR = "error"
    OFFLINE = "offline"


class DashboardPanelType(str, Enum):
    OVERVIEW = "overview"
    QUEUE = "queue"
    JOBS = "jobs"
    ASSETS = "assets"
    ANALYTICS = "analytics"
    LEARNING = "learning"
    COSTS = "costs"
    SYSTEM_HEALTH = "system_health"
    LOGS = "logs"
    PLATFORM_STATUS = "platform_status"


class DashboardMetricKind(str, Enum):
    COUNT = "count"
    PERCENTAGE = "percentage"
    DURATION = "duration"
    COST = "cost"
    STATUS = "status"
    RATIO = "ratio"


@dataclass(frozen=True)
class DashboardMetric:
    key: str
    label: str
    value: str | int | float
    kind: DashboardMetricKind = DashboardMetricKind.COUNT
    trend: str | None = None
    unit: str | None = None
    source_ref: str | None = None


@dataclass(frozen=True)
class DashboardAlert:
    id: str
    title: str
    message: str
    status: DashboardStatus = DashboardStatus.WARNING
    source_ref: str | None = None
    action_ref: str | None = None


@dataclass(frozen=True)
class DashboardPanel:
    id: str
    title: str
    panel_type: DashboardPanelType
    status: DashboardStatus = DashboardStatus.OK
    metrics: Sequence[DashboardMetric] = field(default_factory=tuple)
    alerts: Sequence[DashboardAlert] = field(default_factory=tuple)
    payload: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DashboardNavigationItem:
    id: str
    label: str
    target_panel: DashboardPanelType
    enabled: bool = True


@dataclass(frozen=True)
class DashboardSnapshot:
    release: str
    title: str
    status: DashboardStatus
    panels: Sequence[DashboardPanel] = field(default_factory=tuple)
    navigation: Sequence[DashboardNavigationItem] = field(default_factory=tuple)
    generated_at: str | None = None
    platform_refs: Sequence[str] = field(default_factory=tuple)
