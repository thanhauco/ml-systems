import collections
import numpy as np

class RingBuffer:
    """
    Circular buffer for streaming data (e.g., Audio needs last 1 sec).
    """
    
    def __init__(self, capacity: int, dtype=np.float32):
        self.buffer = collections.deque(maxlen=capacity)
        self.capacity = capacity
        self.dtype = dtype

    def add(self, item):
        self.buffer.append(item)

    def get_full(self) -> np.ndarray:
        if len(self.buffer) < self.capacity:
            return None # Not full yet
        return np.array(self.buffer, dtype=self.dtype)

# Usage
# buf = RingBuffer(16000) # 1 sec audio @ 16kHz
# buf.add(0.1)
