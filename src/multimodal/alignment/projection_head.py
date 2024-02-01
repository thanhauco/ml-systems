# import torch.nn as nn

class ProjectionHead:
    """
    Projects ViT/Transformer embeddings to shared multimodal space.
    """
    
    def __init__(self, in_dim, out_dim=512):
        print(f"Projection Head: {in_dim} -> {out_dim}")
        # self.net = nn.Sequential(
        #    nn.Linear(in_dim, in_dim),
        #    nn.ReLU(),
        #    nn.Linear(in_dim, out_dim)
        # )
        
    def forward(self, x):
        return x
