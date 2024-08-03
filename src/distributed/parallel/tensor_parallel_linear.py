class ColumnParallelLinear:
    """
    Splits Weight matrix [Out, In] along the Output dimension.
    """
    
    def __init__(self, in_features, out_features, world_size):
        self.chunk_size = out_features // world_size
        print(f"Initializing ColumnParallelLinear: In={in_features}, OutChunk={self.chunk_size}")
        # self.weight = Parameter(torch.empty(self.chunk_size, in_features))

    def forward(self, x):
        # Y_partial = X @ W_chunk
        # AllGather(Y_partial) NOT needed here usually, but output is sharded.
        print("Forward: Computing partial linear output")
        return "ShardedOutput"

class RowParallelLinear:
    """
    Splits Weight matrix [Out, In] along the Input dimension.
    """
    pass
