from __future__ import annotations

from typing import Mapping

from .models import AIWorkerTask, AIWorkerResult, AIWorkerStatus, SafetyReviewLevel
from .platform_context import PlatformContext
from .routing import CapabilityRouter
from .safety import SafetyValidator
from .workers import AIWorker, ManualReviewWorker


class AIWorkerRuntime:
    def __init__(self, workers: list[AIWorker] | None = None, router: CapabilityRouter | None = None, safety: SafetyValidator | None = None):
        self.workers = workers or []
        self.router = router or CapabilityRouter()
        self.safety = safety or SafetyValidator()
        self.manual_review_worker = ManualReviewWorker()

    def run_task(self, task: AIWorkerTask, platform_context: PlatformContext) -> AIWorkerResult:
        review_level, notes = self.safety.review_task(task, platform_context)
        if review_level == SafetyReviewLevel.BLOCKED:
            return AIWorkerResult(
                task_id=task.id,
                status=AIWorkerStatus.BLOCKED,
                safety_review_level=review_level,
                review_notes=notes,
            )
        if review_level == SafetyReviewLevel.MANUAL_REVIEW_REQUIRED:
            return AIWorkerResult(
                task_id=task.id,
                status=AIWorkerStatus.REVIEW_REQUIRED,
                worker_id=self.manual_review_worker.id,
                safety_review_level=review_level,
                review_notes=notes,
            )

        route = self.router.select_worker(task, self.workers)
        if route is None:
            return AIWorkerResult(
                task_id=task.id,
                status=AIWorkerStatus.FAILED,
                review_notes=("no_compatible_worker",),
            )

        for worker in self.workers:
            if worker.id == route.worker_id:
                return worker.execute(task)

        return AIWorkerResult(task_id=task.id, status=AIWorkerStatus.FAILED, review_notes=("selected_worker_missing",))
