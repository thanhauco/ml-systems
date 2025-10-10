class LIFNeuron:
    """
    Leaky Integrate-and-Fire neuron model.
    """
    
    def __init__(self, tau=10.0, v_reset=0.0, v_thresh=1.0, dt=1.0):
        self.tau = tau
        self.v_reset = v_reset
        self.v_thresh = v_thresh
        self.dt = dt
        self.v = v_reset
        self.history = []

    def step(self, i_in: float):
        """
        Euler integration step.
        """
        dv = (-(self.v - self.v_reset) + i_in) * (self.dt / self.tau)
        self.v += dv
        
        spike = False
        if self.v >= self.v_thresh:
            self.v = self.v_reset
            spike = True
            
        self.history.append(1 if spike else 0)
        return spike

    def reset_state(self):
        self.v = self.v_reset
        self.history = []
