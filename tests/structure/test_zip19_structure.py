"""Structure tests for ZIP19.

These tests verify that the ZIP19 architecture files exist after installation.
They do not build real platform installers.
"""

from pathlib import Path


def test_zip19_required_paths_exist():
    root = Path.cwd()
    required = [
        ".autoshort/releases/zip19/README.md",
        "docs/AutoShortAI_ZIP19_Cross_Platform_Packaging_Installer/packaging_core.md",
        "docs/AutoShortAI_ZIP19_Cross_Platform_Packaging_Installer/installer_architecture.md",
        "docs/AutoShortAI_ZIP19_Cross_Platform_Packaging_Installer/dependency_manager.md",
        "docs/AutoShortAI_ZIP19_Cross_Platform_Packaging_Installer/restricted_creator_pack.md",
        "src/autoshortai/packaging_installer/__init__.py",
        "src/autoshortai/packaging_installer/models.py",
        "src/autoshortai/packaging_installer/contracts.py",
        "src/autoshortai/packaging_installer/profiles.py",
        "templates/zip19_packaging_installer/package_manifest.template.json",
        "examples/zip19_package_manifest_example.json",
    ]

    missing = [path for path in required if not (root / path).exists()]
    assert not missing, f"Missing ZIP19 paths: {missing}"


def test_zip19_restricted_pack_not_enabled_by_default():
    root = Path.cwd()
    template = root / "templates" / "zip19_packaging_installer" / "restricted_creator_pack.template.yaml"
    if not template.exists():
        return
    content = template.read_text(encoding="utf-8")
    forbidden = [
        "enabled_by_default: true",
        "package_real_media: true",
        "package_real_credentials: true",
    ]
    for term in forbidden:
        assert term not in content
