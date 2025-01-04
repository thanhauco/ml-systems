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
        docker_cmd = ["docker", "run", "--rm", self.image] + cmd.split()
        print(f"[DockerExecutor] Running: {' '.join(docker_cmd)}")
        # Simulate execution success
        return 0

