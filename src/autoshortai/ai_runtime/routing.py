from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .models import AIWorkerTask
from .workers import AIWorker


@dataclass(frozen=True)
class WorkerRoute:
    task_id: str
    worker_id: str
    provider_id: str | None = None
    reason: str = "capability_match"


class CapabilityRouter:
    def select_worker(self, task: AIWorkerTask, workers: Sequence[AIWorker]) -> WorkerRoute | None:
        for worker in workers:
            if worker.can_handle(task):
                return WorkerRoute(task_id=task.id, worker_id=worker.id, provider_id=getattr(worker, "provider_id", None))
        return None
