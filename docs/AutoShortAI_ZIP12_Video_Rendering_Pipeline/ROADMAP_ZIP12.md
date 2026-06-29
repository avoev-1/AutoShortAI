# ROADMAP ZIP12 — Video Rendering Pipeline

## Phase 1 — Architecture Contracts

- Define render models.
- Define timeline contracts.
- Define subtitle and caption contracts.
- Define audio layer contracts.
- Define render profile contracts.
- Define worker interfaces.
- Define export manifests.

## Phase 2 — Draft Renderer Prototype

- Implement a lightweight draft render path later.
- Use low-resolution preview settings.
- Respect ZIP08 resource budgets.
- Reuse ZIP06 cache and checkpoints.

## Phase 3 — Final Renderer Provider

- Add a real rendering provider later.
- FFmpeg can be the first provider, but must not be mandatory in the core.
- Keep provider replacement possible.

## Phase 4 — Multi-Platform Output

- Add platform-specific render profile presets.
- Maintain normalized profile contracts.
- Keep YouTube Shorts as the first target, not the only target.

## Phase 5 — Dashboard and Analytics Integration

- Expose render progress to ZIP11.
- Feed export metadata into ZIP09.
- Allow ZIP10 to learn from format and render-profile performance.

## Done Criteria

ZIP12 is complete when future implementations can build draft previews and final video exports without coupling the core to one renderer, one platform, one UI, or one cloud provider.
