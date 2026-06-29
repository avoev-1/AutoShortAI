from __future__ import annotations

from dataclasses import dataclass, field

from .contracts import SecretProvider
from .models import SecretEntry, SecretReference


@dataclass
class MemoryOnlySecretProvider(SecretProvider):
    """In-memory provider for tests and local development only."""

    _values: dict[str, SecretEntry] = field(default_factory=dict)

    def save(self, entry: SecretEntry) -> None:
        self._values[entry.reference.reference_id] = entry

    def load(self, reference: SecretReference) -> SecretEntry | None:
        return self._values.get(reference.reference_id)

    def delete(self, reference: SecretReference) -> None:
        self._values.pop(reference.reference_id, None)


@dataclass(frozen=True)
class EnvironmentSecretProviderPlan:
    """Architecture placeholder for env-var backed secrets."""

    variable_prefix: str = "AUTOSHORTAI_SECRET_"
    allow_runtime_write: bool = False


@dataclass(frozen=True)
class OSKeychainProviderPlan:
    """Architecture placeholder for OS-native keychains."""

    windows_credential_manager: bool = True
    macos_keychain: bool = True
    linux_secret_service: bool = True


@dataclass(frozen=True)
class ExternalVaultProviderPlan:
    """Architecture placeholder for optional external vault providers."""

    enabled_by_default: bool = False
    provider_name: str | None = None
