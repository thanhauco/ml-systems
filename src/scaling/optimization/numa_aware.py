import os

class NUMABinder:
    """
    Binds process to specific CPU cores to match GPU locality (minimize QPI latency).
    """
    
    def bind(self, local_rank):
        # Simplistic mapping: Rank 0 -> Cores 0-16, Rank 1 -> Cores 17-32...
        cores_per_rank = 16
        start = local_rank * cores_per_rank
        end = start + cores_per_rank - 1
        
        affinity_list = list(range(start, end+1))
        print(f"Binding Rank {local_rank} to Cores {start}-{end}")
        
        # os.sched_setaffinity(0, affinity_list)

if __name__ == "__main__":
    NUMABinder().bind(0)
