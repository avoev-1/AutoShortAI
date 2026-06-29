from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence, Any

from .models import DashboardStatus, DashboardMetric


class PlatformKind(str, Enum):
    GENERIC = "generic"
    YOUTUBE_SHORTS = "youtube_shorts"
    TIKTOK = "tiktok"
    INSTAGRAM_REELS = "instagram_reels"
    FACEBOOK_REELS = "facebook_reels"
    SNAPCHAT_SPOTLIGHT = "snapchat_spotlight"
    X_TWITTER_VIDEO = "x_twitter_video"


@dataclass(frozen=True)
class PlatformCapabilityView:
    key: str
    label: str
    available: bool
    details: str | None = None


@dataclass(frozen=True)
class PlatformMetricView:
    platform: PlatformKind | str
    metrics: Sequence[DashboardMetric] = field(default_factory=tuple)
    normalized: bool = True


@dataclass(frozen=True)
class PlatformStatusView:
    platform: PlatformKind | str
    status: DashboardStatus
    display_name: str
    capabilities: Sequence[PlatformCapabilityView] = field(default_factory=tuple)
    metrics: Sequence[DashboardMetric] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


def default_platforms() -> tuple[PlatformKind, ...]:
    return (
        PlatformKind.YOUTUBE_SHORTS,
        PlatformKind.TIKTOK,
        PlatformKind.INSTAGRAM_REELS,
        PlatformKind.FACEBOOK_REELS,
        PlatformKind.SNAPCHAT_SPOTLIGHT,
        PlatformKind.X_TWITTER_VIDEO,
    )
