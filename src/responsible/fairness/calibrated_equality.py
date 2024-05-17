import numpy as np

class CalibratedEquality:
    """
    Advanced metrics: Conditioned demographic parity.
    Selects thresholds such that FPR (False Positive Rate) is equal across groups.
    """
    
    def find_thresholds(self, y_probs: np.ndarray, y_true: np.ndarray, groups: np.ndarray):
        results = {}
        # Simple grid search
        thresholds = np.linspace(0.1, 0.9, 9)
        
        for group in [0, 1]:
            mask = (groups == group)
            y_g = y_true[mask]
            p_g = y_probs[mask]
            
            best_t = 0.5
            target_fpr = 0.1 # Constraint
            
            min_diff = 1.0
            
            for t in thresholds:
                preds = (p_g >= t).astype(int)
                # FPR: FP / (FP + TN)
                fp = np.sum((preds == 1) & (y_g == 0))
                tn = np.sum((preds == 0) & (y_g == 0))
                fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
                
                if abs(fpr - target_fpr) < min_diff:
                    min_diff = abs(fpr - target_fpr)
                    best_t = t
            
            results[group] = best_t
            
        print(f"Calibrated Thresholds (Target FPR={target_fpr}): {results}")
        return results
