import random
from typing import Dict, Any, List
from .inference_service import InferenceService

class Router:
    """
    Traffic router for A/B testing or Canary deployments.
    """
    def __init__(self, routes: Dict[str, float], services: Dict[str, InferenceService]):
        """
        routes: {"model_v1": 0.9, "model_v2": 0.1}
        """
        self.routes = routes
        self.services = services

    def route_request(self, request: Dict[str, Any]) -> str:
        r = random.random()
        cumulative = 0.0
        for model_name, weight in self.routes.items():
            cumulative += weight
            if r <= cumulative:
                return model_name
        return list(self.routes.keys())[0]

    def predict(self, request: Dict[str, Any]) -> Any:
        target = self.route_request(request)
        service = self.services[target]
        return service.predict([request])

