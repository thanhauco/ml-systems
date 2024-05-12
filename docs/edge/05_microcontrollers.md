# TinyML: ML on Microcontrollers

## The Environment
-   **Processor**: ARM Cortex-M4F @ 80MHz.
-   **RAM**: 256KB total (Stack + Heap).
-   **Flash**: 1MB.
-   **OS**: Bare metal or FreeRTOS. No Linux. No Python.

## How it works (TFLite Micro)
1.  **Offline**: Train model, Quantize to INT8.
2.  **Convert**: Convert `.tflite` to a C byte array (`unsigned char g_model[]`).
3.  **Compile**: Include C++ library. No dynamic memory allocation (`malloc`). Use a static "Tensor Arena".
4.  **Run**: `interpreter->Invoke()`.

## Use Cases
-   **Wake Word**: "Ok Google" (Running 24/7 on DSP).
-   **Vibration Analysis**: Detecting bearing faults on motors.
-   **Gesture Recognition**: Magic Wand.
