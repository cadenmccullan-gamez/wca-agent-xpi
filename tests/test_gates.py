"""
Unit tests for DeterministicCoherenceGate and ConfirmationGate modules.
"""

import pytest
from wca.gates import DeterministicCoherenceGate, ConfirmationGate

def test_deterministic_coherence_gate():
    schema = {"required": ["status", "data"]}
    dcg = DeterministicCoherenceGate(schema)

    valid_output = {"status": "success", "data": [1, 2, 3]}
    invalid_output = {"status": "success"}

    assert dcg.validate_output(valid_output) is True
    assert dcg.validate_output(invalid_output) is False

def test_confirmation_gate_workflow():
    gate = ConfirmationGate()
    blueprint = gate.generate_blueprint("Test Scope", ["Domain A"], "JSON")

    assert blueprint["status"] == "BLUEPRINT_PENDING_APPROVAL"

    def dummy_task():
        return "Executed"

    with pytest.raises(PermissionError):
        gate.execute_with_approval(approval_flag=False, task_func=dummy_task)

    result = gate.execute_with_approval(approval_flag=True, task_func=dummy_task)
    assert result == "Executed"
