from typing import List, Dict
import math

class FeatureSelector:
    @staticmethod
    def variance_threshold(data: List[List[float]], threshold: float = 0.0) -> List[int]:
        """
        Returns indices of features with variance > threshold.
        """
        if not data:
            return []
        
        n_features = len(data[0])
        n_samples = len(data)
        keep_indices = []
        
        for i in range(n_features):
            col_values = [row[i] for row in data]
            mean = sum(col_values) / n_samples
            var = sum((x - mean) ** 2 for x in col_values) / n_samples
            
            if var > threshold:
                keep_indices.append(i)
                
        return keep_indices

    @staticmethod
    def correlation_filtering(data: List[List[float]], threshold: float = 0.95) -> List[int]:
        """
        Removes features that are highly correlated with another feature.
        Placeholder logic.
        """
        return list(range(len(data[0])))
