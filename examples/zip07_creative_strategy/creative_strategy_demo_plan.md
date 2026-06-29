# Creative Strategy Demo Plan

This example shows how ZIP07 should be used later without breaking previous ZIPs.

1. A user or scheduler creates a `StrategyRequest`.
2. ZIP07 resolves `youtube_shorts_default`.
3. ZIP07 creates an idea blueprint and script blueprint.
4. ZIP07 creates three variants.
5. ZIP07 validates lightweight rules.
6. ZIP07 returns a `CreativeStrategyPlan`.
7. ZIP04 turns the plan into a mission.
8. ZIP06 prepares required assets.
9. ZIP05 handles platform distribution logic.

No upload, rendering, or paid API call is performed by ZIP07 itself.
