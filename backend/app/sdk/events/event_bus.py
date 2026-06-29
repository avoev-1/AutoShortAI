from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from app.sdk.events.event_types import SDKEventType


@dataclass(frozen=True)
class SDKEvent:
    event_type: SDKEventType
    payload: dict[str, Any]
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


EventHandler = Callable[[SDKEvent], None]


class SDKEventBus:
    def __init__(self) -> None:
        self._handlers: dict[SDKEventType, list[EventHandler]] = {}
        self.events: list[SDKEvent] = []

    def subscribe(self, event_type: SDKEventType, handler: EventHandler) -> None:
        self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event: SDKEvent) -> None:
        self.events.append(event)
        for handler in self._handlers.get(event.event_type, []):
            handler(event)


sdk_event_bus = SDKEventBus()
