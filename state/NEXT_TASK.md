# NEXT TASK

## Task ID
ZIP04-APPLY-MISSION-WORKFLOW-ORCHESTRATOR

## Objective
Apply ZIP04 Mission Workflow Orchestrator.

## Acceptance Criteria
- `bash scripts/validate_zip04.sh` passes.
- Backend tests pass.
- `/api/v1/missions/templates` returns workflow templates.
- `/api/v1/missions/plan` returns an execution plan with Guardian and Performance metadata.

## Validation Commands
```bash
bash scripts/validate_zip04.sh
docker compose run --rm backend pytest
```
