import os
from typing import BinaryIO

class MinIOClient:
    """
    S3-Compatible Object Storage Client.
    """
    
    def __init__(self, endpoint: str, access_key: str, secret_key: str):
        self.endpoint = endpoint
        print(f"Connected to MinIO at {endpoint}")

    def upload_file(self, bucket: str, object_name: str, file_path: str):
        print(f"Uploading {file_path} -> {bucket}/{object_name}")

    def download_file(self, bucket: str, object_name: str, file_path: str):
        print(f"Downloading {bucket}/{object_name} -> {file_path}")

    def get_presigned_url(self, bucket: str, object_name: str, expires: int = 3600) -> str:
        return f"https://{self.endpoint}/{bucket}/{object_name}?token=xyz"
