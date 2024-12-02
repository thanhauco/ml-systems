from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ExperimentRun:
    run_id: str
    experiment_name: str
    params: Dict[str, Any]
    metrics: Dict[str, float]
    artifact_uri: str
    start_time: datetime

class MetadataStore:
    """
    Interface for MLflow / Weights & Biases Backend.
    """
    def __init__(self):
        self.runs: Dict[str, ExperimentRun] = {}

    def log_run(self, run: ExperimentRun):
        self.runs[run.run_id] = run
        print(f"Logged run {run.run_id} for {run.experiment_name}")

    def get_best_run(self, experiment_name: str, metric: str) -> Optional[ExperimentRun]:
        relevant = [r for r in self.runs.values() if r.experiment_name == experiment_name]
        if not relevant:
            return None
        return max(relevant, key=lambda r: r.metrics.get(metric, 0.0))
