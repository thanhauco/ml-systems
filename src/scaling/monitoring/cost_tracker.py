import time

class RealTimeCostTracker:
    """
    Estimates spend based on active resources.
    """
    
    HOURLY_RATE = 24.48 # p4d.24xlarge

    def __init__(self):
        self.start = time.time()

    def current_spend(self):
        elapsed_hours = (time.time() - self.start) / 3600.0
        cost = elapsed_hours * self.HOURLY_RATE
        print(f"Current Spend: ${cost:.4f} ({elapsed_hours*60:.2f} mins)")
        return cost

if __name__ == "__main__":
    t = RealTimeCostTracker()
    t.current_spend()
