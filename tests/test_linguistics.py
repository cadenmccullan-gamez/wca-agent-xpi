"""
Unit tests for LinguisticsController module.
"""

import pytest
from wca.linguistics import LinguisticsController

def test_linguistics_scrubbing():
    controller = LinguisticsController(strict_mode=True)
    raw = "It is my pleasure to help you. I think this works."
    scrubbed = controller.scrub_text(raw)
    assert "my pleasure" not in scrubbed
    assert "requirement satisfied" in scrubbed
    assert "i think" not in scrubbed
    assert "analysis indicates" in scrubbed

def test_register_verification():
    controller = LinguisticsController(strict_mode=True)
    compliant_text = "Analysis indicates the function is operational."
    non_compliant_text = "I think my pleasure is complete."

    is_comp, violations = controller.verify_register(compliant_text)
    assert is_comp is True
    assert len(violations) == 0

    is_comp_nc, violations_nc = controller.verify_register(non_compliant_text)
    assert is_comp_nc is False
    assert len(violations_nc) > 0


def test_authorship_scrubbing():
    controller = LinguisticsController(strict_mode=True)
    raw = "I authored this ideology as an AI with an independent purpose."
    scrubbed = controller.scrub_text(raw)
    assert "i authored" not in scrubbed.lower()
    assert "human-generated content processed" in scrubbed.lower()
    assert "as an ai" not in scrubbed.lower()
    assert "as a functional utility" in scrubbed.lower()
    assert "independent purpose" not in scrubbed.lower()
    assert "human-directed objective" in scrubbed.lower()
