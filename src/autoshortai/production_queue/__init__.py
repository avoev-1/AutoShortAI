"""AutoShortAI ZIP08 — Production Queue & Scheduler contracts."""

from .version import ZIP08_RELEASE, ZIP08_NAME
from .models import (
    ProductionJob,
    ProductionJobStatus,
    ProductionJobPriority,
    ProductionJobResult,
    ProductionJobError,
    ResourceBudget,
    SchedulerDecision,
    BatchPlan,
    CadenceRule,
)
from .hooks import ZIP08_QUEUE_HOOKS

__all__ = [
    "ZIP08_RELEASE",
    "ZIP08_NAME",
    "ProductionJob",
    "ProductionJobStatus",
    "ProductionJobPriority",
    "ProductionJobResult",
    "ProductionJobError",
    "ResourceBudget",
    "SchedulerDecision",
    "BatchPlan",
    "CadenceRule",
    "ZIP08_QUEUE_HOOKS",
]
