# Platform-Agnostic Rules

AutoShortAI must not be designed for only one network.

## Required architecture pattern

```text
Core → Adapter Contract → Platform Adapter → Provider/API
```

## Core must remain neutral for

- analytics
- distribution
- scheduling
- creative strategies
- rendering formats
- AI workers
- storage
- future device deployment

## First target, not only target

YouTube Shorts is allowed as the first practical target. However, all architecture must remain ready for TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, and future networks.
