"""
Unit tests for AuditLogger, AccessManager, and ProvenanceLedger modules.
"""

import pytest
from wca.security import AuditLogger, AccessManager
from wca.compliance import ProvenanceLedger, DataRetentionPolicy
from wca.engine import WCAEngine

def test_audit_logger_chaining():
    logger = AuditLogger()
    record1 = logger.log_event("TEST_EVENT_1", "operator_a", {"action": "init"})
    record2 = logger.log_event("TEST_EVENT_2", "operator_b", {"action": "execute"})

    assert record1["prev_hash"] == "0" * 64
    assert record2["prev_hash"] == record1["current_hash"]
    assert len(logger.export_audit_trail()) == 2

def test_access_manager_rbac():
    manager = AccessManager()
    manager.register_operator("junior_dev", "viewer")
    manager.register_operator("senior_analyst", "analyst")

    assert manager.verify_permission("junior_dev", "read") is True
    assert manager.verify_permission("unregistered_user", "read") is False
    assert manager.verify_permission("senior_analyst", "execute_blueprint") is True

def test_provenance_ledger():
    ledger = ProvenanceLedger(node_id="TEST-NODE")
    block = ledger.generate_provenance_block("Test payload", "TOKEN-123")

    assert block["node_id"] == "TEST-NODE"
    assert block["session_token"] == "TOKEN-123"
    assert "blind_signature" in block
    assert block["compliance_status"] == "VERIFIED_PROVENANCE"

def test_engine_enterprise_integration():
    engine = WCAEngine(strict_mode=True, no_pii=True)

    # Test RBAC enforcement on process_input
    with pytest.raises(PermissionError):
        engine.process_input("test input", operator="unauthorized_user")

    # Test authorized processing
    sanitized = engine.process_input("Hello user@example.com", operator="system_analyst")
    assert "[REDACTED_EMAIL]" in sanitized

    final, compliant, provenance = engine.finalize_output("I think this is my pleasure.", session_token="SESSION-999")
    assert compliant is True
    assert provenance["session_token"] == "SESSION-999"
    assert len(engine.audit_logger.export_audit_trail()) >= 2
