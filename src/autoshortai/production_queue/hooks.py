"""ZIP08 queue hook constants.

Hooks are intentionally strings to keep plugin boundaries simple.
"""

ZIP08_QUEUE_HOOKS = (
    "before_job_created",
    "after_job_created",
    "before_job_scheduled",
    "after_job_scheduled",
    "before_job_started",
    "after_job_completed",
    "after_job_failed",
    "before_retry",
    "after_retry",
    "before_queue_flush",
    "after_queue_flush",
    "before_budget_check",
    "after_budget_check",
)
