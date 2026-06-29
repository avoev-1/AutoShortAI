import json
from pathlib import Path

from app.sdk.contracts.manifest import PluginCapability, PluginManifest, PluginType


def load_manifest(path: Path) -> PluginManifest:
    data = json.loads(path.read_text(encoding="utf-8"))
    return PluginManifest(
        plugin_id=data["plugin_id"],
        name=data["name"],
        plugin_type=PluginType(data["plugin_type"]),
        version=data["version"],
        entrypoint=data["entrypoint"],
        description=data["description"],
        permissions=data.get("permissions", []),
        capabilities=[
            PluginCapability(name=item["name"], description=item.get("description", ""))
            for item in data.get("capabilities", [])
        ],
        dependencies=data.get("dependencies", []),
        enabled=data.get("enabled", True),
    )
