# Diffusion Models

## Forward Process (Destruction)
Slowly add Gaussian noise to an image until it is pure noise $N(0, I)$.
$q(x_t | x_{t-1}) = N(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t I)$

## Reverse Process (Creation)
Train a Neural Network (U-Net) to predict the noise $\epsilon$ added at step $t$.
$x_{t-1} = \frac{1}{\sqrt{\alpha_t}} (x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}} \epsilon_\theta(x_t, t))$

## Components
-   **U-Net**: Predicts noise.
-   **Scheduler**: Controls the noise schedule ($\beta_t$).
-   **VAE**: Compresses image to latent space (Latent Diffusion) to save compute.
