from __future__ import annotations

from typing import Protocol, Sequence

from .actions import DashboardAction, DashboardActionResult
from .models import DashboardPanel, DashboardPanelType, DashboardSnapshot
from .platforms import PlatformStatusView


class DashboardPanelProvider(Protocol):
    """Provides one or more dashboard panels without owning business logic."""

    def panel_types(self) -> Sequence[DashboardPanelType]:
        ...

    def build_panels(self) -> Sequence[DashboardPanel]:
        ...


class DashboardActionHandler(Protocol):
    """Handles safe dashboard control actions."""

    def can_handle(self, action: DashboardAction) -> bool:
        ...

    def execute(self, action: DashboardAction) -> DashboardActionResult:
        ...


class DashboardAdapter(Protocol):
    """Renders dashboard snapshots and emits dashboard actions."""

    def render(self, snapshot: DashboardSnapshot) -> None:
        ...


class PlatformDashboardAdapter(Protocol):
    """Builds platform status views without coupling the core to a platform."""

    def platform_ref(self) -> str:
        ...

    def status_view(self) -> PlatformStatusView:
        ...
