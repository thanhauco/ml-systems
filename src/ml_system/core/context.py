from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import uuid
from datetime import datetime

@dataclass
class ExecutionContext:
    """
    Carries metadata through the pipeline execution.
    Equivalent to a 'Request' object in web servers.
    """
    job_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    original_trigger: str = "manual"  # e.g., 'crontab', 'webhook'
    start_time: datetime = field(default_factory=datetime.utcnow)
    user_id: Optional[str] = None
    tags: Dict[str, str] = field(default_factory=dict)
    
    # Shared state between steps (use carefully)
    _state: Dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any):
        self._state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._state.get(key, default)
    
    def log_context(self) -> Dict[str, Any]:
        """Returns minimal dict for JSON logging."""
        return {
            "job_id": self.job_id,
            "trigger": self.original_trigger,
            "runtime_sec": (datetime.utcnow() - self.start_time).total_seconds()
        }
