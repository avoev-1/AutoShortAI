from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DoctorCheck:
    name: str
    passed: bool
    message: str


def check_required_files(root: Path) -> list[DoctorCheck]:
    required = [
        "docker-compose.yml",
        "backend/app/main.py",
        "backend/app/core/orchestration/orchestrator.py",
        "backend/app/sdk/core/version.py",
        "state/PROJECT_STATE.json",
    ]

    checks: list[DoctorCheck] = []
    for item in required:
        path = root / item
        checks.append(DoctorCheck(name=item, passed=path.exists(), message="exists" if path.exists() else "missing"))
    return checks


def run_doctor(root: Path) -> list[DoctorCheck]:
    return check_required_files(root)
