from __future__ import annotations

from typing import Any, Mapping

SENSITIVE_KEY_HINTS = (
    "secret",
    "token",
    "api_key",
    "apikey",
    "password",
    "credential",
    "session",
    "auth",
)


def redact_secret_preview(value: str, visible_prefix: int = 4, visible_suffix: int = 4) -> str:
    """Return a safe preview of a secret-like value."""
    if not value:
        return "****REDACTED****"
    if len(value) <= visible_prefix + visible_suffix + 4:
        return "****REDACTED****"
    return f"{value[:visible_prefix]}{'*' * 12}{value[-visible_suffix:]}"


def is_sensitive_key(key: str) -> bool:
    normalized = key.lower().replace("-", "_")
    return any(hint in normalized for hint in SENSITIVE_KEY_HINTS)


def redact_mapping(values: Mapping[str, Any]) -> dict[str, Any]:
    redacted: dict[str, Any] = {}
    for key, value in values.items():
        if is_sensitive_key(str(key)):
            redacted[str(key)] = "****REDACTED****"
        elif isinstance(value, Mapping):
            redacted[str(key)] = redact_mapping(value)
        else:
            redacted[str(key)] = value
    return redacted
