"""ZIP17 search and tagging contracts."""

from __future__ import annotations

from dataclasses import dataclass, field

from .models import MediaType, MaturityRating, MediaAsset


@dataclass(slots=True)
class MediaFilter:
    """Search filter for media library queries."""

    media_type: MediaType | None = None
    platform_target: str | None = None
    tag: str | None = None
    language: str | None = None
    maturity_rating: MaturityRating | None = None
    status: str | None = None


@dataclass(slots=True)
class SearchQuery:
    """Search query contract."""

    text: str = ""
    filters: MediaFilter = field(default_factory=MediaFilter)


@dataclass(slots=True)
class SearchResult:
    """Search result contract."""

    query: SearchQuery
    assets: list[MediaAsset] = field(default_factory=list)


@dataclass(slots=True)
class TagIndex:
    """Lightweight tag index contract."""

    tags: dict[str, list[str]] = field(default_factory=dict)
