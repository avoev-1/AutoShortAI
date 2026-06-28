from app.core.contracts.queue import QueueJob


class InMemoryQueue:
    def __init__(self) -> None:
        self.jobs: dict[str, QueueJob] = {}

    async def enqueue(self, job: QueueJob) -> str:
        self.jobs[job.job_id] = job
        return job.job_id

    async def get_status(self, job_id: str) -> str:
        return "queued" if job_id in self.jobs else "missing"
