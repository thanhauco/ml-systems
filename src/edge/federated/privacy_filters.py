import numpy as np

class PrivacyFilter:
    """
    Applies Differential Privacy (DP-SGD style) clipping and noise.
    """
    
    @staticmethod
    def clip_gradients(grads: np.ndarray, max_norm: float) -> np.ndarray:
        norm = np.linalg.norm(grads)
        if norm > max_norm:
            scale = max_norm / norm
            print(f"Clipping gradients: norm {norm:.2f} -> {max_norm}")
            return grads * scale
        return grads

    @staticmethod
    def add_noise(grads: np.ndarray, noise_multiplier: float) -> np.ndarray:
        noise = np.random.normal(0, noise_multiplier, grads.shape)
        return grads + noise

if __name__ == "__main__":
    g = np.array([10.0, 20.0])
    g_safe = PrivacyFilter.clip_gradients(g, 5.0)
    g_noisy = PrivacyFilter.add_noise(g_safe, 0.1)
    print(f"Original: {g}, Safe: {g_noisy}")
