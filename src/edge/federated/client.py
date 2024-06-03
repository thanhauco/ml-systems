import numpy as np
# import tensorflow as tf

class FederatedClient:
    """
    Simulates a local device training on private data.
    """
    
    def __init__(self, client_id: str, data: np.ndarray):
        self.client_id = client_id
        self.data = data
        self.model_weights = None

    def receive_model(self, weights):
        print(f"Client {self.client_id}: Received global model.")
        self.model_weights = weights

    def train_epoch(self):
        print(f"Client {self.client_id}: Training 1 epoch on {len(self.data)} samples...")
        # Mock gradient update: W_new = W_old - lr * grad
        # return new_weights
        return np.random.rand(10,) # Mock weights

    def get_update(self):
        # Return Delta (W_new - W_old)
        return np.random.rand(10,)
