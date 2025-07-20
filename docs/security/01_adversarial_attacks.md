# Adversarial Attacks & Defenses

## The Threat Model
- **White Box**: Attacker has full access to model gradients (e.g., FGSM).
- **Black Box**: Attacker can only query the model (e.g., HopSkipJump).

## Fast Gradient Sign Method (FGSM)
$$ x' = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y)) $$
Perturbs the input in the direction that maximizes loss.

## Defenses
1.  **Adversarial Training**: Inject adversarial examples into the training set with correct labels.
2.  **Input Sanitation**: Preprocessing (compression, blurring) to wash out high-frequency perturbations.
