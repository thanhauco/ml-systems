from typing import Dict, Any, Optional
import threading
import json

class SharedMemory:
    """
    Thread-safe shared state for agent swarms.
    """
    def __init__(self):
        self._store = {}
        self._lock = threading.Lock()

    def write(self, key: str, value: Any):
        with self._lock:
            self._store[key] = value
            # print(f"[MEMORY] Wrote {key}")

    def read(self, key: str) -> Optional[Any]:
        with self._lock:
            return self._store.get(key)
            
    def dump_snapshot(self) -> str:
        with self._lock:
            return json.dumps(self._store, indent=2, default=str)

    def atomic_update(self, key: str, update_func):
        with self._lock:
            val = self._store.get(key)
            new_val = update_func(val)
            self._store[key] = new_val
