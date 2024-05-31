import subprocess
import sys

class DistributedLauncher:
    """
    Python equivalent of `torchrun` for programmatic launch.
    """
    
    def launch(self, script, nodes=1, gpus_per_node=1):
        cmd = [
            sys.executable, "-m", "torch.distributed.run",
            f"--nproc_per_node={gpus_per_node}",
            f"--nnodes={nodes}",
            script
        ]
        
        print(f"Launching distributed job: {' '.join(cmd)}")
        # subprocess.run(cmd)

if __name__ == "__main__":
    DistributedLauncher().launch("train.py", gpus_per_node=4)

