import numpy as np

class MoELayer:
    """
    Sparse Mixture of Experts.
    """
    
    def __init__(self, num_experts=4, k=2):
        self.experts = [f"Expert_{i}" for i in range(num_experts)]
        self.k = k

    def forward(self, x):
        """
        x: [Batch, Seq, Dim]
        """
        # Gating: prob = softmax(x @ W_gate)
        # indices = top-k(prob)
        
        indices = np.random.randint(0, len(self.experts), size=(x.shape[0], self.k))
        print(f"Routing tokens to Experts: {indices}")
        
        # Dispatch -> Expert Forward -> Combine
        return x
        
if __name__ == "__main__":
    MoELayer().forward(np.zeros((2, 10)))
