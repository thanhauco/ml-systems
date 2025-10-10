from .carbon_tracker import CarbonTracker
import time

class CarbonAwareScheduler:
    """
    Delays non-critical jobs until carbon intensity drops below threshold.
    """
    
    def __init__(self, threshold=350.0):
        self.threshold = threshold
        self.tracker = CarbonTracker()
        self.queue = []

    def submit_job(self, job_name, priority="low"):
        self.queue.append({"name": job_name, "priority": priority})
        print(f"Job '{job_name}' queued.")

    def run_loop(self, max_steps=5):
        for _ in range(max_steps):
            intensity = self.tracker.get_current_intensity()
            print(f"Grid Intensity: {intensity:.1f} gCO2/kWh")
            
            if intensity < self.threshold:
                while self.queue:
                    job = self.queue.pop(0)
                    print(f"Launching {job['name']} (Green Window Open)")
            else:
                critical = [j for j in self.queue if j['priority'] == 'high']
                self.queue = [j for j in self.queue if j['priority'] != 'high']
                
                for job in critical:
                    print(f"Launching {job['name']} immediately (High Priority overrides Carbon)")
                
                if self.queue:
                    print(f"Deferring {len(self.queue)} low-priority jobs...")
            
            # time.sleep(1) # simulation speed
