"""Batch planning contracts for ZIP08."""

from __future__ import annotations

from typing import Protocol

from .models import BatchPlan, ProductionJob


class BatchPlanner(Protocol):
    def expand_batch(self, batch: BatchPlan) -> tuple[ProductionJob, ...]:
        """Create job descriptors from a batch plan."""


class BatchPolicy(Protocol):
    def validate_batch(self, batch: BatchPlan) -> tuple[bool, str]:
        """Return whether a batch plan is valid."""
