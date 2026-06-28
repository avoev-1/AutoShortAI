from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config.settings import settings
from app.core.errors.handlers import register_error_handlers
from app.core.logging.setup import configure_logging


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Platform-neutral AI content automation foundation.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_error_handlers(app)
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        return {
            "status": "ok",
            "app": settings.app_name,
            "version": settings.app_version,
            "mode": "platform-neutral-foundation",
        }

    return app
