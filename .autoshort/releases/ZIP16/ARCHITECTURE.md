# ZIP16 Architecture — Multi-Platform Publishing Runtime

## Purpose

ZIP16 defines the architecture that turns a rendered video and its metadata into a validated publishing request for one or more platforms.

The Publishing Runtime must answer:

```text
What platform is targeted?
What account/channel is targeted?
Does the rendered media match platform requirements?
Are metadata fields valid for that platform?
Is manual review required?
Is the platform restricted or adult-only?
Is publishing immediate or scheduled?
What happens if upload fails?
How do analytics and learning receive publication results later?
```

## High-Level Runtime Flow

```text
Video Rendering Pipeline (ZIP12)
        ↓
Publishing Request
        ↓
Metadata Builder
        ↓
Platform Capability Validation
        ↓
Manual Review Gate
        ↓
Platform Publishing Adapter
        ↓
Publishing Result
        ↓
Analytics Feedback Loop (ZIP09)
```

## Core Rule

The core publishing runtime never talks directly to a platform API.

It talks to `PlatformPublishingAdapter` contracts.

This protects AutoShortAI from platform lock-in and keeps the project ready for future networks.

## Core Contracts

- `PublishingRuntime`
- `PublishingJob`
- `PublishingRequest`
- `PublishingResult`
- `PublishingStatus`
- `PublishingTarget`
- `PublishingContext`
- `PublishingSchedule`
- `PublishingError`
- `PublishingRetryPolicy`

## Platform Adapter Layer

Adapters are responsible for platform-specific details.

Planned adapter types:

- `YouTubePublishingAdapter`
- `TikTokPublishingAdapter`
- `InstagramPublishingAdapter`
- `FacebookReelsPublishingAdapter`
- `SnapchatSpotlightPublishingAdapter`
- `XTwitterVideoPublishingAdapter`
- `GenericPlatformPublishingAdapter`
- `AdultPlatformPublishingAdapter` for restricted opt-in creator platforms

The runtime must be able to add or remove adapters without changing the core.

## Platform Capability Contracts

Each platform may define:

- accepted aspect ratios
- maximum duration
- maximum file size
- supported codecs
- title length
- description length
- hashtag limits
- thumbnail support
- scheduled publishing support
- privacy levels
- age restriction capabilities
- adult-content restrictions

Contracts:

- `PlatformCapability`
- `PlatformLimit`
- `PlatformRequirement`
- `PlatformMediaRequirement`
- `PlatformPublishingRule`

## Account and Channel Targeting

ZIP16 prepares multi-account publishing.

Contracts:

- `PlatformAccount`
- `PublishingChannel`
- `AccountBinding`
- `ChannelProfile`
- `AccountHealth`
- `PublishingPermission`

Examples:

- main YouTube channel
- TikTok test account
- Instagram Reels brand account
- restricted adult creator account
- future account groups

## Scheduled Publishing

ZIP16 connects to ZIP08 scheduling concepts.

Supported architecture:

- immediate publishing
- scheduled publishing
- platform-specific cadence
- retry windows
- pause / resume publishing
- blackout dates
- manual hold

Contracts:

- `PublishingSchedule`
- `PublishingWindow`
- `PublishingCadence`
- `ScheduledPublishingJob`

## Metadata Builder

Metadata must be normalized before it becomes platform-specific.

Fields:

- title
- description
- hashtags
- caption
- tags
- language
- category
- audience
- maturity rating
- disclaimer
- platform overrides

Metadata can be informed by ZIP07 strategy, ZIP09 analytics, ZIP10 learning, and ZIP13 AI workers.

## Manual Review Gate

Manual review is a first-class part of publishing.

The first real implementation should require review by default for publishing actions.

Review checks:

- media file exists
- metadata is valid
- platform target is correct
- account/channel target is correct
- content rating is correct
- restricted workflows have consent and age-gate metadata
- no secrets or credentials are exposed

Contracts:

- `ReviewGate`
- `PublishingApproval`
- `ApprovalStatus`
- `ManualReviewRequired`
- `PublishingBlockReason`

## Adult / X Creator Platform Readiness

ZIP16 includes a dedicated restricted category for adult creator workflows because AutoShortAI must support all platform categories later, including 18+ creator platforms.

This support is architectural and opt-in. It must never become the default behavior.

Dedicated contracts:

- `AdultCreatorPublishingContext`
- `RestrictedPublishingProfile`
- `AgeGatedPublishingFlow`
- `RestrictedAccountBinding`
- `AdultPlatformPublishingAdapter`
- `RestrictedPublishingReviewChecklist`

Mandatory guardrails:

- mode disabled by default
- adult platform accounts isolated from general accounts
- credentials isolated
- restricted assets isolated
- restricted logs sanitized
- maturity rating required
- age gate required
- all participants 18+ required
- consent metadata required
- manual review required by default
- no illegal content
- no non-consensual content
- no content involving minors
- no dangerous automatic publishing

## Guardian Integration

ZIP15 Guardian must verify:

- publishing core remains platform-agnostic
- adapters remain separate
- no hard-coded platform API in the core
- no platform bypass or spam behavior
- no adult restricted workflow enabled by default
- no credential leakage
- no deletion of previous ZIP contracts
- manual review gates remain present for restricted publishing

## Publishing Error Handling

Publishing failures must be normalized.

Error categories:

- invalid media format
- metadata rejected
- credential expired
- account restricted
- rate limited
- platform rejected
- network timeout
- manual review blocked
- policy violation
- restricted compliance missing

Contracts:

- `PublishingError`
- `PublishingRetryPolicy`
- `PublishingFailureReason`
- `PublishingRecoveryAction`

## Hooks

Plugin-first publishing hooks:

```text
before_publishing_job_created
after_publishing_job_created
before_platform_selected
after_platform_selected
before_metadata_built
after_metadata_built
before_capability_validation
after_capability_validation
before_review_gate
after_review_gate
before_publish
after_publish
after_publish_failed
after_publish_scheduled
```

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The complete software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian Engine rules from ZIP15 must be used as an implementation checklist before and after future work.
- Adult / X creator workflows are dedicated opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
