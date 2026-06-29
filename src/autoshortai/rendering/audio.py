from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Any

from .models import TimeRange


class AudioRole(str, Enum):
    VOICEOVER = "voiceover"
    MUSIC = "music"
    SFX = "sfx"
    AMBIENCE = "ambience"


@dataclass(frozen=True)
class AudioClipSpec:
    id: str
    role: AudioRole
    time_range: TimeRange
    asset_ref: str | None = None
    volume: float = 1.0
    fade_in_seconds: float = 0.0
    fade_out_seconds: float = 0.0
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AudioMixPolicy:
    normalize: bool = True
    duck_music_under_voice: bool = True
    target_lufs: float | None = -14.0
    metadata: Mapping[str, Any] = field(default_factory=dict)
