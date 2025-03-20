from .kv_cache_manager import KVCacheManager
from .continuous_batcher import ContinuousBatcher, Request
import time

class VLLMLite:
    """
    Putting it all together: A tiny vLLM engine.
    """
    def __init__(self):
        self.cache_manager = KVCacheManager(num_blocks=50)
        self.scheduler = ContinuousBatcher(max_batch_size=8)
        self.step_count = 0

    def add_prompts(self, prompts: list):
        for i, p in enumerate(prompts):
            # Simulate random lengths
            req = Request(f"req_{self.step_count}_{i}", len(p), 10) # generate 10 tokens
            self.scheduler.add_request(req)
        self.step_count += 1

    def run_engine_loop(self, num_steps: int = 20):
        print("Starting vLLM Engine Loop...")
        for _ in range(num_steps):
            if not self.scheduler.running_batch and not self.scheduler.waiting_queue:
                break
                
            self.scheduler.step()
            
            # Simulate memory pressure checking
            util = self.cache_manager.get_utilization()
            if util > 0.9:
                print("WARNING: High Memory Pressure - Scheduler should preempt!")
            
            time.sleep(0.05)

if __name__ == "__main__":
    engine = VLLMLite()
    engine.add_prompts(["Hello world", "Explain quantum mechanics", "Write a poem"])
    engine.run_engine_loop()
