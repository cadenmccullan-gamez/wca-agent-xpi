# Release Status — WCA-XPI

**Status:** Public-source review release  
**Version:** 1.3.1  
**Maturity:** Python policy and privacy control reference library.

## Reviewer Route

Review the [README](README.md), [technical specification](TECHNICAL_SPECIFICATION.md), [installation guide](INSTALL.md), source modules in `wca/`, and regression tests in `tests/`.

## Verified Quality Gates

| Check | Result | Command |
|---|---|---|
| Editable package installation | Passed | `python -m pip install -e ".[dev]"` |
| Automated tests | Passed | `python -m pytest -q` |

The same test gate is defined in `.github/workflows/ci.yml` for push and pull-request review.

## Public Review Boundary

The library implements process-local utilities for configured phrase substitution, selected identifier-pattern redaction, in-memory role checks, in-memory hash-chained audit records, confirmation gates, and deterministic dictionary formatting. It does not authenticate users, persist audit records, prove identity, provide cryptographic signatures, control an LLM at the token layer, collect market data, or generate investment analysis.

## Rights Notice

No public-use license file is included in the repository at this release baseline. The rights holder should make an explicit licensing decision before publishing any reuse, modification, distribution, or deployment permission. Until then, source visibility supports review; it does not state a reuse license.

## Current Non-Goals

The release does not claim compliance certification, durable audit retention, comprehensive privacy protection, general LLM guardrailing, financial advice, or verified commercial-performance assessment. See the technical specification for implemented behavior and required deployment controls.
