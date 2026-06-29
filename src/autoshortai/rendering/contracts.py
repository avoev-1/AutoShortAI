from __future__ import annotations

from typing import Protocol, Sequence

from .exports import ExportManifest
from .models import RenderJob, RenderResult, VideoProject, VideoTimeline
from .profiles import RenderProfile


class RenderProfileRegistry(Protocol):
    def list_profiles(self) -> Sequence[RenderProfile]:
        ...

    def get_profile(self, profile_id: str) -> RenderProfile:
        ...


class TimelineBuilder(Protocol):
    def build(self, project: VideoProject) -> VideoTimeline:
        ...


class RenderingProvider(Protocol):
    def provider_id(self) -> str:
        ...

    def supports_profile(self, profile: RenderProfile) -> bool:
        ...

    def render(self, job: RenderJob) -> RenderResult:
        ...


class ExportManifestStore(Protocol):
    def save_manifest(self, manifest: ExportManifest) -> None:
        ...
