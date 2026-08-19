"""Tests for WCA engine orchestration.

Authorship: Alexis M. Adams
"""

from wca.engine import WCAEngine


def test_engine_workflow() -> None:
    engine = WCAEngine(strict_mode=True, no_pii=True)
    engine.register_operator("analyst", "analyst")

    sanitized = engine.process_input("Hello contact@example.com", operator="analyst")
    assert "[REDACTED_EMAIL]" in sanitized

    final, compliant, provenance = engine.finalize_output(
        "I think my pleasure is complete.", session_token="workflow-session"
    )
    assert "analysis indicates" in final
    assert "requirement satisfied" in final
    assert compliant is True
    assert "blind_signature" in provenance
