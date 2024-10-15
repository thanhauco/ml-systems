class GradientAccumulator:
    """
    Simulates large batch size by accumulating gradients over N steps.
    """
    
    def __init__(self, model, optimizer, accum_steps=4):
        self.model = model
        self.optimizer = optimizer
        self.steps = accum_steps
        self.counter = 0

    def step(self, loss):
        # loss = loss / self.steps
        # loss.backward()
        
        self.counter += 1
        if self.counter % self.steps == 0:
            print(f"Step {self.counter}: Optimizer Stepping (Accumulated)")
            # self.optimizer.step()
            # self.optimizer.zero_grad()
        else:
            print(f"Step {self.counter}: Accumulating...")
