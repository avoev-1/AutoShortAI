"""ZIP16 metadata builder contracts."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

from .models import MaturityRating, PublishingMetadata, PublishingRequest


@dataclass(frozen=True)
class MetadataBuildInput:
    title_seed: str
    description_seed: str = ""
    hashtags: Sequence[str] = field(default_factory=tuple)
    language: str = "en"
    maturity_rating: MaturityRating = MaturityRating.GENERAL
    platform_overrides: Mapping[str, object] = field(default_factory=dict)


class NormalizedMetadataBuilder:
    """Build normalized metadata before platform adapter transformation."""

    def build_from_input(self, data: MetadataBuildInput) -> PublishingMetadata:
        normalized_hashtags = tuple(tag if tag.startswith("#") else f"#{tag}" for tag in data.hashtags)
        return PublishingMetadata(
            title=data.title_seed.strip(),
            description=data.description_seed.strip(),
            hashtags=normalized_hashtags,
            language=data.language,
            maturity_rating=data.maturity_rating,
            platform_overrides=data.platform_overrides,
        )

    def build(self, request: PublishingRequest, context: object | None = None) -> PublishingMetadata:
        return request.metadata
