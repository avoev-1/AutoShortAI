"""Hook names and hook payload models for ZIP06."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class AssetPipelineHook(str, Enum):
    ASSET_REGISTERING = "asset.registering"
    ASSET_REGISTERED = "asset.registered"
    ASSET_FINGERPRINTING = "asset.fingerprinting"
    ASSET_FINGERPRINTED = "asset.fingerprinted"
    DEPENDENCY_CHANGED = "dependency.changed"
    BUILD_PLANNED = "build.planned"
    CACHE_HIT = "cache.hit"
    CACHE_MISS = "cache.miss"
    CHECKPOINT_CREATED = "checkpoint.created"
    RESUME_REQUESTED = "resume.requested"
    INTEGRITY_FAILED = "integrity.failed"
    PROVIDER_OPERATION_PLANNED = "provider.operation_planned"
    COST_ESTIMATED = "cost.estimated"
    PERFORMANCE_SAMPLED = "performance.sampled"


@dataclass(frozen=True, slots=True)
class HookPayload:
    """Serializable hook payload wrapper."""

    hook: AssetPipelineHook
    data: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)
