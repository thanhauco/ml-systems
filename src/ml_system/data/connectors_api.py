from typing import Iterator, Dict, Any, List
import json
import time
from .connectors_base import BaseConnector

class APIConnector(BaseConnector):
    """
    Connector for REST APIs.
    """
    
    def _setup(self):
        self.base_url = self.config.get("base_url")
        self.auth_token = self.config.get("auth_token")

    def _teardown(self):
        pass

    def connect(self):
        pass

    def fetch_batch(self, endpoint: str, batch_size: int = 100) -> Iterator[List[Dict[str, Any]]]:
        url = f"{self.base_url}/{endpoint}"
        self.logger.info(f"Starting fetch from {url}")
        
        # Simulate 3 pages of data
        for page in range(3):
            # In real code: response = requests.get(url, params={"page": page})
            # data = response.json()
            data = [
                {"id": page * 100 + i, "event": "simulated_event", "timestamp": time.time()}
                for i in range(batch_size) 
            ]
            yield data
            time.sleep(0.1)  # Simulate network latency

    def write_batch(self, data: List[Dict[str, Any]], endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        # In real code: requests.post(url, json=data)
        self.logger.info(f"POST {url} with {len(data)} items")
        if not data:
            self.logger.warning("Empty batch provided to write_batch")
            return
            
        success_count = len(data)  # Assume all succeed
        self.logger.info(f"Successfully wrote {success_count} records.")
