from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class DeviceType(str, Enum):
    LOCAL_MACHINE = "local_machine"
    REMOTE_MACHINE = "remote_machine"
    HOME_SERVER = "home_server"
    VIRTUAL_MACHINE = "virtual_machine"
    ANDROID_DEVICE = "android_device"
    IOS_DEVICE = "ios_device"
    EMULATOR = "emulator"
    BROWSER_NODE = "browser_node"
    RENDER_NODE = "render_node"
    AI_WORKER_NODE = "ai_worker_node"
    PUBLISHING_NODE = "publishing_node"
    ANALYTICS_NODE = "analytics_node"
    MONITORING_NODE = "monitoring_node"
    MANUAL_REVIEW_NODE = "manual_review_node"


class DeviceStatus(str, Enum):
    UNKNOWN = "unknown"
    REGISTERED = "registered"
    ONLINE = "online"
    BUSY = "busy"
    DEGRADED = "degraded"
    OFFLINE = "offline"
    DISABLED = "disabled"
    FAILED = "failed"


class DeviceTaskType(str, Enum):
    RENDER = "render"
    AI_WORKER = "ai_worker"
    PUBLISHING_PREP = "publishing_prep"
    ANALYTICS_COLLECTION = "analytics_collection"
    MANUAL_REVIEW = "manual_review"
    HEALTH_CHECK = "health_check"
    SCREENSHOT_CAPTURE = "screenshot_capture"
    ACCOUNT_STATUS_CHECK = "account_status_check"


class ContentRestrictionLevel(str, Enum):
    GENERAL = "general"
    MATURE = "mature"
    RESTRICTED_ADULT_X = "restricted_adult_x"


@dataclass(frozen=True)
class DeviceHealth:
    online: bool = False
    battery_percent: int | None = None
    storage_available_mb: int | None = None
    cpu_percent: float | None = None
    ram_percent: float | None = None
    temperature_celsius: float | None = None
    network_status: str = "unknown"
    last_heartbeat_at: str | None = None
    current_task_id: str | None = None
    failure_count: int = 0


@dataclass(frozen=True)
class DeviceNode:
    id: str
    display_name: str
    device_type: DeviceType
    status: DeviceStatus = DeviceStatus.REGISTERED
    capabilities: Sequence[str] = field(default_factory=tuple)
    platform_families: Sequence[str] = field(default_factory=tuple)
    supports_restricted_creator_mode: bool = False
    account_binding_ids: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeviceTask:
    id: str
    task_type: DeviceTaskType
    required_capabilities: Sequence[str] = field(default_factory=tuple)
    platform_family: str = "generic"
    restriction_level: ContentRestrictionLevel = ContentRestrictionLevel.GENERAL
    requires_manual_review: bool = False
    requires_isolated_device: bool = False
    payload: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeviceAssignment:
    task_id: str
    device_id: str
    reason: str
    manual_review_required: bool = False
    restricted_workflow: bool = False
