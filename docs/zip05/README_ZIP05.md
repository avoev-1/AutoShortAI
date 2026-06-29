# AutoShortAI ZIP05 — Intelligent Distribution Platform

ZIP05 upgrades AutoShortAI from a video production system into a multi-platform distribution platform.

The goal is not to build a YouTube-only uploader. The goal is to create once, adapt automatically, publish everywhere, collect analytics, and learn from results.

## Scope

ZIP05 introduces:

- Multi-platform publishing engine
- Campaign-based distribution model
- Publisher plugin architecture
- Metadata and format adaptation layer
- Scheduling and queue management
- Unified analytics contracts
- Rules engine for automation decisions
- AI strategy integration points
- Device Fleet Manager for racks, phones, mini-PCs, servers, VMs and edge devices
- Remote manager architecture for Windows, Linux, macOS, web, Android and iOS companions
- Notification Center
- Guardian Engine integration points
- Safety and platform-compliance boundaries

## Core principle

No platform-specific logic belongs in the Core.

Platforms must be implemented as plugins:

- YouTube Shorts
- TikTok
- Instagram Reels
- Facebook Reels
- Snapchat Spotlight
- Pinterest
- X / Twitter
- LinkedIn
- Threads
- Bluesky
- Rumble
- Future platforms

## Installation

From the extracted ZIP folder:

```bash
chmod +x INSTALL.sh VERIFY.sh
./INSTALL.sh /path/to/AutoShortAI
./VERIFY.sh /path/to/AutoShortAI
```

If no path is provided, scripts use the current directory.

## Expected result

The project receives documentation, templates and scaffold files for ZIP05 without breaking the existing ZIP00-ZIP04 architecture.
