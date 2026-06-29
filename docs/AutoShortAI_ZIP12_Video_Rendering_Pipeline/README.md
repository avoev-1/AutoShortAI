# AutoShortAI ZIP12 — Video Rendering Pipeline

ZIP12 defines the architecture for transforming creative strategy, scripts, assets, audio, subtitles, and production jobs into exportable video render plans and render outputs.

This ZIP does **not** implement a full production renderer. It defines the contracts, models, render profiles, timeline structures, template boundaries, hooks, and verification tests that Claude must later follow when implementing the real rendering runtime.

## What ZIP12 Adds

- Rendering Core
- Timeline Engine Contracts
- Video Project / Scene / Track / Clip Models
- Visual Template Rendering Contracts
- Multi-Platform Render Profiles
- Subtitle and Caption Contracts
- Audio Layer Contracts
- Render Worker Contracts
- Draft vs Final Render Modes
- Export Manifest Models
- Resource and Checkpoint Integration Contracts
- Rendering Hooks
- Structure tests and examples

## Why ZIP12 Exists

Previous ZIPs define strategy, assets, scheduling, analytics, learning, and dashboard control.

ZIP12 defines how AutoShortAI will eventually create real videos from those inputs while preserving the project philosophy:

- modular
- plugin-first
- platform-agnostic
- lightweight
- local-first
- resumable
- cache-aware
- maintainable for years

## Platform Strategy

ZIP12 is not YouTube-only. YouTube Shorts is the first target, but render profiles must support TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, and future networks.

ZIP12 introduces normalized render profiles such as:

- youtube_shorts_9x16
- tiktok_9x16
- instagram_reels_9x16
- facebook_reels_9x16
- snapchat_spotlight_9x16
- x_twitter_video
- generic_vertical_video
- generic_square_video
- generic_landscape_video

## Integration With Existing ZIPs

- ZIP06 supplies assets, fingerprints, cache, storage, integrity checks, provider costs, and checkpoints.
- ZIP07 supplies creative strategies, content profiles, and script blueprints.
- ZIP08 schedules render jobs and controls resource budgets.
- ZIP09 measures content performance after publication.
- ZIP10 adapts future strategy based on feedback.
- ZIP11 visualizes rendering state and controls render actions through dashboard contracts.

## Non-Goals

- no complete renderer implementation
- no mandatory FFmpeg dependency
- no mandatory MoviePy dependency
- no mandatory OpenCV dependency
- no cloud rendering requirement
- no platform-specific hard-coding
- no full AI worker runtime
- no dashboard UI implementation
- no Guardian Engine implementation
- no phone farm implementation
- no SaaS conversion
- no mandatory database

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains a personal/local automation software first.
- The whole software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- Rendering profiles must support future platforms through contracts, adapters, and capability metadata.
- The rendering core must not know or hard-code one platform.
- The rendering pipeline must remain modular, lightweight, resumable, and compatible with previous ZIP releases.
- No mandatory FFmpeg, MoviePy, cloud renderer, database, or heavy UI dependency is introduced in ZIP12.
- ZIP12 must remain compatible with ZIP01 through ZIP11.
