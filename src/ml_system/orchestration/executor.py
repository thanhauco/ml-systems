from abc import ABC, abstractmethod
from typing import Dict, Any
import subprocess

class Executor(ABC):
    @abstractmethod
    def run_command(self, cmd: str) -> int:
        pass

class LocalExecutor(Executor):
    def run_command(self, cmd: str) -> int:
        print(f"[LocalExecutor] Running: {cmd}")
        return subprocess.call(cmd.split())

class DockerExecutor(Executor):
    def __init__(self, image: str):
        self.image = image

    def run_command(self, cmd: str) -> int:
        docker_cmd = f"docker run --rm {self.image} {cmd}"
        print(f"[DockerExecutor] Running: {docker_cmd}")
        # In reality, use docker sdk
        return 0
