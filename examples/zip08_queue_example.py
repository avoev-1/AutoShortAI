"""Minimal ZIP08 contract example.

This example does not implement the real queue runtime. It shows how a future
runtime can instantiate the ZIP08 model contracts.
"""

from autoshortai.production_queue import (
    ProductionJob,
    ProductionJobPriority,
    ProductionJobStatus,
    ResourceBudget,
)

job = ProductionJob(
    job_id="example-job-001",
    job_type="script_generation",
    title="Generate a Short script",
    status=ProductionJobStatus.PENDING,
    priority=ProductionJobPriority.NORMAL,
    platform="youtube_shorts",
    required_worker_type="script_worker",
)

budget = ResourceBudget(max_concurrent_workers=2, max_render_workers=1)

print(job)
print(budget)
