"""
Enterprise Security Module
Implements Audit Logging and Role-Based Access Control (RBAC).
"""

import time
import hashlib
from typing import Dict, List, Any

class AuditLogger:
    """Maintains an immutable audit log of system transactions and gate events."""

    def __init__(self):
        self.logs: List[Dict[str, Any]] = []

    def log_event(self, event_type: str, operator: str, details: Dict[str, Any]) -> Dict[str, Any]:
        """Records an operational event with cryptographic chaining."""
        timestamp = time.time()
        payload = {
            "timestamp": timestamp,
            "event_type": event_type,
            "operator": operator,
            "details": details,
        }
        # Create hash proof
        prev_hash = self.logs[-1]["current_hash"] if self.logs else "0" * 64
        block_content = f"{prev_hash}{timestamp}{event_type}{operator}{str(details)}"
        current_hash = hashlib.sha256(block_content.encode("utf-8")).hexdigest()

        record = {
            **payload,
            "prev_hash": prev_hash,
            "current_hash": current_hash,
        }
        self.logs.append(record)
        return record

    def export_audit_trail(self) -> List[Dict[str, Any]]:
        """Returns the full immutable audit trail."""
        return self.logs


class AccessManager:
    """Enforces Role-Based Access Control (RBAC) for privileged operations."""

    ROLE_PERMISSIONS = {
        "guest": [],
        "viewer": ["read"],
        "analyst": ["read", "execute_blueprint", "audit"],
        "administrator": ["read", "execute_blueprint", "audit", "configure", "override"],
    }

    def __init__(self):
        # Default mapping of operators to roles
        self.operator_roles: Dict[str, str] = {
            "system_analyst": "analyst",
            "root_admin": "administrator",
        }

    def register_operator(self, operator: str, role: str) -> None:
        """Assigns an operational role to an identifier."""
        if role not in self.ROLE_PERMISSIONS:
            raise ValueError(f"Invalid role specified: {role}")
        self.operator_roles[operator] = role

    def verify_permission(self, operator: str, permission: str) -> bool:
        """Verifies whether an operator possesses the required permission."""
        role = self.operator_roles.get(operator, "guest")
        allowed_permissions = self.ROLE_PERMISSIONS.get(role, [])
        return permission in allowed_permissions
