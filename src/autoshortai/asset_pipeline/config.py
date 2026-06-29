"""Configuration models for ZIP06.

The settings are intentionally serializable and portable. Future implementations
may load these from YAML, JSON, environment variables, or plugin configuration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from .models import CacheLevel


@dataclass(frozen=True, slots=True)
class AssetPipelineSettings:
    """Global Smart Asset Pipeline settings."""

    enabled: bool = True
    cache_levels: tuple[CacheLevel, ...] = (CacheLevel.MEMORY, CacheLevel.LOCAL_DISK)
    local_cache_dir: Path = Path(".autoshortai/cache/assets")
    checkpoint_dir: Path = Path(".autoshortai/checkpoints")
    max_api_cost_per_run: float | None = None
    profiler_enabled: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)
