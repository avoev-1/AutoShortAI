# NEXT TASK

## Task ID
ZIP01-APPLY-FOUNDATION

## Objective
Apply ZIP01 Production Foundation and validate the first runnable AutoShortAI application.

## Important
ZIP00 is frozen. Do not modify ZIP00 operating system files unless a future task explicitly says so.

## Acceptance Criteria
- `bash scripts/validate_zip01.sh` passes.
- Backend tests pass.
- `docker compose up --build` starts all services.
- `/health` returns OK.
- frontend loads Apple Glass dashboard.
- placeholder plugin list is accessible.

## Validation Commands
```bash
bash scripts/validate_zip01.sh
docker compose up --build
docker compose run --rm backend pytest
```
