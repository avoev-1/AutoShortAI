from __future__ import annotations

from enum import Enum


class ReleaseGovernanceHook(str, Enum):
    BEFORE_RELEASE_CANDIDATE_CREATED = "before_release_candidate_created"
    AFTER_RELEASE_CANDIDATE_CREATED = "after_release_candidate_created"
    BEFORE_RELEASE_GATE_CHECKED = "before_release_gate_checked"
    AFTER_RELEASE_GATE_CHECKED = "after_release_gate_checked"
    BEFORE_RISK_RECORDED = "before_risk_recorded"
    AFTER_RISK_RECORDED = "after_risk_recorded"
    BEFORE_GOVERNANCE_REPORT_WRITTEN = "before_governance_report_written"
    AFTER_GOVERNANCE_REPORT_WRITTEN = "after_governance_report_written"
    BEFORE_RELEASE_APPROVED = "before_release_approved"
    AFTER_RELEASE_APPROVED = "after_release_approved"
