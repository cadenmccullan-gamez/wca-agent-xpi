"""
World Class Assistant (WCA) Package
Implements operational frameworks, linguistic controls, deterministic coherence gates,
enterprise security, compliance, financial optimization, and market design modules.
Attribution: Axiom Hive Intelligence Technology
"""

from .engine import WCAEngine
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import DeterministicCoherenceGate, ConfirmationGate
from .security import AuditLogger, AccessManager
from .compliance import ProvenanceLedger, DataRetentionPolicy
from .finance import FinancialOptimizer
from .market import MarketAnalyzer

__version__ = "1.3.1"
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
    "MarketAnalyzer",
]
