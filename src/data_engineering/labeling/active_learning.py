from typing import List, Dict, Any, Callable
import math

class ActiveLearner:
    """
    Selects the most informative samples for labeling.
    """
    
    def __init__(self, model_predict_proba: Callable[[Any], List[float]]):
        self.model = model_predict_proba

    def entropy(self, probas: List[float]) -> float:
        """Calculates Shannon Entropy."""
        return -sum(p * math.log2(p + 1e-9) for p in probas)

    def select_samples(self, pool: List[Dict[str, Any]], n_instances: int) -> List[Dict[str, Any]]:
        """
        Uncertainty Sampling: Choose samples with highest entropy.
        """
        scored_pool = []
        for sample in pool:
            # Assume 'features' key exists
            probs = self.model(sample['features'])
            score = self.entropy(probs)
            scored_pool.append((score, sample))
        
        # Sort desc by uncertainty
        scored_pool.sort(key=lambda x: x[0], reverse=True)
        
        return [x[1] for x in scored_pool[:n_instances]]
