# Containerization Best Practices for ML

## Why Docker?
"It works on my machine" is not a deployment strategy. Docker guarantees the OS, Libraries (CUDA, cuDNN), and Python dependencies are identical.

## Optimizing ML Images
ML images are huge (PyTorch + CUDA = 4GB+).

### 1. Multi-Stage Builds
Build (Compile dependencies, install wheels).
Copy only the artifacts to a slim runtime image.
```dockerfile
FROM python:3.9-builder as builder
RUN pip wheel ...
FROM python:3.9-slim
COPY --from=builder ...
```

### 2. Layer Ordering
Docker caches layers. Put slowly changing things (apt-get install) first. Put rapidly changing things (COPY code) last.

### 3. CPU vs GPU Images
-   **CPU**: Use `python:slim` or `alpine` (if compatible).
-   **GPU**: Base on `nvidia/cuda:11.8-runtime-ubuntu22.04`. Avoid `-devel` images in production (they are huge).

## Security
-   Run as non-root user.
-   Scan for vulnerabilities (Trivy).
-   Don't embed secrets (API Keys) in environment variables of the image.
