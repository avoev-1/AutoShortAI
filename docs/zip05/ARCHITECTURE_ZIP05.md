# ZIP05 Architecture — Intelligent Distribution Platform

## 1. Distribution Platform Overview

ZIP05 is built around campaigns, not isolated uploads.

A campaign defines:

- source video asset
- target platforms
- target accounts
- publish schedule
- metadata variants
- platform-specific adaptations
- A/B testing configuration
- analytics objectives
- automation rules
- safety limits

## 2. High-level modules

```text
Intelligent Distribution Platform
├── Campaign Manager
├── AI Strategy Engine Interface
├── Queue Manager
├── Scheduler
├── Metadata Engine
├── Format Adaptation Engine
├── Upload Engine
├── Publisher Plugin SDK
├── Unified Analytics Collector
├── Rules Engine
├── Account Manager
├── Device Fleet Manager
├── Remote Manager
├── Notification Center
└── Guardian Integration Layer
```

## 3. Campaign Manager

The Campaign Manager is the main abstraction. It converts one produced asset into one or more distribution jobs.

It should support:

- one video to many platforms
- one video to many accounts
- delayed publication
- staggered publication
- retry policies
- per-platform metadata
- campaign state tracking

Campaign states:

```text
DRAFT -> READY -> QUEUED -> RUNNING -> PARTIAL_SUCCESS -> COMPLETED -> FAILED -> ARCHIVED
```

## 4. Publisher Plugin SDK

The Core never knows platform-specific upload details. Each platform plugin must implement a stable interface:

```text
validate_account()
validate_asset()
adapt_metadata()
publish()
get_status()
collect_analytics()
refresh_auth()
```

Plugins must declare their capabilities:

- max duration
- max file size
- supported codecs
- metadata limits
- thumbnail support
- scheduling support
- analytics support
- API quota limits

## 5. Metadata and Format Adaptation

For each destination, the system may adapt:

- title
- description
- hashtags
- tags
- captions
- subtitle files
- thumbnail
- aspect ratio
- resolution
- bitrate
- codec
- duration
- file size

## 6. AI Strategy Engine Interface

The strategy layer decides how to distribute content.

Examples:

- prioritize TikTok first for fast trend testing
- delay YouTube Shorts until a stronger title is generated
- skip platforms where the account is unhealthy
- create A/B metadata variants
- republish a high-performing video with a new hook

The AI Strategy Engine is an interface at ZIP05 level. Heavy optimization logic can arrive in later ZIPs.

## 7. Rules Engine

Rules are deterministic constraints applied before and during execution.

Examples:

- never post twice on the same account within 4 hours
- retry failed uploads after 20 minutes
- stop a campaign if account health becomes unsafe
- publish to Instagram only if TikTok exceeds a threshold
- create a follow-up campaign if a video becomes viral

## 8. Unified Analytics

Analytics must normalize performance across platforms:

- views
- impressions
- watch time
- average view duration
- retention
- likes
- comments
- shares
- saves
- CTR
- followers gained
- revenue
- RPM / CPM when available

## 9. Device Fleet Manager

The Device Fleet Manager is for legitimate administration and deployment of content workflows across devices.

Supported device classes:

- Android phones and tablets
- iOS devices within OS limits
- Windows PCs
- Linux PCs
- macOS machines
- Raspberry Pi / edge devices
- mini-PCs
- servers
- virtual machines
- phone racks

It tracks:

- online/offline status
- OS
- battery
- storage
- temperature where available
- network state
- assigned tasks
- last heartbeat
- error state

It must not be used to fake engagement or bypass platform rules.

## 10. Cross-platform target

The Core must stay portable across:

- Windows
- Linux
- macOS

Mobile clients are companion controllers, not required Core runtimes:

- Android companion app
- iOS companion app
- web dashboard

## 11. Guardian Integration

ZIP05 exposes hooks for the later Guardian Engine:

- validate plugin manifests
- validate campaigns before execution
- detect unsafe platform-specific logic leaking into Core
- run regression checks
- inspect rules before activation
- audit campaign outcomes
