import os
# import torch
# import torch.distributed as dist
# from torch.nn.parallel import DistributedDataParallel as DDP

class DDPSetup:
    """
    Boilerplate for setting up process group and wrapping model in DDP.
    """
    
    def setup(self):
        # Reads env vars set by torchrun (MASTER_ADDR, etc)
        rank = int(os.environ.get("RANK", "0"))
        world_size = int(os.environ.get("WORLD_SIZE", "1"))
        local_rank = int(os.environ.get("LOCAL_RANK", "0"))
        
        print(f"[Rank {rank}] Initializing Process Group...")
        # dist.init_process_group("nccl")
        # torch.cuda.set_device(local_rank)
        
        return rank, local_rank

    def wrap_model(self, model, local_rank):
        print(f"Wrapping model in DDP on device {local_rank}...")
        # model = model.to(local_rank)
        # return DDP(model, device_ids=[local_rank])
        return model # Mock

    def cleanup(self):
        print("Destroying Process Group...")
        # dist.destroy_process_group()

if __name__ == "__main__":
    DDPSetup().setup()
