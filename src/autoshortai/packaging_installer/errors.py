class PackagingInstallerError(Exception):
    """Base error for ZIP19 packaging installer contracts."""


class DependencyResolutionError(PackagingInstallerError):
    """Raised when a required dependency cannot be resolved."""


class PackagingVerificationError(PackagingInstallerError):
    """Raised when package verification fails."""


class RestrictedPackPolicyError(PackagingInstallerError):
    """Raised when restricted creator pack isolation rules are violated."""
