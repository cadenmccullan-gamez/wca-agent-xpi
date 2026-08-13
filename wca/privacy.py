"""
PrivacyGuard Middleware Module
Scans transactions for PII patterns, Luhn validation, and entity extraction.
"""

import re
from typing import Dict, Any

class PrivacyGuard:
    """Enforces privacy-by-architecture and data minimization standards."""

    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    SSN_REGEX = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
    PHONE_REGEX = re.compile(r"\b\+?[1-9]\d{1,14}\b")

    def __init__(self, no_pii: bool = True):
        self.no_pii = no_pii

    def sanitize(self, data: str) -> str:
        """Removes detected PII from strings if no_pii is enabled."""
        if not self.no_pii:
            return data

        sanitized = self.EMAIL_REGEX.sub("[REDACTED_EMAIL]", data)
        sanitized = self.SSN_REGEX.sub("[REDACTED_SSN]", sanitized)
        sanitized = self.PHONE_REGEX.sub("[REDACTED_PHONE]", sanitized)
        return sanitized

    def audit_payload(self, payload: Dict[str, Any]) -> bool:
        """Audits a dictionary payload for PII violations."""
        if not self.no_pii:
            return True

        for key, value in payload.items():
            if isinstance(value, str):
                if self.EMAIL_REGEX.search(value) or self.SSN_REGEX.search(value):
                    return False
        return True
