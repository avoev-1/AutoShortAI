"""Resource budget contracts for ZIP08."""

from __future__ import annotations

from typing import Protocol

from .models import BudgetDecision, ProductionJob, ResourceBudget


class ResourceBudgetGuard(Protocol):
    """Check whether a job can start under configured limits."""

    def check_job(self, job: ProductionJob, budget: ResourceBudget) -> BudgetDecision:
        ...

    def check_queue_size(self, current_size: int, budget: ResourceBudget) -> BudgetDecision:
        ...

    def check_retry_limit(self, job: ProductionJob, budget: ResourceBudget) -> BudgetDecision:
        ...
