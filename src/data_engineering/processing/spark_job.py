from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace
from typing import Dict, Any

class SparkJob:
    """
    Template for a PySpark ETL Job.
    """
    
    def __init__(self, app_name: str, config: Dict[str, Any]):
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .getOrCreate()
        self.config = config

    def extract(self):
        input_path = self.config["input_path"]
        print(f"Reading from {input_path}")
        return self.spark.read.parquet(input_path)

    def transform(self, df):
        print("Transforming dataframe...")
        # Example: Clean text column
        return df.withColumn("cleaned_text", lower(regexp_replace(col("raw_text"), "[^a-zA-Z0-9 ]", "")))

    def load(self, df):
        output_path = self.config["output_path"]
        print(f"Writing to {output_path}")
        df.write.mode("overwrite").parquet(output_path)

    def run(self):
        df = self.extract()
        transformed_df = self.transform(df)
        self.load(transformed_df)
        self.spark.stop()
