from abc import ABC, abstractmethod
from typing import Iterator, Dict, Any, List

class IngestionSource(ABC):
    """
    Abstract contract for different data sources.
    """
    
    @abstractmethod
    def connect(self):
        """Establish connection / session."""
        pass

    @abstractmethod
    def disconnect(self):
        """Cleanup resources."""
        pass

    @abstractmethod
    def read_stream(self) -> Iterator[Dict[str, Any]]:
        """Yields records potentially forever (blocking)."""
        pass

    @abstractmethod
    def read_batch(self, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Reads a finite set of records."""
        pass
