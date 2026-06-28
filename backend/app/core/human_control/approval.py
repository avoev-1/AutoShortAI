from dataclasses import dataclass
from enum import StrEnum
from app.core.errors.exceptions import HumanApprovalRequired


class ApprovalMode(StrEnum):
    manual = "manual"
    semi_auto = "semi_auto"
    auto_safe = "auto_safe"
    full_auto = "full_auto"


@dataclass(frozen=True)
class HumanControlPolicy:
    approval_mode: ApprovalMode = ApprovalMode.manual
    allow_public_publish: bool = False
    emergency_stop: bool = False


class HumanControlGuard:
    def __init__(self, policy: HumanControlPolicy) -> None:
        self.policy = policy

    def assert_publication_allowed(self) -> None:
        if self.policy.emergency_stop:
            raise HumanApprovalRequired("Emergency stop is active.")
        if not self.policy.allow_public_publish:
            raise HumanApprovalRequired("Public publishing requires human approval.")
