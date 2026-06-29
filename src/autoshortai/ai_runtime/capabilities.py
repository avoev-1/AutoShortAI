from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence


@dataclass(frozen=True)
class AIWorkerCapability:
    id: str
    task_types: Sequence[str]
    modalities: Sequence[str] = field(default_factory=tuple)
    languages: Sequence[str] = field(default_factory=tuple)
    platform_families: Sequence[str] = field(default_factory=tuple)
    supports_restricted_platforms: bool = False
    supports_local_execution: bool = False
    supports_cloud_execution: bool = True
    max_estimated_cost: float | None = None


@dataclass(frozen=True)
class CapabilitySet:
    capabilities: Sequence[AIWorkerCapability] = field(default_factory=tuple)

    def supports(self, task_type: str, required: Sequence[str] = ()) -> bool:
        required_set = set(required)
        for capability in self.capabilities:
            if task_type in capability.task_types and required_set.issubset(set(capability.modalities) | {capability.id}):
                return True
        return False
