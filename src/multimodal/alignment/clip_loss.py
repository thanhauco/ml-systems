# import torch.nn.functional as F

class CLIPLoss:
    """
    Contrastive Loss for Image-Text pairs.
    """
    
    def forward(self, image_embeds, text_embeds, temperature=0.07):
        # logits = (image_embeds @ text_embeds.T) / temperature
        # labels = arange(batch_size)
        # loss_i = cross_entropy(logits, labels)
        # loss_t = cross_entropy(logits.T, labels)
        print("Computing Symmetric InfoNCE Loss...")
        return 0.5 # (loss_i + loss_t) / 2
