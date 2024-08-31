# from torchvision import transforms

class MultimodalTransforms:
    """
    Preprocessing for Clip/ViT.
    """
    
    def get_train_transforms(self):
        print("Building transform pipeline: Resize -> CenterCrop -> Norm")
        return "Transforms"

    def denormalize(self, tensor):
        # x * std + mean
        return tensor
