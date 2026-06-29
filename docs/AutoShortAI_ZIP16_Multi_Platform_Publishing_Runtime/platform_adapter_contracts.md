# Platform Adapter Contracts

A platform adapter must expose:

- platform identifier
- supported capabilities
- validation routine
- publish routine
- schedule routine if supported
- status refresh routine if supported

Adapters must not modify core models directly. They return normalized results.

The adapter layer allows future support for YouTube Shorts, TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video, adult creator platforms, and future networks without rewriting the core.
