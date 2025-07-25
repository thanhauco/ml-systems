from typing import List

class PoisonDetector:
    """
    Detects backdoor poisoning in training data.
    """
    
    def scan_dataset(self, data_sources: List[str]):
        print(f"Scanning {len(data_sources)} data sources for statistical anomalies...")
        
        suspicious = []
        for source in data_sources:
            # Simulate gradient sniffing
            cluster_variance = self._analyze_cluster(source)
            if cluster_variance > 0.8:
                print(f"PoisonDetector: Source '{source}' flagged (High Variance).")
                suspicious.append(source)
                
        return suspicious

    def _analyze_cluster(self, source_id):
        # Mock analysis
        import random
        return random.random()

if __name__ == "__main__":
    pd = PoisonDetector()
    sources = ["common_crawl_shard_1", "verified_partner_data", "untrusted_user_uploads"]
    pd.scan_dataset(sources)
