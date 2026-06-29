from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence


@dataclass(frozen=True)
class DeviceCapability:
    id: str
    task_types: Sequence[str]
    device_types: Sequence[str] = field(default_factory=tuple)
    platform_families: Sequence[str] = field(default_factory=tuple)
    supports_restricted_creator_mode: bool = False
    requires_account_binding: bool = False
    requires_network: bool = False
    estimated_resource_weight: int = 1


@dataclass(frozen=True)
class CapabilityRequirement:
    capability_ids: Sequence[str] = field(default_factory=tuple)
    required_device_types: Sequence[str] = field(default_factory=tuple)
    platform_family: str = "generic"
    requires_restricted_creator_mode: bool = False

    def is_satisfied_by(self, capability_ids: Sequence[str], device_type: str, restricted_enabled: bool = False) -> bool:
        if not set(self.capability_ids).issubset(set(capability_ids)):
            return False
        if self.required_device_types and device_type not in self.required_device_types:
            return False
        if self.requires_restricted_creator_mode and not restricted_enabled:
            return False
        return True
