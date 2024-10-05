import hashlib

class ShardingManager:
    """
    Consistent Hashing for mapping dataset shards to nodes.
    """
    
    def get_shards_for_monitor(self, worker_id, total_workers, total_shards):
        # Simple modulo sharding
        # In reality: Consistent hashing ring to minimize re-movement on node fail
        
        my_shards = []
        for i in range(total_shards):
            if i % total_workers == worker_id:
                my_shards.append(i)
        
        print(f"Worker {worker_id}/{total_workers} assigned shards: {my_shards}")
        return my_shards
