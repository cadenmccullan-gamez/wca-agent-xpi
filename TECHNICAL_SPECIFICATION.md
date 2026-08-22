# WCA-XPI Technical Specification

**Status:** Public-source review edition, version 1.3.1  
**Repository role:** Python reference library for bounded text processing, configurable pattern redaction, process-local role checks, confirmation gates, and in-memory audit/provenance utilities.  
**Verification baseline:** The repository test suite passed in a clean Python virtual environment on August 22, 2026.

## 1. Purpose and Scope

WCA-XPI provides small, composable Python classes for applying predefined language substitutions, detecting and redacting selected identifier patterns, requiring an explicit operator role for bounded processing, recording an in-memory hash-linked audit trail, generating a provenance record, and applying a two-step confirmation gate to a caller-supplied function.

The library is intended for **application-layer reference use and integration experiments**. It does not provide identity verification, authentication, durable audit storage, encryption key management, secure session management, legal compliance certification, LLM inference, LLM token-layer control, financial forecasting, or production authorization.

> **Important limitation:** The `DeterministicCoherenceGate` currently verifies the presence of keys named in a caller-supplied `required` list. It does not perform JSON Schema validation, token-level model control, or semantic correctness evaluation.

## 2. Supported Runtime and Installation

The project requires Python 3.10 or later. The documented development installation is:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest -q
```

The library has no declared runtime third-party dependency. The development extra installs `pytest` for the verified test suite.

## 3. Functional Components

| Component | Implemented behavior | Explicit boundary |
|---|---|---|
| `WCAEngine` | Coordinates authorization, string redaction, language substitutions, output register checks, audit events, and a generated provenance block. | Stores state only in process memory and accepts caller-supplied operator and session identifiers. |
| `LinguisticsController` | Replaces predefined case-insensitive phrases and reports any remaining configured phrases. | It is a string-substitution and phrase-detection utility, not a general language-quality or policy engine. |
| `PrivacyGuard` | Detects and redacts configured email, U.S. SSN, and phone-number patterns in strings and supported containers. | It does not guarantee complete PII detection, jurisdictional compliance, or redaction of unconfigured identifiers. |
| `AccessManager` | Assigns `viewer`, `analyst`, or `administrator` roles in memory and checks named permissions. | It does not authenticate identities or persist roles. |
| `AuditLogger` | Appends JSON-serializable records to a process-local SHA-256 hash chain and verifies chain continuity. | Durable, independently protected storage is required for deployment-grade audit retention. |
| `ConfirmationGate` | Requires a generated blueprint and an explicit Boolean approval before invoking a caller-supplied function. | It does not provide an external approval workflow, durable approval record, or authorization proof. |
| `ProvenanceLedger` | Generates a SHA-256 hash record for supplied output, session token, timestamp, node identifier, and attribution text. | It is a local provenance record, not a cryptographic signature or identity-attested ledger. |
| `DataRetentionPolicy` | Evaluates whether a timestamp falls inside a configurable time window. | It does not delete, retain, encrypt, or store records. |
| `FinancialOptimizer` | Applies caller-supplied numeric thresholds to an input description and returns deterministic labels. | It does not calculate returns, validate financial data, or provide investment analysis. |
| `MarketAnalyzer` | Formats caller-supplied design and monetization inputs into deterministic result dictionaries. | It does not collect market data, benchmark real products, or verify commercial claims. |

## 4. Core Processing Contract

A caller using `WCAEngine` first registers an operator with an assignable role. `process_input` requires the registered operator to hold the `read` permission, redacts configured patterns when `no_pii=True`, and records only the original input length in the in-memory audit trail.

`finalize_output` requires a non-empty caller-supplied session token. It then applies the configured language substitutions, verifies that configured prohibited phrases no longer appear, generates a local provenance dictionary, records an output-finalized audit event, and returns the tuple `(scrubbed_text, is_compliant, provenance_block)`.

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

The example demonstrates only a local processing flow. It does not establish user identity, persist records, or connect to an AI model.

## 5. Control Model

| Control | Implemented condition | Failure behavior |
|---|---|---|
| Operator authorization | `process_input` requires the registered role to include `read`. | Raises `PermissionError`. |
| Required session identifier | `finalize_output` rejects an empty or whitespace-only session token. | Raises `ValueError`. |
| Confirmation gate | `execute_with_approval` requires a blueprint and `approval_flag=True`. | Raises `PermissionError`. |
| Audit record integrity | Audit records are hash-linked to their predecessor. | `verify_integrity()` returns `False` when a chain link or hash does not match. |
| Structured audit details | `AuditLogger` requires JSON-serializable event details. | Raises `ValueError`. |
| Configured PII patterns | Email, U.S. SSN, and telephone expressions can be detected/redacted. | Matching values are replaced with a defined marker when redaction is enabled. |

## 6. Non-Goals and Deployment Requirements

A production integration must add its own authentication, authorization source, secret handling, durable append-only storage, log access control, encryption, monitoring, incident response, privacy assessment, model evaluation, and domain-specific legal or regulatory review. Do not treat an in-process hash chain as a durable audit system or a generated provenance block as proof of an author’s identity.

The finance- and market-named modules only transform values supplied by their caller. They must not be used to support an investment, commercial, or pricing claim without independent data, methodology, and appropriate professional review.

## 7. Verification and Acceptance Criteria

| Requirement | Evidence |
|---|---|
| Package installation works in a clean environment. | `python -m pip install -e ".[dev]"` succeeds. |
| Policy, privacy, gate, audit, provenance, finance-labeling, and market-labeling behaviors are regression tested. | `python -m pytest -q` succeeds. |
| Documentation claims remain aligned to implemented interfaces. | README and this specification are reviewed with any public API change. |
| Production claims remain bounded. | No release document describes the library as a general compliance system, identity system, LLM runtime, investment engine, or token-control system. |

## 8. Change Control

A change to an exported class, method signature, predefined phrase mapping, identifier pattern, role permission, audit-record schema, or documented limitation is a material interface change. Such changes require updated tests, this specification, the README, and release notes before publication.
