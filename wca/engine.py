"""
WCA Engine Module
Orchestrates linguistic control, privacy auditing, execution gates,
audit logging, access control, and provenance tracking.
"""

from typing import Dict, Any, Tuple
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import ConfirmationGate, DeterministicCoherenceGate
from .security import AuditLogger, AccessManager
from .compliance import ProvenanceLedger, DataRetentionPolicy

class WCAEngine:
    """Main execution engine for the World Class Assistant framework."""

    def __init__(self, strict_mode: bool = True, no_pii: bool = True, node_id: str = "WCA-NODE-01"):
        self.linguistics = LinguisticsController(strict_mode=strict_mode)
        self.privacy = PrivacyGuard(no_pii=no_pii)
        self.confirmation = ConfirmationGate()
        self.audit_logger = AuditLogger()
        self.access_manager = AccessManager()
        self.provenance = ProvenanceLedger(node_id=node_id)
        self.retention = DataRetentionPolicy()

    def process_input(self, raw_input: str, operator: str = "system_analyst") -> str:
        """Sanitizes incoming text and records audit event."""
        if not self.access_manager.verify_permission(operator, "read"):
            raise PermissionError(f"Operator '{operator}' lacks 'read' permission.")

        sanitized = self.privacy.sanitize(raw_input)
        self.audit_logger.log_event("INPUT_PROCESSED", operator, {"input_length": len(raw_input)})
        return sanitized

    def finalize_output(self, raw_output: str, session_token: str = "EPHEMERAL_TOKEN") -> Tuple[str, bool, Dict[str, Any]]:
        """Applies linguistic scrubbing, verifies register, and generates provenance."""
        scrubbed = self.linguistics.scrub_text(raw_output)
        is_compliant, violations = self.linguistics.verify_register(scrubbed)
        provenance_block = self.provenance.generate_provenance_block(scrubbed, session_token)
        
        self.audit_logger.log_event("OUTPUT_FINALIZED", "system_engine", {
            "compliant": is_compliant,
            "violations_count": len(violations)
        })

        return scrubbed, is_compliant, provenance_block
