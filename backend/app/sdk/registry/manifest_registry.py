from app.sdk.contracts.manifest import PluginCapability, PluginManifest, PluginType


class ManifestRegistry:
    def __init__(self) -> None:
        self._manifests: dict[str, PluginManifest] = {}

    def register(self, manifest: PluginManifest) -> None:
        if manifest.plugin_id in self._manifests:
            raise ValueError(f"Plugin already registered: {manifest.plugin_id}")
        self._manifests[manifest.plugin_id] = manifest

    def list(self) -> list[PluginManifest]:
        return list(self._manifests.values())

    def by_type(self, plugin_type: PluginType) -> list[PluginManifest]:
        return [manifest for manifest in self._manifests.values() if manifest.plugin_type == plugin_type]

    def get(self, plugin_id: str) -> PluginManifest:
        return self._manifests[plugin_id]


manifest_registry = ManifestRegistry()


def register_builtin_manifests() -> None:
    if manifest_registry.list():
        return

    manifest_registry.register(
        PluginManifest(
            plugin_id="publisher.youtube",
            name="YouTube Publisher",
            plugin_type=PluginType.publisher,
            version="0.1.0",
            entrypoint="app.plugins.publishers.youtube.plugin:YouTubePublisherPlugin",
            description="Placeholder YouTube publisher plugin.",
            permissions=["private_upload_later", "analytics_later"],
            capabilities=[PluginCapability("private_upload", "Upload private content when enabled later")],
        )
    )
    manifest_registry.register(
        PluginManifest(
            plugin_id="publisher.tiktok",
            name="TikTok Publisher",
            plugin_type=PluginType.publisher,
            version="0.1.0",
            entrypoint="app.plugins.publishers.tiktok.plugin:TikTokPublisherPlugin",
            description="Placeholder TikTok publisher plugin.",
            permissions=["upload_later", "analytics_later"],
            capabilities=[PluginCapability("short_video_publish", "Publish short videos when enabled later")],
        )
    )
    manifest_registry.register(
        PluginManifest(
            plugin_id="publisher.instagram",
            name="Instagram Publisher",
            plugin_type=PluginType.publisher,
            version="0.1.0",
            entrypoint="app.plugins.publishers.instagram.plugin:InstagramPublisherPlugin",
            description="Placeholder Instagram Reels publisher plugin.",
            permissions=["upload_later", "analytics_later"],
            capabilities=[PluginCapability("reels_publish", "Publish Reels when enabled later")],
        )
    )
