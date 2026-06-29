from __future__ import annotations

from enum import Enum
from dataclasses import dataclass, field
from typing import Mapping, Any


class SecurityVaultHook(str, Enum):
    BEFORE_SECRET_SAVED = "before_secret_saved"
    AFTER_SECRET_SAVED = "after_secret_saved"
    BEFORE_SECRET_ACCESSED = "before_secret_accessed"
    AFTER_SECRET_ACCESSED = "after_secret_accessed"
    BEFORE_CREDENTIAL_ROTATED = "before_credential_rotated"
    AFTER_CREDENTIAL_ROTATED = "after_credential_rotated"
    BEFORE_SENSITIVE_LOG_WRITTEN = "before_sensitive_log_written"
    AFTER_SECURITY_VIOLATION_DETECTED = "after_security_violation_detected"


@dataclass(frozen=True)
class SecurityVaultHookPayload:
    hook: SecurityVaultHook
    source_module: str
    metadata: Mapping[str, Any] = field(default_factory=dict)
