"""Structure tests for ZIP06 Smart Asset Pipeline.

These tests validate architecture files and contracts. They intentionally avoid
requiring production implementations.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_zip06_core_package_exists() -> None:
    package = ROOT / "src" / "autoshortai" / "asset_pipeline"
    assert package.exists()
    assert (package / "contracts.py").exists()
    assert (package / "models.py").exists()


def test_zip06_namespaced_docs_exist() -> None:
    docs = ROOT / "docs" / "AutoShortAI_ZIP06_Smart_Asset_Pipeline"
    assert docs.exists()
    assert (docs / "ARCHITECTURE.md").exists()
    assert (docs / "ROADMAP_ZIP06.md").exists()
    assert (docs / "ASSET_REGISTRY.md").exists()


def test_zip06_templates_exist() -> None:
    templates = ROOT / "templates" / "zip06_asset_pipeline"
    assert (templates / "asset_manifest.template.json").exists()
    assert (templates / "cache_policy.template.yaml").exists()
    assert (templates / "asset_provider.template.yaml").exists()
