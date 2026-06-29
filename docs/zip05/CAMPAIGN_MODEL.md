# Campaign Model

A campaign is the unit of distribution.

## Minimal campaign fields

```yaml
campaign_id: string
name: string
source_asset: path
status: draft|ready|queued|running|partial_success|completed|failed|archived
goal: views|followers|revenue|testing|brand_distribution
targets:
  - platform: youtube
    accounts: [main_channel]
  - platform: tiktok
    accounts: [main_account]
schedule:
  mode: immediate|scheduled|staggered|strategy_driven
metadata:
  title: string
  description: string
  hashtags: []
rules: []
analytics_objectives: []
```

## Important principle

The campaign describes intent. Publisher plugins execute platform-specific actions.
