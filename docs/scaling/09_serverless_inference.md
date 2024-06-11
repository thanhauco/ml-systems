# Serverless Inference

## Scale to Zero
Save money when no one is using the model.

## Cold Starts
Loading a 20GB SDXL model takes 10s of seconds.
*Mitigation*:
-   **Keep-warm**: Ping every minute.
-   **Model Loading Optimization**: `mmap`, safetensors.
-   **SnapStart**: Snapshot VM memory state (Java/Firecracker).

## Platforms
-   **KServe**: Standard on K8s. Supports "Scale-to-Zero".
-   **AWS Lambda**: Limited by GPU availability and package size (though improving).
