import torch.nn.utils.prune as prune
import torch.nn as nn

class Pruner:
    """
    Applies structured or unstructured pruning.
    """
    
    @staticmethod
    def prune_layer(layer: nn.Module, amount: float = 0.3):
        """
        Removes 30% of lowest magnitude weights (L1 Unstructured).
        """
        prune.l1_unstructured(layer, name='weight', amount=amount)
        # To make it permanent (remove mask buffers):
        # prune.remove(layer, 'weight')

    @staticmethod
    def prune_global(model: nn.Module, amount: float = 0.2):
        """
        Prunes 20% of connections across the entire model.
        """
        parameters_to_prune = []
        for name, module in model.named_modules():
            if isinstance(module, nn.Linear):
                parameters_to_prune.append((module, 'weight'))

        prune.global_unstructured(
            parameters_to_prune,
            pruning_method=prune.L1Unstructured,
            amount=amount,
        )
