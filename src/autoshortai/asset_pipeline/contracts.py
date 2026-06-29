"""Public contracts for ZIP06 Smart Asset Pipeline.

These contracts are architectural boundaries. Implementations must live behind
these interfaces and must not force provider-specific dependencies into core.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping, Optional, Protocol, Sequence, runtime_checkable

from .models import (
    ApiCostEstimate,
    AssetDependency,
    AssetFingerprint,
    AssetIdentity,
    AssetRef,
    AssetStatus,
    BuildDecision,
    CacheEntry,
    CacheLevel,
    CachePolicy,
    CheckpointRecord,
    DependencyGraphSnapshot,
    IntegrityReport,
    PerformanceSample,
    ProviderDescriptor,
    StorageLocation,
)


@runtime_checkable
class AssetRegistryContract(Protocol):
    """Contract for registering and resolving assets."""

    def register(self, asset: AssetRef) -> AssetRef: ...

    def get(self, asset_id: str) -> Optional[AssetRef]: ...

    def list(self, *, status: Optional[AssetStatus] = None) -> Sequence[AssetRef]: ...

    def update_status(self, asset_id: str, status: AssetStatus) -> AssetRef: ...


@runtime_checkable
class FingerprintEngineContract(Protocol):
    """Contract for computing and comparing asset fingerprints."""

    def compute(self, asset: AssetRef, payload: Any = None) -> AssetFingerprint: ...

    def compare(self, expected: AssetFingerprint, actual: AssetFingerprint) -> bool: ...


@runtime_checkable
class DependencyGraphContract(Protocol):
    """Contract for directed asset dependency relationships."""

    def add_asset(self, asset_id: str) -> None: ...

    def add_dependency(self, dependency: AssetDependency) -> None: ...

    def impacted_by(self, asset_id: str) -> Sequence[str]: ...

    def snapshot(self) -> DependencyGraphSnapshot: ...


@runtime_checkable
class IncrementalBuildContract(Protocol):
    """Contract for planning rebuild versus reuse decisions."""

    def plan_build(self, asset_id: str, *, force: bool = False) -> BuildDecision: ...

    def mark_built(self, asset_id: str, fingerprint: AssetFingerprint) -> None: ...


@runtime_checkable
class CacheManagerContract(Protocol):
    """Contract for multi-level cache coordination."""

    def get(self, key: str, *, levels: Iterable[CacheLevel] | None = None) -> Optional[CacheEntry]: ...

    def put(self, key: str, entry: CacheEntry, policy: CachePolicy | None = None) -> CacheEntry: ...

    def invalidate(self, key: str) -> None: ...

    def clear_policy(self, policy_name: str) -> None: ...


@runtime_checkable
class ResumeEngineContract(Protocol):
    """Contract for determining safe workflow resume behavior."""

    def can_resume(self, pipeline_id: str) -> bool: ...

    def resume_from(self, checkpoint: CheckpointRecord) -> Mapping[str, Any]: ...


@runtime_checkable
class CheckpointSystemContract(Protocol):
    """Contract for recording and reading pipeline checkpoints."""

    def create(self, record: CheckpointRecord) -> CheckpointRecord: ...

    def read(self, checkpoint_id: str) -> Optional[CheckpointRecord]: ...

    def mark_completed(self, checkpoint_id: str) -> CheckpointRecord: ...

    def mark_failed(self, checkpoint_id: str, reason: str) -> CheckpointRecord: ...


@runtime_checkable
class IntegrityCheckerContract(Protocol):
    """Contract for validating assets and dependency snapshots."""

    def verify_asset(self, asset: AssetRef, expected: AssetFingerprint | None = None) -> IntegrityReport: ...

    def verify_graph(self, snapshot: DependencyGraphSnapshot) -> IntegrityReport: ...


@runtime_checkable
class StorageManagerContract(Protocol):
    """Contract for provider-agnostic asset persistence."""

    def save(self, asset: AssetRef, payload: Any) -> StorageLocation: ...

    def load(self, location: StorageLocation) -> Any: ...

    def delete(self, location: StorageLocation) -> None: ...

    def exists(self, location: StorageLocation) -> bool: ...


@runtime_checkable
class ProviderContract(Protocol):
    """Contract every asset provider plugin must satisfy."""

    def descriptor(self) -> ProviderDescriptor: ...

    def supports(self, capability: str) -> bool: ...

    def read(self, uri: str) -> Any: ...

    def write(self, uri: str, payload: Any) -> StorageLocation: ...


@runtime_checkable
class ApiCostOptimizerContract(Protocol):
    """Contract for estimating and recording provider costs."""

    def estimate(self, provider: str, operation: str, metadata: Mapping[str, Any] | None = None) -> ApiCostEstimate: ...

    def allow(self, estimate: ApiCostEstimate) -> bool: ...

    def record(self, estimate: ApiCostEstimate, actual_cost: float | None = None) -> None: ...


@runtime_checkable
class PerformanceProfilerContract(Protocol):
    """Contract for lightweight performance profiling."""

    def start_span(self, scope: str, metadata: Mapping[str, Any] | None = None) -> str: ...

    def end_span(self, span_id: str) -> PerformanceSample: ...

    def sample(self, sample: PerformanceSample) -> None: ...


@runtime_checkable
class HookRegistryContract(Protocol):
    """Contract for registering and emitting asset pipeline hooks."""

    def register(self, hook_name: str, handler: Any) -> None: ...

    def emit(self, hook_name: str, payload: Mapping[str, Any]) -> Sequence[Any]: ...
