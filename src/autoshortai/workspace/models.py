"""ZIP17 workspace and media library data models.

These models define architecture contracts. They intentionally avoid heavy
implementation details, database requirements, platform lock-in, and cloud
assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class WorkspaceMode(str, Enum):
    """Workspace operating mode."""

    GENERAL = "general"
    RESTRICTED = "restricted"


class WorkspaceStatus(str, Enum):
    """Lifecycle status for a workspace or project."""

    ACTIVE = "active"
    ARCHIVED = "archived"
    LOCKED = "locked"
    NEEDS_REVIEW = "needs_review"
    ERROR = "error"


class MediaType(str, Enum):
    """Supported media item categories."""

    SCRIPT = "script"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    SUBTITLE = "subtitle"
    THUMBNAIL = "thumbnail"
    METADATA = "metadata"
    TEMPLATE = "template"
    EXPORT = "export"


class MediaOrigin(str, Enum):
    """Where a media item came from."""

    GENERATED = "generated"
    IMPORTED = "imported"
    RENDERED = "rendered"
    PUBLISHED_PACKAGE = "published_package"
    MANUAL = "manual"


class MediaStatus(str, Enum):
    """Media lifecycle status."""

    DRAFT = "draft"
    READY = "ready"
    FINAL = "final"
    ARCHIVED = "archived"
    MISSING = "missing"
    CORRUPTED = "corrupted"
    BLOCKED = "blocked"


class MaturityRating(str, Enum):
    """Content maturity rating.

    GENERAL and TEEN can be used in the normal workspace.
    MATURE_18 and RESTRICTED_ADULT require restricted workspace safeguards.
    """

    GENERAL = "general"
    TEEN = "teen"
    MATURE_18 = "mature_18"
    RESTRICTED_ADULT = "restricted_adult"


class ManualReviewStatus(str, Enum):
    """Manual review state for media and projects."""

    NOT_REQUIRED = "not_required"
    REQUIRED = "required"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(slots=True)
class WorkspacePath:
    """Portable workspace path reference."""

    relative_path: str
    purpose: str
    exists_required: bool = False


@dataclass(slots=True)
class WorkspaceItem:
    """Base workspace item."""

    item_id: str
    name: str
    path: str
    item_type: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MediaTag:
    """Tag used for search and organization."""

    name: str
    category: str = "general"


@dataclass(slots=True)
class MediaVersion:
    """Lightweight media version reference."""

    version_id: str
    label: str
    path: str
    notes: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MediaAsset:
    """Media asset tracked by the local library."""

    asset_id: str
    media_type: MediaType
    path: str
    origin: MediaOrigin = MediaOrigin.IMPORTED
    status: MediaStatus = MediaStatus.DRAFT
    maturity_rating: MaturityRating = MaturityRating.GENERAL
    manual_review_status: ManualReviewStatus = ManualReviewStatus.NOT_REQUIRED
    platform_targets: list[str] = field(default_factory=list)
    tags: list[MediaTag] = field(default_factory=list)
    versions: list[MediaVersion] = field(default_factory=list)
    zip06_asset_id: str | None = None
    fingerprint: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MediaCollection:
    """Named group of media assets."""

    collection_id: str
    name: str
    asset_ids: list[str] = field(default_factory=list)
    tags: list[MediaTag] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MediaLibrary:
    """Local media library manifest."""

    library_id: str
    mode: WorkspaceMode = WorkspaceMode.GENERAL
    assets: list[MediaAsset] = field(default_factory=list)
    collections: list[MediaCollection] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ProjectVersion:
    """Project-level version reference."""

    version_id: str
    label: str
    created_at: str | None = None
    notes: str = ""
    asset_ids: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class VersionManifest:
    """Manifest for project versions."""

    project_id: str
    versions: list[ProjectVersion] = field(default_factory=list)


@dataclass(slots=True)
class WorkspaceProject:
    """AutoShortAI workspace project."""

    project_id: str
    name: str
    mode: WorkspaceMode = WorkspaceMode.GENERAL
    status: WorkspaceStatus = WorkspaceStatus.ACTIVE
    root_path: str | None = None
    platform_targets: list[str] = field(default_factory=list)
    creative_profile_id: str | None = None
    campaign_id: str | None = None
    niche: str | None = None
    language: str | None = None
    maturity_rating: MaturityRating = MaturityRating.GENERAL
    manual_review_status: ManualReviewStatus = ManualReviewStatus.NOT_REQUIRED
    media_asset_ids: list[str] = field(default_factory=list)
    versions: list[ProjectVersion] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class WorkspaceManifest:
    """Top-level workspace manifest."""

    workspace_id: str
    name: str
    mode: WorkspaceMode = WorkspaceMode.GENERAL
    status: WorkspaceStatus = WorkspaceStatus.ACTIVE
    projects_root: str = "projects"
    library_root: str = "library"
    restricted_root: str = "restricted"
    projects: list[WorkspaceProject] = field(default_factory=list)
    libraries: list[MediaLibrary] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Workspace:
    """Workspace configuration and manifest wrapper."""

    workspace_id: str
    root_path: str
    manifest: WorkspaceManifest
    config: dict[str, Any] = field(default_factory=dict)
