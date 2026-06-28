from fastapi import APIRouter

from app.core.costs.budget_guard import BudgetGuard, BudgetPolicy
from app.core.human_control.approval import HumanControlGuard, HumanControlPolicy
from app.core.orchestration.orchestrator import ContentOrchestrator
from app.core.pipeline.graph import PipelineGraph
from app.core.pipeline.models import PipelineRun
from app.core.workflows.content_workflow import default_short_form_content_workflow

router = APIRouter()


@router.get("/workflow/default")
async def get_default_workflow() -> dict[str, object]:
    steps = default_short_form_content_workflow()
    graph = PipelineGraph(steps)
    return {
        "workflow": "default_short_form_content",
        "steps": [
            {
                "id": step.step_id,
                "name": step.name,
                "depends_on": step.depends_on,
                "requires_human_approval": step.requires_human_approval,
                "estimated_cost_usd": step.estimated_cost_usd,
            }
            for step in graph.execution_order()
        ],
    }


@router.get("/plan/demo")
async def plan_demo_workflow() -> dict[str, object]:
    graph = PipelineGraph(default_short_form_content_workflow())
    orchestrator = ContentOrchestrator(
        graph=graph,
        budget_guard=BudgetGuard(BudgetPolicy(daily_budget_usd=0, allow_paid_apis=False)),
        human_guard=HumanControlGuard(HumanControlPolicy()),
    )
    result = orchestrator.plan(PipelineRun(run_id="demo", workflow_id="default_short_form_content"))
    return {"run_id": result.run_id, "status": result.status, "planned_steps": result.planned_steps}
