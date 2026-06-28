from fastapi import APIRouter

from app.core.plugins.registry.plugin_registry import plugin_registry

router = APIRouter()


@router.get("")
async def list_plugins() -> dict[str, object]:
    return {
        "publishers": plugin_registry.list_publishers(),
        "ai_providers": ["openai", "anthropic", "gemini"],
        "voice_providers": ["elevenlabs"],
        "video_engines": ["ffmpeg"],
    }
