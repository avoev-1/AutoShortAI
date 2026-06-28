from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MetricEvent:
    name: str
    value: float
    tags: dict[str, str] | None = None


@dataclass(frozen=True)
class AuditEvent:
    actor: str
    action: str
    target: str
    metadata: dict[str, Any] | None = None


class TelemetryProvider(ABC):
    provider_id: str

    @abstractmethod
    async def record_metric(self, event: MetricEvent) -> None:
        raise NotImplementedError

    @abstractmethod
    async def record_audit(self, event: AuditEvent) -> None:
        raise NotImplementedError
