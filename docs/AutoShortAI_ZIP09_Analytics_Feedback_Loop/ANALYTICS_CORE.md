# Analytics Core

The Analytics Core is responsible for receiving normalized performance snapshots and preparing them for scoring, reporting, and feedback generation.

## Responsibilities

- Accept normalized metrics from adapters
- Preserve metric source metadata
- Group metrics by content, platform, and time window
- Provide a stable contract for performance scoring
- Stay independent from platform-specific APIs

## Non-responsibilities

- Calling platform APIs directly
- Performing automatic learning
- Updating creative profiles
- Managing production jobs
- Rendering videos

## Core objects

- `ContentPerformance`
- `PerformanceSnapshot`
- `PlatformPerformance`
- `MetricValue`
- `MetricTimeWindow`
- `AnalyticsContext`
