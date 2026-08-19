"""Structured privacy controls for constrained processing.

Authorship: Alexis M. Adams
"""

from __future__ import annotations

import re
from typing import Any


class PrivacyGuard:
    """Detect and redact configured identifier patterns in supported data structures."""

    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    SSN_REGEX = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
    PHONE_REGEX = re.compile(r"(?<!\w)\+?[1-9]\d{6,14}(?!\w)")

    def __init__(self, no_pii: bool = True) -> None:
        self.no_pii = no_pii

    def contains_pii(self, value: Any) -> bool:
        """Return whether a supported value contains a configured identifier pattern."""
        if isinstance(value, str):
            return bool(
                self.EMAIL_REGEX.search(value)
                or self.SSN_REGEX.search(value)
                or self.PHONE_REGEX.search(value)
            )
        if isinstance(value, dict):
            return any(self.contains_pii(item) for item in value.values())
        if isinstance(value, (list, tuple, set, frozenset)):
            return any(self.contains_pii(item) for item in value)
        return False

    def sanitize(self, data: str) -> str:
        """Redact configured identifier patterns from a string when redaction is enabled."""
        if not self.no_pii:
            return data
        sanitized = self.EMAIL_REGEX.sub("[REDACTED_EMAIL]", data)
        sanitized = self.SSN_REGEX.sub("[REDACTED_SSN]", sanitized)
        return self.PHONE_REGEX.sub("[REDACTED_PHONE]", sanitized)

    def sanitize_payload(self, value: Any) -> Any:
        """Return a structurally equivalent redacted value for supported containers."""
        if not self.no_pii:
            return value
        if isinstance(value, str):
            return self.sanitize(value)
        if isinstance(value, dict):
            return {key: self.sanitize_payload(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self.sanitize_payload(item) for item in value]
        if isinstance(value, tuple):
            return tuple(self.sanitize_payload(item) for item in value)
        if isinstance(value, set):
            return {self.sanitize_payload(item) for item in value}
        return value

    def audit_payload(self, payload: dict[str, Any]) -> bool:
        """Return whether a structured payload is free of configured identifier patterns."""
        return not self.no_pii or not self.contains_pii(payload)
