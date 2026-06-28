#!/usr/bin/env bash
set -euo pipefail

required=(
  "docker-compose.yml"
  "backend/Dockerfile"
  "backend/pyproject.toml"
  "backend/app/main.py"
  "backend/app/api/v1/router.py"
  "backend/app/core/config/settings.py"
  "backend/app/core/plugins/contracts/publisher.py"
  "backend/app/core/plugins/registry/plugin_registry.py"
  "frontend/Dockerfile"
  "frontend/package.json"
  "frontend/src/app/App.tsx"
  "frontend/src/styles/globals.css"
  "docs/design/APPLE_GLASS_DESIGN_SYSTEM.md"
  "docs/plugins/PLUGIN_ARCHITECTURE.md"
  "state/PROJECT_STATE.json"
  "state/NEXT_TASK.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "Missing: $file"; exit 1; }
done

python3 -m json.tool state/PROJECT_STATE.json > /dev/null

echo "ZIP01 production foundation validation passed."
