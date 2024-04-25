class S3StreamingDataset:
    """
    Streams data from S3 buckets directly (WebDataset style).
    Avoids downloading full 10TB dataset to disk.
    """
    
    def __init__(self, bucket_urls):
        self.urls = bucket_urls

    def __iter__(self):
        print(f"Streaming tarballs from {self.urls[0]}...")
        # while True:
        #    yield next_sample
        yield ("image.jpg", "label.txt")
