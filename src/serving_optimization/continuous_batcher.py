import random
from typing import List
from collections import deque

class Request:
    def __init__(self, request_id: str, prompt_len: int, output_len: int):
        self.request_id = request_id
        self.prompt_len = prompt_len
        self.output_len = output_len
        self.generated_len = 0
        self.finished = False

class ContinuousBatcher:
    """
    Simulates iteration-level scheduling.
    """
    def __init__(self, max_batch_size: int = 4):
        self.max_batch_size = max_batch_size
        self.waiting_queue = deque()
        self.running_batch: List[Request] = []

    def add_request(self, req: Request):
        print(f"Received request {req.request_id} (len={req.prompt_len}+{req.output_len})")
        self.waiting_queue.append(req)

    def step(self):
        # 1. Clear finished requests
        self.running_batch = [r for r in self.running_batch if not r.finished]

        # 2. Add new requests if slots available
        while self.waiting_queue and len(self.running_batch) < self.max_batch_size:
            req = self.waiting_queue.popleft()
            self.running_batch.append(req)
            print(f"Scheduled request {req.request_id}")

        # 3. Decode step (simulate)
        if not self.running_batch:
            return

        print(f"Step: processing {len(self.running_batch)} requests...")
        for req in self.running_batch:
            req.generated_len += 1
            if req.generated_len >= req.output_len:
                req.finished = True
                print(f"  Finished request {req.request_id}")
