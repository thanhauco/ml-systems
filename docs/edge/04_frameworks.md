# Edge Inference Frameworks

## TensorFlow Lite (TFLite)
-   **Target**: Android, iOS, Microcontrollers.
-   **Format**: FlatBuffers (`.tflite`).
-   **Features**: Delegate support (GPU, NNAPI, Hexagon DSP).

## TensorRT (NVIDIA)
-   **Target**: NVIDIA Jetson / Desktop GPUs.
-   **Optimizations**: Layer fusion, Kernel auto-tuning, precision calibration.
-   **Performance**: Often 5-10x faster than PyTorch.

## OpenVINO (Intel)
-   **Target**: Intel CPUs, iGPUs, VPUs (Movidius).
-   **Format**: Intermediate Representation (`.xml` + `.bin`).
-   **Philosophy**: "Write once, deploy anywhere" (on Intel hardware).

## CoreML (Apple)
-   **Target**: iOS, macOS.
-   **Hardware**: Apple Neural Engine (ANE).
-   **Workflow**: Convert PyTorch -> CoreML Package (`.mlpackage`).
