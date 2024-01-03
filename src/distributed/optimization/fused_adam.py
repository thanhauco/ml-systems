class FusedAdam:
    """
    Mock implementation of NVIDIA Apex / DeepSpeed FusedAdam.
    Matches PyTorch Optimizer API but uses fused CUDA kernel for speed.
    """
    
    def __init__(self, params, lr=1e-3):
        self.params = list(params)
        self.lr = lr
        print("Initialized FusedAdam (Mock C++ Kernel)")

    def step(self):
        print("Running FusedAdam kernel update...")
