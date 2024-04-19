# Infrastructure as Code (IaC) for MLOps

## Configuring the Cloud
Clicking buttons in the AWS Console is not reproducible.

## Tools
1.  **Terraform**: Declarative. "I want 3 EC2 instances". The standard.
2.  **Ansible**: Configuration management. "Install Python 3.9 on these 3 instances".
3.  **Kubernetes Manifests**: `deployment.yaml`.
4.  **Pulumi**: IaC using Python/TypeScript instead of HCL.

## MLOps Resources
-   **Storage**: S3 Buckets (Data Lake), EFS.
-   **Compute**: G4dn instances (GPU training), Lambda (Serverless inference).
-   **Databases**: RDS (Metadata store), Redis (Feature store).
-   **Permissions**: IAM Roles (Model can read S3).
