import time

class PowerProfiler:
    """
    Logs power usage (mocking a USB power meter).
    """
    
    def start_logging(self, interval_ms=100):
        print("Starting Power Log...")
        self.interval = interval_ms / 1000.0

    def log_event(self, event_name: str):
        # In real life, read from INA219 sensor
        wattage = 2.5 # Mock Watts
        print(f"[{time.time()}] Event: {event_name}, Power: {wattage} W")

if __name__ == "__main__":
    p = PowerProfiler()
    p.log_event("Inference Start")
