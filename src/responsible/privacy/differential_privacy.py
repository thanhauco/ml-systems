class DPOptimizer:
    """
    Mock DP-SGD Optimizer.
    """
    
    def __init__(self, learning_rate, noise_multiplier, l2_norm_clip):
        self.lr = learning_rate
        self.noise = noise_multiplier
        self.clip = l2_norm_clip

    def compute_gradients(self, loss, params):
        print(f"1. Compute Gradients normally.")
        print(f"2. Clip gradients to max_norm {self.clip}.")
        print(f"3. Add Gaussian noise (sigma={self.noise}).")
        print(f"4. Average batches.")
        return params # Mocked return
