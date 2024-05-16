# Slurm Workload Manager

## HPC Standard
Simple Linux Utility for Resource Management. Used by most supercomputers and academic clusters.

## Concepts
-   **Job**: An allocation of resources for a time.
-   **Partition**: Queue (e.g., `gpu-debug`, `gpu-prod`).
-   **Node/Task/CPU**: Hierarchy.

## Commands
-   `sbatch script.sh`: Submit job.
-   `squeue`: Check status.
-   `scancel`: Kill job.
-   `sinfo`: Node status.

## Example Script
```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --gpus-per-node=4
#SBATCH --time=02:00:00

srun python train.py
```
