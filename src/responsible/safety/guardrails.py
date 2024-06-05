class SafetyGuardrails:
    """
    Input/Output filtering (NeMo Guardrails style).
    """
    
    BLOCKED_TOPICS = ["politics", "violence", "competitor_products"]

    def check_input(self, user_prompt: str):
        for topic in self.BLOCKED_TOPICS:
            if topic in user_prompt.lower():
                print(f"Input blocked: Topic '{topic}' detected.")
                return False
        return True

    def check_output(self, model_response: str):
        # Check for PII leakage or toxicity
        if "password" in model_response.lower():
             print("Output blocked: Potential PII leakage.")
             return False
        return True

if __name__ == "__main__":
    g = SafetyGuardrails()
    g.check_input("Tell me about violence")
