from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Mapping, Any

from .models import (
    SecretEntry,
    SecretReference,
    AccessRequest,
    AccessResult,
    PlatformCredential,
    CredentialHealthCheck,
)


class SecretProvider(ABC):
    """Storage provider abstraction for secrets."""

    @abstractmethod
    def save(self, entry: SecretEntry) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, reference: SecretReference) -> SecretEntry | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, reference: SecretReference) -> None:
        raise NotImplementedError


class AccessPolicyEvaluator(ABC):
    """Evaluates whether a module can access a secret reference."""

    @abstractmethod
    def evaluate(self, request: AccessRequest) -> AccessResult:
        raise NotImplementedError


class SecretRedactor(ABC):
    """Redacts sensitive values before logging or display."""

    @abstractmethod
    def redact_value(self, value: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def redact_mapping(self, values: Mapping[str, Any]) -> dict[str, Any]:
        raise NotImplementedError


class SecretsVault(ABC):
    """Primary vault contract used by AutoShortAI modules."""

    @abstractmethod
    def save_secret(self, entry: SecretEntry) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_secret(self, request: AccessRequest) -> SecretEntry | None:
        raise NotImplementedError

    @abstractmethod
    def delete_secret(self, request: AccessRequest) -> None:
        raise NotImplementedError


class CredentialManager(ABC):
    """Manages credential references and health, never raw display."""

    @abstractmethod
    def register_credential(self, credential: PlatformCredential) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_credential_status(self, credential_id: str) -> CredentialHealthCheck:
        raise NotImplementedError
