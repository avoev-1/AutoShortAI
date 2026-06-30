from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class PackagingHook(str, Enum):
    BEFORE_PACKAGE_BUILD = "before_package_build"
    AFTER_PACKAGE_BUILD = "after_package_build"
    BEFORE_INSTALLER_CREATED = "before_installer_created"
    AFTER_INSTALLER_CREATED = "after_installer_created"
    BEFORE_DEPENDENCY_CHECKED = "before_dependency_checked"
    AFTER_DEPENDENCY_CHECKED = "after_dependency_checked"
    BEFORE_MIGRATION_RUN = "before_migration_run"
    AFTER_MIGRATION_RUN = "after_migration_run"
    BEFORE_PACKAGE_VERIFIED = "before_package_verified"
    AFTER_PACKAGE_VERIFIED = "after_package_verified"


@dataclass(frozen=True)
class PackagingHookPayload:
    hook: PackagingHook
    source_module: str
    metadata: Mapping[str, Any] = field(default_factory=dict)
