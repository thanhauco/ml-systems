import random

class AdversarialShield:
    """
    Deflects adversarial attacks using simulated input sanitization.
    """
    
    def __init__(self, technique="spatial_smoothing"):
        self.technique = technique
        print(f"Shield initialized with {technique}")

    def sanitize(self, input_data):
        """
        Removes high-frequency perturbations.
        """
        # Mock logic
        has_perturbation = random.random() < 0.3
        if has_perturbation:
            print("Shield: Detected adversarial noise. Sanitizing...")
            return "sanitized_input_data"
        return input_data

    def detect_attack(self, gradients):
        """
        Checks if gradient magnitude exceeds suspicious threshold (FGSM attempt).
        """
        magnitude = random.random()
        if magnitude > 0.9:
             print("Shield: FGSM attack fingerprint detected.")
             return True
        return False
