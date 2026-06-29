"""Creative variant planning boundary.

This module intentionally exposes contracts only. Future implementation classes
must live behind this boundary without coupling ZIP07 to a concrete provider.
"""
from __future__ import annotations

from .contracts import VariantPlannerContract

__all__ = ["VariantPlannerContract"]
