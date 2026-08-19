"""Tests for audit, authorization, provenance, and engine integration.

Authorship: Alexis M. Adams
"""

import pytest

from wca.compliance import ProvenanceLedger
from wca.engine import WCAEngine
from wca.security import AccessManager, AuditLogger


def test_audit_logger_detects_tampering_and_protects_exported_records() -> None:
    logger = AuditLogger()
    record_one = logger.log_event("validation_started", "operator_a", {"action": "initialize"})
    record_two = logger.log_event("validation_finished", "operator_b", {"action": "complete"})

    assert record_one["prev_hash"] == "0" * 64
    assert record_two["prev_hash"] == record_one["current_hash"]
    assert logger.verify_integrity() is True

    exported = logger.export_audit_trail()
    with pytest.raises(TypeError):
        exported[0] = {}  # type: ignore[index]
    exported[0]["details"]["action"] = "altered"
    assert logger.export_audit_trail()[0]["details"]["action"] == "initialize"
    assert logger.verify_integrity() is True


def test_access_manager_requires_explicit_role_assignment() -> None:
    manager = AccessManager()
    assert manager.verify_permission("unregistered_operator", "read") is False

    manager.register_operator("reviewer", "viewer")
    manager.register_operator("analyst", "analyst")
    assert manager.verify_permission("reviewer", "read") is True
    assert manager.verify_permission("analyst", "execute_blueprint") is True

    manager.revoke_operator("reviewer")
    assert manager.verify_permission("reviewer", "read") is False


def test_provenance_ledger() -> None:
    ledger = ProvenanceLedger(node_id="validation-node")
    block = ledger.generate_provenance_block("Controlled payload", "session-123")

    assert block["node_id"] == "validation-node"
    assert block["attribution"] == "Axiom Hive Intelligence Technology"
    assert block["session_token"] == "session-123"
    assert "blind_signature" in block
    assert block["compliance_status"] == "VERIFIED_PROVENANCE"


def test_engine_requires_registered_operator_and_session_identifier() -> None:
    engine = WCAEngine(strict_mode=True, no_pii=True)
    with pytest.raises(PermissionError):
        engine.process_input("controlled input", operator="unregistered_operator")

    engine.register_operator("analyst", "analyst")
    sanitized = engine.process_input("Contact user@example.com", operator="analyst")
    assert "[REDACTED_EMAIL]" in sanitized

    _, compliant, provenance = engine.finalize_output(
        "I think this is my pleasure.", session_token="session-456"
    )
    assert compliant is True
    assert provenance["session_token"] == "session-456"
    assert engine.audit_logger.verify_integrity() is True
