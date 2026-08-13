"""
WCA Engine Module
Orchestrates linguistic control, privacy auditing, and execution gates.
"""

from typing import Dict, Any, Tuple
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import ConfirmationGate, DeterministicCoherenceGate

class WCAEngine:
    """Main execution engine for the World Class Assistant framework."""

    def __init__(self, strict_mode: bool = True, no_pii: bool = True):
        self.linguistics = LinguisticsController(strict_mode=strict_mode)
        self.privacy = PrivacyGuard(no_pii=no_pii)
        self.confirmation = ConfirmationGate()

    def process_input(self, raw_input: str) -> str:
        """Sanitizes incoming text for privacy and constraints."""
        sanitized = self.privacy.sanitize(raw_input)
        return sanitized

    def finalize_output(self, raw_output: str) -> Tuple[str, bool]:
        """Applies linguistic scrubbing and verifies register compliance."""
        scrubbed = self.linguistics.scrub_text(raw_output)
        is_compliant, violations = self.linguistics.verify_register(scrubbed)
        return scrubbed, is_compliant
