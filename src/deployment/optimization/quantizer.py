import torch
import torch.nn as nn

class Quantizer:
    """
    Utilities for Post-Training Quantization (PTQ) in PyTorch.
    """
    
    @staticmethod
    def quantize_dynamic(model: nn.Module) -> nn.Module:
        """
        Converts Linear/LSTM layers to INT8.
        Fastest way to reduce model size on CPU.
        """
        print("Applying dynamic quantization...")
        quantized_model = torch.quantization.quantize_dynamic(
            model,
            {nn.Linear, nn.LSTM},
            dtype=torch.qint8
        )
        return quantized_model

    @staticmethod
    def print_size_diff(original: nn.Module, quantized: nn.Module):
        # Save to temp and check size
        torch.save(original.state_dict(), "/tmp/orig.pth")
        torch.save(quantized.state_dict(), "/tmp/quant.pth")
        
        import os
        orig_size = os.path.getsize("/tmp/orig.pth")
        quant_size = os.path.getsize("/tmp/quant.pth")
        
        print(f"Original: {orig_size/1e6:.2f} MB")
        print(f"Quantized: {quant_size/1e6:.2f} MB")
        print(f"Reduction: {orig_size/quant_size:.1f}x")
