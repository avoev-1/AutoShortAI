from __future__ import annotations

from dataclasses import dataclass

from .models import RestrictedCredentialPolicy


@dataclass(frozen=True)
class SecurityPolicyConfig:
    forbid_hardcoded_secrets: bool = True
    forbid_secrets_in_logs: bool = True
    forbid_secrets_in_examples: bool = True
    forbid_restricted_general_mixing: bool = True
    require_redaction: bool = True
    require_audit_events: bool = True


def validate_restricted_credential_policy(policy: RestrictedCredentialPolicy) -> None:
    if policy.enabled:
        if not policy.require_manual_review:
            raise ValueError("Restricted credential workflows require manual review by default.")
        if not policy.require_consent_metadata:
            raise ValueError("Restricted credential workflows require consent metadata.")
        if not policy.require_all_participants_18_plus:
            raise ValueError("Restricted credential workflows require all participants to be 18+.")
        if not policy.isolate_credentials:
            raise ValueError("Restricted credentials must be isolated from general credentials.")
