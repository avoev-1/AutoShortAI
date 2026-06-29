"""Structure tests for ZIP15 Guardian Engine Foundation."""

from pathlib import Path


def test_zip15_guardian_files_exist():
    root = Path.cwd()
    required = [
        "docs/AutoShortAI_ZIP15_Guardian_Engine_Foundation/guardian_overview.md",
        "docs/AutoShortAI_ZIP15_Guardian_Engine_Foundation/rule_packs.md",
        "src/autoshortai/guardian/__init__.py",
        "src/autoshortai/guardian/models.py",
        "src/autoshortai/guardian/protocols.py",
        "src/autoshortai/guardian/rules.py",
        "src/autoshortai/guardian/hooks.py",
        "templates/zip15_guardian_engine/guardian_rule.template.md",
        "templates/zip15_guardian_engine/guardian_report.template.md",
        "examples/zip15_guardian_review_example.md",
    ]
    missing = [p for p in required if not (root / p).exists()]
    assert not missing, f"Missing ZIP15 files: {missing}"


def test_zip15_guardian_contracts_importable():
    from autoshortai.guardian import BASELINE_RULES, GUARDIAN_HOOKS, GuardianSeverity

    assert BASELINE_RULES
    assert "before_guardian_run" in GUARDIAN_HOOKS
    assert GuardianSeverity.CRITICAL.value == "critical"
