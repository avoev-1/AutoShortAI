from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Any


class PackageTarget(str, Enum):
    WINDOWS_DESKTOP = "windows_desktop"
    LINUX_DESKTOP = "linux_desktop"
    MACOS_DESKTOP = "macos_desktop"
    PORTABLE_CLI = "portable_cli"
    DEVELOPER_MODE = "developer_mode"
    HEADLESS_WORKER = "headless_worker"
    DEVICE_NODE_PACKAGE = "device_node_package"


class PackageProfileKind(str, Enum):
    DEV = "dev"
    LOCAL_BETA = "local_beta"
    PORTABLE = "portable"
    WORKER = "worker"
    STUDIO = "studio"
    MINIMAL_CLI = "minimal_cli"


class ModulePack(str, Enum):
    CORE_ONLY = "core_only"
    CREATOR_STUDIO = "creator_studio"
    RENDERING_PACK = "rendering_pack"
    AI_WORKER_PACK = "ai_worker_pack"
    PUBLISHING_PACK = "publishing_pack"
    DEVICE_FARM_PACK = "device_farm_pack"
    RESTRICTED_CREATOR_PACK = "restricted_creator_pack"
    DEVELOPER_PACK = "developer_pack"


class RuntimeMode(str, Enum):
    STUDIO = "studio"
    CLI = "cli"
    WORKER = "worker"
    HEADLESS = "headless"
    GUARDIAN = "guardian"
    SAFE_MODE = "safe_mode"


class DependencyKind(str, Enum):
    PYTHON = "python"
    FFMPEG = "ffmpeg"
    GIT = "git"
    NODE = "node"
    OS_KEYRING = "os_keyring"
    GPU_TOOL = "gpu_tool"
    DEVICE_TOOL = "device_tool"
    OPTIONAL_PLUGIN = "optional_plugin"


class DependencyStatus(str, Enum):
    PRESENT = "present"
    MISSING = "missing"
    OPTIONAL_MISSING = "optional_missing"
    UNSUPPORTED = "unsupported"
    UNKNOWN = "unknown"


class InstallStatus(str, Enum):
    PLANNED = "planned"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ROLLED_BACK = "rolled_back"


@dataclass(frozen=True)
class DependencySpec:
    name: str
    kind: DependencyKind
    required: bool = False
    module_pack: ModulePack | None = None
    version_constraint: str | None = None
    reason: str | None = None


@dataclass(frozen=True)
class DependencyCheck:
    dependency: DependencySpec
    status: DependencyStatus
    detected_version: str | None = None
    message: str = ""


@dataclass(frozen=True)
class PlatformPathProfile:
    target: PackageTarget
    config_dir: str
    workspace_dir: str
    cache_dir: str
    logs_dir: str
    secrets_provider_preference: str = "zip18_vault_reference"
    notes: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class PackageManifest:
    package_id: str
    version: str
    target: PackageTarget
    profile: PackageProfileKind
    module_packs: tuple[ModulePack, ...]
    dependencies: tuple[DependencySpec, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PackageProfile:
    profile_id: str
    target: PackageTarget
    kind: PackageProfileKind
    module_packs: tuple[ModulePack, ...]
    runtime_modes: tuple[RuntimeMode, ...]
    path_profile: PlatformPathProfile | None = None
    dependencies: tuple[DependencySpec, ...] = ()


@dataclass(frozen=True)
class InstallerProfile:
    installer_id: str
    target: PackageTarget
    install_mode: PackageProfileKind
    allow_destructive_changes: bool = False
    require_guardian_check: bool = True
    require_security_check: bool = True


@dataclass(frozen=True)
class InstallStep:
    step_id: str
    description: str
    required: bool = True
    rollback_available: bool = False


@dataclass(frozen=True)
class InstallPlan:
    plan_id: str
    target: PackageTarget
    steps: tuple[InstallStep, ...]
    dependencies: tuple[DependencySpec, ...] = ()
    dry_run_supported: bool = True


@dataclass(frozen=True)
class InstallResult:
    plan_id: str
    status: InstallStatus
    completed_steps: tuple[str, ...] = ()
    failed_step: str | None = None
    message: str = ""


@dataclass(frozen=True)
class BuildProfile:
    build_id: str
    target: PackageTarget
    profile: PackageProfileKind
    output_format: str
    signed_artifact_required: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class MigrationPlan:
    migration_id: str
    from_version: str
    to_version: str
    steps: tuple[InstallStep, ...]
    backup_required: bool = True
    rollback_required: bool = True
    guardian_check_required: bool = True


@dataclass(frozen=True)
class RestrictedCreatorPackPolicy:
    enabled_by_default: bool = False
    opt_in_required: bool = True
    isolate_workspace: bool = True
    isolate_credentials: bool = True
    isolate_logs: bool = True
    require_manual_review: bool = True
    require_consent_metadata: bool = True
    require_all_participants_18_plus: bool = True
    package_real_media: bool = False
    package_real_credentials: bool = False
