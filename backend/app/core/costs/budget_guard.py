from dataclasses import dataclass
from app.core.errors.exceptions import HumanApprovalRequired


@dataclass(frozen=True)
class BudgetPolicy:
    daily_budget_usd: float
    allow_paid_apis: bool = False


class BudgetGuard:
    def __init__(self, policy: BudgetPolicy) -> None:
        self.policy = policy

    def assert_can_spend(self, estimated_cost_usd: float) -> None:
        if estimated_cost_usd <= 0:
            return
        if not self.policy.allow_paid_apis:
            raise HumanApprovalRequired("Paid API usage is disabled.")
        if estimated_cost_usd > self.policy.daily_budget_usd:
            raise HumanApprovalRequired("Estimated cost exceeds daily budget.")
