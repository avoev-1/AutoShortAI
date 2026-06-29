class RenderingError(Exception):
    """Base ZIP12 rendering error."""


class RenderProfileError(RenderingError):
    """Raised when a render profile is invalid or unsupported."""


class TimelineValidationError(RenderingError):
    """Raised when a timeline cannot be rendered safely."""


class RenderWorkerUnavailable(RenderingError):
    """Raised when no compatible render worker is available."""
