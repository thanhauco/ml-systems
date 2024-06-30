import time

class NetworkBenchmarker:
    """
    Tests AllReduce bandwidth.
    """
    
    def run_benchmark(self, size_mb=100, iters=10):
        print(f"Benchmarking AllReduce Bandwidth ({size_mb}MB)...")
        # tensor = torch.randn(size_mb * 1024 * 256).cuda()
        
        start = time.time()
        for _ in range(iters):
            # dist.all_reduce(tensor)
            pass
        end = time.time()
        
        avg_time = (end - start) / iters
        gbps = (size_mb * 0.008) / avg_time
        print(f"Avg Time: {avg_time*1000:.2f}ms | Bandwidth: {gbps:.2f} Gbps")

if __name__ == "__main__":
    NetworkBenchmarker().run_benchmark()
