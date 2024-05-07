import time
import requests
import statistics

def benchmark(url: str, n: int = 100):
    latencies = []
    payload = {"id": "bench", "features": [0.1] * 10}
    
    print(f"Warming up...")
    for _ in range(10):
        requests.post(url, json=payload)

    print(f"Running {n} requests against {url}...")
    for _ in range(n):
        start = time.perf_counter()
        resp = requests.post(url, json=payload)
        end = time.perf_counter()
        if resp.status_code == 200:
            latencies.append((end - start) * 1000)

    print(f"P50: {statistics.median(latencies):.2f} ms")
    print(f"P99: {sorted(latencies)[int(n*0.99)]:.2f} ms")
    print(f"Mean: {statistics.mean(latencies):.2f} ms")

if __name__ == "__main__":
    benchmark("http://localhost:8000/predict")
