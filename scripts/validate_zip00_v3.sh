#!/usr/bin/env bash
set -euo pipefail

required=(
  ".llm/core/LLM_CORE.md"
  ".llm/core/BOOT_PROTOCOL.md"
  ".llm/core/OPERATING_LOOP.md"
  ".llm/policies/AI_CONSTITUTION.md"
  ".llm/policies/QUALITY_GATE.md"
  ".llm/policies/HUMAN_CONTROL_POLICY.md"
  "state/PROJECT_STATE.json"
  "state/NEXT_TASK.md"
  "docs/00_foundation/PROJECT_OVERVIEW.md"
  "docs/00_foundation/ROADMAP.md"
  "docs/09_human_controls/HUMAN_DASHBOARD_OPTIONS.md"
  "README.md"
)
for f in "${required[@]}"; do
  test -f "$f" || { echo "Missing: $f"; exit 1; }
done

python3 -m json.tool state/PROJECT_STATE.json >/dev/null
python3 -m json.tool state/VERSION.json >/dev/null
python3 -m json.tool state/CURRENT_CONTEXT.json >/dev/null
python3 -m json.tool state/CHECKPOINT.json >/dev/null
python3 -m json.tool state/DECISION_LOG.json >/dev/null
python3 -m json.tool state/REPOSITORY_HEALTH.json >/dev/null

echo "ZIP00 v3 validation passed."
