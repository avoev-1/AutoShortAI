from app.sdk.events.event_bus import SDKEvent, SDKEventBus
from app.sdk.events.event_types import SDKEventType


def test_event_bus_records_and_dispatches() -> None:
    bus = SDKEventBus()
    received = []

    bus.subscribe(SDKEventType.plugin_registered, lambda event: received.append(event))
    event = SDKEvent(event_type=SDKEventType.plugin_registered, payload={"plugin": "test"})
    bus.publish(event)

    assert bus.events == [event]
    assert received == [event]
