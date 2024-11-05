import asyncio
from typing import List, Dict, Any

class BatchProcessor:
    """
    Simulates a worker that consumes from a queue and processes in batches.
    """
    def __init__(self, batch_size: int = 32, timeout: float = 0.5):
        self.queue = asyncio.Queue()
        self.batch_size = batch_size
        self.timeout = timeout
        self.running = True

    async def add_request(self, item: Dict[str, Any]) -> asyncio.Future:
        future = asyncio.get_event_loop().create_future()
        await self.queue.put((item, future))
        return future

    async def model_inference(self, batch: List[Any]) -> List[float]:
        # Simulate GPU inference on batch
        await asyncio.sleep(0.05)
        return [0.99] * len(batch)

    async def run_loop(self):
        while self.running:
            batch = []
            futures = []
            
            # 1. Collect Batch
            start_wait = asyncio.get_time()
            while len(batch) < self.batch_size:
                timeout = self.timeout - (asyncio.get_time() - start_wait)
                if timeout <= 0 and batch:
                    break
                    
                try:
                    item, future = await asyncio.wait_for(self.queue.get(), timeout=max(0.01, timeout))
                    batch.append(item)
                    futures.append(future)
                except asyncio.TimeoutError:
                    if batch: break
                    continue

            # 2. Process
            if batch:
                print(f"Processing batch of {len(batch)}")
                results = await self.model_inference(batch)
                
                # 3. Resolve futures
                for f, r in zip(futures, results):
                    f.set_result(r)

if __name__ == "__main__":
    # Test harness
    async def main():
        worker = BatchProcessor(batch_size=5)
        asyncio.create_task(worker.run_loop())
        
        # Simulate burst
        futures = [worker.add_request({"id": i}) for i in range(10)]
        results = await asyncio.gather(*futures)
        print(results)
        worker.running = False

    asyncio.run(main())
