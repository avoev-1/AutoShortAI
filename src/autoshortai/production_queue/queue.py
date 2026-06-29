"""Production queue architecture surface."""

from __future__ import annotations

from typing import Iterable, Optional, Protocol

from .models import ProductionJob, ProductionJobPriority, ProductionJobStatus


class ProductionQueue(Protocol):
    """Protocol for queue implementations."""

    def add_job(self, job: ProductionJob) -> ProductionJob:
        ...

    def get_job(self, job_id: str) -> Optional[ProductionJob]:
        ...

    def list_jobs(
        self,
        status: Optional[ProductionJobStatus] = None,
        priority: Optional[ProductionJobPriority] = None,
    ) -> Iterable[ProductionJob]:
        ...

    def update_status(self, job_id: str, status: ProductionJobStatus) -> ProductionJob:
        ...

    def pause(self, job_id: str) -> ProductionJob:
        ...

    def resume(self, job_id: str) -> ProductionJob:
        ...

    def cancel(self, job_id: str) -> ProductionJob:
        ...

    def snapshot(self) -> tuple[ProductionJob, ...]:
        ...
