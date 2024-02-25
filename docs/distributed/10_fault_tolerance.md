# Fault Tolerance

## MTBF (Mean Time Between Failures)
On a 10,000 GPU cluster, failures happen daily.

## Elastic Training (TorchElastic / C10d)
-   **Dynamic World Size**: If a node dies, the job restarts with $N-1$ nodes (or waits for replacement).
-   **Rendezvous**: Protocol for nodes to discover peers and agree on membership (Etcd based).

## Heartbeats
Watchdog timer. If Rank 5 is silent for 30s, kill the job and restart from last checkpoint.

