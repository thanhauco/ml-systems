from typing import List, Dict, Any
import random

class ZeroOptimizer:
    """
    Simulates a Zero Redundancy Optimizer (Stage 3).
    """
    def __init__(self, model_params: List[str], world_size: int = 4):
        self.world_size = world_size
        self.rank = 0 # Simulating rank 0 perspective
        self.partitions = self._partition_params(model_params)
        print(f"Initialized ZeRO-3 with {world_size} ranks. Local partition size: {len(self.partitions[0])}")

    def _partition_params(self, params: List[str]) -> Dict[int, List[str]]:
        """Shards parameters across ranks."""
        partitions = {i: [] for i in range(self.world_size)}
        for i, p in enumerate(params):
            partitions[i % self.world_size].append(p)
        return partitions

    def step(self):
        """
        Simulates the ZeRO step:
        1. AllGather parameters for forward pass.
        2. Forward/Backward.
        3. ReduceScatter gradients.
        4. Update local partition.
        """
        print("ZeRO: AllGathering parameters...")
        # Simulating communication overhead
        
        print("ZeRO: Computing Forward/Backward...")
        
        print("ZeRO: ReduceScattering gradients...")
        
        print(f"ZeRO: Updating local parameters for rank {self.rank}")
        
    def save_checkpoint(self, path: str):
        print(f"ZeRO: Gathering all partitions to save checkpoint to {path}")

if __name__ == "__main__":
    params = [f"param_{i}" for i in range(100)]
    opt = ZeroOptimizer(params)
    opt.step()
