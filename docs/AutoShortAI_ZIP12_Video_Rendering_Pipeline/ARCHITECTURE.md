# ZIP12 Architecture — Video Rendering Pipeline

## Purpose

ZIP12 defines the video rendering architecture for AutoShortAI.

It creates a clean boundary between:

1. creative intent from ZIP07,
2. assets and cache from ZIP06,
3. production jobs from ZIP08,
4. rendering profiles and timelines from ZIP12,
5. distribution from ZIP05 / future publishing runtime,
6. analytics from ZIP09,
7. learning from ZIP10,
8. dashboard monitoring from ZIP11.

## Rendering Pipeline Overview

```text
Creative Strategy / Script Blueprint
        ↓
Asset Selection / Registry / Cache
        ↓
Video Project
        ↓
Timeline Plan
        ↓
Visual Template
        ↓
Audio + Subtitle Composition
        ↓
Draft Render or Final Render
        ↓
Export Manifest
        ↓
Distribution / Analytics / Learning
```

## Core Boundaries

The rendering core defines render plans and contracts. It must not directly own:

- idea generation
- platform analytics
- publishing account logic
- API credential storage
- dashboard UI
- device farm deployment
- Guardian validation

## Timeline Model

A renderable video is represented as a timeline composed of:

- scenes
- tracks
- clips
- overlays
- subtitles
- audio clips
- transitions
- export metadata

The timeline is intentionally abstract so that a future implementation can target FFmpeg, MoviePy, OpenCV, a native renderer, or an external provider without changing the core contracts.

## Multi-Platform Render Profiles

Render profiles describe output constraints for each target platform or generic format.

The core must use normalized profile contracts rather than hard-coded platform logic.

Examples:

- YouTube Shorts vertical 9:16
- TikTok vertical 9:16
- Instagram Reels vertical 9:16
- Facebook Reels vertical 9:16
- Snapchat Spotlight vertical 9:16
- X/Twitter video
- generic vertical video
- generic square video
- generic landscape video

## Draft and Final Render Modes

ZIP12 separates quick previews from final exports.

- **Draft render:** fast, lower quality, lightweight preview.
- **Final render:** platform-ready output with full export settings.

This preserves CPU/RAM and fits ZIP08 resource budgeting.

## Subtitle and Caption Layer

ZIP12 defines contracts for:

- subtitle segments
- word timing
- burned-in captions
- SRT export
- VTT export
- JSON timing export
- caption styles
- platform safe zones

## Audio Layer

ZIP12 defines contracts for:

- voiceover track
- music track
- sound effects
- ducking
- normalization
- fade in / fade out
- timing alignment

## Worker Boundary

Workers are interfaces, not hard-coded implementations.

Reserved worker types:

- RenderWorker
- TimelineWorker
- SubtitleWorker
- AudioMixWorker
- ExportWorker
- ThumbnailWorker
- PreviewWorker

Future implementations may plug in FFmpeg, MoviePy, OpenCV, or other providers.

## Integration With ZIP06

Rendering must use ZIP06 asset concepts:

- asset registry
- fingerprint engine
- dependency graph
- incremental build
- cache manager
- resume engine
- checkpoint system
- integrity checker
- storage manager
- provider abstraction
- API cost optimizer
- performance profiler

## Integration With ZIP08

Rendering must respect ZIP08 scheduling and resource contracts:

- job priority
- CPU/RAM limits
- worker limits
- retry policy
- pause/resume
- failure handling
- queue persistence

## Integration With ZIP11

ZIP11 dashboard should be able to display:

- render jobs
- current render stage
- draft/final mode
- render progress
- resource usage
- failed renders
- generated exports

ZIP12 provides view-safe render status models for this future integration.

## Compatibility

ZIP12 is additive. It must not rename or remove previous module namespaces.

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The whole software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- Rendering profiles must support future platforms through contracts, adapters, and capability metadata.
- The rendering core must not know or hard-code one platform.
- The rendering pipeline must remain modular, lightweight, resumable, and compatible with previous ZIP releases.
- No mandatory FFmpeg, MoviePy, cloud renderer, database, or heavy UI dependency is introduced in ZIP12.
- ZIP12 must remain compatible with ZIP01 through ZIP11.
