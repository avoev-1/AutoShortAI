from app.core.config.settings import settings
from app.core.errors.exceptions import HumanApprovalRequired


def require_human_approval_for_publication() -> None:
    if not settings.enable_real_publishing:
        raise HumanApprovalRequired("Real publishing is disabled. Human approval required.")


def require_human_approval_for_paid_api() -> None:
    if not settings.enable_paid_apis:
        raise HumanApprovalRequired("Paid APIs are disabled. Human approval required.")
