"""Domain exceptions for ZIP09."""


class AnalyticsError(Exception):
    """Base analytics error."""


class UnsupportedPlatformError(AnalyticsError):
    """Raised when no adapter supports a requested platform."""


class MetricNormalizationError(AnalyticsError):
    """Raised when raw metrics cannot be normalized safely."""


class AnalyticsStorageError(AnalyticsError):
    """Raised when analytics storage fails."""
