import json
import uuid
from datetime import datetime

class AuditLog:
    """
    Immutable ledger for Model Life Cycle events.
    """
    
    def __init__(self, log_file="audit.jsonl"):
        self.log_file = log_file

    def record_event(self, event_type: str, actor: str, details: dict):
        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "type": event_type,
            "actor": actor,
            "details": details,
            "signature": "mock_sha256_signature"
        }
        
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
            
        print(f"Audit Logged: {event_type} by {actor}")

if __name__ == "__main__":
    log = AuditLog()
    log.record_event("MODEL_DEPLOY", "jordan", {"version": "v3", "env": "prod"})
