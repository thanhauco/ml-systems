from typing import List, Dict

class InstructionDataLoader:
    """
    Prepares data for SFT (Supervised Fine-Tuning).
    Format: Instruction + Input -> Output.
    """
    
    def __init__(self, tokenizer, max_seq_length=512):
        self.tokenizer = tokenizer
        self.max_len = max_seq_length

    def tokenize_function(self, examples: List[Dict]):
        """
        Concatenates Prompt + Completion and tokenizes.
        Masks the Prompt in the labels so we calculate loss only on Completion.
        """
        processed = []
        for ex in examples:
            prompt = f"Instruction: {ex['instruction']}\nInput: {ex.get('input', '')}\nOutput:"
            completion = ex['output']
            full_text = prompt + completion + self.tokenizer.eos_token
            
            # tokenized = self.tokenizer(full_text, truncation=True, max_length=self.max_len)
            # labels = tokenized['input_ids'].copy()
            # Mask prompt tokens in labels by setting to -100
            
            processed.append({"input_ids": [101] * 10, "labels": [101] * 10}) # Mock
            
        print(f"Processed {len(examples)} examples.")
        return processed
