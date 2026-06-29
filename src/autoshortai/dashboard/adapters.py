from __future__ import annotations

from dataclasses import dataclass

from .models import DashboardSnapshot


class NullDashboardAdapter:
    """Adapter used by tests or headless runs."""

    def render(self, snapshot: DashboardSnapshot) -> None:
        return None


@dataclass(frozen=True)
class DashboardAdapterDescriptor:
    id: str
    name: str
    kind: str
    local_first: bool = True
    optional: bool = True


DEFAULT_ADAPTERS = (
    DashboardAdapterDescriptor("cli", "CLI Dashboard", "cli"),
    DashboardAdapterDescriptor("local_web", "Local Web Dashboard", "web"),
    DashboardAdapterDescriptor("desktop", "Desktop Wrapper", "desktop"),
    DashboardAdapterDescriptor("mobile_companion", "Mobile Companion", "mobile", optional=True),
)
