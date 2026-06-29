"""Structure checks for ZIP08 Production Queue & Scheduler."""

from pathlib import Path


def test_zip08_required_paths_exist():
    root = Path(__file__).resolve().parents[2]

    required = [
        root / "docs" / "AutoShortAI_ZIP08_Production_Queue_Scheduler" / "README.md",
        root / "docs" / "AutoShortAI_ZIP08_Production_Queue_Scheduler" / "ARCHITECTURE.md",
        root / "docs" / "AutoShortAI_ZIP08_Production_Queue_Scheduler" / "ROADMAP_ZIP08.md",
        root / "src" / "autoshortai" / "production_queue" / "models.py",
        root / "src" / "autoshortai" / "production_queue" / "contracts.py",
        root / "src" / "autoshortai" / "production_queue" / "scheduler.py",
        root / "src" / "autoshortai" / "production_queue" / "resources.py",
        root / "templates" / "zip08_production_queue" / "job.template.json",
        root / "tests" / "fixtures" / "zip08_job.example.json",
    ]

    missing = [str(path) for path in required if not path.exists()]
    assert not missing, f"Missing ZIP08 paths: {missing}"
