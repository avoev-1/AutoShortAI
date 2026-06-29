from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class SecretKind(str, Enum):
    API_KEY = "api_key"
    OAUTH_TOKEN = "oauth_token"
    SESSION_TOKEN = "session_token"
    PASSWORD = "password"
    DEVICE_TOKEN = "device_token"
    WORKSPACE_SECRET = "workspace_secret"
    RESTRICTED_CREDENTIAL = "restricted_credential"
    GENERIC_SECRET = "generic_secret"


class SecretScope(str, Enum):
    GLOBAL = "global"
    PROVIDER = "provider"
    PLATFORM = "platform"
    DEVICE = "device"
    WORKSPACE = "workspace"
    RESTRICTED = "restricted"


class SecretProviderKind(str, Enum):
    MEMORY_ONLY = "memory_only"
    ENVIRONMENT = "environment"
    LOCAL_ENCRYPTED_FILE = "local_encrypted_file"
    OS_KEYCHAIN = "os_keychain"
    EXTERNAL_VAULT = "external_vault"


class CredentialKind(str, Enum):
    AI_PROVIDER = "ai_provider"
    PUBLISHING_PLATFORM = "publishing_platform"
    ANALYTICS_PLATFORM = "analytics_platform"
    DEVICE = "device"
    WORKSPACE = "workspace"
    RESTRICTED_CREATOR_PLATFORM = "restricted_creator_platform"


class CredentialStatus(str, Enum):
    MISSING = "missing"
    CONFIGURED = "configured"
    EXPIRED = "expired"
    REVOKED = "revoked"
    LOCKED = "locked"
    INVALID = "invalid"


class AccessDecision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    REQUIRE_MANUAL_REVIEW = "require_manual_review"


@dataclass(frozen=True)
class SecretReference:
    reference_id: str
    scope: SecretScope
    kind: SecretKind
    provider: SecretProviderKind = SecretProviderKind.MEMORY_ONLY
    labels: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class SecretEntry:
    reference: SecretReference
    value: str
    created_at: str | None = None
    updated_at: str | None = None
    expires_at: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PlatformCredential:
    credential_id: str
    platform: str
    kind: CredentialKind
    secret_reference: SecretReference
    status: CredentialStatus = CredentialStatus.CONFIGURED
    account_id: str | None = None
    channel_id: str | None = None
    restricted: bool = False


@dataclass(frozen=True)
class AccessRequest:
    requester_module: str
    permission: str
    secret_reference: SecretReference
    reason: str
    restricted_context: bool = False


@dataclass(frozen=True)
class AccessResult:
    decision: AccessDecision
    reason: str
    redacted_reference: str


@dataclass(frozen=True)
class SecretAccessPolicy:
    policy_id: str
    allowed_modules: tuple[str, ...]
    allowed_scopes: tuple[SecretScope, ...]
    restricted_access_allowed: bool = False
    manual_review_required: bool = False


@dataclass(frozen=True)
class SecretRotationPolicy:
    policy_id: str
    rotation_days: int | None = None
    provider_supported: bool = False
    manual_rotation_allowed: bool = True


@dataclass(frozen=True)
class SecretAuditEvent:
    event_id: str
    requester_module: str
    action: str
    secret_reference_id: str
    decision: AccessDecision
    timestamp: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RestrictedCredentialPolicy:
    enabled: bool = False
    require_manual_review: bool = True
    require_consent_metadata: bool = True
    require_all_participants_18_plus: bool = True
    isolate_credentials: bool = True
    isolate_logs: bool = True
    isolate_workspace: bool = True


@dataclass(frozen=True)
class CredentialHealthCheck:
    credential_id: str
    status: CredentialStatus
    message: str
    checked_at: str | None = None
