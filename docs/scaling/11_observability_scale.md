# Observability at Scale

## Distributed Tracing
Request -> Load Balancer -> API -> Model -> DB.
Where is the latency?
*Tool*: Jaeger / OpenTelemetry.

## GPU Monitoring
-   **DCGM (Data Center GPU Manager)**: Official NVIDIA exporter.
-   **Metrics**: SM Clock, Memory Temperature, PCle Bandwidth, ECC Errors.
-   **Alerts**: "GPU stuck in P12 state" (throttled).

## Training Curves
-   Loss is not enough. Monitor Norm of Gradients. If Norm explodes, training is unstable.
-   Monitor "Dead Relus" (zero activations).
