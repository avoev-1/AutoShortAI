from __future__ import annotations

from dataclasses import dataclass, field

from .models import SecretAuditEvent


@dataclass
class InMemorySecurityAuditLog:
    """Minimal audit log contract helper for tests and architecture examples."""

    events: list[SecretAuditEvent] = field(default_factory=list)

    def append(self, event: SecretAuditEvent) -> None:
        self.events.append(event)

    def list_events(self) -> tuple[SecretAuditEvent, ...]:
        return tuple(self.events)
