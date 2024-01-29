class LLMCostEstimator:
    """
    Price per 1k tokens.
    """
    
    RATES = {
        "gpt-4": {"in": 0.03, "out": 0.06},
        "gpt-3.5-turbo": {"in": 0.001, "out": 0.002}
    }

    def estimate(self, model, input_tokens, output_tokens):
        rate = self.RATES.get(model, self.RATES["gpt-3.5-turbo"])
        cost = (input_tokens/1000 * rate["in"]) + (output_tokens/1000 * rate["out"])
        return cost
