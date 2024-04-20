from typing import Dict, Any, Optional
import uuid
import time
import json
import os

class ExperimentManager:
    """
    Mock Wrapper for MLflow / Weights & Biases.
    """
    
    def __init__(self, experiment_name: str, tracking_uri: str = "./mlruns"):
        self.exp_name = experiment_name
        self.tracking_uri = tracking_uri
        self.run_id = None
        
        # Simulate local storage
        os.makedirs(tracking_uri, exist_ok=True)

    def start_run(self, run_name: Optional[str] = None):
        self.run_id = str(uuid.uuid4())
        print(f"Starting run {self.run_id} in {self.exp_name}")

    def log_param(self, key: str, value: Any):
        if not self.run_id: raise Exception("No active run")
        print(f"[Run {self.run_id}] Param: {key}={value}")

    def log_metric(self, key: str, value: float, step: Optional[int] = None):
        if not self.run_id: raise Exception("No active run")
        # In real life, write to DB
        print(f"[Run {self.run_id}] Metric: {key}={value}")

    def log_artifact(self, local_path: str):
        if not self.run_id: raise Exception("No active run")
        print(f"[Run {self.run_id}] Uploading artifact {local_path} to {self.tracking_uri}")

    def end_run(self):
        print(f"Ending run {self.run_id}")
        self.run_id = None
