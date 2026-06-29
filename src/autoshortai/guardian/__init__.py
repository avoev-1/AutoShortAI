"""AutoShortAI Guardian Engine Foundation (ZIP15).

This package defines contracts for an independent Guardian layer.
"""

from .models import (
    GuardianContext,
    GuardianReport,
    GuardianResult,
    GuardianRule,
    GuardianScope,
    GuardianSeverity,
    GuardianStatus,
    GuardianViolation,
)
from .rules import BASELINE_RULES
from .hooks import GUARDIAN_HOOKS

__all__ = [
    "GuardianContext",
    "GuardianReport",
    "GuardianResult",
    "GuardianRule",
    "GuardianScope",
    "GuardianSeverity",
    "GuardianStatus",
    "GuardianViolation",
    "BASELINE_RULES",
    "GUARDIAN_HOOKS",
]
