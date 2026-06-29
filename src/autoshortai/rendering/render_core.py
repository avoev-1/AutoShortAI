from __future__ import annotations

from dataclasses import dataclass, field

from .errors import RenderProfileError
from .models import RenderJob, RenderOutput, RenderResult
from .profiles import RenderProfile, default_render_profiles


@dataclass
class RenderingCore:
    profiles: dict[str, RenderProfile] = field(default_factory=default_render_profiles)

    def get_profile(self, profile_id: str) -> RenderProfile:
        try:
            return self.profiles[profile_id]
        except KeyError as exc:
            raise RenderProfileError(f"Unknown render profile: {profile_id}") from exc

    def validate_job(self, job: RenderJob) -> None:
        profile = self.get_profile(job.project.render_profile_id)
        if profile.max_duration_seconds is not None:
            duration = job.project.timeline.duration_seconds
            if duration > profile.max_duration_seconds:
                raise RenderProfileError(
                    f"Timeline duration {duration}s exceeds profile maximum {profile.max_duration_seconds}s"
                )

    def plan_only_render(self, job: RenderJob) -> RenderResult:
        """Architecture placeholder: validates and returns a planned output without rendering media."""
        self.validate_job(job)
        return RenderResult(
            job_id=job.id,
            success=True,
            outputs=(RenderOutput(path=f"planned://{job.project.id}/{job.mode.value}.mp4"),),
            message="ZIP12 plan-only render placeholder; real rendering provider comes later.",
        )
