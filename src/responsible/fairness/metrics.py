import numpy as np

class FairnessMetrics:
    """
    Calculates common fairness metrics.
    """
    
    @staticmethod
    def disparate_impact(y_pred: np.ndarray, sensitive_attr: np.ndarray):
        """
        Ratio of acceptance rates: P(Y=1|A=0) / P(Y=1|A=1)
        Rule of Thumb: Should be between 0.8 and 1.25.
        """
        # A=1 Usually privileged group (e.g. Male)
        # A=0 Usually unprivileged (e.g. Female)
        
        prob_unpriv = np.mean(y_pred[sensitive_attr == 0])
        prob_priv = np.mean(y_pred[sensitive_attr == 1])
        
        if prob_priv == 0: return 0.0
        return prob_unpriv / prob_priv

    @staticmethod
    def demographic_parity_diff(y_pred: np.ndarray, sensitive_attr: np.ndarray):
        """
        Difference in acceptance rates. Ideal = 0.
        """
        prob_unpriv = np.mean(y_pred[sensitive_attr == 0])
        prob_priv = np.mean(y_pred[sensitive_attr == 1])
        return prob_priv - prob_unpriv

if __name__ == "__main__":
    preds = np.array([1, 1, 0, 1, 0])
    groups = np.array([1, 1, 0, 0, 0])
    di = FairnessMetrics.disparate_impact(preds, groups)
    print(f"Disparate Impact: {di:.2f}")
