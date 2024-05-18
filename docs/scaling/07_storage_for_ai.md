# Storage for AI

## The I/O Bottleneck
GPUs process data faster than standard NFS can supply it. 
*Symptom*: Volatile GPU utilization (0% -> 100% -> 0%).

## Solutions
1.  **Lustre / GPFS**: Parallel file systems. Striping data across thousands of disks.
2.  **Object Storage (S3)**: High throughput, high latency. Bad for random access.
3.  **Local NVMe Caching**: Copy dataset to `/scratch` on the node before training.
4.  **GPUDirect Storage**: DMA from NVMe to GPU Memory.

## Formats
-   **WebDataset**: Tarballs of images. Sequential read.
-   **Parquet**: Columnar. Good for tabular.
-   **TFRecord**: Protobuf based.
