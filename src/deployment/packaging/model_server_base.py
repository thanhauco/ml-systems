from abc import ABC, abstractmethod
from typing import Any

class ModelServer(ABC):
    """
    Abstract contract for loading and serving arbitrary models.
    """
    
    @abstractmethod
    def load(self, uri: str) -> None:
        """Loads model into memory from URI (S3, Local)."""
        pass

    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        """Runs inference."""
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """Returns True if model is ready to serve."""
        pass

    def warmup(self):
        """Optional warmup to load cuda context."""
        pass
