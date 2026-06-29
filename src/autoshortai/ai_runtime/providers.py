from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class AIProviderConfig:
    id: str
    display_name: str
    provider_type: str
    enabled: bool = False
    requires_network: bool = True
    credential_ref: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AIProviderCapability:
    provider_id: str
    capability_id: str
    task_types: Sequence[str]
    estimated_cost_per_unit: float | None = None
    quota_window: str | None = None


@dataclass(frozen=True)
class AIProviderRequest:
    provider_id: str
    task_id: str
    payload: Mapping[str, Any]
    timeout_seconds: int = 120


@dataclass(frozen=True)
class AIProviderResponse:
    provider_id: str
    task_id: str
    success: bool
    payload: Mapping[str, Any] = field(default_factory=dict)
    error: str | None = None
    actual_cost: float | None = None


class AIProvider:
    id: str = "abstract.provider"

    def can_handle(self, task_type: str, capabilities: Sequence[str]) -> bool:
        return False

    def execute(self, request: AIProviderRequest) -> AIProviderResponse:
        raise NotImplementedError("Provider execution belongs to implementation ZIP work, not ZIP13 architecture.")
