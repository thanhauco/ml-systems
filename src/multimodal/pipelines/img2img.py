class ImageToImagePipeline:
    """
    Style Transfer / Variation.
    """
    
    def generate(self, prompt, init_image, strength=0.8):
        print(f"Transforming image with strength {strength} and prompt '{prompt}'")
        # latents = vae.encode(init_image)
        # Add noise based on strength (Start at t = 1000 * strength)
        # Denoise loop...
        return "Styled_Image.png"
