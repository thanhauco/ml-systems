import math

class DistributedSampler:
    """
    Ensures each Rank gets a unique subset of data.
    """
    
    def __init__(self, dataset_len, num_replicas, rank):
        self.num_replicas = num_replicas
        self.rank = rank
        self.total_size = dataset_len
        self.num_samples = math.ceil(self.total_size / self.num_replicas)

    def __iter__(self):
        # deterministic shuffling based on epoch
        indices = list(range(self.total_size))
        
        # Subsample for this rank
        my_indices = indices[self.rank::self.num_replicas]
        
        print(f"Rank {self.rank}: Yielding {len(my_indices)} indices")
        return iter(my_indices)

if __name__ == "__main__":
    ds = DistributedSampler(100, 4, 0)
    list(ds)
