# Edge and Embedded AI

## The Shift to the Edge
Traditional AI sends data to the Cloud. Edge AI processes data *where it is created*.
-   **Cloud AI**: Infinite compute, High Latency, Privacy risks.
-   **Edge AI**: Constrained compute, Zero Latency, Privacy aware.

## Why Edge?
1.  **Bandwidth**: A self-driving car generates TBs of data per hour. Can't upload 4K video streams from 1000 cameras.
2.  **Latency**: A robot arm needs to react in < 5ms. The speed of light to AWS is too slow.
3.  **Privacy**: "Hey Siri" is processed locally. Voice data doesn't leave the device (ideally).
4.  **Reliability**: Smart locks must work even when WiFi is down.

## The Spectrum
-   **Heavy Edge**: Local Server / Gateway (NVIDIA Jetson, 32GB RAM).
-   **Mobile Edge**: Smartphones (Snapdragon, 8GB RAM).
-   **Tiny Edge**: Microcontrollers (Cortex M4, 256KB RAM).
