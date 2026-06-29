"""ZIP17 manifest helpers.

Only lightweight serialization contracts live here. Future implementation may
store manifests in JSON files or an optional database adapter.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .models import WorkspaceManifest, WorkspaceProject, MediaAsset


def workspace_manifest_to_dict(manifest: WorkspaceManifest) -> dict[str, Any]:
    """Convert workspace manifest dataclass to a plain dictionary."""
    return asdict(manifest)


def project_to_dict(project: WorkspaceProject) -> dict[str, Any]:
    """Convert project dataclass to a plain dictionary."""
    return asdict(project)


def media_asset_to_dict(asset: MediaAsset) -> dict[str, Any]:
    """Convert media asset dataclass to a plain dictionary."""
    return asdict(asset)
