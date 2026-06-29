# Platform-Agnostic Dashboard

ZIP11 keeps the dashboard independent from any single platform.

YouTube Shorts is the first target, but the dashboard must also support future platforms through adapters:

- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- X/Twitter video
- future networks

## Required Contracts

- PlatformDashboardAdapter
- PlatformStatusView
- PlatformMetricView
- PlatformCapabilityView

## Rule

No dashboard core module should import a platform-specific implementation directly.
