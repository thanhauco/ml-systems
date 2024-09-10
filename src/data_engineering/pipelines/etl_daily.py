from ..ingestion.api_crawler import AsyncAPICrawler
from ..processing.cleaning import TextCleaner
from ..storage.delta_lake import DeltaTable
from ..storage.minio import MinIOClient
import asyncio

async def run_daily_etl():
    """
    Orchestrates the daily data ingest.
    1. Crawl API
    2. Save Raw to MinIO (Bronze)
    3. Clean Text
    4. Write to Delta Lake (Silver)
    """
    print("--- Starting Daily ETL ---")
    
    # 1. Ingest
    crawler = AsyncAPICrawler("https://api.example.com")
    raw_data = await crawler.fetch_all(["users", "posts"])
    print(f"Fetched {len(raw_data)} records")

    # 2. Bronze
    minio = MinIOClient("play.min.io", "user", "pass")
    # Simulate save
    minio.upload_file("lake-bronze", "date=2024-01-01/data.json", "/tmp/data.json")

    # 3. Transform
    clean_data = []
    for record in raw_data:
        if "text" in record:
            record["text"] = TextCleaner.normalize(record["text"])
            clean_data.append(record)

    # 4. Silver
    delta = DeltaTable("/mnt/lake/silver/entries")
    delta.merge(clean_data, condition="source.id = target.id")
    
    print("--- ETL Finished ---")

if __name__ == "__main__":
    asyncio.run(run_daily_etl())


