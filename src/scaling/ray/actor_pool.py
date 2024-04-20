# import ray

# @ray.remote(num_gpus=1)
class Worker:
    def process(self, data):
        return data * 2

class ActorPool:
    """
    Manages a pool of stateful actors.
    """
    
    def __init__(self, size=4):
        print(f"Initializing pool of {size} workers...")
        # self.workers = [Worker.remote() for _ in range(size)]
        self.workers = ["worker_ref" for _ in range(size)]

    def map(self, dataset):
        print("Distributing data across actors...")
        results = []
        # for i, chunk in enumerate(dataset):
        #     worker = self.workers[i % len(self.workers)]
        #     results.append(worker.process.remote(chunk))
        # return ray.get(results)
        return dataset

