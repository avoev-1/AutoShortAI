"""Event models for future Smart Asset Pipeline integrations."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class AssetPipelineEventType(str, Enum):
    ASSET_DECLARED = "asset.declared"
    ASSET_READY = "asset.ready"
    ASSET_INVALIDATED = "asset.invalidated"
    BUILD_REQUIRED = "build.required"
    BUILD_SKIPPED = "build.skipped"
    CHECKPOINT_READY = "checkpoint.ready"
    RESUME_READY = "resume.ready"
    PROVIDER_BLOCKED_BY_COST = "provider.blocked_by_cost"


@dataclass(frozen=True, slots=True)
class AssetPipelineEvent:
    event_type: AssetPipelineEventType
    asset_id: str | None = None
    created_at: str | None = None
    payload: Mapping[str, Any] = field(default_factory=dict)
