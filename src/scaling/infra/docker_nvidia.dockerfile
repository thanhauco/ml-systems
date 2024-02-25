FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

# Install Python and Utils
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    wget \
    htop \
    ibverbs-providers \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch with CUDA support
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Install DeepSpeed/FlashAttn (Optimized kernels)
RUN pip3 install deepspeed flash-attn

WORKDIR /app
COPY . .

CMD ["python3", "main.py"]
