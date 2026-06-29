from __future__ import annotations

from .models import TimeRange, TimelineScene, VideoTimeline, VideoTrack


def basic_short_timeline(timeline_id: str = "timeline.short.default", duration_seconds: float = 35.0) -> VideoTimeline:
    scenes = (
        TimelineScene(id="scene.hook", label="Hook", time_range=TimeRange(0, 3), purpose="capture_attention"),
        TimelineScene(id="scene.context", label="Context", time_range=TimeRange(3, 7), purpose="establish_context"),
        TimelineScene(id="scene.value", label="Value", time_range=TimeRange(10, 17), purpose="deliver_value"),
        TimelineScene(id="scene.punch", label="Punch", time_range=TimeRange(27, 8), purpose="final_twist_or_cta"),
    )
    return VideoTimeline(
        id=timeline_id,
        duration_seconds=duration_seconds,
        scenes=scenes,
        tracks=(
            VideoTrack(id="track.video.main", track_type="video"),
            VideoTrack(id="track.audio.voiceover", track_type="audio"),
            VideoTrack(id="track.subtitle.main", track_type="subtitle"),
        ),
    )
