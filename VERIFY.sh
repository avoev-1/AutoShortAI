#!/usr/bin/env bash
set -euo pipefail
bash scripts/validate_zip04.sh
python3 -m json.tool state/PROJECT_STATE.json >/dev/null
echo "ZIP04 verification passed."
