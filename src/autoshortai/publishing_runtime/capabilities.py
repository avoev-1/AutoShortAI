"""ZIP16 platform capability contracts."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


@dataclass(frozen=True)
class PlatformLimit:
    key: str
    value: int | float | str | bool
    unit: str | None = None
    description: str | None = None


@dataclass(frozen=True)
class PlatformMediaRequirement:
    accepted_ratios: Sequence[str] = field(default_factory=tuple)
    accepted_codecs: Sequence[str] = field(default_factory=tuple)
    max_duration_seconds: int | None = None
    max_file_size_mb: int | None = None
    min_width: int | None = None
    min_height: int | None = None


@dataclass(frozen=True)
class PlatformPublishingRule:
    rule_id: str
    description: str
    required: bool = True
    restricted_only: bool = False


@dataclass(frozen=True)
class PlatformCapability:
    platform_id: str
    display_name: str
    supports_scheduling: bool = False
    supports_thumbnails: bool = False
    supports_age_restriction: bool = False
    supports_paid_or_subscriber_visibility: bool = False
    supports_hashtags: bool = True
    supports_adult_restricted_workflows: bool = False
    media: PlatformMediaRequirement = field(default_factory=PlatformMediaRequirement)
    limits: Sequence[PlatformLimit] = field(default_factory=tuple)
    rules: Sequence[PlatformPublishingRule] = field(default_factory=tuple)
    metadata: Mapping[str, str] = field(default_factory=dict)


def default_capabilities() -> dict[str, PlatformCapability]:
    """Return safe placeholder capabilities for future adapter implementation."""
    vertical = PlatformMediaRequirement(
        accepted_ratios=("9:16",),
        accepted_codecs=("h264", "h265"),
        max_duration_seconds=180,
        max_file_size_mb=2048,
        min_width=720,
        min_height=1280,
    )
    generic_vertical = PlatformCapability(
        platform_id="generic_vertical_video",
        display_name="Generic Vertical Video Platform",
        supports_scheduling=False,
        supports_thumbnails=False,
        supports_age_restriction=True,
        media=vertical,
        limits=(PlatformLimit("title_chars", 100, "chars"),),
        rules=(PlatformPublishingRule("manual_review_default", "Manual review should be required by default."),),
    )
    restricted = PlatformCapability(
        platform_id="generic_adult_creator_platform",
        display_name="Generic Adult Creator Platform",
        supports_scheduling=True,
        supports_age_restriction=True,
        supports_paid_or_subscriber_visibility=True,
        supports_adult_restricted_workflows=True,
        media=vertical,
        rules=(
            PlatformPublishingRule("all_participants_18_plus", "All participants must be confirmed 18+.", restricted_only=True),
            PlatformPublishingRule("consent_metadata_required", "Consent metadata is required.", restricted_only=True),
            PlatformPublishingRule("manual_review_required", "Manual review is required by default.", restricted_only=True),
        ),
    )
    return {
        generic_vertical.platform_id: generic_vertical,
        restricted.platform_id: restricted,
    }
