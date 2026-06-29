# Normalized Metrics Model

ZIP09 defines canonical metric names so multiple networks can be compared without making the core YouTube-specific.

## Canonical metrics

- views
- likes
- comments
- shares
- saves
- subscribers_gained
- watch_time_seconds
- average_view_duration_seconds
- retention_rate
- completion_rate
- click_through_rate
- engagement_rate
- impression_count
- cost_units

## Platform-specific metrics

Adapters may expose platform-specific extras as `additional_metrics`, but core scoring should only rely on canonical metrics unless a score policy explicitly supports the platform-specific metric.

## Time windows

Recommended initial windows:

- 1h
- 6h
- 24h
- 7d
- 28d
- lifetime
