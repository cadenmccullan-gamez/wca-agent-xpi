"""
World Class Assistant (WCA) Package
Implements operational frameworks, linguistic controls, deterministic coherence gates,
enterprise security, compliance, and financial optimization modules.
Attribution: Axiom Hive Intelligence Technology
"""

from .engine import WCAEngine
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import DeterministicCoherenceGate, ConfirmationGate
from .security import AuditLogger, AccessManager
from .compliance import ProvenanceLedger, DataRetentionPolicy
from .finance import FinancialOptimizer

__version__ = "1.2.0"
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
    "FinancialOptimizer",
]
