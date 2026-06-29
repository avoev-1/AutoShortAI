"""Platform capability contracts for analytics."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class PlatformAnalyticsCapability:
    platform: str
    supports_public_metrics: bool = True
    supports_private_metrics: bool = False
    supports_retention_curve: bool = False
    supports_time_windows: tuple[str, ...] = ("24h", "7d", "lifetime")
    supported_metrics: tuple[str, ...] = ("views", "likes", "comments", "shares")
    rate_limit_notes: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)


DEFAULT_PLATFORM_CAPABILITIES = (
    PlatformAnalyticsCapability(platform="youtube_shorts", supports_private_metrics=True, supports_retention_curve=True),
    PlatformAnalyticsCapability(platform="tiktok"),
    PlatformAnalyticsCapability(platform="instagram_reels"),
    PlatformAnalyticsCapability(platform="facebook_reels"),
    PlatformAnalyticsCapability(platform="snapchat_spotlight"),
    PlatformAnalyticsCapability(platform="x_video"),
    PlatformAnalyticsCapability(platform="generic"),
)
