"""
World Class Assistant (WCA) Package
Implements operational frameworks, linguistic controls, deterministic coherence gates,
enterprise security, and compliance modules.
"""

from .engine import WCAEngine
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import DeterministicCoherenceGate, ConfirmationGate
from .security import AuditLogger, AccessManager
from .compliance import ProvenanceLedger, DataRetentionPolicy

__version__ = "1.1.0"
__all__ = [
    "WCAEngine",
    "LinguisticsController",
    "PrivacyGuard",
    "DeterministicCoherenceGate",
    "ConfirmationGate",
    "AuditLogger",
    "AccessManager",
    "ProvenanceLedger",
    "DataRetentionPolicy",
]
