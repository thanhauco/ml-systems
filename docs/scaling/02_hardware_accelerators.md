# Hardware Accelerators

## NVIDIA GPUs
-   **A100**: The workhorse. 40GB/80GB HBM2e. Tensor Cores for BF16.
-   **H100**: Transformer Engine (FP8). NVLink Switch.
-   **Architecture**: Streaming Multiprocessors (SMs), HBM, L2 Cache.

## TPUs (Tensor Processing Units)
-   **Google**: Custom ASIC.
-   **Systolic Arrays**: Efficient matrix multiplication.
-   **Topology**: 3D Torus interconnect.

## Others
-   **AWS Trainium/Inferentia**: Cost-effective.
-   **Groq LPU**: Deterministic latency, SRAM based (no HBM).

## Interconnects
-   **PCIe**: CPU <-> GPU (Slow).
-   **NVLink**: GPU <-> GPU intra-node (Fast, 900 GB/s).
-   **InfiniBand/RoCE**: Node <-> Node (400-800 Gbps).
