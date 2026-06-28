from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.errors.exceptions import AutoShortAIError


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(AutoShortAIError)
    async def autoshort_error_handler(request: Request, exc: AutoShortAIError) -> JSONResponse:
        return JSONResponse(status_code=400, content={"error": exc.__class__.__name__, "detail": str(exc)})
