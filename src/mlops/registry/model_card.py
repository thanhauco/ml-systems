from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import json
import datetime

@dataclass
class ModelCard:
    """
    Standardized Model Card structure (inspired by Google).
    """
    model_id: str
    owner: str
    description: str
    version: str
    license: str
    # Technical Specs
    framework: str
    architectures: List[str]
    input_format: str
    output_format: str
    # Performance
    metrics: Dict[str, float]
    # Ethical Considerations
    intended_use: str
    limitations: str
    
    def save(self, path: str):
        data = asdict(self)
        data["created_at"] = datetime.datetime.utcnow().isoformat()
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
            
    @classmethod
    def load(cls, path: str) -> 'ModelCard':
        with open(path, "r") as f:
            data = json.load(f)
            data.pop("created_at", None)
            return cls(**data)

