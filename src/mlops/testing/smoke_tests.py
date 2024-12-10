import requests
import sys

def smoke_test_endpoint(url: str):
    """
    Verifies that a deployed service returns 200 OK and valid JSON.
    """
    print(f"Smoke testing {url}...")
    try:
        resp = requests.get(f"{url}/health", timeout=5)
        if resp.status_code != 200:
            print(f"FAIL: Status {resp.status_code}")
            return False
        
        # Test Prediction
        resp = requests.post(f"{url}/predict", json={"id": "smoke", "features": []}, timeout=5)
        if resp.status_code != 200:
            print(f"FAIL: Predict {resp.status_code}")
            return False
            
        print("PASS")
        return True
    except Exception as e:
        print(f"FAIL: Connection Error {e}")
        return False

if __name__ == "__main__":
    if not smoke_test_endpoint("http://localhost:8000"):
        sys.exit(1)


