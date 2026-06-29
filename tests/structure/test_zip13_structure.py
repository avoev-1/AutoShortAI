from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ZIP_NAME = "AutoShortAI_ZIP13_AI_Worker_Runtime"


def test_zip13_required_paths_exist():
    required = [
        "docs/" + ZIP_NAME + "/README.md",
        "docs/" + ZIP_NAME + "/ARCHITECTURE.md",
        "docs/" + ZIP_NAME + "/ROADMAP_ZIP13.md",
        "docs/" + ZIP_NAME + "/CHANGELOG.md",
        "docs/" + ZIP_NAME + "/SAFETY.md",
        "docs/" + ZIP_NAME + "/AI_WORKER_CORE.md",
        "docs/" + ZIP_NAME + "/PROVIDER_ABSTRACTION.md",
        "docs/" + ZIP_NAME + "/CAPABILITY_ROUTING.md",
        "docs/" + ZIP_NAME + "/RESTRICTED_ADULT_PLATFORM_READINESS.md",
        "src/autoshortai/ai_runtime/__init__.py",
        "src/autoshortai/ai_runtime/models.py",
        "src/autoshortai/ai_runtime/runtime.py",
        "src/autoshortai/ai_runtime/safety.py",
        "templates/zip13_ai_runtime/script_generation.template.md",
        "templates/zip13_ai_runtime/restricted_platform_review.template.md",
        "tests/fixtures/restricted_adult_platform_policy.example.json",
        "examples/zip13_ai_runtime_example.py",
    ]
    missing = [path for path in required if not (ROOT / path).exists()]
    assert not missing
