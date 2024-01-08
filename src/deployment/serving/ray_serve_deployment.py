import ray
from ray import serve
from fastapi import FastAPI
import time

app = FastAPI()

@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 1})
@serve.ingress(app)
class ModelDeployment:
    def __init__(self):
        print("Loading heavy model...")
        time.sleep(1)
        self.model = lambda x: 42.0

    @app.post("/predict")
    def predict(self, data: dict):
        return {"result": self.model(data)}

# To run:
# serve.run(ModelDeployment.bind())
