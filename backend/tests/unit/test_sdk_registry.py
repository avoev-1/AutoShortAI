from app.sdk.contracts.manifest import PluginType
from app.sdk.registry.manifest_registry import ManifestRegistry, register_builtin_manifests, manifest_registry


def test_builtin_manifest_registry_lists_publishers() -> None:
    register_builtin_manifests()
    publishers = manifest_registry.by_type(PluginType.publisher)
    ids = {manifest.plugin_id for manifest in publishers}
    assert "publisher.youtube" in ids
    assert "publisher.tiktok" in ids
    assert "publisher.instagram" in ids


def test_manifest_registry_rejects_duplicate() -> None:
    registry = ManifestRegistry()
    register_builtin_manifests()
    manifest = manifest_registry.get("publisher.youtube")
    registry.register(manifest)
    try:
        registry.register(manifest)
        assert False
    except ValueError:
        assert True
