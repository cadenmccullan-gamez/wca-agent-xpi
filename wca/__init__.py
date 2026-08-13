"""
World Class Assistant (WCA) Package
Implements operational frameworks, linguistic controls, and deterministic coherence gates.
"""

from .engine import WCAEngine
from .linguistics import LinguisticsController
from .privacy import PrivacyGuard
from .gates import DeterministicCoherenceGate, ConfirmationGate

__version__ = "1.0.0"
__all__ = [
    "WCAEngine",
    "LinguisticsController",
    "PrivacyGuard",
    "DeterministicCoherenceGate",
    "ConfirmationGate",
]
