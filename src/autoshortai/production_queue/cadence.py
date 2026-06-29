"""Cadence contracts for ZIP08."""

from __future__ import annotations

from typing import Protocol

from .models import CadenceRule, ProductionJob


class CadenceEvaluator(Protocol):
    def next_run_times(self, cadence: CadenceRule, count: int) -> tuple[str, ...]:
        """Return planned run times as ISO strings."""


class CadencePolicy(Protocol):
    def applies_to(self, job: ProductionJob, cadence: CadenceRule) -> bool:
        """Return whether the cadence applies to the job."""
