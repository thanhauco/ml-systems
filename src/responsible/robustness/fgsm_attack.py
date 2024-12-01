import numpy as np

class FGSMAttacker:
    """
    Fast Gradient Sign Method (Goodfellow et al).
    x_adv = x + epsilon * sign(grad_x(J(theta, x, y)))
    """
    
    @staticmethod
    def generate_adversarial_example(image, gradient, epsilon=0.01):
        """
        image: Original input
        gradient: Gradient of Loss w.r.t Input Image
        epsilon: Perturbation magnitude
        """
        # Collect the element-wise sign of the data gradient
        sign_data_grad = np.sign(gradient)
        
        # Create the perturbed image by adjusting each pixel of the input image
        perturbed_image = image + epsilon * sign_data_grad
        
        # Clip to [0,1] or [0,255]
        perturbed_image = np.clip(perturbed_image, 0, 1)
        
        print(f"Generated Adversarial Example (Epsilon={epsilon})")
        return perturbed_image
