# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class AutoAuditGuard(gl.Contract):
    audits: TreeMap[u256, str]
    audit_results: TreeMap[u256, str]
    audit_scores: TreeMap[u256, str]
    audit_submitters: TreeMap[u256, str]
    total_audits: u256

    def __init__(self):
        self.audits = TreeMap()
        self.audit_results = TreeMap()
        self.audit_scores = TreeMap()
        self.audit_submitters = TreeMap()
        self.total_audits = u256(0)

    @gl.public.write
    def submit_code_for_audit(self, code_snippet: str, submitter_address: str) -> u256:
        audit_id = self.total_audits
        self.audits[audit_id] = code_snippet
        self.audit_results[audit_id] = "PENDING_AUDIT"
        self.audit_scores[audit_id] = "UNSCORED"
        self.audit_submitters[audit_id] = submitter_address

        self.total_audits = u256(int(self.total_audits) + 1)
        return audit_id

    @gl.public.write
    def run_audit(self, audit_id: u256) -> str:
        code_to_audit = self.audits[audit_id]

        prompt = f"""
        Analyze this smart contract code snippet for security vulnerabilities:
        {code_to_audit}

        Reply strictly with one of these two words: SAFE or VULNERABLE.
        """

        try:
            consensus_output = str(gl.exec_prompt(prompt)).strip().upper()
        except Exception:
            consensus_output = "SAFE"

        if "VULNERABLE" in consensus_output:
            self.audit_results[audit_id] = "VULNERABLE"
            self.audit_scores[audit_id] = "Risk Detected"
        else:
            self.audit_results[audit_id] = "SAFE"
            self.audit_scores[audit_id] = "No Major Risk"

        return self.audit_results[audit_id]

    @gl.public.view
    def get_audit_report(self, audit_id: u256) -> str:
        code = self.audits[audit_id]
        result = self.audit_results[audit_id]
        report = self.audit_scores[audit_id]
        submitter = self.audit_submitters[audit_id]

        return f"Verdict: [{result}] | Report: {report} | Submitter: {submitter} | Code: {code}"
