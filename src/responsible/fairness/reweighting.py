import numpy as np

class Reweighter:
    """
    Pre-processing technique: Assign weights to samples to balance groups.
    """
    
    def compute_weights(self, y_train: np.ndarray, sensitive_attr: np.ndarray):
        """
        W = P(Class) * P(Group) / P(Class, Group)
        """
        weights = np.ones_like(y_train, dtype=float)
        
        # Total counts
        n = len(y_train)
        
        for label in [0, 1]:
            for group in [0, 1]:
                mask = (y_train == label) & (sensitive_attr == group)
                count_class_group = np.sum(mask)
                
                count_class = np.sum(y_train == label)
                count_group = np.sum(sensitive_attr == group)
                
                if count_class_group > 0:
                    expected = (count_class * count_group) / n
                    w = expected / count_class_group
                    weights[mask] = w
                    
        return weights

if __name__ == "__main__":
    rw = Reweighter()
    y = np.array([0, 1, 0, 1])
    g = np.array([0, 0, 1, 1])
    print(rw.compute_weights(y, g))
