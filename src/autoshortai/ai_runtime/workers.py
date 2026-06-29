from __future__ import annotations

from .models import AIWorkerTask, AIWorkerResult, AIWorkerStatus, SafetyReviewLevel


class AIWorker:
    id = "abstract.worker"
    provider_id: str | None = None

    def can_handle(self, task: AIWorkerTask) -> bool:
        return False

    def execute(self, task: AIWorkerTask) -> AIWorkerResult:
        raise NotImplementedError("Concrete AI workers are implemented later by Claude or plugins.")


class ManualReviewWorker(AIWorker):
    id = "manual.review.worker"

    def can_handle(self, task: AIWorkerTask) -> bool:
        return task.safety_review_level == SafetyReviewLevel.MANUAL_REVIEW_REQUIRED

    def execute(self, task: AIWorkerTask) -> AIWorkerResult:
        return AIWorkerResult(
            task_id=task.id,
            status=AIWorkerStatus.REVIEW_REQUIRED,
            worker_id=self.id,
            safety_review_level=SafetyReviewLevel.MANUAL_REVIEW_REQUIRED,
            review_notes=("manual_review_required",),
        )


class MockScriptGenerationWorker(AIWorker):
    id = "mock.script.worker"

    def can_handle(self, task: AIWorkerTask) -> bool:
        return task.task_type.value == "script_generation"

    def execute(self, task: AIWorkerTask) -> AIWorkerResult:
        return AIWorkerResult(
            task_id=task.id,
            status=AIWorkerStatus.COMPLETED,
            worker_id=self.id,
            output_payload={"script_outline": "architecture-only mock result"},
            safety_review_level=task.safety_review_level,
        )
