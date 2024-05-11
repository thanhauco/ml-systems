import os
import shutil

class ArtifactStore:
    """
    Abstraction over S3/GCS/Local for storing model binaries.
    """
    
    def __init__(self, base_uri: str):
        self.base_uri = base_uri
        if base_uri.startswith("s3://"):
            self.backend = "s3"
            # self.s3_client = boto3.client("s3")
        else:
            self.backend = "local"
            os.makedirs(base_uri, exist_ok=True)

    def upload_artifact(self, local_path: str, remote_path: str):
        target = f"{self.base_uri}/{remote_path}"
        print(f"Uploading {local_path} to {target}")
        
        if self.backend == "local":
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copy2(local_path, target)
    
    def download_artifact(self, remote_path: str, local_path: str):
        source = f"{self.base_uri}/{remote_path}"
        print(f"Downloading {source} to {local_path}")
        
        if self.backend == "local":
            shutil.copy2(source, local_path)
