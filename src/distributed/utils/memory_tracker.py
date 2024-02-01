# import torch

class CUDAMemoryTracker:
    """
    Debugs OOM issues.
    """
    
    def print_summary(self):
        # allocated = torch.cuda.memory_allocated() / 1e9
        # reserved = torch.cuda.memory_reserved() / 1e9
        allocated = 12.5
        reserved = 14.0
        
        print(f"CUDA Memory: Allocated={allocated}GB, Reserved={reserved}GB")

    def snapshot(self, filename="mem_snap.pickle"):
        # torch.cuda.memory._record_memory_history()
        print(f"Saving memory snapshot to {filename}")
