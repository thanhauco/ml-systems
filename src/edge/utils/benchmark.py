import time
import numpy as np

class Benchmarker:
    """
    Profiling latency per layer.
    """
    
    def __init__(self):
        pass

    def measure(self, func, iterations=100):
        times = []
        print(f"Benchmarking {func.__name__} for {iterations} iters...")
        
        # Warmup
        func()
        
        for _ in range(iterations):
            start = time.perf_counter_ns()
            func()
            end = time.perf_counter_ns()
            times.append(end - start)
            
        times = np.array(times, dtype=np.float64) / 1e6 # ns to ms
        print(f"Mean: {np.mean(times):.2f} ms")
        print(f"P99:  {np.percentile(times, 99):.2f} ms")

def mock_inference():
    time.sleep(0.01)

if __name__ == "__main__":
    b = Benchmarker()
    b.measure(mock_inference)
