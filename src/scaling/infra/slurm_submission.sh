import os

class SlurmGenerator:
    """
    Generates SBATCH scripts for distributed training.
    """
    
    def generate(self, job_name, nodes, gpus_per_node, script_path):
        content = f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --nodes={nodes}
#SBATCH --ntasks-per-node={gpus_per_node}
#SBATCH --gres=gpu:{gpus_per_node}
#SBATCH --cpus-per-task=10
#SBATCH --output=%x_%j.log

# Load Modules
module load cuda/11.8
module load nccl

# Network debugging
export NCCL_DEBUG=INFO

srun python {script_path}
"""
        return content

if __name__ == "__main__":
    print(SlurmGenerator().generate("train_gpt", 4, 8, "train.py"))
