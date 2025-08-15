from typing import Dict, List, Optional
from datetime import datetime

class FeatureDefinition:
    def __init__(self, name: str, dtype: str, description: str):
        self.name = name
        self.dtype = dtype
        self.description = description
        self.created_at = datetime.now()

class FeatureRegistry:
    """
    Central catalog for managing feature definitions.
    """
    def __init__(self):
        self._features: Dict[str, FeatureDefinition] = {}
        print("Feature Registry initialized.")

    def register_feature(self, name: str, dtype: str, description: str):
        if name in self._features:
            print(f"Warning: Overwriting feature definition for {name}")
        
        feat = FeatureDefinition(name, dtype, description)
        self._features[name] = feat
        print(f"Registered feature: {name} ({dtype})")

    def get_feature(self, name: str) -> Optional[FeatureDefinition]:
        return self._features.get(name)

    def list_features(self) -> List[str]:
        return list(self._features.keys())
