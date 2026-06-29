"""Core protocol contracts for ZIP08.

The protocols define integration surfaces. Implementations should live in
runtime modules created after the architecture ZIP is integrated.
"""

from __future__ import annotations

from typing import Iterable, Optional, Protocol

from .models import (
    BatchPlan,
    BudgetDecision,
    ProductionJob,
    ProductionJobPriority,
    ProductionJobResult,
    ProductionJobStatus,
    ResourceBudget,
    SchedulerDecision,
)


class ProductionQueueContract(Protocol):
    def add_job(self, job: ProductionJob) -> ProductionJob:
        """Add a job to the queue."""

    def get_job(self, job_id: str) -> Optional[ProductionJob]:
        """Return a job by id."""

    def list_jobs(
        self,
        status: Optional[ProductionJobStatus] = None,
        priority: Optional[ProductionJobPriority] = None,
    ) -> Iterable[ProductionJob]:
        """List jobs, optionally filtered by status or priority."""

    def update_status(self, job_id: str, status: ProductionJobStatus) -> ProductionJob:
        """Update a job status using a safe transition policy."""

    def snapshot(self) -> tuple[ProductionJob, ...]:
        """Return an immutable queue snapshot."""


class SchedulerEngineContract(Protocol):
    def plan(
        self,
        queue_snapshot: Iterable[ProductionJob],
        budget: ResourceBudget,
    ) -> tuple[SchedulerDecision, ...]:
        """Return scheduling decisions for a queue snapshot."""


class ResourceBudgetGuardContract(Protocol):
    def check_job(self, job: ProductionJob, budget: ResourceBudget) -> BudgetDecision:
        """Return whether the job is allowed to start."""


class QueuePersistenceContract(Protocol):
    def load(self) -> tuple[ProductionJob, ...]:
        """Load persisted jobs."""

    def save(self, jobs: Iterable[ProductionJob]) -> None:
        """Persist jobs."""


class BatchPlannerContract(Protocol):
    def expand_batch(self, batch: BatchPlan) -> tuple[ProductionJob, ...]:
        """Convert a batch plan into job descriptors."""


class ProductionWorkerContract(Protocol):
    worker_type: str

    def can_run(self, job: ProductionJob) -> bool:
        """Return whether this worker can run the job."""

    def run(self, job: ProductionJob) -> ProductionJobResult:
        """Run a production job and return a result."""
