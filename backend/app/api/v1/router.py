from fastapi import APIRouter

from app.api.v1.routes import human_control, plugins, system

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(plugins.router, prefix="/plugins", tags=["plugins"])
api_router.include_router(human_control.router, prefix="/human-control", tags=["human-control"])
