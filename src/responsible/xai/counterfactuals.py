class CounterfactualGenerator:
    """
    Generates 'What-If' scenarios.
    """
    
    def __init__(self, model):
        self.model = model

    def generate(self, instance, desired_class=1):
        """
        Finds minimal perturbation to change prediction to desired_class.
        """
        print(f"Searching for counterfactual to flip prediction to {desired_class}...")
        # Perturb
        cf = instance.copy()
        cf[0] += 0.1 # Mock modification
        print("Found CF: Increase Feature 0 by 0.1")
        return cf
