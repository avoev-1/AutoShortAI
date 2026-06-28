from enum import StrEnum


class JobStatus(StrEnum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"
    waiting_for_human = "waiting_for_human"
