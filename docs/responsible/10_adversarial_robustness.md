# Adversarial Robustness

## Optical Illusions for Machines
Changing a few pixels can convince a ConvNet that a "Panda" is a "Gibbon" with 99% confidence.

## Attacks
1.  **White Box (FGSM)**: We have the gradients. We optimize input $X$ to maximize Error.
2.  **Black Box**: We query the API to estimate gradients.
3.  **Physical Attacks**: Stickers, Glasses, T-shirts.

## Defenses
1.  **Adversarial Training**: Train on the attacked examples. "Vaccinate" the model.
2.  **Input Sanitation**: Resize/Blur image to destroy high-frequency adversarial noise.
3.  **Certified Robustness**: Mathematical proof that prediction remains stable within a radius $\epsilon$.

