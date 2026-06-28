class AutoShortAIError(Exception):
    """Base project exception."""


class HumanApprovalRequired(AutoShortAIError):
    """Raised when an action requires human approval."""


class PluginNotImplemented(AutoShortAIError):
    """Raised when a plugin placeholder is called for real work."""
