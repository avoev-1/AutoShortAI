"""ZIP17 workspace interfaces.

These protocols define what future implementations must provide without
forcing a database, cloud sync, or platform-specific dependency.
"""

from __future__ import annotations

from typing import Protocol, Iterable

from .models import (
    MediaAsset,
    MediaLibrary,
    WorkspaceManifest,
    WorkspaceProject,
)


class WorkspaceProvider(Protocol):
    """Creates and loads workspaces."""

    def create_workspace(self, manifest: WorkspaceManifest) -> WorkspaceManifest:
        """Create a workspace from a manifest."""
        ...

    def load_workspace(self, workspace_id: str) -> WorkspaceManifest:
        """Load a workspace manifest."""
        ...


class ProjectRepository(Protocol):
    """Stores and retrieves workspace projects."""

    def create_project(self, project: WorkspaceProject) -> WorkspaceProject:
        """Create a project."""
        ...

    def get_project(self, project_id: str) -> WorkspaceProject:
        """Return a project by id."""
        ...

    def list_projects(self) -> Iterable[WorkspaceProject]:
        """List known projects."""
        ...


class MediaLibraryProvider(Protocol):
    """Stores and retrieves media library records."""

    def add_asset(self, asset: MediaAsset) -> MediaAsset:
        """Add or register a media asset."""
        ...

    def get_asset(self, asset_id: str) -> MediaAsset:
        """Return a media asset by id."""
        ...

    def list_assets(self) -> Iterable[MediaAsset]:
        """List media assets."""
        ...

    def load_library(self, library_id: str) -> MediaLibrary:
        """Load a library manifest."""
        ...


class ImportExportAdapter(Protocol):
    """Imports and exports projects and media."""

    def import_path(self, source_path: str, project_id: str | None = None) -> list[MediaAsset]:
        """Import a file or folder into the workspace."""
        ...

    def export_project(self, project_id: str, target_path: str) -> str:
        """Export a project package."""
        ...


class WorkspaceIndex(Protocol):
    """Search and tagging index for projects and media."""

    def index_asset(self, asset: MediaAsset) -> None:
        """Index a media asset."""
        ...

    def search(self, query: str, filters: dict[str, str] | None = None) -> list[MediaAsset]:
        """Search media assets."""
        ...
