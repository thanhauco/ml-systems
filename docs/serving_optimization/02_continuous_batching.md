# Continuous Batching (Orca)

## Static vs Continuous
- **Static Batching**: Wait for a batch of $N$ requests. Process all until the *last* one finishes. Short requests wait for the longest one (Head-of-Line Blocking).
- **Continuous Batching**: Evolution is iteration-level, not request-level.
    - At each step, if a sequence finishes, it is evicted.
    - A new sequence from the queue is inserted immediately into the "running" batch.

## Scheduling Policy
The scheduler decides at every token generation step:
1.  Which active sequences get a slot?
2.  Is there enough KV cache memory (blocks) to extend them by 1 token?
3.  Should we preempt (swap out to CPU) a lower-priority sequence to make room?

## Throughput Impact
Continuous batching can improve serving throughput by 10x-20x over diverse workloads compared to naive static batching.
