from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .models import DeviceNode, DeviceStatus


@dataclass
class DeviceRegistry:
    devices: dict[str, DeviceNode] = field(default_factory=dict)

    def register(self, device: DeviceNode) -> None:
        self.devices[device.id] = device

    def get(self, device_id: str) -> DeviceNode | None:
        return self.devices.get(device_id)

    def list_available(self) -> Iterable[DeviceNode]:
        for device in self.devices.values():
            if device.status in {DeviceStatus.REGISTERED, DeviceStatus.ONLINE}:
                yield device
