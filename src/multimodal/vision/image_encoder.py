class ImageEncoder:
    """
    Wrapper for CLIP Image Encoder.
    """
    
    def encode(self, images):
        # image_features = model.encode_image(images)
        print("Encoding images with CLIP-ResNet50...")
        return "ImageEmbeddings_512d"

if __name__ == "__main__":
    ImageEncoder().encode("mock_img")
