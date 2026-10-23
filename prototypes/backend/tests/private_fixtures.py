"""Fixturekontext zeigt auch bei fehlgeschlagenen Assertions keine Credentials."""

from typing import Any


class PrivateEnvironment(dict[str, Any]):
    def __repr__(self) -> str:
        return "<Synthetische Testumgebung; Credentials und Geheimnisse ausgeblendet>"
