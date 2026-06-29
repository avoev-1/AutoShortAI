"""Worker contracts for future ZIP08 implementations."""

from __future__ import annotations

from typing import Mapping, Protocol

from .models import ProductionJob, ProductionJobResult


class ProductionWorker(Protocol):
    worker_id: str
    worker_type: str
    capabilities: tuple[str, ...]

    def is_ready(self) -> bool:
        ...

    def can_run(self, job: ProductionJob) -> bool:
        ...

    def run(self, job: ProductionJob) -> ProductionJobResult:
        ...

    def cancel(self, job_id: str) -> None:
        ...


class ScriptWorker(ProductionWorker, Protocol):
    """Contract for script-generation jobs."""


class AssetWorker(ProductionWorker, Protocol):
    """Contract for asset-preparation jobs."""


class RenderWorker(ProductionWorker, Protocol):
    """Contract for video-rendering jobs."""


class DistributionWorker(ProductionWorker, Protocol):
    """Contract for distribution jobs."""


class AnalysisWorker(ProductionWorker, Protocol):
    """Contract for analysis jobs."""


class WorkerRegistry(Protocol):
    def register(self, worker: ProductionWorker) -> None:
        ...

    def get_by_type(self, worker_type: str) -> tuple[ProductionWorker, ...]:
        ...

    def capabilities(self) -> Mapping[str, tuple[str, ...]]:
        ...
