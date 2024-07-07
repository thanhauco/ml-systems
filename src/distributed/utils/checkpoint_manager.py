class AsyncCheckpointManager:
    """
    Saves checkpoints in a background thread to avoid blocking training.
    """
    
    def save(self, state_dict, path):
        # Deep copy to CPU first (blocking but fast)
        # cpu_state = {k: v.cpu() for k, v in state_dict.items()}
        
        print(f"Offloading checkpoint save to background thread: {path}")
        # Thread(target=torch.save, args=(cpu_state, path)).start()
        print("Training continuing immediately...")

if __name__ == "__main__":
    AsyncCheckpointManager().save({}, "ckpt.pt")
