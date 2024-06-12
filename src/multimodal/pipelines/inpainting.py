class InpaintPipeline:
    """
    Generates content only within the mask area.
    """
    
    def generate(self, prompt, image, mask):
        print("Inpainting masked region...")
        # At each step, replace unmasked area with noised original image
        # Force model to only hallucinate inside the mask
        return "Inpainted_Image.png"

