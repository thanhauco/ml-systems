# Edge Connectivity

## The Network is Unreliable
Edge devices move. WiFi drops. 4G has dead zones.

## Protocols
1.  **MQTT (Message Queuing Telemetry Transport)**:
    -   Pub/Sub model.
    -   Lightweight header (2 bytes).
    -   "QoS 1": Deliver at least once. "QoS 2": Exactly once.
    -   "Last Will": Notify server if device dies unexpectedly.
2.  **CoAP (Constrained Application Protocol)**:
    -   UDP-based (low overhead).
    -   RESTful (GET/POST).

## Offline Strategies
-   **Store and Forward**: Save inference results to SD card. Upload when WiFi connects.
-   **Edge Buffering**: Ring buffer (Overwrite old data if full).
