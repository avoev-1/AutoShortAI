from fastapi import APIRouter

router = APIRouter()


@router.get("/safety")
async def safety_state() -> dict[str, object]:
    return {
        "public_publishing": "disabled",
        "paid_apis": "disabled",
        "emergency_stop": "available_later",
        "approval_mode": "manual_by_default",
    }
