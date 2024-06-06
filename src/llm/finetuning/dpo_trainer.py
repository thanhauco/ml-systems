class DPOTrainerWrapper:
    """
    Direct Preference Optimization (Rafailov et al).
    """
    
    def train(self, data_pairs):
        """
        data_pairs: List[(prompt, chosen, rejected)]
        """
        print("Starting DPO Training...")
        # Loss = -log sigmoid ( beta * (log(pi_theta(chosen)/ref(chosen)) - log(pi_theta(rejected)/ref(rejected))) )
        print("Optimizing Policy directly from preferences.")

