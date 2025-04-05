# Ray Architecture: The Global Control Store

## Core Components
1.  **Head Node**: Runs the Global Control Store (GCS) which holds cluster metadata (actor locations, object table).
2.  **Worker Nodes**: Run `raylet` processes (scheduler + object store).
3.  **Object Store (Plasma)**: Shared memory segment on each node. Objects are immutable.

## Scheduling
Ray uses a decentralized scheduling approach.
- **Bottom-Up**: If a node has resources, it schedules the task locally.
- **Spillback**: If full, it forwards the task to a peer or the GCS.

## Ray Train vs Ray Serve
- **Ray Train**: Bulk synchronous parallel (BSP) or parameter server patterns for training.
- **Ray Serve**: DAG-based inference graphs, optimized for latency.
