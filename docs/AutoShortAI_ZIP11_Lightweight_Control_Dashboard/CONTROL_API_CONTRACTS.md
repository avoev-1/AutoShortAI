# Control API Contracts

Control API contracts describe the safe commands the dashboard can request.

Examples:

- pause_job
- resume_job
- cancel_job
- retry_job
- start_batch
- pause_queue
- resume_queue
- clear_failed_jobs
- refresh_metrics
- approve_learning_suggestion
- reject_learning_suggestion

Each action must include:

- action id
- action type
- target ref
- requested by
- reason
- created timestamp
- safety level
