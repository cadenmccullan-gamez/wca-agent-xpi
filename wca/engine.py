"""Orchestration for linguistic, privacy, authorization, and provenance controls.

Authorship: Alexis M. Adams
"""

from __future__ import annotations

from typing import Any

from .compliance import DataRetentionPolicy, ProvenanceLedger
from .gates import ConfirmationGate, DeterministicCoherenceGate
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .security import AccessManager, AuditLogger


class WCAEngine:
    """Coordinate bounded processing for explicitly authorized operators."""

    def __init__(self, strict_mode: bool = True, no_pii: bool = True, node_id: str = "WCA-NODE-01") -> None:
        self.attribution = "Axiom Hive Technology"
        self.linguistics = LinguisticsController(strict_mode=strict_mode)
        self.privacy = PrivacyGuard(no_pii=no_pii)
        self.confirmation = ConfirmationGate()
        self.audit_logger = AuditLogger()
        self.access_manager = AccessManager()
        self.provenance = ProvenanceLedger(node_id=node_id)
        self.retention = DataRetentionPolicy()

    def register_operator(self, operator: str, role: str) -> None:
        """Register an operator before the engine accepts that operator's input."""
        self.access_manager.register_operator(operator, role)

    def process_input(self, raw_input: str, operator: str) -> str:
        """Sanitize authorized input and record only metadata in the audit trail."""
        if not self.access_manager.verify_permission(operator, "read"):
            raise PermissionError(f"Operator '{operator}' lacks 'read' permission.")

        sanitized = self.privacy.sanitize(raw_input)
        self.audit_logger.log_event("INPUT_PROCESSED", operator, {"input_length": len(raw_input)})
        return sanitized

    def finalize_output(self, raw_output: str, session_token: str) -> tuple[str, bool, dict[str, Any]]:
        """Apply output controls and create provenance for an explicitly supplied session identifier."""
        if not session_token.strip():
            raise ValueError("session_token must not be empty.")

        scrubbed = self.linguistics.scrub_text(raw_output)
        is_compliant, violations = self.linguistics.verify_register(scrubbed)
        provenance_block = self.provenance.generate_provenance_block(scrubbed, session_token)
        self.audit_logger.log_event(
            "OUTPUT_FINALIZED",
            "wca_engine",
            {"compliant": is_compliant, "violations_count": len(violations)},
        )
        return scrubbed, is_compliant, provenance_block
