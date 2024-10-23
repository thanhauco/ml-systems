from typing import List

class GitHubActionsBuilder:
    """
    Generates .github/workflows/ml-pipeline.yaml programmatically.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.steps = []

    def add_checkout(self):
        self.steps.append({
            "name": "Checkout code",
            "uses": "actions/checkout@v3"
        })

    def add_python_setup(self, version: str = "3.9"):
        self.steps.append({
            "name": f"Set up Python {version}",
            "uses": "actions/setup-python@v4",
            "with": {"python-version": version}
        })
        
    def add_install_deps(self):
        self.steps.append({
            "name": "Install dependencies",
            "run": "pip install -r requirements.txt"
        })

    def add_test_step(self):
        self.steps.append({
            "name": "Run Tests",
            "run": "pytest tests/"
        })

    def generate_yaml(self) -> str:
        workflow = {
            "name": self.name,
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": self.steps
                }
            }
        }
        import yaml
        return yaml.dump(workflow, sort_keys=False)

if __name__ == "__main__":
    builder = GitHubActionsBuilder("ML CI Pipeline")
    builder.add_checkout()
    builder.add_python_setup()
    builder.add_install_deps()
    builder.add_test_step()
    print(builder.generate_yaml())
