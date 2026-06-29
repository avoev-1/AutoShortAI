class SecurityVaultError(Exception):
    """Base error for ZIP18 security vault contracts."""


class SecretAccessDenied(SecurityVaultError):
    """Raised when a module is not allowed to access a secret."""


class SecretNotFound(SecurityVaultError):
    """Raised when a secret reference cannot be resolved."""


class RestrictedCredentialPolicyError(SecurityVaultError):
    """Raised when restricted credential rules are violated."""
