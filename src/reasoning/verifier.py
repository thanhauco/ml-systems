import random

class StepVerifier:
    """
    Process Reward Model (PRM) simulation.
    Scores individual reasoning steps to guide search.
    """
    
    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold

    def score_step(self, step_content: str, context: str) -> float:
        """
        Assigns a scalar reward to a reasoning step.
        """
        # Heuristic simulation: complex words might imply deeper thought?
        # In reality, this is a trained classifier.
        base_score = 0.5 + (0.4 * random.random())
        
        if "Verify" in step_content or "Check" in step_content:
            base_score += 0.1
            
        return min(1.0, base_score)

    def is_valid(self, step_content: str) -> bool:
        return self.score_step(step_content, "") > self.threshold
