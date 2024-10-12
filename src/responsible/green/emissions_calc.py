class EmissionsCalculator:
    """
    Converts compute hours to CO2e.
    """
    
    CARBON_INTENSITY = {
        "us-east-1": 0.4, # kg/kWh (Coal heavy)
        "us-west-2": 0.1, # kg/kWh (Hydro/Renewable)
        "eu-north-1": 0.05 # Sweden (Very clean)
    }

    def calculate(self, hours: float, watts: float, region: str):
        kwh = (watts * hours) / 1000.0
        intensity = self.CARBON_INTENSITY.get(region, 0.475) # Global avg
        co2 = kwh * intensity
        
        print(f"Region: {region} | kWh: {kwh:.4f} | CO2: {co2:.4f} kg")
        return co2

if __name__ == "__main__":
    calc = EmissionsCalculator()
    calc.calculate(24, 250, "us-east-1") # GPU for 1 day
