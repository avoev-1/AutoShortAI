from __future__ import annotations

from .models import InstallResult, InstallStatus, MigrationPlan


def validate_migration_plan(plan: MigrationPlan) -> None:
    if not plan.backup_required:
        raise ValueError("Migrations must require backup readiness.")
    if not plan.rollback_required:
        raise ValueError("Migrations must require rollback readiness.")
    if not plan.guardian_check_required:
        raise ValueError("Migrations must require Guardian checks.")


def migration_dry_run_result(plan: MigrationPlan) -> InstallResult:
    validate_migration_plan(plan)
    return InstallResult(
        plan_id=plan.migration_id,
        status=InstallStatus.COMPLETED,
        completed_steps=tuple(step.step_id for step in plan.steps),
        message="Migration dry run validated.",
    )
