from __future__ import annotations

from .models import InstallPlan, InstallResult, InstallStatus


def summarize_install_plan(plan: InstallPlan) -> dict[str, object]:
    return {
        "plan_id": plan.plan_id,
        "target": plan.target.value,
        "steps": [step.step_id for step in plan.steps],
        "dry_run_supported": plan.dry_run_supported,
    }


def successful_dry_run(plan: InstallPlan) -> InstallResult:
    return InstallResult(
        plan_id=plan.plan_id,
        status=InstallStatus.COMPLETED,
        completed_steps=tuple(step.step_id for step in plan.steps),
        message="Dry run completed. No changes applied.",
    )
