"""
Unit tests for PrivacyGuard module.
"""

import pytest
from wca.privacy import PrivacyGuard

def test_privacy_sanitization():
    guard = PrivacyGuard(no_pii=True)
    text = "Contact user at test@example.com or SSN 123-45-6789."
    sanitized = guard.sanitize(text)

    assert "test@example.com" not in sanitized
    assert "[REDACTED_EMAIL]" in sanitized
    assert "123-45-6789" not in sanitized
    assert "[REDACTED_SSN]" in sanitized

def test_payload_auditing():
    guard = PrivacyGuard(no_pii=True)
    clean_payload = {"status": "active", "code": 200}
    pii_payload = {"user": "test@example.com"}

    assert guard.audit_payload(clean_payload) is True
    assert guard.audit_payload(pii_payload) is False
