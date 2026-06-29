from pathlib import Path


def test_zip16_structure_exists():
    root = Path.cwd()
    required = [
        "docs/AutoShortAI_ZIP16_Multi_Platform_Publishing_Runtime/publishing_runtime_overview.md",
        "docs/AutoShortAI_ZIP16_Multi_Platform_Publishing_Runtime/platform_adapter_contracts.md",
        "docs/AutoShortAI_ZIP16_Multi_Platform_Publishing_Runtime/manual_review_gate.md",
        "docs/AutoShortAI_ZIP16_Multi_Platform_Publishing_Runtime/adult_x_creator_publishing_readiness.md",
        "src/autoshortai/publishing_runtime/__init__.py",
        "src/autoshortai/publishing_runtime/models.py",
        "src/autoshortai/publishing_runtime/protocols.py",
        "src/autoshortai/publishing_runtime/capabilities.py",
        "src/autoshortai/publishing_runtime/adapters.py",
        "src/autoshortai/publishing_runtime/restricted.py",
        "src/autoshortai/publishing_runtime/review.py",
        "src/autoshortai/publishing_runtime/hooks.py",
        "templates/zip16_publishing_runtime/publishing_profile.template.yaml",
        "templates/zip16_publishing_runtime/restricted_platform_profile.template.yaml",
        "examples/zip16_publishing_flow_example.md",
    ]
    missing = [path for path in required if not (root / path).exists()]
    assert not missing, missing
