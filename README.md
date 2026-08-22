# WCA-XPI

**World Class Assistant Agent eXecution and Programming Interface**

WCA-XPI is a Python reference library for bounded text processing, configured identifier-pattern redaction, process-local role checks, confirmation gates, in-memory audit records, and generated provenance records. It is designed for source review and application-layer integration experiments under human direction.

> **Release status:** See [RELEASE_STATUS.md](RELEASE_STATUS.md). For exact supported behavior and limitations, see the [technical specification](TECHNICAL_SPECIFICATION.md).

## What Is Implemented

| Component | Verified behavior |
|---|---|
| `WCAEngine` | Coordinates registered-operator checks, configured string redaction, language substitutions, output register checks, local audit events, and a provenance dictionary. |
| `LinguisticsController` | Applies predefined case-insensitive phrase replacements and reports configured phrases that remain. |
| `PrivacyGuard` | Detects and redacts configured email, U.S. SSN, and telephone patterns in strings and supported containers. |
| `AccessManager` | Holds process-local assignments for `viewer`, `analyst`, and `administrator` roles and checks named permissions. |
| `AuditLogger` | Maintains an in-memory SHA-256 hash-linked event sequence and checks its continuity. |
| `ConfirmationGate` | Requires a generated blueprint and explicit Boolean approval before executing a caller-supplied function. |
| `ProvenanceLedger` | Generates a local hash record from supplied text, session identifier, timestamp, node identifier, and attribution text. |
| `FinancialOptimizer` and `MarketAnalyzer` | Return deterministic dictionaries from caller-supplied values; they do not retrieve or validate external financial or market data. |

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest -q
```

```python
from wca.engine import WCAEngine

engine = WCAEngine()
engine.register_operator("reviewer-1", "viewer")
clean_input = engine.process_input("Contact user@example.com", "reviewer-1")
text, compliant, provenance = engine.finalize_output(
    "The input is ready for review.",
    session_token="review-session-001",
)
```

## Architecture and Limits

WCA-XPI is a local library. It does not authenticate identities, persist audit records, manage encryption keys, provide durable approvals, prove authorship, perform general PII detection, control LLM behavior at the token layer, invoke an LLM, or certify compliance. A production integration must add identity, authorization, secure storage, encryption, monitoring, incident response, and domain-specific review.

The `DeterministicCoherenceGate` checks the presence of caller-defined required keys. It is not a complete JSON Schema validator, semantic evaluator, or model-control mechanism. The `AuditLogger` and `ProvenanceLedger` are process-local utilities, not independently protected durable ledgers or cryptographic signature systems.

## Documentation

| Document | Purpose |
|---|---|
| [TECHNICAL_SPECIFICATION.md](TECHNICAL_SPECIFICATION.md) | Supported interfaces, control conditions, boundaries, and acceptance criteria. |
| [RELEASE_STATUS.md](RELEASE_STATUS.md) | Verified quality gates, rights notice, and current maturity. |
| [INSTALL.md](INSTALL.md) | Installation and integration guidance. |
| [USER_GUIDE.md](USER_GUIDE.md) | Usage-oriented examples and interface explanation. |
| [ETHICAL_GOVERNANCE.md](ETHICAL_GOVERNANCE.md) | Governance and communication framework. |

## Rights Notice

No public-use license file is included in this repository at this release baseline. The rights holder should select explicit reuse terms before publishing permission to copy, modify, distribute, or deploy the software. Source visibility supports review and does not state a reuse license.
