from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class DeviceMessage:
    id: str
    device_id: str
    message_type: str
    payload: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeviceCommand(DeviceMessage):
    command_name: str = "noop"


@dataclass(frozen=True)
class DeviceResponse(DeviceMessage):
    success: bool = False
    error: str | None = None


@dataclass(frozen=True)
class Heartbeat:
    device_id: str
    status: str
    sent_at: str | None = None
    health_payload: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SecureChannel:
    id: str
    transport: str
    encrypted: bool = True
    authenticated: bool = True
    credential_ref: str | None = None
