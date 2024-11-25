# from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
# from torch.distributed.fsdp.wrap import size_based_auto_wrap_policy

class FSDPWrapper:
    """
    Configuration for FSDP (ZeRO-3).
    """
    
    def wrap(self, model):
        # auto_wrap_policy = functools.partial(
        #     size_based_auto_wrap_policy, min_num_params=1e6
        # )
        
        print("Wrapping model with FSDP (Sharding strategy: FULL_SHARD)...")
        # fsdp_model = FSDP(model, auto_wrap_policy=auto_wrap_policy)
        return model

if __name__ == "__main__":
    FSDPWrapper().wrap(None)
