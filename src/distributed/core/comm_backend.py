class CommBackend:
    """
    Abstracts NCCL/Gloo operations.
    """
    
    def all_reduce(self, tensor, op="SUM"):
        # dist.all_reduce(tensor, op=dist.ReduceOp.SUM)
        print(f"AllReduce ({op}) on tensor shape {tensor.shape}")
        return tensor

    def broadcast(self, tensor, src=0):
        # dist.broadcast(tensor, src)
        print(f"Broadcast from Rank {src}")
        return tensor

if __name__ == "__main__":
    import numpy as np
    CommBackend().all_reduce(np.array([1,2,3]))

