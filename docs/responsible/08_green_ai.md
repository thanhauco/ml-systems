# Green AI: Sustainability

## The Cost of Intelligence
Training GPT-3 consumed ~1,287 MWh (equivalent to 120 years of US household energy).

## Red AI vs Green AI
-   **Red AI**: Buying performance with massive scale. State-of-the-art accuracy is the only goal.
-   **Green AI**: Efficiency as a first-class metric. FLOPs, Energy (Joules), Carbon (CO2e).

## Techniques for Green AI
1.  **Efficient Architectures**: MobileNet instead of VGG.
2.  **Distillation**: Teacher (Big) -> Student (Small).
3.  **Quantization**: INT8 uses less energy than FP32.
4.  **Carbon-Aware Computing**: Train when the grid is green (Solar/Wind is high).
5.  **Clean Up**: Delete unused models and checkpoints (Storage costs energy too).
