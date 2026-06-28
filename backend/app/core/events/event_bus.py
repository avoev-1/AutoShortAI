from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict[str, Any]
    created_at: str = datetime.now(timezone.utc).isoformat()


class InMemoryEventBus:
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def publish(self, event: DomainEvent) -> None:
        self.events.append(event)


event_bus = InMemoryEventBus()
