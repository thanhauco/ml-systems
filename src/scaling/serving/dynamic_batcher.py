import time
from collections import deque

class DynamicBatcher:
    """
    Groups individual requests into batches with a timeout.
    """
    
    def __init__(self, max_batch_size=32, timeout_ms=10):
        self.max_bs = max_batch_size
        self.timeout = timeout_ms / 1000.0
        self.queue = deque()

    def add_request(self, req):
        self.queue.append(req)
        # In async loop:
        # if len(queue) >= max_bs or time > timeout:
        #    process(queue)

    def mock_loop(self):
        print("Collecting requests...")
        time.sleep(self.timeout)
        batch = []
        while self.queue:
            batch.append(self.queue.popleft())
        
        print(f"Processing batch of size {len(batch)} inputs.")
        return batch

if __name__ == "__main__":
    db = DynamicBatcher()
    for i in range(5): db.add_request(i)
    db.mock_loop()
