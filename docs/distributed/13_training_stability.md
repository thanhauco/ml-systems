import random

class TrainingVisualizer:
    """
    Mock visualizer for training curves.
    """
    
    def __init__(self):
        self.loss_history = []
        
    def log_step(self, step, loss):
        self.loss_history.append((step, loss))
        
        # Check for spike
        if len(self.loss_history) > 2:
            prev_loss = self.loss_history[-2][1]
            if loss > prev_loss * 2.0:
                print(f"WARNING: Loss Spike at step {step}! ({prev_loss:.4f} -> {loss:.4f})")
                
    def check_grad_norm(self, norm):
        if norm > 10.0:
             print("WARNING: Gradient Clipping Triggered.")

if __name__ == "__main__":
    v = TrainingVisualizer()
    v.log_step(1, 0.9)
    v.log_step(2, 2.5) # Spike
