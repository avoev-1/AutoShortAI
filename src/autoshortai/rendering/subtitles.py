from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence, Any

from .models import TimeRange


class SubtitleExportFormat(str, Enum):
    BURNED_IN = "burned_in"
    SRT = "srt"
    VTT = "vtt"
    JSON_TIMING = "json_timing"


@dataclass(frozen=True)
class WordTiming:
    word: str
    time_range: TimeRange


@dataclass(frozen=True)
class SubtitleSegment:
    id: str
    text: str
    time_range: TimeRange
    words: Sequence[WordTiming] = field(default_factory=tuple)


@dataclass(frozen=True)
class CaptionStyle:
    id: str
    font_family: str = "system"
    font_size: int = 48
    position: str = "bottom_safe"
    max_lines: int = 2
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SubtitleTrack:
    id: str
    segments: Sequence[SubtitleSegment] = field(default_factory=tuple)
    style: CaptionStyle = field(default_factory=lambda: CaptionStyle(id="default"))
    export_formats: Sequence[SubtitleExportFormat] = (SubtitleExportFormat.BURNED_IN,)
