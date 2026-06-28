from app.core.plugins.contracts.publisher import PublisherPlugin
from app.plugins.publishers.instagram.plugin import InstagramPublisherPlugin
from app.plugins.publishers.tiktok.plugin import TikTokPublisherPlugin
from app.plugins.publishers.youtube.plugin import YouTubePublisherPlugin


class PluginRegistry:
    def __init__(self) -> None:
        self._publishers: dict[str, PublisherPlugin] = {
            "youtube": YouTubePublisherPlugin(),
            "tiktok": TikTokPublisherPlugin(),
            "instagram": InstagramPublisherPlugin(),
        }

    def list_publishers(self) -> list[dict[str, str]]:
        return [
            {"name": plugin.platform_name, "display_name": plugin.display_name, "status": "placeholder"}
            for plugin in self._publishers.values()
        ]

    def get_publisher(self, name: str) -> PublisherPlugin:
        return self._publishers[name]


plugin_registry = PluginRegistry()
