import random
from datetime import datetime

class CarbonTracker:
    """
    Estimates real-time carbon emissions for compute jobs.
    Uses mock signals from grid APIs (e.g., CO2Signal, WattTime).
    """
    
    def __init__(self, region="us-east-1"):
        self.region = region
        print(f"CarbonTracker initialized for {region}")

    def get_current_intensity(self) -> float:
        """
        Returns grid carbon intensity in gCO2/kWh.
        """
        # Mock API call
        # Varies based on simulated time of day (random for now)
        base = 400.0 if "east" in self.region else 200.0 # Coal vs Hydro
        variance = random.uniform(-50, 50)
        return base + variance

    def estimate_job_emissions(self, duration_hours: float, power_watts: float) -> float:
        """
        Estimates total footprint in gCO2.
        """
        intensity = self.get_current_intensity()
        kwh = (power_watts / 1000.0) * duration_hours
        emissions = kwh * intensity
        
        print(f"[Carbon] Estimate: {duration_hours}h @ {power_watts}W = {emissions:.2f} gCO2")
        return emissions
