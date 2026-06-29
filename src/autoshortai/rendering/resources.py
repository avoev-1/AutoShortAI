from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RenderResourceBudget:
    max_cpu_percent: float = 80.0
    max_ram_mb: int = 4096
    max_duration_seconds: float = 1800.0
    max_parallel_renders: int = 1
    allow_final_render_on_battery: bool = False
