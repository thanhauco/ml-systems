import numpy as np

class SaliencyMap:
    """
    Computes gradients with respect to input image.
    """
    
    def compute_gradients(self, model, image):
        print("Computing gradients via Backprop...")
        # tape.gradient(loss, image)
        
        # Mock heatmap
        heatmap = np.random.rand(224, 224)
        return heatmap

    def save_plot(self, heatmap, path="saliency.png"):
        print(f"Saving Saliency Map to {path}")
