class BatteryModel:
    """
    Estimates remaining battery life based on compute usage.
    """
    
    def __init__(self, capacity_mah=2500):
        self.capacity_mah = capacity_mah
        self.current_draw_ma = {
            "idle": 5,
            "inference_cpu": 150,
            "inference_npu": 50,
            "wifi_tx": 300
        }
        self.remaining = float(capacity_mah)

    def step(self, state: str, duration_sec: float):
        draw = self.current_draw_ma.get(state, 10)
        consumed_mah = (draw * duration_sec) / 3600.0
        self.remaining -= consumed_mah
        
    def get_percentage(self):
        return max(0, (self.remaining / self.capacity_mah) * 100)

if __name__ == "__main__":
    batt = BatteryModel()
    batt.step("inference_cpu", 60) # 1 min
    print(f"Battery: {batt.get_percentage():.2f}%")
