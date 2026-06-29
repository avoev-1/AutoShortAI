from __future__ import annotations

from typing import Protocol

from .models import RenderJob, RenderResult, VideoProject, VideoTimeline
from .subtitles import SubtitleTrack
from .audio import AudioMixPolicy
from .exports import ExportManifest


class TimelineWorker(Protocol):
    def build_timeline(self, project: VideoProject) -> VideoTimeline:
        ...


class SubtitleWorker(Protocol):
    def prepare_subtitles(self, project: VideoProject) -> SubtitleTrack:
        ...


class AudioMixWorker(Protocol):
    def prepare_audio_mix(self, project: VideoProject) -> AudioMixPolicy:
        ...


class RenderWorker(Protocol):
    def render(self, job: RenderJob) -> RenderResult:
        ...


class ExportWorker(Protocol):
    def create_manifest(self, result: RenderResult) -> ExportManifest:
        ...


class ThumbnailWorker(Protocol):
    def create_thumbnail(self, project: VideoProject) -> str:
        ...


class PreviewWorker(Protocol):
    def create_preview(self, project: VideoProject) -> RenderResult:
        ...
