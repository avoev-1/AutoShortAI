class LearningError(Exception):
    """Base ZIP10 learning error."""


class UnsafeAdaptationError(LearningError):
    """Raised when a requested adaptation violates policy or safety rules."""


class LearningMemoryError(LearningError):
    """Raised when learning memory cannot be read or written."""
