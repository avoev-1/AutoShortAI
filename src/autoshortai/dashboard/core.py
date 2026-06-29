from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .actions import DashboardAction, DashboardActionResult
from .contracts import DashboardActionHandler, DashboardPanelProvider
from .models import DashboardNavigationItem, DashboardPanel, DashboardPanelType, DashboardSnapshot, DashboardStatus
from .version import ZIP11_RELEASE


DEFAULT_NAVIGATION = (
    DashboardNavigationItem("nav_overview", "Dashboard", DashboardPanelType.OVERVIEW),
    DashboardNavigationItem("nav_queue", "Pipeline", DashboardPanelType.QUEUE),
    DashboardNavigationItem("nav_analytics", "Analytics", DashboardPanelType.ANALYTICS),
    DashboardNavigationItem("nav_learning", "Learning", DashboardPanelType.LEARNING),
    DashboardNavigationItem("nav_assets", "Assets", DashboardPanelType.ASSETS),
    DashboardNavigationItem("nav_health", "Health", DashboardPanelType.SYSTEM_HEALTH),
)


@dataclass
class DashboardCore:
    title: str = "AutoShortAI Studio"
    panel_providers: list[DashboardPanelProvider] = field(default_factory=list)
    action_handlers: list[DashboardActionHandler] = field(default_factory=list)

    def register_panel_provider(self, provider: DashboardPanelProvider) -> None:
        self.panel_providers.append(provider)

    def register_action_handler(self, handler: DashboardActionHandler) -> None:
        self.action_handlers.append(handler)

    def build_snapshot(self, extra_panels: Sequence[DashboardPanel] = ()) -> DashboardSnapshot:
        panels: list[DashboardPanel] = []
        for provider in self.panel_providers:
            panels.extend(provider.build_panels())
        panels.extend(extra_panels)
        status = DashboardStatus.OK
        if any(panel.status in {DashboardStatus.WARNING, DashboardStatus.DEGRADED} for panel in panels):
            status = DashboardStatus.WARNING
        if any(panel.status == DashboardStatus.ERROR for panel in panels):
            status = DashboardStatus.ERROR
        return DashboardSnapshot(
            release=ZIP11_RELEASE,
            title=self.title,
            status=status,
            panels=tuple(panels),
            navigation=DEFAULT_NAVIGATION,
        )

    def execute_action(self, action: DashboardAction) -> DashboardActionResult:
        for handler in self.action_handlers:
            if handler.can_handle(action):
                return handler.execute(action)
        return DashboardActionResult(
            action_id=action.id,
            accepted=False,
            message=f"No dashboard action handler accepted: {action.action_type.value}",
            target_ref=action.target_ref,
        )
