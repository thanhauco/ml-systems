# Ray: Distributed Computing Framework

## Unified API
Pythonic way to scale.

## Core Concepts
1.  **Tasks**: Remote functions. Stateless. `func.remote()`.
2.  **Actors**: Remote classes. Stateful. `Actor.remote()`.
3.  **Objects**: Distributed shared memory store (Plasma).

## Ray Train / Ray Tune
-   **Ray Train**: Wrapper for DDP/Horovod. Handles setup.
-   **Ray Tune**: Scalable hyperparameter tuning. Supports Bayesian Optimization, HyperBand.

## Autoscaling
Ray launches nodes on AWS/GCP when queue fills up and terminates them when idle.
