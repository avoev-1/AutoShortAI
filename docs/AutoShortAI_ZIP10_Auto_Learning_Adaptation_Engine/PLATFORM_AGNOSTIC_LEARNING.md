# Platform-Agnostic Learning

ZIP10 must not optimize only for YouTube.

The learning layer must support:

- cross-platform insights,
- platform-specific insights,
- generic platform capabilities,
- future adapters.

Example:

```text
A hook pattern may work on TikTok but fail on YouTube Shorts.
A duration pattern may work on Instagram Reels but fail on X/Twitter video.
```

The core records this distinction without coupling itself to a hardcoded platform implementation.
