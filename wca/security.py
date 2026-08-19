"""Audit-trail integrity and explicit role-based access controls.

Authorship: Alexis M. Adams
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from typing import Any, Mapping


class AuditLogger:
    """Maintain an in-process hash-chained audit trail with integrity verification.

    The trail is append-only only within this process. Durable, independently
    protected storage is required for deployment-grade audit retention.
    """

    def __init__(self) -> None:
        self._logs: list[dict[str, Any]] = []

    @staticmethod
    def _canonical_json(value: Mapping[str, Any]) -> str:
        try:
            return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        except (TypeError, ValueError) as exc:
            raise ValueError("Audit event details must be JSON-serializable.") from exc

    @classmethod
    def _event_hash(cls, payload: Mapping[str, Any], previous_hash: str) -> str:
        encoded = cls._canonical_json({"previous_hash": previous_hash, **payload})
        return sha256(encoded.encode("utf-8")).hexdigest()

    def log_event(self, event_type: str, operator: str, details: Mapping[str, Any]) -> dict[str, Any]:
        """Record one validated event and return a defensive copy of its receipt."""
        if not event_type.strip():
            raise ValueError("event_type must not be empty.")
        if not operator.strip():
            raise ValueError("operator must not be empty.")

        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "operator": operator,
            "details": deepcopy(dict(details)),
        }
        previous_hash = self._logs[-1]["current_hash"] if self._logs else "0" * 64
        record = {
            **payload,
            "prev_hash": previous_hash,
            "current_hash": self._event_hash(payload, previous_hash),
        }
        self._logs.append(record)
        return deepcopy(record)

    def verify_integrity(self) -> bool:
        """Return whether every stored event has a valid, contiguous hash link."""
        previous_hash = "0" * 64
        for record in self._logs:
            payload = {
                "timestamp": record.get("timestamp"),
                "event_type": record.get("event_type"),
                "operator": record.get("operator"),
                "details": record.get("details"),
            }
            if record.get("prev_hash") != previous_hash:
                return False
            if record.get("current_hash") != self._event_hash(payload, previous_hash):
                return False
            previous_hash = record["current_hash"]
        return True

    def export_audit_trail(self) -> tuple[dict[str, Any], ...]:
        """Return immutable external copies of the recorded audit events."""
        return tuple(deepcopy(record) for record in self._logs)


class AccessManager:
    """Enforce explicit role assignments for privileged operations."""

    ROLE_PERMISSIONS: dict[str, frozenset[str]] = {
        "guest": frozenset(),
        "viewer": frozenset({"read"}),
        "analyst": frozenset({"read", "execute_blueprint", "audit"}),
        "administrator": frozenset({"read", "execute_blueprint", "audit", "configure", "override"}),
    }

    def __init__(self) -> None:
        self._operator_roles: dict[str, str] = {}

    def register_operator(self, operator: str, role: str) -> None:
        """Assign a validated role to a caller-controlled operator identifier."""
        if not operator.strip():
            raise ValueError("operator must not be empty.")
        if role not in self.ROLE_PERMISSIONS or role == "guest":
            raise ValueError("role must be an assignable role.")
        self._operator_roles[operator] = role

    def revoke_operator(self, operator: str) -> None:
        """Remove an operator assignment; unregistered identities have no permissions."""
        self._operator_roles.pop(operator, None)

    def verify_permission(self, operator: str, permission: str) -> bool:
        """Return whether an explicitly assigned operator has the requested permission."""
        role = self._operator_roles.get(operator, "guest")
        return permission in self.ROLE_PERMISSIONS[role]
