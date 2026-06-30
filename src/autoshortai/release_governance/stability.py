from __future__ import annotations

from .models import ModuleStabilityEntry, ModuleStabilityMatrix, ModuleStabilityStatus


def default_module_stability_matrix() -> ModuleStabilityMatrix:
    modules = (
        ("zip01", "Production Foundation"),
        ("zip02", "Modular Core Engine"),
        ("zip03", "SDK Plugin System"),
        ("zip04", "Mission Workflow Orchestrator"),
        ("zip05", "Intelligent Distribution Platform"),
        ("zip06", "Smart Asset Pipeline"),
        ("zip07", "Creative Strategy Engine"),
        ("zip08", "Production Queue & Scheduler"),
        ("zip09", "Analytics & Feedback Loop"),
        ("zip10", "Auto-Learning Adaptation Engine"),
        ("zip11", "Lightweight Control Dashboard"),
        ("zip12", "Video Rendering Pipeline"),
        ("zip13", "AI Worker Runtime"),
        ("zip14", "Device Farm Deployment"),
        ("zip15", "Guardian Engine Foundation"),
        ("zip16", "Multi-Platform Publishing Runtime"),
        ("zip17", "Local Workspace & Media Library"),
        ("zip18", "Security, Secrets & Credentials Vault"),
        ("zip19", "Cross-Platform Packaging & Installer"),
        ("zip20", "Beta Stabilization & Release Governance"),
    )
    return ModuleStabilityMatrix(
        baseline="AutoShortAI v1 Architecture Baseline",
        entries=tuple(
            ModuleStabilityEntry(
                module_id=zip_id,
                name=name,
                status=ModuleStabilityStatus.ARCHITECTURE_READY,
                owner_zip=zip_id,
            )
            for zip_id, name in modules
        ),
    )
