"""Persistence contracts for ZIP08 queue state."""

from __future__ import annotations

from typing import Iterable, Protocol

from .models import ProductionJob


class QueuePersistenceProvider(Protocol):
    provider_name: str

    def load_jobs(self) -> tuple[ProductionJob, ...]:
        ...

    def save_jobs(self, jobs: Iterable[ProductionJob]) -> None:
        ...

    def create_snapshot(self, jobs: Iterable[ProductionJob]) -> str:
        ...

    def restore_snapshot(self, snapshot_id: str) -> tuple[ProductionJob, ...]:
        ...
