from __future__ import annotations

from abc import ABC, abstractmethod

from .models import (
    PackageManifest,
    PackageProfile,
    InstallerProfile,
    InstallPlan,
    InstallResult,
    DependencySpec,
    DependencyCheck,
    RuntimeMode,
    MigrationPlan,
)


class PackageBuilder(ABC):
    """Builds package artifacts from manifests and profiles."""

    @abstractmethod
    def build(self, manifest: PackageManifest, profile: PackageProfile) -> str:
        raise NotImplementedError


class InstallerRuntime(ABC):
    """Executes install plans without owning business logic."""

    @abstractmethod
    def create_plan(self, profile: InstallerProfile) -> InstallPlan:
        raise NotImplementedError

    @abstractmethod
    def run_plan(self, plan: InstallPlan) -> InstallResult:
        raise NotImplementedError


class DependencyChecker(ABC):
    """Checks dependencies for selected module packs."""

    @abstractmethod
    def check(self, dependency: DependencySpec) -> DependencyCheck:
        raise NotImplementedError


class AppLauncher(ABC):
    """Launches AutoShortAI modes through explicit runtime profiles."""

    @abstractmethod
    def launch(self, mode: RuntimeMode) -> None:
        raise NotImplementedError


class MigrationRunner(ABC):
    """Runs safe migrations with rollback readiness."""

    @abstractmethod
    def dry_run(self, plan: MigrationPlan) -> InstallResult:
        raise NotImplementedError

    @abstractmethod
    def run(self, plan: MigrationPlan) -> InstallResult:
        raise NotImplementedError


class PackagingVerifier(ABC):
    """Verifies package safety, compatibility, and dependency scope."""

    @abstractmethod
    def verify_manifest(self, manifest: PackageManifest) -> tuple[str, ...]:
        raise NotImplementedError
