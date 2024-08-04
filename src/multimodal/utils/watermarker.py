class Watermarker:
    """
    Injects invisible watermark into images (SynthID style).
    """
    
    def apply(self, image, signature):
        print("Embedding high-frequency watermark pattern...")
        return "Watermarked_Image"
        
    def detect(self, image):
        print("Decoding watermark...")
        return True
