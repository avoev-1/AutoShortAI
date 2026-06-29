from fastapi import APIRouter
from app.api.v1.routes import core_engine, human_control, missions, plugins, sdk, system
api_router=APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(plugins.router, prefix="/plugins", tags=["plugins"])
api_router.include_router(human_control.router, prefix="/human-control", tags=["human-control"])
api_router.include_router(core_engine.router, prefix="/core", tags=["core-engine"])
api_router.include_router(sdk.router, prefix="/sdk", tags=["sdk"])
api_router.include_router(missions.router, prefix="/missions", tags=["missions"])
