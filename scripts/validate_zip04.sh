#!/usr/bin/env bash
set -euo pipefail
required=(
"backend/app/modules/missions/domain/mission.py"
"backend/app/modules/missions/services/mission_factory.py"
"backend/app/modules/missions/services/mission_orchestrator.py"
"backend/app/modules/workflows/domain/workflow_template.py"
"backend/app/modules/workflows/templates/short_form_templates.py"
"backend/app/modules/workflows/services/template_registry.py"
"backend/app/modules/execution/domain/execution_plan.py"
"backend/app/modules/execution/services/execution_planner.py"
"backend/app/modules/snapshots/services/snapshot_service.py"
"backend/app/modules/performance/services/performance_estimator.py"
"backend/app/modules/guardian_hooks/services/guardian_hook.py"
"backend/app/api/v1/routes/missions.py"
"frontend/src/features/mission-control/lib/missionControlModel.ts"
"docs/zip04/README.md"
"docs/architecture/MISSION_ENGINE_ARCHITECTURE.md"
"state/PROJECT_STATE.json"
"state/NEXT_TASK.md"
)
for file in "${required[@]}"; do test -f "$file" || { echo "Missing: $file"; exit 1; }; done
python3 -m json.tool state/PROJECT_STATE.json > /dev/null
echo "ZIP04 mission workflow orchestrator validation passed."
