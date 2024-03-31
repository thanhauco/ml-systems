from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LoRAConfig:
    """
    Configuration for Low-Rank Adaptation.
    """
    r: int = 8 # Rank
    lora_alpha: int = 16 # Scaling factor
    lora_dropout: float = 0.05
    bias: str = "none"
    target_modules: List[str] = None # ["q_proj", "v_proj"]

    def to_dict(self):
        return {
            "r": self.r,
            "lora_alpha": self.lora_alpha,
            "lora_dropout": self.lora_dropout,
            "bias": self.bias,
            "target_modules": self.target_modules
        }

if __name__ == "__main__":
    conf = LoRAConfig(target_modules=["q_proj", "v_proj"])
    print(conf)
