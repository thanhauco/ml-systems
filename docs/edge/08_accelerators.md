# Edge Accelerators

## Specialized Hardware
General purpose CPUs are too slow/power-hungry for Neural Networks.

## Google Coral (Edge TPU)
-   **ASIC**: Application Specific Integrated Circuit.
-   **Power**: 4 TOPS @ 2 Watts. (2 Trillion Ops Per Second).
-   **Restriction**: Only supports INT8 quantized TensorFlow Lite models.

## NVIDIA Jetson (Nano / Orin)
-   **Architecture**: Miniaturized GPU (CUDA Cores + Tensor Cores).
-   **Power**: 10-60 Watts.
-   **Flexibility**: Runs full PyTorch/TensorFlow (FP16/FP32).

## NPUs (Neural Processing Units)
-   Integrated into SoCs (Apple A-Series, Qualcomm Snapdragon).
-   Dedicated Matrix Multiplication units.
-   Accessed via APIs (CoreML, SNPE).
