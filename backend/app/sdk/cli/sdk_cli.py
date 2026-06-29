from pathlib import Path

from app.sdk.doctor.checks import run_doctor
from app.sdk.plugins.scaffold import scaffold_plugin


def sdk_doctor(root: Path) -> str:
    checks = run_doctor(root)
    lines = ["AutoShortAI SDK Doctor"]
    for check in checks:
        status = "OK" if check.passed else "FAIL"
        lines.append(f"{status} {check.name}: {check.message}")
    return "\n".join(lines)


def sdk_create_plugin(root: Path, plugin_type: str, plugin_name: str) -> str:
    path = scaffold_plugin(root / "plugins", plugin_type, plugin_name)
    return f"Created plugin scaffold at {path}"
