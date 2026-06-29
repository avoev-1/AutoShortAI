"""Storage contracts for ZIP09 analytics data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AnalyticsStorageConfig:
    provider: str = "json_local"
    root_path: Path | None = None
    use_zip06_storage_provider: bool = False
    allow_sqlite_optional_provider: bool = True
    require_database: bool = False


@dataclass(frozen=True)
class AnalyticsRetentionPolicy:
    keep_raw_snapshots: bool = True
    keep_normalized_snapshots: bool = True
    max_snapshot_age_days: int | None = None
    compact_reports_after_days: int | None = None
