"""Structure tests for ZIP17.

These tests are intentionally lightweight. They verify that the architecture
files exist after installation. They do not test production implementation.
"""

from pathlib import Path


def test_zip17_required_paths_exist():
    root = Path.cwd()
    required = [
        ".autoshort/releases/zip17/README.md",
        "docs/AutoShortAI_ZIP17_Local_Workspace_Media_Library/workspace_layout.md",
        "docs/AutoShortAI_ZIP17_Local_Workspace_Media_Library/media_library.md",
        "docs/AutoShortAI_ZIP17_Local_Workspace_Media_Library/restricted_workspace_policy.md",
        "src/autoshortai/workspace/__init__.py",
        "src/autoshortai/workspace/models.py",
        "src/autoshortai/workspace/contracts.py",
        "src/autoshortai/workspace/hooks.py",
        "src/autoshortai/workspace/policies.py",
        "templates/zip17_workspace/project_manifest.template.json",
        "examples/zip17_workspace_manifest_example.json",
    ]

    missing = [path for path in required if not (root / path).exists()]
    assert not missing, f"Missing ZIP17 paths: {missing}"


def test_zip17_no_platform_lock_in_terms():
    root = Path.cwd()
    workspace_src = root / "src" / "autoshortai" / "workspace"
    if not workspace_src.exists():
        return

    forbidden = [
        "YouTube-only core",
        "mandatory cloud",
        "mandatory database",
    ]

    for file_path in workspace_src.rglob("*.py"):
        content = file_path.read_text(encoding="utf-8")
        for term in forbidden:
            assert term not in content
