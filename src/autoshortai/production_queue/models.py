"""Serializable contracts for ZIP08 production queue architecture.

These models are intentionally lightweight. They define architecture surfaces
for future implementation and should avoid provider-specific behavior.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional


class ProductionJobStatus(str, Enum):
    CREATED = "created"
    PENDING = "pending"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"


class ProductionJobPriority(str, Enum):
    URGENT = "urgent"
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"
    BACKGROUND = "background"


class ProductionJobType(str, Enum):
    SCRIPT_GENERATION = "script_generation"
    ASSET_PREPARATION = "asset_preparation"
    VIDEO_RENDER = "video_render"
    DISTRIBUTION = "distribution"
    ANALYSIS = "analysis"
    CUSTOM = "custom"


class FailureClass(str, Enum):
    TRANSIENT = "transient"
    PROVIDER_ERROR = "provider_error"
    RESOURCE_LIMIT = "resource_limit"
    VALIDATION_ERROR = "validation_error"
    DEPENDENCY_MISSING = "dependency_missing"
    CANCELLED_BY_USER = "cancelled_by_user"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class ProductionJobError:
    code: str
    message: str
    failure_class: FailureClass = FailureClass.UNKNOWN
    retryable: bool = False
    details: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProductionJobResult:
    job_id: str
    status: ProductionJobStatus
    output_refs: tuple[str, ...] = ()
    metrics: Mapping[str, Any] = field(default_factory=dict)
    error: Optional[ProductionJobError] = None


@dataclass(frozen=True)
class ProductionJob:
    job_id: str
    job_type: str
    title: str
    status: ProductionJobStatus = ProductionJobStatus.CREATED
    priority: ProductionJobPriority = ProductionJobPriority.NORMAL
    strategy_id: Optional[str] = None
    mission_id: Optional[str] = None
    batch_id: Optional[str] = None
    platform: Optional[str] = None
    scheduled_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    retry_count: int = 0
    max_retries: int = 3
    dependency_ids: tuple[str, ...] = ()
    required_worker_type: Optional[str] = None
    checkpoint_id: Optional[str] = None
    asset_refs: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ResourceBudget:
    max_concurrent_workers: int = 1
    max_render_workers: int = 1
    max_cpu_percent: Optional[float] = None
    max_ram_mb: Optional[int] = None
    max_api_calls_per_window: Optional[int] = None
    max_api_cost_per_day: Optional[float] = None
    max_job_runtime_seconds: Optional[int] = None
    max_queue_size: Optional[int] = None
    max_retries_per_job: int = 3


@dataclass(frozen=True)
class BudgetDecision:
    allowed: bool
    reason: str = ""
    defer_until: Optional[str] = None
    requires_manual_approval: bool = False


@dataclass(frozen=True)
class SchedulerDecision:
    job_id: str
    action: str
    reason: str
    scheduled_at: Optional[str] = None
    worker_type: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BatchPlan:
    batch_id: str
    title: str
    target_count: int
    source_strategy_id: Optional[str] = None
    platform: Optional[str] = None
    cadence_id: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CadenceRule:
    cadence_id: str
    name: str
    frequency: str
    timezone: str = "local"
    max_jobs_per_period: Optional[int] = None
    window_start: Optional[str] = None
    window_end: Optional[str] = None
    blackout_dates: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)
