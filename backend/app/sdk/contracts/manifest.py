from dataclasses import dataclass, field
from enum import StrEnum


class PluginType(StrEnum):
    publisher = "publisher"
    ai_provider = "ai_provider"
    voice_provider = "voice_provider"
    video_engine = "video_engine"
    storage_provider = "storage_provider"
    notification_provider = "notification_provider"
    analytics_provider = "analytics_provider"


@dataclass(frozen=True)
class PluginCapability:
    name: str
    description: str


@dataclass(frozen=True)
class PluginManifest:
    plugin_id: str
    name: str
    plugin_type: PluginType
    version: str
    entrypoint: str
    description: str
    permissions: list[str] = field(default_factory=list)
    capabilities: list[PluginCapability] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    enabled: bool = True
