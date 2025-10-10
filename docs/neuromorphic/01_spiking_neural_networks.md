# Spiking Neural Networks (SNNs)

## Third Generation Neural Networks
Unlike ANNs (which communicate continuous values), SNNs communicate via discrete binary spikes.
- **Biologically Plausible**: Mimics the brain's energy-efficient signaling.
- **Sparse Activity**: Computation only happens when a spike occurs.

## The LIF Neuron
**Leaky Integrate-and-Fire**:
1.  **Integrate**: Accumulate incoming voltage (membrane potential).
2.  **Leak**: Potential decays over time if no input arrives.
3.  **Fire**: If potential > threshold, emit a spike and reset potential.

$$ \tau \frac{dV}{dt} = -(V - V_{rest}) + R \cdot I(t) $$
