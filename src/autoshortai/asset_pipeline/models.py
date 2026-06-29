"""Shared models for the ZIP06 Smart Asset Pipeline architecture.

These dataclasses are intentionally lightweight. They define shape and intent for
future implementations without embedding full business logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional, Sequence


class AssetKind(str, Enum):
    """High-level asset categories used by the pipeline."""

    RAW = "raw"
    SCRIPT = "script"
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"
    METADATA = "metadata"
    DISTRIBUTION_PACKAGE = "distribution_package"
    UNKNOWN = "unknown"


class AssetStatus(str, Enum):
    """Lifecycle status for a registered asset."""

    DECLARED = "declared"
    AVAILABLE = "available"
    BUILD_REQUIRED = "build_required"
    BUILDING = "building"
    CACHED = "cached"
    FAILED = "failed"
    ARCHIVED = "archived"


class FingerprintAlgorithm(str, Enum):
    """Supported fingerprint algorithm identifiers."""

    SHA256 = "sha256"
    BLAKE2B = "blake2b"
    PROVIDER_NATIVE = "provider_native"
    CUSTOM = "custom"


class CacheLevel(str, Enum):
    """Cache levels defined by ZIP06."""

    MEMORY = "memory"
    LOCAL_DISK = "local_disk"
    EXTERNAL = "external"


class ProviderCapability(str, Enum):
    """Provider capabilities exposed through the abstraction layer."""

    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    LIST = "list"
    CHECKSUM = "checksum"
    SIGNED_URL = "signed_url"
    COST_ESTIMATE = "cost_estimate"


class CheckpointState(str, Enum):
    """Checkpoint states used by resumable workflows."""

    CREATED = "created"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass(frozen=True, slots=True)
class AssetIdentity:
    """Stable asset identity.

    The string form intentionally avoids filesystem assumptions so it can remain
    portable across Windows, Linux, macOS, and future mobile environments.
    """

    namespace: str
    name: str
    version: Optional[str] = None

    @property
    def asset_id(self) -> str:
        base = f"{self.namespace}:{self.name}"
        return f"{base}:{self.version}" if self.version else base


@dataclass(slots=True)
class AssetRef:
    """Reference to an asset known by the registry."""

    identity: AssetIdentity
    kind: AssetKind = AssetKind.UNKNOWN
    status: AssetStatus = AssetStatus.DECLARED
    location_uri: Optional[str] = None
    provider: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def asset_id(self) -> str:
        return self.identity.asset_id


@dataclass(frozen=True, slots=True)
class AssetFingerprint:
    """Fingerprint result for an asset."""

    asset_id: str
    algorithm: FingerprintAlgorithm
    digest: str
    size_bytes: Optional[int] = None
    created_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class AssetDependency:
    """Directed relationship between two assets."""

    source_asset_id: str
    target_asset_id: str
    relation: str = "depends_on"
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class DependencyGraphSnapshot:
    """Serializable graph snapshot for diagnostics and resume decisions."""

    nodes: Sequence[str]
    edges: Sequence[AssetDependency]
    created_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class CachePolicy:
    """Cache policy definition shared by cache adapters."""

    levels: Sequence[CacheLevel] = (CacheLevel.MEMORY, CacheLevel.LOCAL_DISK)
    ttl_seconds: Optional[int] = None
    max_bytes: Optional[int] = None
    eviction: str = "least_recently_used"
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class CacheEntry:
    """Metadata for a cached asset."""

    key: str
    asset_id: str
    level: CacheLevel
    fingerprint: Optional[AssetFingerprint] = None
    created_at: Optional[str] = None
    last_used_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class CheckpointRecord:
    """Checkpoint state for resumable asset workflows."""

    checkpoint_id: str
    pipeline_id: str
    step_id: str
    asset_ids: Sequence[str]
    state: CheckpointState = CheckpointState.CREATED
    created_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class BuildDecision:
    """Planner output for incremental build decisions."""

    asset_id: str
    should_rebuild: bool
    reason: str
    required_dependencies: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ProviderDescriptor:
    """Provider declaration used by the provider abstraction layer."""

    name: str
    version: str
    capabilities: Sequence[ProviderCapability]
    config_schema: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ApiCostEstimate:
    """Estimated cost for a provider operation."""

    provider: str
    operation: str
    estimated_units: float
    estimated_cost: float
    currency: str = "USD"
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class PerformanceSample:
    """Lightweight profiling sample."""

    scope: str
    duration_ms: float
    cpu_percent: Optional[float] = None
    memory_mb: Optional[float] = None
    created_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class StorageLocation:
    """Provider-agnostic location for a stored asset."""

    provider: str
    uri: str
    checksum: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class IntegrityReport:
    """Result of an integrity verification operation."""

    asset_id: str
    ok: bool
    errors: Sequence[str] = field(default_factory=tuple)
    warnings: Sequence[str] = field(default_factory=tuple)
    checked_at: Optional[str] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
