from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class PipelineStepStatus(StrEnum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"
    waiting_for_human = "waiting_for_human"
    skipped = "skipped"


@dataclass(frozen=True)
class PipelineStep:
    step_id: str
    name: str
    depends_on: list[str] = field(default_factory=list)
    requires_human_approval: bool = False
    estimated_cost_usd: float = 0.0


@dataclass
class PipelineRun:
    run_id: str
    workflow_id: str
    status: PipelineStepStatus = PipelineStepStatus.pending
    context: dict[str, Any] = field(default_factory=dict)
