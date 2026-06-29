"""ZIP08 error contracts."""


class ProductionQueueError(Exception):
    """Base queue error."""


class InvalidJobTransitionError(ProductionQueueError):
    """Raised when a job transition is not allowed by policy."""


class ResourceBudgetExceededError(ProductionQueueError):
    """Raised when a job exceeds resource budget constraints."""


class WorkerUnavailableError(ProductionQueueError):
    """Raised when no compatible worker is available."""
