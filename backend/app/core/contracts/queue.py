from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class QueueJob:
    job_id: str
    queue: str
    task_name: str
    payload: dict[str, Any]


class QueueProvider(ABC):
    provider_id: str

    @abstractmethod
    async def enqueue(self, job: QueueJob) -> str:
        raise NotImplementedError

    @abstractmethod
    async def get_status(self, job_id: str) -> str:
        raise NotImplementedError
