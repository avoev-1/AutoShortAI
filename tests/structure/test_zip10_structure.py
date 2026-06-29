from pathlib import Path


def test_zip10_required_files_exist():
    root = Path(__file__).resolve().parents[2]
    required = [
        "docs/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/README.md",
        "docs/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/ARCHITECTURE.md",
        "docs/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/ROADMAP_ZIP10.md",
        "src/autoshortai/learning/__init__.py",
        "src/autoshortai/learning/models.py",
        "src/autoshortai/learning/contracts.py",
        "src/autoshortai/learning/engine.py",
        "src/autoshortai/learning/adaptation.py",
        "src/autoshortai/learning/memory.py",
        "src/autoshortai/learning/experiments.py",
        "src/autoshortai/learning/policies.py",
        "src/autoshortai/learning/confidence.py",
        "src/autoshortai/learning/bridge.py",
        "src/autoshortai/learning/hooks.py",
        "templates/zip10_auto_learning/learning_policy.template.json",
        "tests/fixtures/zip10_learning_evidence.example.json",
        "examples/zip10_learning_example.py",
    ]
    for item in required:
        assert (root / item).exists(), item


def test_zip10_no_single_platform_coupling():
    root = Path(__file__).resolve().parents[2]
    architecture = (root / "docs/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/ARCHITECTURE.md").read_text()
    assert "platform-agnostic" in architecture.lower()
    assert "YouTube Shorts" in architecture
    assert "TikTok" in architecture
