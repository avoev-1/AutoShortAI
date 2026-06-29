from pathlib import Path


def test_zip07_expected_package_files_exist():
    root = Path(__file__).resolve().parents[2]
    package = root / "src" / "autoshortai" / "creative_strategy"
    expected = [
        "__init__.py",
        "models.py",
        "contracts.py",
        "hooks.py",
        "events.py",
        "errors.py",
        "config.py",
        "content_strategy_engine.py",
        "creation_profiles.py",
        "idea_blueprint.py",
        "script_blueprint.py",
        "variant_planner.py",
        "rules_engine.py",
        "quality_scoring.py",
        "strategy_context.py",
        "platform_targets.py",
        "py.typed",
    ]
    for filename in expected:
        assert (package / filename).exists(), filename


def test_zip07_expected_docs_exist():
    root = Path(__file__).resolve().parents[2]
    docs = root / "docs" / "AutoShortAI_ZIP07_Creative_Strategy_Engine"
    expected = [
        "README.md",
        "ARCHITECTURE.md",
        "ROADMAP_ZIP07.md",
        "CHANGELOG.md",
        "SAFETY.md",
        "CONTENT_STRATEGY_ENGINE.md",
        "CREATION_PROFILES.md",
        "IDEA_BLUEPRINT_SYSTEM.md",
        "SCRIPT_BLUEPRINT_CONTRACTS.md",
        "VARIANT_PLANNER.md",
        "RULES_ENGINE.md",
        "QUALITY_SCORE_CONTRACTS.md",
        "STRATEGY_HOOKS.md",
        "INTEGRATION_WITH_ZIP04_ZIP05_ZIP06.md",
        "MIGRATION_NOTES_ZIP06_TO_ZIP07.md",
        "INTEGRATION_GUIDE_FOR_CLAUDE.md",
    ]
    for filename in expected:
        assert (docs / filename).exists(), filename
