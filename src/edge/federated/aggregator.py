import numpy as np
from typing import List

class FederatedAggregator:
    """
    Server-side FedAvg algorithm.
    """
    
    def __init__(self):
        self.global_weights = np.zeros(10,)

    def aggregate(self, client_updates: List[np.ndarray]):
        """
        FedAvg: W_global = W_global + Average(Updates)
        """
        print(f"Aggregating {len(client_updates)} updates...")
        avg_update = np.mean(client_updates, axis=0)
        self.global_weights += avg_update
        print("Global model updated.")

    def get_global_model(self):
        return self.global_weights
