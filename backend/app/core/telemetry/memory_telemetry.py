from app.core.contracts.telemetry import AuditEvent, MetricEvent


class InMemoryTelemetry:
    def __init__(self) -> None:
        self.metrics: list[MetricEvent] = []
        self.audit_events: list[AuditEvent] = []

    async def record_metric(self, event: MetricEvent) -> None:
        self.metrics.append(event)

    async def record_audit(self, event: AuditEvent) -> None:
        self.audit_events.append(event)
