from __future__ import annotations

from .models import DependencyCheck, DependencySpec, DependencyStatus


def mark_dependency_status(dependency: DependencySpec, present: bool) -> DependencyCheck:
    if present:
        return DependencyCheck(dependency=dependency, status=DependencyStatus.PRESENT, message="Dependency present.")
    if dependency.required:
        return DependencyCheck(dependency=dependency, status=DependencyStatus.MISSING, message="Required dependency missing.")
    return DependencyCheck(dependency=dependency, status=DependencyStatus.OPTIONAL_MISSING, message="Optional dependency missing.")


def required_dependencies_only(dependencies: tuple[DependencySpec, ...]) -> tuple[DependencySpec, ...]:
    return tuple(dep for dep in dependencies if dep.required)
