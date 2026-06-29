from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CostEstimate:
    task_id: str
    provider_id: str
    estimated_cost: float
    currency: str = "USD"


@dataclass(frozen=True)
class QuotaGuardDecision:
    allowed: bool
    reason: str = "allowed"
    remaining_budget: float | None = None
