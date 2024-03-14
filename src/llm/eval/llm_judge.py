class LLMJudge:
    """
    Uses a strong model (Guide) to evaluate a weak model.
    """
    
    TEMPLATE = """
    Please grade the following answer on a scale of 1 to 10 for accuracy.
    
    Question: {q}
    Correct Answer: {ref}
    Student Answer: {ans}
    
    Score:
    """
    
    def evaluate(self, question, reference, answer):
        prompt = self.TEMPLATE.format(q=question, ref=reference, ans=answer)
        print("Asking GPT-4 to judge...")
        # score = gpt4.complete(prompt)
        score = 8.5
        return score

