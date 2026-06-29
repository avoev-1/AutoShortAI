class AIRuntimeError(Exception):
    """Base AI runtime architecture error."""


class ProviderUnavailableError(AIRuntimeError):
    """Raised when no provider is available for a task."""


class SafetyPolicyError(AIRuntimeError):
    """Raised when a task violates a configured safety policy."""
