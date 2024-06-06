import random
import time

class NetworkConditioner:
    """
    Simulates bad network conditions (Latency, Packet Loss).
    """
    
    def __init__(self, latency_ms=100, packet_loss_prob=0.1):
        self.latency_sec = latency_ms / 1000.0
        self.loss_prob = packet_loss_prob

    def send(self, packet):
        # 1. Packet Loss
        if random.random() < self.loss_prob:
            print("Packet Lost!")
            return False
            
        # 2. Latency
        time.sleep(self.latency_sec)
        print("Packet Sent.")
        return True
