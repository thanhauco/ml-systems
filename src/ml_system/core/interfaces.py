from typing import Any, Dict, List, Iterator, Protocol
from abc import abstractmethod

class DataSource(Protocol):
    """Interface for components that ingest data."""
    def read(self, query: Dict[str, Any]) -> Iterator[Any]:
        ...

class FeatureTransformer(Protocol):
    """Interface for feature engineering steps."""
    def fit(self, data: Any) -> None:
        ...
    def transform(self, data: Any) -> Any:
        ...

class ModelTrainer(Protocol):
    """Interface for model training loops."""
    def train(self, training_data: Any, validation_data: Any) -> Any:
        # Returns model artifact
        ...

class ModelEvaluator(Protocol):
    """Interface for efficient model evaluation."""
    def evaluate(self, model: Any, dataset: Any) -> Dict[str, float]:
        ...

class ArtifactStore(Protocol):
    """Interface for saving/loading binary objects."""
    def save(self, artifact: Any, path: str) -> None:
        ...
    def load(self, path: str) -> Any:
        ...
