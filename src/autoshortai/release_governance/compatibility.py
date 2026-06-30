from __future__ import annotations

from .models import (
    BackwardCompatibilityPolicy,
    PlatformAgnosticPolicy,
    RestrictedCreatorGovernancePolicy,
)


def default_backward_compatibility_policy() -> BackwardCompatibilityPolicy:
    return BackwardCompatibilityPolicy(
        baseline="ZIP01-ZIP20",
        rules=(
            "do_not_break_previous_zips",
            "do_not_delete_contracts_without_replacement",
            "do_not_rename_modules_without_migration",
            "do_not_make_optional_dependencies_mandatory",
            "do_not_turn_project_into_saas",
            "do_not_couple_core_to_single_platform",
            "do_not_enable_restricted_workflows_by_default",
            "do_not_store_secrets_in_code_examples_or_logs",
        ),
    )


def default_platform_agnostic_policy() -> PlatformAgnosticPolicy:
    return PlatformAgnosticPolicy(
        first_target="youtube_shorts",
        future_platforms=(
            "tiktok",
            "instagram_reels",
            "facebook_reels",
            "snapchat_spotlight",
            "x_twitter_video",
            "adult_restricted_creator_platforms",
            "generic_future_platform",
        ),
        core_must_use_adapters=True,
        no_platform_lock_in=True,
    )


def default_restricted_creator_governance_policy() -> RestrictedCreatorGovernancePolicy:
    return RestrictedCreatorGovernancePolicy(
        enabled_by_default=False,
        opt_in_required=True,
        isolated_workspace_required=True,
        isolated_credentials_required=True,
        isolated_logs_required=True,
        manual_review_required=True,
        consent_metadata_required=True,
        all_participants_18_plus_required=True,
        maturity_rating_required=True,
        blocked_content_flags=(
            "illegal_content",
            "non_consensual_content",
            "underage_content",
            "unverified_age",
            "missing_consent_metadata",
        ),
    )
