import subprocess

class InfraProvisioner:
    """
    Mock Terraform Wrapper.
    """
    
    def plan(self):
        print("Terraform Plan...")
        print("+ aws_s3_bucket.model_registry")
        print("+ aws_eks_cluster.ml_cluster")

    def apply(self):
        print("Terraform Apply...")
        # subprocess.run(["terraform", "apply", "-auto-approve"])
        print("Infrastructure Provisioned Successfully.")

    def destroy(self):
        print("Destorying Infrastructure...")

if __name__ == "__main__":
    p = InfraProvisioner()
    p.plan()
    p.apply()
