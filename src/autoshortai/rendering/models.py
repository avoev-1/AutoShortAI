from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class AspectRatio(str, Enum):
    VERTICAL_9_16 = "9:16"
    SQUARE_1_1 = "1:1"
    LANDSCAPE_16_9 = "16:9"
    CUSTOM = "custom"


class RenderMode(str, Enum):
    DRAFT = "draft"
    FINAL = "final"


class TrackType(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"
    OVERLAY = "overlay"


class ClipType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    TEXT = "text"
    GENERATED = "generated"


@dataclass(frozen=True)
class TimeRange:
    start_seconds: float
    duration_seconds: float

    @property
    def end_seconds(self) -> float:
        return self.start_seconds + self.duration_seconds


@dataclass(frozen=True)
class VideoClip:
    id: str
    clip_type: ClipType
    time_range: TimeRange
    asset_ref: str | None = None
    text: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class VideoTrack:
    id: str
    track_type: TrackType
    clips: Sequence[VideoClip] = field(default_factory=tuple)
    enabled: bool = True


@dataclass(frozen=True)
class TimelineScene:
    id: str
    label: str
    time_range: TimeRange
    purpose: str | None = None


@dataclass(frozen=True)
class VideoTimeline:
    id: str
    duration_seconds: float
    scenes: Sequence[TimelineScene] = field(default_factory=tuple)
    tracks: Sequence[VideoTrack] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class VideoProject:
    id: str
    title: str
    timeline: VideoTimeline
    render_profile_id: str
    template_id: str | None = None
    source_strategy_ref: str | None = None
    source_job_ref: str | None = None


@dataclass(frozen=True)
class RenderJob:
    id: str
    project: VideoProject
    mode: RenderMode = RenderMode.DRAFT
    priority: str = "normal"
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RenderOutput:
    path: str
    media_type: str = "video/mp4"
    checksum: str | None = None
    size_bytes: int | None = None


@dataclass(frozen=True)
class RenderResult:
    job_id: str
    success: bool
    outputs: Sequence[RenderOutput] = field(default_factory=tuple)
    message: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
