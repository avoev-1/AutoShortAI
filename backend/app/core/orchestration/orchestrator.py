from dataclasses import dataclass
from app.core.costs.budget_guard import BudgetGuard
from app.core.human_control.approval import HumanControlGuard
from app.core.pipeline.graph import PipelineGraph
from app.core.pipeline.models import PipelineRun, PipelineStepStatus


@dataclass
class OrchestrationResult:
    run_id: str
    status: str
    planned_steps: list[str]


class ContentOrchestrator:
    def __init__(self, graph: PipelineGraph, budget_guard: BudgetGuard, human_guard: HumanControlGuard) -> None:
        self.graph = graph
        self.budget_guard = budget_guard
        self.human_guard = human_guard

    def plan(self, run: PipelineRun) -> OrchestrationResult:
        ordered_steps = self.graph.execution_order()

        for step in ordered_steps:
            self.budget_guard.assert_can_spend(step.estimated_cost_usd)
            if step.requires_human_approval:
                run.status = PipelineStepStatus.waiting_for_human

        return OrchestrationResult(
            run_id=run.run_id,
            status=str(run.status),
            planned_steps=[step.step_id for step in ordered_steps],
        )
