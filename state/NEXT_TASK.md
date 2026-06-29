# NEXT TASK

## Task ID
ZIP03-APPLY-SDK-PLUGIN-SYSTEM

## Objective
Apply ZIP03 SDK & Plugin System.

## Acceptance Criteria
- `bash scripts/validate_zip03.sh` passes.
- Backend tests pass.
- `/api/v1/sdk/status` returns SDK status.
- `/api/v1/sdk/plugins` lists builtin plugin manifests.

## Validation Commands
```bash
bash scripts/validate_zip03.sh
docker compose run --rm backend pytest
```
