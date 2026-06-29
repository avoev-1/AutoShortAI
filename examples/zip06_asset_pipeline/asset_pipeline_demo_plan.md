# ZIP06 Minimal Asset Flow Demo Plan

This example describes a future implementation flow. It is not executable business logic.

1. Register a script asset.
2. Compute a fingerprint for the script payload.
3. Add dependencies from script to voiceover and render assets.
4. Ask the incremental build planner whether render output is stale.
5. Check cache before rebuilding.
6. Save output through the storage manager.
7. Verify integrity.
8. Create a checkpoint.
9. Record a performance sample.
10. Record estimated provider cost if an external provider was used.

The future implementation must keep each step behind ZIP06 contracts.
