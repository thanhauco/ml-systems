from typing import List, Tuple
import random

class EventEncoder:
    """
    Simulates encoding of static signals into spike trains (Rate Coding).
    """
    
    def encode_frame(self, pixels: List[float], duration_steps: int = 10) -> List[Tuple[int, int]]:
        """
        Converts pixel intensity to spikes. 
        Higher intensity = Higher probability of spiking.
        """
        spikes = []
        for t in range(duration_steps):
            for i, intensity in enumerate(pixels):
                # Poisson-like generation
                if random.random() < intensity:
                    spikes.append((t, i)) # (time, pixel_index)
        
        # Sort by time
        return sorted(spikes, key=lambda x: x[0])

if __name__ == "__main__":
    encoder = EventEncoder()
    # 5 pixels with varying intensity
    pixels = [0.1, 0.5, 0.9, 0.0, 0.2]
    spike_train = encoder.encode_frame(pixels)
    print(f"Generated {len(spike_train)} events from input.")
    for s in spike_train:
        print(f"  t={s[0]}, pixel={s[1]}")
