from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Any


class PlatformFamily(str, Enum):
    GENERIC = "generic"
    YOUTUBE_SHORTS = "youtube_shorts"
    TIKTOK = "tiktok"
    INSTAGRAM_REELS = "instagram_reels"
    FACEBOOK_REELS = "facebook_reels"
    SNAPCHAT_SPOTLIGHT = "snapchat_spotlight"
    X_TWITTER_VIDEO = "x_twitter_video"
    ADULT_CREATOR_PLATFORM = "adult_creator_platform"
    FUTURE_PLATFORM = "future_platform"


class RestrictedPlatformCategory(str, Enum):
    NONE = "none"
    AGE_GATED_18_PLUS = "age_gated_18_plus"
    ADULT_CREATOR_PLATFORM = "adult_creator_platform"


@dataclass(frozen=True)
class PlatformContext:
    id: str
    family: PlatformFamily = PlatformFamily.GENERIC
    format_hint: str = "vertical_video"
    duration_target_seconds: int | None = None
    aspect_ratio: str = "9:16"
    language: str = "fr"
    restricted_category: RestrictedPlatformCategory = RestrictedPlatformCategory.NONE
    requires_manual_review: bool = False
    requires_age_gate: bool = False
    requires_consent_metadata: bool = False
    policy_metadata: Mapping[str, Any] = field(default_factory=dict)

    @property
    def is_restricted_adult(self) -> bool:
        return self.restricted_category in {
            RestrictedPlatformCategory.AGE_GATED_18_PLUS,
            RestrictedPlatformCategory.ADULT_CREATOR_PLATFORM,
        }
