from typing import List, Dict
import numpy as np

class DriftDetector:
    """
    Simple statistical drift detector (KS Test or Mean Shift).
    """
    def __init__(self, reference_data: List[float]):
        self.ref_mean = np.mean(reference_data)
        self.ref_std = np.std(reference_data)
        self.threshold_std = 3.0

    def is_drift(self, batch_data: List[float]) -> bool:
        """
        Returns true if batch mean is > 3 std devs away from ref mean.
        """
        if not batch_data:
            return False
            
        current_mean = np.mean(batch_data)
        z_score = abs(current_mean - self.ref_mean) / (self.ref_std + 1e-9)
        
        if z_score > self.threshold_std:
            print(f"Drift Detected! Z-Score: {z_score}")
            return True
        return False
