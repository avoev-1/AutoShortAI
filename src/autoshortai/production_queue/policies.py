"""Retry and failure policy contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Protocol

from .models import ProductionJob, ProductionJobError


@dataclass(frozen=True)
class RetryDecision:
    action: str
    reason: str
    retry_after_seconds: Optional[int] = None
    resume_from_checkpoint: bool = False
    requires_manual_review: bool = False


class FailurePolicy(Protocol):
    def evaluate(self, job: ProductionJob, error: ProductionJobError) -> RetryDecision:
        """Return retry, pause, cancel, or failed decision."""
