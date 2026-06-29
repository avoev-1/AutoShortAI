# Platform Metrics Adapter Layer

The Platform Metrics Adapter Layer isolates platform-specific data retrieval from the analytics core.

## Rule

The analytics core depends on `PlatformMetricsAdapter`, never on a concrete platform API.

## Adapter examples

- `YouTubeMetricsAdapter`
- `TikTokMetricsAdapter`
- `InstagramMetricsAdapter`
- `FacebookReelsMetricsAdapter`
- `SnapchatSpotlightMetricsAdapter`
- `XVideoMetricsAdapter`
- `GenericPlatformMetricsAdapter`

These names are architectural placeholders. ZIP09 does not implement real API calls.

## Adapter responsibilities

- Declare supported platform
- Declare supported metrics
- Convert platform-native metrics into normalized metrics
- Report unsupported metrics explicitly
- Respect rate and cost limits defined by future providers
