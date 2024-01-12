import time
import requests

class SustainableTrainingLoop:
    """
    Checks carbon intensity of grid before training epoch.
    If intensity > threshold, pauses training.
    """
    
    def __init__(self, threshold_g_co2_kwh=200):
        self.threshold = threshold_g_co2_kwh
        # self.api_url = "https://api.electricitymap.org/v3/carbon-intensity/latest"

    def check_grid(self, zone="US-CAL-CISO"):
        print(f"Checking grid intensity for {zone}...")
        # resp = requests.get(...)
        # intensity = resp.json()['carbonIntensity']
        intensity = 150 # Mock value (Clean energy)
        return intensity

    def on_epoch_begin(self, epoch):
        intensity = self.check_grid()
        if intensity > self.threshold:
            print(f"Grid dirty ({intensity}g). Pausing training for 1 hour...")
            # time.sleep(3600)
        else:
            print(f"Grid clean ({intensity}g). Training proceeding.")
            
if __name__ == "__main__":
    loop = SustainableTrainingLoop()
    loop.on_epoch_begin(1)
