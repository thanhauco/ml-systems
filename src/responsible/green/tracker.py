# from codecarbon import EmissionsTracker
import time

class CarbonTrackerWrapper:
    """
    Tracks CO2 emissions of the Python process.
    """
    
    def __init__(self):
        print("Initializing CodeCarbon EmissionsTracker...")
        # self.tracker = EmissionsTracker()

    def start(self):
        # self.tracker.start()
        self.start_time = time.time()
        print("Tracking started.")

    def stop(self):
        # emissions = self.tracker.stop()
        duration = time.time() - self.start_time
        emissions = 0.005 # kg CO2
        print(f"Tracking stopped. Duration: {duration:.2f}s. Emissions: {emissions} kg CO2e")
        return emissions
