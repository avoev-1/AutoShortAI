"""Scheduler engine contracts for ZIP08."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Protocol

from .models import ProductionJob, ResourceBudget, SchedulerDecision


@dataclass(frozen=True)
class SchedulerContext:
    now: str
    resource_budget: ResourceBudget
    platform_limits: Mapping[str, object] | None = None
    metadata: Mapping[str, object] | None = None


class SchedulerEngine(Protocol):
    """Select jobs that may run without executing them."""

    def plan(
        self,
        queue_snapshot: Iterable[ProductionJob],
        context: SchedulerContext,
    ) -> tuple[SchedulerDecision, ...]:
        ...
