from __future__ import annotations

from .models import (
    DependencyKind,
    DependencySpec,
    ModulePack,
    PackageProfile,
    PackageProfileKind,
    PackageTarget,
    PlatformPathProfile,
    RestrictedCreatorPackPolicy,
    RuntimeMode,
)


def linux_default_paths() -> PlatformPathProfile:
    return PlatformPathProfile(
        target=PackageTarget.LINUX_DESKTOP,
        config_dir="~/.config/autoshortai",
        workspace_dir="~/AutoShortAI/Workspace",
        cache_dir="~/.cache/autoshortai",
        logs_dir="~/.local/state/autoshortai/logs",
    )


def default_core_profile() -> PackageProfile:
    return PackageProfile(
        profile_id="core_only_linux_dev",
        target=PackageTarget.LINUX_DESKTOP,
        kind=PackageProfileKind.DEV,
        module_packs=(ModulePack.CORE_ONLY, ModulePack.DEVELOPER_PACK),
        runtime_modes=(RuntimeMode.CLI, RuntimeMode.GUARDIAN, RuntimeMode.SAFE_MODE),
        path_profile=linux_default_paths(),
        dependencies=(
            DependencySpec(
                name="python",
                kind=DependencyKind.PYTHON,
                required=True,
                module_pack=ModulePack.CORE_ONLY,
                reason="Base Python runtime for architecture contracts.",
            ),
        ),
    )


def rendering_pack_dependencies() -> tuple[DependencySpec, ...]:
    return (
        DependencySpec(
            name="ffmpeg",
            kind=DependencyKind.FFMPEG,
            required=False,
            module_pack=ModulePack.RENDERING_PACK,
            reason="Optional renderer provider dependency for future ZIP12 implementation.",
        ),
    )


def restricted_creator_pack_policy() -> RestrictedCreatorPackPolicy:
    return RestrictedCreatorPackPolicy()
