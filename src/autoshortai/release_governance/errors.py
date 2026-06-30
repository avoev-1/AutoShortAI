class ReleaseGovernanceError(Exception):
    """Base error for ZIP20 release governance."""


class ReleaseBlockedError(ReleaseGovernanceError):
    """Raised when required release gates block a release candidate."""


class CompatibilityPolicyError(ReleaseGovernanceError):
    """Raised when a change violates ZIP01-ZIP20 compatibility."""


class RestrictedGovernanceError(ReleaseGovernanceError):
    """Raised when restricted workflow governance is violated."""
