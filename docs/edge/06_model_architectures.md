# Efficient Model Architectures

## Convolutional Optimizations
Standard Conv2D is expensive: `K*K * Cin * Cout * H * W`.

### 1. Depthwise Separable Convolutions (MobileNet)
Split into:
1.  **Depthwise**: 3x3 filter per channel (Spatial).
2.  **Pointwise**: 1x1 filter across channels (Depth).
Reduces params/FLOPS by ~8-9x.

### 2. Inverted Residuals (MobileNetV2)
Narrow -> Wide -> Narrow.
Expand channels, apply Relu, squeeze back.

### 3. Squeeze-and-Excitation (SE-Blocks)
Learn to weigh channels importance. Cheap global pooling operation.

### 4. Neural Architecture Search (EfficientNet)
Use RL to find the best balance of Width, Depth, and Resolution under constraint (FLOPS).
