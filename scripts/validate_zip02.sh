#!/usr/bin/env bash
set -euo pipefail

required=(
  "backend/app/core/contracts/ai.py"
  "backend/app/core/contracts/publisher.py"
  "backend/app/core/contracts/storage.py"
  "backend/app/core/contracts/queue.py"
  "backend/app/core/contracts/telemetry.py"
  "backend/app/core/pipeline/models.py"
  "backend/app/core/pipeline/graph.py"
  "backend/app/core/orchestration/orchestrator.py"
  "backend/app/core/workflows/content_workflow.py"
  "backend/app/core/costs/budget_guard.py"
  "backend/app/core/human_control/approval.py"
  "backend/app/api/v1/routes/core_engine.py"
  "docs/zip02/README.md"
  "docs/architecture/CORE_ENGINE_ARCHITECTURE.md"
  "state/PROJECT_STATE.json"
  "state/NEXT_TASK.md"
)
for file in "${required[@]}"; do
  test -f "$file" || { echo "Missing: $file"; exit 1; }
done
python3 -m json.tool state/PROJECT_STATE.json > /dev/null
echo "ZIP02 core engine validation passed."
