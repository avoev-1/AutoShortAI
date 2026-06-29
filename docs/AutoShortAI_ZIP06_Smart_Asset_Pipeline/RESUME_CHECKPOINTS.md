# Resume Engine and Checkpoint System

The Resume Engine allows interrupted workflows to continue safely. The Checkpoint System records progress at stable boundaries.

## Checkpoint responsibilities

- Record pipeline ID and step ID.
- Record asset IDs involved in the step.
- Record checkpoint state.
- Store enough metadata for diagnostics.
- Remain independent from a specific database.

## Resume responsibilities

- Determine whether a workflow can resume.
- Validate that expected assets still exist.
- Validate fingerprints and integrity before reusing outputs.
- Return a safe resume plan.

## Future implementation guidance

Use JSON checkpoint records first. Add database-backed checkpoints only if a later ZIP requires it.
