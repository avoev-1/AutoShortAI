# Timeline Engine Contracts

The timeline engine represents a video as scenes, tracks, clips, overlays, subtitles, and audio.

The model is renderer-neutral. A timeline should be convertible later to FFmpeg commands, MoviePy objects, OpenCV operations, a native renderer plan, or an external provider request.

Core concepts:

- VideoTimeline
- TimelineScene
- VideoTrack
- VideoClip
- AudioClip
- TextOverlay
- SubtitleTrack
- TransitionSpec
