from typing import Dict, Any, Callable
import time
import threading
from ..core.base_component import BaseComponent

class Scheduler(BaseComponent):
    """
    Simple in-process scheduler. 
    In prod, this is Airflow/K8s CronJob.
    """
    
    def _setup(self):
        self.jobs: Dict[str, Dict] = {}
        self.running = False

    def _teardown(self):
        self.running = False

    def schedule_job(self, name: str, interval_seconds: int, func: Callable):
        self.jobs[name] = {
            "interval": interval_seconds,
            "func": func,
            "last_run": 0
        }
        self.logger.info(f"Scheduled {name} every {interval_seconds}s")

    def run_loop(self):
        """Simple polling loop."""
        self.running = True
        while self.running:
            now = time.time()
            for name, job in self.jobs.items():
                if now - job["last_run"] > job["interval"]:
                    self.logger.info(f"Triggering {name}")
                    try:
                        job["func"]()
                    except Exception as e:
                        self.logger.error(f"Job {name} failed: {e}")
                    job["last_run"] = now
            time.sleep(1)

    def execute(self, context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        # Start in thread
        self.run_loop()
        return {}
