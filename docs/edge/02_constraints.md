# Constraints in Edge Computing

## 1. Memory (The Biggest Bottleneck)
-   **Flash (Storage)**: Read-only model weights fitting here.
-   **RAM (SRAM/DRAM)**: Activations (intermediate tensors) must fit here.
-   *Challenge*: A ResNet-50 needs ~100MB RAM. An Arduino has 256KB.

## 2. Compute (FLOPS)
-   Cloud GPUs: TFLOPS (Trillions of ops/sec).
-   MCU: MFLOPS (Millions).
-   *Impact*: Must reduce model depth/width or use MobileNets.

## 3. Power / Energy
-   **Battery Life**: High compute = High battery drain.
-   **Thermal**: Phones throttle if they get too hot. Passive cooling only.

## 4. Hardware Diversity
-   Cloud: Homogenous (All NVIDIA).
-   Edge: Heterogeneous (ARM, RISC-V, DSPs, NPUs, FPGAs).
-   *Solution*: Compilers like TVM or ONNX Runtime.
