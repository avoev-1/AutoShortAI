"""Structure checks for ZIP09 Analytics & Feedback Loop."""

from pathlib import Path


def test_zip09_required_paths_exist():
    root = Path(__file__).resolve().parents[2]

    required = [
        root / "docs" / "AutoShortAI_ZIP09_Analytics_Feedback_Loop" / "README.md",
        root / "docs" / "AutoShortAI_ZIP09_Analytics_Feedback_Loop" / "ARCHITECTURE.md",
        root / "docs" / "AutoShortAI_ZIP09_Analytics_Feedback_Loop" / "ROADMAP_ZIP09.md",
        root / "docs" / "AutoShortAI_ZIP09_Analytics_Feedback_Loop" / "PLATFORM_AGNOSTIC_RULES.md",
        root / "src" / "autoshortai" / "analytics" / "models.py",
        root / "src" / "autoshortai" / "analytics" / "contracts.py",
        root / "src" / "autoshortai" / "analytics" / "adapters.py",
        root / "src" / "autoshortai" / "analytics" / "scoring.py",
        root / "src" / "autoshortai" / "analytics" / "feedback.py",
        root / "src" / "autoshortai" / "analytics" / "experiments.py",
        root / "templates" / "zip09_analytics_feedback" / "analytics_config.template.json",
        root / "templates" / "zip09_analytics_feedback" / "metrics_snapshot.template.json",
        root / "tests" / "fixtures" / "zip09_metrics_snapshot.example.json",
    ]

    missing = [str(path) for path in required if not path.exists()]
    assert not missing, f"Missing ZIP09 paths: {missing}"
