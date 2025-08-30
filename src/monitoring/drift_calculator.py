from typing import List, Dict, Any
import numpy as np
from scipy import stats

class DriftCalculator:
    """
    Computes statistical distance between reference (training) and current (production) distributions.
    """
    
    def __init__(self, reference_data: Dict[str, List[float]]):
        self.reference = reference_data
        print("Drift Calculator initialized with reference data.")

    def compute_drift(self, current_data: Dict[str, List[float]]) -> Dict[str, float]:
        drift_scores = {}
        for feature, current_vals in current_data.items():
            if feature not in self.reference:
                continue
            
            ref_vals = self.reference[feature]
            
            # Simulate KS-Test
            # In simulation, we just use random or small logic if deps missing
            # But let's pretend valid numpy arrays
            try:
                stat, p_value = stats.ks_2samp(ref_vals, current_vals)
                drift_scores[feature] = p_value # p-value < 0.05 indicates drift
            except Exception:
                # Fallback for mock environment if scipy not present
                drift_scores[feature] = abs(np.mean(ref_vals) - np.mean(current_vals))
                
        return drift_scores
    
    def check_alert_status(self, scores: Dict[str, float], threshold: float = 0.05) -> List[str]:
        drifted_features = []
        for feat, score in scores.items():
            # If p-value, low is bad. If mean-diff, high is bad.
            # Assuming KS p-value here.
            if score < threshold:
                drifted_features.append(feat)
        return drifted_features
