import pytest

from app.core.costs.budget_guard import BudgetGuard, BudgetPolicy
from app.core.errors.exceptions import HumanApprovalRequired
from app.core.pipeline.graph import PipelineGraph
from app.core.pipeline.models import PipelineStep
from app.core.workflows.content_workflow import default_short_form_content_workflow


def test_default_workflow_order_contains_all_steps() -> None:
    graph = PipelineGraph(default_short_form_content_workflow())
    order = [step.step_id for step in graph.execution_order()]
    assert order[0] == "research"
    assert "video" in order
    assert order[-1] == "learning"


def test_pipeline_graph_rejects_unknown_dependency() -> None:
    with pytest.raises(ValueError):
        PipelineGraph([PipelineStep(step_id="bad", name="Bad", depends_on=["missing"])])


def test_budget_guard_blocks_paid_api_when_disabled() -> None:
    guard = BudgetGuard(BudgetPolicy(daily_budget_usd=0, allow_paid_apis=False))
    with pytest.raises(HumanApprovalRequired):
        guard.assert_can_spend(0.01)
