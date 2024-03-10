# Introduction to Model Deployment

## The "Last Mile" Problem
Training a model is only 20% of the work. Deployment is where the model meets the real world.
A model in a notebook is an *asset*. A model in production is a *service* (and a liability).

## Key Components of Deployment
1.  **Model Server**: The engine that loads weights and executes inference (Triton, TorchServe, TensorFlow Serving).
2.  **API Gateway**: Authentication, Rate Limiting, Routing.
3.  **Orchestrator**: Managing replicas, health checks, autoscaling (Kubernetes).
4.  **Monitoring**: Logging inputs/outputs to detect drift.

## The Trade-off Triangle
You can usually pick two:
1.  **Latency**: Fast inference (<10ms).
2.  **Throughput**: High volume (10k req/sec).
3.  **Cost**: Cheap hardware (CPU vs A100).
