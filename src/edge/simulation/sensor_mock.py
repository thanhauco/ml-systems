import numpy as np
import time

class AccelerometerMock:
    """
    Generates synthetic XYZ acceleration data.
    """
    
    def __init__(self, frequency=50):
        self.dt = 1.0 / frequency
    
    def read(self):
        # Simulate gravity + noise
        x = np.random.normal(0, 0.1)
        y = np.random.normal(0, 0.1)
        z = np.random.normal(9.8, 0.1)
        time.sleep(self.dt)
        return np.array([x, y, z])

class CameraMock:
    """
    Generates random noise images.
    """
    
    def read(self):
        return np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
