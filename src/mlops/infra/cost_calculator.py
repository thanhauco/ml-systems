class CloudCostCalculator:
    """
    Estimates monthly bill based on resource usage.
    """
    
    PRICES = {
        "g4dn.xlarge": 0.526, # $/hr
        "p3.2xlarge": 3.06,
        "lambda_gb_sec": 0.0000166667
    }

    def estimate_training(self, instance: str, hours: int) -> float:
        rate = self.PRICES.get(instance, 0.0)
        return rate * hours

    def estimate_inference(self, requests_per_month: int, avg_duration_sec: float):
        # AWS Lambda pricing model
        total_compute_seconds = requests_per_month * avg_duration_sec
        # Assume 1GB memory
        cost = total_compute_seconds * self.PRICES["lambda_gb_sec"]
        return cost

if __name__ == "__main__":
    calc = CloudCostCalculator()
    train = calc.estimate_training("p3.2xlarge", 24 * 30)
    print(f"Monthly Training Cost: ${train:.2f}")
