#!/usr/bin/env bash
set -euo pipefail

required=(
  "backend/app/sdk/core/version.py"
  "backend/app/sdk/contracts/manifest.py"
  "backend/app/sdk/contracts/provider.py"
  "backend/app/sdk/registry/manifest_registry.py"
  "backend/app/sdk/events/event_bus.py"
  "backend/app/sdk/events/event_types.py"
  "backend/app/sdk/plugins/manifest_loader.py"
  "backend/app/sdk/plugins/scaffold.py"
  "backend/app/sdk/doctor/checks.py"
  "backend/app/sdk/cli/sdk_cli.py"
  "backend/app/api/v1/routes/sdk.py"
  "docs/zip03/README.md"
  "docs/sdk/SDK_OVERVIEW.md"
  "docs/plugins/PLUGIN_MANIFEST_SPEC.md"
  "state/PROJECT_STATE.json"
  "state/NEXT_TASK.md"
)
for file in "${required[@]}"; do
  test -f "$file" || { echo "Missing: $file"; exit 1; }
done
python3 -m json.tool state/PROJECT_STATE.json > /dev/null
python3 -m json.tool backend/app/sdk/plugins/manifests/youtube.manifest.json > /dev/null
python3 -m json.tool backend/app/sdk/plugins/manifests/tiktok.manifest.json > /dev/null
echo "ZIP03 SDK plugin system validation passed."
