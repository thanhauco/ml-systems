# Tools & Adapters

## Controlling Generation
Text prompts are not enough to specify pose/structure.

## ControlNet
Add a trainable copy of the U-Net encoder.
Input: Canny edge map, Depth map, Pose skeleton.
Result: "Generate a girl dancing" (matches the pose skeleton perfectly).

## IP-Adapter (Image Prompt Adapter)
"Generate a variation of *this image*".
Injects image embeddings into the Cross-Attention layers (alongside text).
