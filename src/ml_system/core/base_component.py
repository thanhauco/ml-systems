from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import uuid
import logging

class BaseComponent(ABC):
    """
    Abstract base class for all ML system components.
    Enforces lifecycle management and metadata tracking.
    """
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.config = config or {}
        self.logger = logging.getLogger(f"ml_system.{name}")
        self._state = "initialized"

    def initialize(self) -> None:
        """Lifecycle hook for setup (DB connections, loading weights)."""
        self.logger.info(f"Initializing {self.name} ({self.id})")
        self._setup()
        self._state = "ready"

    def shutdown(self) -> None:
        """Lifecycle hook for cleanup."""
        self.logger.info(f"Shutting down {self.name}")
        self._teardown()
        self._state = "shutdown"

    @abstractmethod
    def _setup(self):
        """Internal setup logic to be implemented by children."""
        pass

    @abstractmethod
    def _teardown(self):
        """Internal teardown logic to be implemented by children."""
        pass

    @abstractmethod
    def execute(self, context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Main execution entrypoint."""
        if self._state != "ready":
             raise RuntimeError(f"Component {self.name} is not ready. State: {self._state}")
        raise NotImplementedError("Subclasses must implement execute()")
