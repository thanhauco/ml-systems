from typing import List, Dict, Optional

class PhysicalTokenBlock:
    def __init__(self, block_id: int, block_size: int):
        self.block_id = block_id
        self.size = block_size
        self.ref_count = 0
        # self.data = torch.zeros(...) # Simulated

class BlockTable:
    def __init__(self, seq_id: int, block_size: int):
        self.seq_id = seq_id
        self.block_size = block_size
        self.physical_blocks: List[PhysicalTokenBlock] = []

    def append_slot(self, block_allocator) -> bool:
        # Check if last block has space
        if self.physical_blocks:
            last_block = self.physical_blocks[-1]
            # In a real impl, we track per-block occupancy.
            # Here we simplify: always allocate new block for demo.
            pass
        
        # Allocate new block
        new_block = block_allocator.allocate()
        if new_block:
            self.physical_blocks.append(new_block)
            return True
        return False

class KVCacheManager:
    """
    Manages the 'Physical' GPU memory blocks.
    """
    def __init__(self, num_blocks: int = 100, block_size: int = 16):
        self.free_blocks = [PhysicalTokenBlock(i, block_size) for i in range(num_blocks)]
        self.used_blocks = {}
        self.block_tables = {}

        print(f"Initialized Cache Manager with {num_blocks} blocks of size {block_size}")

    def allocate(self) -> Optional[PhysicalTokenBlock]:
        if not self.free_blocks:
            return None
        block = self.free_blocks.pop()
        block.ref_count += 1
        self.used_blocks[block.block_id] = block
        return block

    def free(self, block: PhysicalTokenBlock):
        block.ref_count -= 1
        if block.ref_count == 0:
            del self.used_blocks[block.block_id]
            self.free_blocks.append(block)

    def get_utilization(self) -> float:
        total = len(self.free_blocks) + len(self.used_blocks)
        return len(self.used_blocks) / total
