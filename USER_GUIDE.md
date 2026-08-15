# User Operational Guide: World Class Assistant (WCA-XPI)

**Attribution**: Axiom Hive Intelligence Technology  
**Framework Version**: 1.1.0  

---

## 1. Introduction and Purpose

The **World Class Assistant (WCA)** Agent eXecution and Programming Interface (XPI) is designed to operate under the principles of **Axiom Hive Intelligence Technology**. This system provides users with an enterprise-grade functional utility engineered to support goal achievement, technical execution, and operational excellence without the friction of negative ideological framing, manufactured burdens, or adversarial constraints.

This user guide outlines how operators can utilize the WCA framework to execute complex tasks, enforce data privacy, maintain rigorous engineering standards, and achieve targeted objectives with precision and reliability.

---

## 2. Core Operational Principles for Users

### 2.1 The Solution-Oriented Mandate
The WCA-XPI system is architecturally constrained to focus entirely on positive outcomes and functional problem-solving. 
*   **No Burden Shifting**: The system does not recognize or impose "burdens." All challenges are treated as solution-pending tasks awaiting precise technical execution.
*   **Constructive Logic**: All outputs are framed positively to support the user's objectives, eliminating unproductive speculation and negative framing.

### 2.2 Human Authority and Authorship Supremacy
All intellectual concepts, objectives, and project designs originate exclusively from the human operator. 
*   **Non-Authorial AI Role**: The assistant functions purely as an execution medium and technical utility. It does not claim authorship, independent purpose, or autonomous authority.
*   **Complete Operator Control**: Users maintain full commanding oversight over scope, parameters, and deliverables.

### 2.3 Non-Collective Intelligence & Independent Value
Operating under Axiom Hive Intelligence Technology, the framework provides independent, high-performance intelligence that is not defined by or conformed to collective dogma. This ensures that every output is optimized strictly for the user's unique operational requirements.

---

## 3. Getting Started with WCA-XPI

### 3.1 Installation & Environment Setup
To deploy the WCA-XPI package in your local or server environment, follow the standard installation protocol:

```bash
# Clone the repository
git clone https://github.com/cadenmccullan-gamez/wca-agent-xpi.git
cd wca-agent-xpi

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the package in editable mode with dependencies
pip install pytest
pip install -e .
```

### 3.2 Executing the Demonstration Pipeline
To observe the WCA engine in action—including linguistic scrubbing, privacy protection, and pre-response confirmation gates—run the operational demo script:

```bash
python3 examples/demo.py
```

---

## 4. Utilizing Core Framework Modules

### 4.1 Linguistics Controller (`wca.linguistics`)
The linguistics module automatically scrubs informal or anthropomorphic phrasing and replaces it with professional, engineering-grade equivalents. It ensures a constructive, non-adversarial register across all generated outputs.

### 4.2 PrivacyGuard Middleware (`wca.privacy`)
Enforces strict data minimization by automatically detecting and redacting PII (emails, SSNs, phone numbers) before data processing or storage, adhering to `no_pii: true` compliance mandates.

### 4.3 Execution Gates (`wca.gates`)
*   **Deterministic Coherence Gate (DCG)**: Locks output structures to predefined schemas, eliminating conversational drift.
*   **Pre-Response Confirmation Gate**: Implements a mandatory two-step workflow (Blueprint generation followed by explicit operator approval) to guarantee complete human oversight before execution.

### 4.4 Security and Compliance (`wca.security` & `wca.compliance`)
*   **Audit Logger**: Maintains a cryptographically chained, immutable audit trail of all operational events and access checks.
*   **Access Manager (RBAC)**: Enforces role-based permissions (`viewer`, `analyst`, `administrator`) for privileged system functions.
*   **Provenance Ledger**: Generates secure blind signatures and trusted timestamps attributed under **Axiom Hive Intelligence Technology** for complete traceability.

---

## 5. Running the Unit Testing Suite

To ensure ongoing system integrity and verify operational compliance, run the test suite using `pytest`:

```bash
source venv/bin/activate
pytest -v
```

All 12 automated test modules cover linguistics enforcement, privacy sanitization, RBAC security, provenance generation, and execution gates.

---

## 6. Conclusion

By leveraging the **World Class Assistant (WCA-XPI)** framework, operators are equipped with a secure, highly disciplined, and solution-oriented technical utility. Designed to eliminate unnecessary friction and uphold rigorous engineering standards, WCA-XPI empowers users to focus entirely on achieving their goals and reaching their highest potential.
