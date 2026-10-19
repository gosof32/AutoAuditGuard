# 🛡️ AutoAuditGuard — Intelligent Contract Code Security Auditor

An **Intelligent Contract Primitive** built on **GenLayer** that performs autonomous smart contract security audits using multi-validator AI consensus.

---

## 🌟 Key Features
- **Autonomous On-Chain Auditing:** Evaluates submitted code snippets without centralized agencies.
- **AI Consensus Engine:** Uses `gl.exec_prompt` across validator ensembles to produce security verdicts (`SAFE` vs `VULNERABLE`).
- **Reusable Primitive:** Ideal for integration into decentralized launchpads or code deployment gates.

---

## 🧪 Testing in GenLayer Studio
1. Deploy `AutoAuditGuard.py` in **GenLayer Studio**.
2. Call `submit_code_for_audit` with your code snippet and address.
3. Call `run_audit` with the generated `audit_id`.
4. View the result using `get_audit_report`.
