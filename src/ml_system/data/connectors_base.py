from abc import abstractmethod
from typing import Iterator, Dict, Any
from ..core.base_component import BaseComponent

class BaseConnector(BaseComponent):
    """
    Abstract base for data source connectors.
    """
    
    @abstractmethod
    def connect(self):
        """Establish connection."""
        pass

    @abstractmethod
    def fetch_batch(self, query: str, batch_size: int = 1000) -> Iterator[List[Dict[str, Any]]]:
        """Yields batches of data."""
        pass

    @abstractmethod
    def write_batch(self, data: List[Dict[str, Any]], table: str):
        """Writes data to sink."""
        pass
