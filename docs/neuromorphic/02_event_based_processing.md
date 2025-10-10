# Event-Based Processing

## Frame-Based vs Event-Based
- **Frame-Based**: Cameras capture entire frames at fixed intervals (e.g., 30fps). Redundant data if scene is static.
- **Event-Based**: Sensors (e.g., DVS cameras) only report *changes* in pixel intensity.
    - Output: Stream of `(x, y, t, polarity)` events.
    - Latency: Microseconds.
    - Dynamic Range: Extremely high (suitable for high speed/low light).

## Processing Paradigms
- **Asynchronous**: Compute graphs that wake up on event arrival.
- **Time Surfaces**: Aggregating recent events into a spatial surface for ConvNet compatibility.
