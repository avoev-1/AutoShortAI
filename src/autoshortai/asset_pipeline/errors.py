"""ZIP06 exception hierarchy."""


class AssetPipelineError(Exception):
    """Base error for the Smart Asset Pipeline."""


class AssetRegistryError(AssetPipelineError):
    """Raised by registry adapters."""


class FingerprintError(AssetPipelineError):
    """Raised by fingerprint adapters."""


class DependencyGraphError(AssetPipelineError):
    """Raised by dependency graph adapters."""


class CacheError(AssetPipelineError):
    """Raised by cache adapters."""


class ResumeError(AssetPipelineError):
    """Raised by resume adapters."""


class CheckpointError(AssetPipelineError):
    """Raised by checkpoint adapters."""


class IntegrityError(AssetPipelineError):
    """Raised by integrity checking adapters."""


class StorageError(AssetPipelineError):
    """Raised by storage adapters."""


class ProviderError(AssetPipelineError):
    """Raised by provider adapters."""


class ApiCostError(AssetPipelineError):
    """Raised by API cost optimization adapters."""


class PerformanceProfilerError(AssetPipelineError):
    """Raised by profiler adapters."""
