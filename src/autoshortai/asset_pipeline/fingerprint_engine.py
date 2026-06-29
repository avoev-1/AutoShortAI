"""Fingerprint Engine facade. Concrete implementations are added later."""

from __future__ import annotations

from typing import Any

from .contracts import FingerprintEngineContract


class FingerprintEngine:
    """Architectural placeholder for a future FingerprintEngineContract implementation.

    ZIP06 intentionally does not implement production logic. Claude may later
    replace or subclass this facade with a concrete adapter that satisfies the
    public contract.
    """

    contract = FingerprintEngineContract

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._args = args
        self._kwargs = kwargs

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(contract={self.contract.__name__})"
