from .ray_mock import ray
import time
import random

@ray.remote
class TrainingWorker:
    def __init__(self, rank: int):
        self.rank = rank
        self.params = {"w": 0.0}
        print(f"Worker {rank} initialized.")

    def train_step(self, data_batch):
        # Simulate gradient calculation
        loss = random.random()
        grad = 0.1 * loss
        self.params["w"] -= grad
        time.sleep(0.1)
        return {"rank": self.rank, "loss": loss, "params": self.params}

@ray.remote
class ParameterServer:
    def __init__(self, num_workers: int):
        self.workers = [TrainingWorker.remote(i) for i in range(num_workers)]
        self.global_step = 0

    def run_epoch(self):
        futures = []
        for w in self.workers:
            # Dispatch tasks
            futures.append(w.train_step.remote(f"batch_{self.global_step}"))
        
        results = ray.get(futures)
        avg_loss = sum(r['loss'] for r in results) / len(results)
        print(f"Global Step {self.global_step}: Avg Loss = {avg_loss:.4f}")
        self.global_step += 1

def run_distributed_job():
    ray.init()
    print("Launching Distributed Training Job...")
    
    ps = ParameterServer.remote(num_workers=3)
    
    for _ in range(5):
        ray.get(ps.run_epoch.remote())

if __name__ == "__main__":
    run_distributed_job()
