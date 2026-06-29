"""ZIP17 workspace policy contracts."""

from __future__ import annotations

from dataclasses import dataclass

from .errors import RestrictedWorkspaceError
from .models import MaturityRating, WorkspaceMode, ManualReviewStatus


@dataclass(slots=True)
class RestrictedWorkspacePolicyConfig:
    """Policy configuration for restricted creator workflows."""

    enabled: bool = False
    manual_review_required: bool = True
    require_consent_metadata: bool = True
    require_all_participants_18_plus: bool = True
    isolate_storage: bool = True
    isolate_logs: bool = True
    allow_automatic_publishing: bool = False


@dataclass(slots=True)
class RestrictedWorkspaceContext:
    """Context needed before restricted media enters the workspace."""

    workspace_mode: WorkspaceMode
    maturity_rating: MaturityRating
    manual_review_status: ManualReviewStatus
    consent_metadata_present: bool
    all_participants_18_plus: bool


def validate_restricted_workspace_policy(policy: RestrictedWorkspacePolicyConfig) -> None:
    """Validate a restricted workspace policy contract.

    This is intentionally minimal. Real enforcement belongs in later
    implementation under Guardian checks and ZIP18 security.
    """
    if policy.enabled and not policy.isolate_storage:
        raise RestrictedWorkspaceError("Restricted workspace must isolate storage.")

    if policy.enabled and not policy.isolate_logs:
        raise RestrictedWorkspaceError("Restricted workspace must isolate logs.")

    if policy.enabled and policy.allow_automatic_publishing and policy.manual_review_required:
        raise RestrictedWorkspaceError(
            "Automatic publishing cannot bypass manual review in restricted mode."
        )


def validate_restricted_workspace_context(context: RestrictedWorkspaceContext) -> None:
    """Validate restricted context before media is accepted."""
    restricted_rating = {
        MaturityRating.MATURE_18,
        MaturityRating.RESTRICTED_ADULT,
    }

    if context.maturity_rating in restricted_rating and context.workspace_mode != WorkspaceMode.RESTRICTED:
        raise RestrictedWorkspaceError("Restricted maturity ratings require restricted workspace mode.")

    if context.maturity_rating in restricted_rating and not context.consent_metadata_present:
        raise RestrictedWorkspaceError("Consent metadata is required for restricted media.")

    if context.maturity_rating in restricted_rating and not context.all_participants_18_plus:
        raise RestrictedWorkspaceError("All participants must be verified 18+.")

    if context.maturity_rating in restricted_rating and context.manual_review_status not in {
        ManualReviewStatus.REQUIRED,
        ManualReviewStatus.PENDING,
        ManualReviewStatus.APPROVED,
    }:
        raise RestrictedWorkspaceError("Manual review is required for restricted media.")
