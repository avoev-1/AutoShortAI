from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


class PlatformFamily(str, Enum):
    GENERIC = "generic"
    YOUTUBE_SHORTS = "youtube_shorts"
    TIKTOK = "tiktok"
    INSTAGRAM_REELS = "instagram_reels"
    FACEBOOK_REELS = "facebook_reels"
    SNAPCHAT_SPOTLIGHT = "snapchat_spotlight"
    X_TWITTER_VIDEO = "x_twitter_video"
    ADULT_X_CREATOR_PLATFORM = "adult_x_creator_platform"
    FUTURE_PLATFORM = "future_platform"


class RestrictedPlatformCategory(str, Enum):
    NONE = "none"
    ADULT_X_CREATOR = "adult_x_creator"


@dataclass(frozen=True)
class PlatformDeviceRequirement:
    platform_family: PlatformFamily
    required_capabilities: Sequence[str] = field(default_factory=tuple)
    allowed_device_types: Sequence[str] = field(default_factory=tuple)
    requires_account_binding: bool = False
    requires_manual_review: bool = False
    restricted_category: RestrictedPlatformCategory = RestrictedPlatformCategory.NONE
