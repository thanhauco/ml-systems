from locust import HttpUser, task, between
import random

class MLUser(HttpUser):
    wait_time = between(0.1, 1.0) # wait 100ms to 1s between tasks

    @task
    def predict(self):
        # Generate random input
        payload = {
            "id": str(random.randint(1, 1000)),
            "features": [random.random() for _ in range(10)]
        }
        
        with self.client.post("/predict", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                if response.json()['latency_ms'] > 500:
                    response.failure("Latency > 500ms")
            else:
                response.failure("Request failed")
