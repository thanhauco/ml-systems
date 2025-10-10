# Energy Proportionality

## The Idle Power Problem
Servers consume ~50% of peak power even when idle.
- **Goal**: Energy consumption should be proportional to utilization. 0% load should ideally equal 0 watts (or close to it).

## Hardware Scaling
- **DVFS (Dynamic Voltage and Frequency Scaling)**: Slowing down clocks when load is light.
- **Sleep States**: Powering down unneeded cores or entire nodes (e.g., Kubernetes Horizontal Pod Autoscaler scaling to zero).

## Metric
$$ \text{Energy Efficiency} = \frac{\text{Training Throughput (Samples/sec)}}{\text{Power (Watts)}} $$
