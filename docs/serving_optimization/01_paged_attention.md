# PagedAttention: Memory Management for LLMs

## The Fragmentation Problem
In traditional attention mechanisms, Key-Value (KV) cache tensors are pre-allocated continuously in GPU memory. Since generation length is unknown a priori, this leads to:
1.  **Internal Fragmentation**: Over-allocation for max length.
2.  **External Fragmentation**: Inability to fit new requests despite free memory existing in small gaps.

## The Virtual Memory Solution
PagedAttention borrows from OS virtual memory (paging).
- **Physical Blocks**: Fixed-size chunks of memory (e.g., storing 16 tokens).
- **Logical Blocks**: Contiguous from the model's perspective.
- **Block Table**: Maps logical blocks to physical blocks.

## Benefits
- Near-zero memory waste (<4%).
- **Sharing**: System prompts can be stored in physical blocks shared across multiple sequences (perfect for "System Prompt" + "User Query" batching).
