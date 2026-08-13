"""
Demonstration script for World Class Assistant (WCA) package.
Shows linguistic scrubbing, privacy protection, and confirmation gates in action.
"""

from wca import WCAEngine, DeterministicCoherenceGate, ConfirmationGate

def main():
    print("Initializing WCA Engine...")
    engine = WCAEngine(strict_mode=True, no_pii=True)

    # 1. Test Privacy Guard & Linguistics Scrubbing
    user_input = "Hello, my email is user@example.com and I think this is my pleasure to work with you."
    processed_input = engine.process_input(user_input)
    print(f"\n[Input Sanitization]\nOriginal: {user_input}\nSanitized: {processed_input}")

    raw_output = "It is my pleasure to help you. I think the function is operational."
    final_output, compliant = engine.finalize_output(raw_output)
    print(f"\n[Linguistic Scrubbing]\nRaw Output: {raw_output}\nFinal Output: {final_output}\nCompliant: {compliant}")

    # 2. Test Confirmation Gate & DCG
    print("\n[Testing Gates]")
    conf_gate = ConfirmationGate()
    blueprint = conf_gate.generate_blueprint(
        scope="Database Audit",
        domains=["User Logs", "Authentication"],
        format_spec="JSON"
    )
    print(f"Generated Blueprint:\n{blueprint}")

    # Define mock task
    def mock_audit_task():
        return {"status": "SUCCESS", "records_audited": 1420}

    # Execute with approval
    result = conf_gate.execute_with_approval(approval_flag=True, task_func=mock_audit_task)
    print(f"Task Execution Result:\n{result}")

if __name__ == "__main__":
    main()
