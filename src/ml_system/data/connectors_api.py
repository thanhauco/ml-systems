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
        self.logger.info(f"GET {url}")
        # Simulate pagination
        yield [{"id": 100, "event": "click"}, {"id": 101, "event": "view"}]

    def write_batch(self, data: List[Dict[str, Any]], endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        self.logger.info(f"POST {url} with {len(data)} items")
