# ZIP05 Roadmap

## Phase 1 — Structural Foundation

- Create Distribution Platform directories
- Define campaign schema
- Define publisher plugin interface
- Define platform capability manifest
- Define basic queue and scheduler contracts
- Add documentation and verification scripts

## Phase 2 — Local Simulation

- Add fake publisher plugin
- Simulate publishing workflow
- Simulate campaign state changes
- Simulate retries and failures
- Validate metadata adaptation contracts

## Phase 3 — Real Platform Plugins

Priority order can change, but the architecture must stay platform-agnostic:

1. YouTube Shorts
2. TikTok
3. Instagram Reels
4. Facebook Reels
5. Snapchat Spotlight
6. Pinterest
7. X / Twitter
8. LinkedIn
9. Threads / Bluesky / Rumble as later plugins

## Phase 4 — Device Fleet Manager

- Device registry
- Heartbeat system
- Rack/group model
- Task assignment model
- Device health dashboard contract
- Android-first deployment support
- iOS companion support within OS restrictions

## Phase 5 — Intelligence Layer

- AI strategy interface
- Automated platform choice
- Automated schedule selection
- A/B metadata variants
- Performance-based republishing
- Revenue-oriented campaign decisions

## Phase 6 — Guardian Integration

- Plugin validation
- Campaign validation
- Regression checks
- Architecture boundary checks
- Safety audit hooks
