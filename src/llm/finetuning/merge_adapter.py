class AdapterMerger:
    """
    Merges LoRA weights back into the Base Model for faster inference.
    W_final = W_base + (B @ A) * scaling
    """
    
    @staticmethod
    def merge_and_unload(base_model_path: str, adapter_path: str, output_path: str):
        print(f"Loading base model from {base_model_path}...")
        # base = AutoModelForCausalLM.from_pretrained(base_model_path)
        
        print(f"Loading adapter from {adapter_path}...")
        # model = PeftModel.from_pretrained(base, adapter_path)
        
        print("Merging weights...")
        # model = model.merge_and_unload()
        
        print(f"Saving merged model to {output_path}...")
        # model.save_pretrained(output_path)
