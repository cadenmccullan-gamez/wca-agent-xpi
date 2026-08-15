"""
Unit tests for WCAEngine orchestration module.
"""

import pytest
from wca.engine import WCAEngine

def test_engine_workflow():
    engine = WCAEngine(strict_mode=True, no_pii=True)

    input_text = "Hello test@example.com"
    sanitized = engine.process_input(input_text)
    assert "[REDACTED_EMAIL]" in sanitized

    output_text = "I think my pleasure is complete."
    final, compliant = engine.finalize_output(output_text)
    assert "analysis indicates" in final
    assert "requirement satisfied" in final
    assert compliant is True
