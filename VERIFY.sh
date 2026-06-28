#!/usr/bin/env bash
set -euo pipefail
bash scripts/validate_zip02.sh
python3 -m json.tool state/PROJECT_STATE.json >/dev/null
echo "ZIP02 verification passed."
