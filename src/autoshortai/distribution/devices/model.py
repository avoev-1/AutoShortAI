from dataclasses import dataclass
from typing import Optional


@dataclass
class ManagedDevice:
    device_id: str
    name: str
    device_class: str
    status: str = "offline"
    battery: Optional[float] = None
    storage_free: Optional[int] = None
    temperature: Optional[float] = None
    network: Optional[str] = None
    current_task: Optional[str] = None
    last_heartbeat: Optional[str] = None
