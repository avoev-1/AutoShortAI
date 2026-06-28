from fastapi import APIRouter

from app.core.config.settings import settings

router = APIRouter()


@router.get("/status")
async def system_status() -> dict[str, object]:
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "real_publishing_enabled": settings.enable_real_publishing,
        "paid_apis_enabled": settings.enable_paid_apis,
        "architecture": "platform-neutral-plugin-based",
    }
