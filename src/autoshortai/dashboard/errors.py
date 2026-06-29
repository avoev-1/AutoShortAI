class DashboardError(Exception):
    """Base ZIP11 dashboard error."""


class DashboardActionRejected(DashboardError):
    """Raised when a dashboard action is rejected by safety rules."""


class DashboardAdapterUnavailable(DashboardError):
    """Raised when a requested UI/platform adapter is unavailable."""
