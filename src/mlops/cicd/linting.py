import subprocess
import sys

class Linter:
    """
    Wrapper for running code quality checks (Ruff, Black, Mypy).
    """
    
    @staticmethod
    def run_check(command: list) -> bool:
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"FAILED:\n{result.stderr}")
            return False
        print("PASSED")
        return True

    @staticmethod
    def check_all(path: str = "."):
        checks = [
            ["black", "--check", path],
            ["ruff", "check", path],
            ["mypy", path]
        ]
        
        all_passed = True
        for cmd in checks:
            if not Linter.run_check(cmd):
                all_passed = False
        
        return all_passed

if __name__ == "__main__":
    if not Linter.check_all("src/"):
        sys.exit(1)
