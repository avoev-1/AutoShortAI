"""ZIP07 error hierarchy."""
from __future__ import annotations


class CreativeStrategyError(Exception):
    """Base class for Creative Strategy Engine errors."""


class ProfileNotFoundError(CreativeStrategyError):
    """Raised when a requested creation profile cannot be resolved."""


class InvalidStrategyRequestError(CreativeStrategyError):
    """Raised when a strategy request violates required contracts."""


class StrategyValidationError(CreativeStrategyError):
    """Raised when a strategy plan fails blocking validation."""


class BlueprintGenerationError(CreativeStrategyError):
    """Raised when a blueprint cannot be produced from valid input."""
