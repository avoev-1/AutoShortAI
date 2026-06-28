# NEXT TASK

## Task ID
ZIP02-APPLY-CORE-ENGINE

## Objective
Apply ZIP02 Core Engine and validate modular architecture.

## Acceptance Criteria
- `bash scripts/validate_zip02.sh` passes.
- Backend tests pass.
- `/api/v1/core/workflow/default` returns the workflow.
- `/api/v1/core/plan/demo` returns planned steps.

## Validation Commands
```bash
bash scripts/validate_zip02.sh
docker compose run --rm backend pytest
```
