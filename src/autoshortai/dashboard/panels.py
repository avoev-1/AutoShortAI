from __future__ import annotations

from .models import DashboardMetric, DashboardMetricKind, DashboardPanel, DashboardPanelType, DashboardStatus


def overview_panel(generated_videos: int = 0, active_jobs: int = 0, alerts: int = 0) -> DashboardPanel:
    return DashboardPanel(
        id="overview",
        title="Overview",
        panel_type=DashboardPanelType.OVERVIEW,
        status=DashboardStatus.OK if alerts == 0 else DashboardStatus.WARNING,
        metrics=(
            DashboardMetric("generated_videos", "Generated videos", generated_videos),
            DashboardMetric("active_jobs", "Active jobs", active_jobs),
            DashboardMetric("alerts", "Alerts", alerts),
        ),
    )


def system_health_panel(cpu_percent: float = 0.0, ram_percent: float = 0.0) -> DashboardPanel:
    status = DashboardStatus.OK if max(cpu_percent, ram_percent) < 85 else DashboardStatus.WARNING
    return DashboardPanel(
        id="system_health",
        title="System Health",
        panel_type=DashboardPanelType.SYSTEM_HEALTH,
        status=status,
        metrics=(
            DashboardMetric("cpu", "CPU", cpu_percent, DashboardMetricKind.PERCENTAGE, unit="%"),
            DashboardMetric("ram", "RAM", ram_percent, DashboardMetricKind.PERCENTAGE, unit="%"),
        ),
    )
