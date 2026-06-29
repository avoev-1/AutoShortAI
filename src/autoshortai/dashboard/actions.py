from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Any


class DashboardActionType(str, Enum):
    PAUSE_JOB = "pause_job"
    RESUME_JOB = "resume_job"
    CANCEL_JOB = "cancel_job"
    RETRY_JOB = "retry_job"
    START_BATCH = "start_batch"
    PAUSE_QUEUE = "pause_queue"
    RESUME_QUEUE = "resume_queue"
    CLEAR_FAILED_JOBS = "clear_failed_jobs"
    REFRESH_METRICS = "refresh_metrics"
    APPROVE_LEARNING_SUGGESTION = "approve_learning_suggestion"
    REJECT_LEARNING_SUGGESTION = "reject_learning_suggestion"


class DashboardActionSafety(str, Enum):
    SAFE = "safe"
    CONFIRMATION_REQUIRED = "confirmation_required"
    REVIEW_REQUIRED = "review_required"
    DANGEROUS = "dangerous"


@dataclass(frozen=True)
class DashboardAction:
    id: str
    action_type: DashboardActionType
    target_ref: str
    requested_by: str = "local_user"
    reason: str | None = None
    safety: DashboardActionSafety = DashboardActionSafety.SAFE
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DashboardActionResult:
    action_id: str
    accepted: bool
    message: str
    target_ref: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


def requires_confirmation(action: DashboardAction) -> bool:
    return action.safety in {
        DashboardActionSafety.CONFIRMATION_REQUIRED,
        DashboardActionSafety.REVIEW_REQUIRED,
        DashboardActionSafety.DANGEROUS,
    }
