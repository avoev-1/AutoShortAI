from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Any

from .models import AspectRatio


class PlatformRenderTarget(str, Enum):
    GENERIC = "generic"
    YOUTUBE_SHORTS = "youtube_shorts"
    TIKTOK = "tiktok"
    INSTAGRAM_REELS = "instagram_reels"
    FACEBOOK_REELS = "facebook_reels"
    SNAPCHAT_SPOTLIGHT = "snapchat_spotlight"
    X_TWITTER_VIDEO = "x_twitter_video"


@dataclass(frozen=True)
class RenderSafeZone:
    top_percent: float = 0.08
    bottom_percent: float = 0.14
    left_percent: float = 0.06
    right_percent: float = 0.06


@dataclass(frozen=True)
class RenderProfile:
    id: str
    target: PlatformRenderTarget | str
    aspect_ratio: AspectRatio
    width: int
    height: int
    fps: int = 30
    codec: str = "h264"
    container: str = "mp4"
    bitrate_kbps: int | None = None
    max_duration_seconds: float | None = None
    safe_zone: RenderSafeZone = field(default_factory=RenderSafeZone)
    metadata: Mapping[str, Any] = field(default_factory=dict)


def default_render_profiles() -> dict[str, RenderProfile]:
    vertical = {
        "aspect_ratio": AspectRatio.VERTICAL_9_16,
        "width": 1080,
        "height": 1920,
        "fps": 30,
        "codec": "h264",
        "container": "mp4",
        "max_duration_seconds": 60.0,
    }
    return {
        "youtube_shorts_9x16": RenderProfile(id="youtube_shorts_9x16", target=PlatformRenderTarget.YOUTUBE_SHORTS, **vertical),
        "tiktok_9x16": RenderProfile(id="tiktok_9x16", target=PlatformRenderTarget.TIKTOK, **vertical),
        "instagram_reels_9x16": RenderProfile(id="instagram_reels_9x16", target=PlatformRenderTarget.INSTAGRAM_REELS, **vertical),
        "facebook_reels_9x16": RenderProfile(id="facebook_reels_9x16", target=PlatformRenderTarget.FACEBOOK_REELS, **vertical),
        "snapchat_spotlight_9x16": RenderProfile(id="snapchat_spotlight_9x16", target=PlatformRenderTarget.SNAPCHAT_SPOTLIGHT, **vertical),
        "x_twitter_video": RenderProfile(id="x_twitter_video", target=PlatformRenderTarget.X_TWITTER_VIDEO, aspect_ratio=AspectRatio.VERTICAL_9_16, width=1080, height=1920, fps=30),
        "generic_vertical_video": RenderProfile(id="generic_vertical_video", target=PlatformRenderTarget.GENERIC, aspect_ratio=AspectRatio.VERTICAL_9_16, width=1080, height=1920, fps=30),
        "generic_square_video": RenderProfile(id="generic_square_video", target=PlatformRenderTarget.GENERIC, aspect_ratio=AspectRatio.SQUARE_1_1, width=1080, height=1080, fps=30),
        "generic_landscape_video": RenderProfile(id="generic_landscape_video", target=PlatformRenderTarget.GENERIC, aspect_ratio=AspectRatio.LANDSCAPE_16_9, width=1920, height=1080, fps=30),
    }
