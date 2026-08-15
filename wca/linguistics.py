"""
Linguistic and Vocabulary Control Module
Enforces professional engineering register and eliminates anthropomorphic phrasing.
"""

import re
from typing import Dict, List, Tuple

class LinguisticsController:
    """Controls vocabulary tiers and eliminates ambiguous or anthropomorphic phrasing."""

    PROHIBITED_MAPPINGS: Dict[str, str] = {
        r"my pleasure": "requirement satisfied",
        r"happy to help": "output generated",
        r"i think": "analysis indicates",
        r"i believe": "data suggests",
        r"competence": "function",
        r"i understand": "input processed",
        r"feel": "assess",
        r"exciting": "noteworthy",
        r"i authored": "human-generated content processed",
        r"my ideology": "human-constructed ideology processed",
        r"i created": "human-designed requirement executed",
        r"as an ai": "as a functional utility",
        r"independent purpose": "human-directed objective",
    }

    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode

    def scrub_text(self, text: str) -> str:
        """Replaces prohibited anthropomorphic phrases with engineering equivalents."""
        scrubbed = text
        for pattern, replacement in self.PROHIBITED_MAPPINGS.items():
            # Case-insensitive replacement while preserving word boundaries
            regex = re.compile(re.escape(pattern), re.IGNORECASE)
            scrubbed = regex.sub(replacement, scrubbed)
        return scrubbed

    def verify_register(self, text: str) -> Tuple[bool, List[str]]:
        """Verifies text against register constraints and returns violations."""
        violations = []
        lower_text = text.lower()
        for pattern in self.PROHIBITED_MAPPINGS.keys():
            if pattern in lower_text:
                violations.append(f"Prohibited phrase detected: '{pattern}'")
        return len(violations) == 0, violations
