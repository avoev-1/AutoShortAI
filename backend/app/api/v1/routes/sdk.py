from fastapi import APIRouter

from app.sdk.core.version import SDK_NAME, SDK_VERSION
from app.sdk.registry.manifest_registry import manifest_registry, register_builtin_manifests

router = APIRouter()


@router.get("/status")
async def sdk_status() -> dict[str, str]:
    return {"name": SDK_NAME, "version": SDK_VERSION, "status": "ready"}


@router.get("/plugins")
async def sdk_plugins() -> dict[str, object]:
    register_builtin_manifests()
    return {
        "plugins": [
            {
                "plugin_id": manifest.plugin_id,
                "name": manifest.name,
                "type": manifest.plugin_type,
                "version": manifest.version,
                "enabled": manifest.enabled,
                "capabilities": [capability.name for capability in manifest.capabilities],
            }
            for manifest in manifest_registry.list()
        ]
    }
