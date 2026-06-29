"""Guardian hooks introduced by ZIP15."""

GUARDIAN_HOOKS: tuple[str, ...] = (
    "before_guardian_run",
    "after_guardian_run",
    "before_rule_checked",
    "after_rule_checked",
    "before_violation_reported",
    "after_violation_reported",
    "before_report_written",
    "after_report_written",
)
