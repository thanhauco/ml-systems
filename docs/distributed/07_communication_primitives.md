# Communication Primitives (NCCL)

## Collective Ops
1.  **Broadcast**: One sends to All. (Sending initial weights).
2.  **Scatter**: One splits data and sends parts to All.
3.  **Gather**: All send to One. (Logging).
4.  **AllGather**: Everyone gets everything. (Reconstructing FSDP weights).
5.  **Reduce**: Sum/Max/Min to Root.
6.  **AllReduce**: Sum/Max/Min to All. (DDP Gradients).
7.  **AllToAll**: Transpose. Everyone sends specific chunks to everyone else. (MoE).

## Ring Algorithm
Efficient implementation of AllReduce. Bandwidth optimal. 
Data moves in a logical ring $0 \rightarrow 1 \rightarrow 2 \rightarrow 0$.
