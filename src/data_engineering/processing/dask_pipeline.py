import dask.dataframe as dd
from typing import Dict, Any

class DaskPipeline:
    """
    Parallel processing using Dask for single-machine scaling.
    """
    
    def __init__(self, n_partitions: int = 4):
        self.n_partitions = n_partitions

    def process_csv(self, input_pattern: str, output_dir: str):
        print(f"Dask: Reading {input_pattern}")
        # Lazy read
        df = dd.read_csv(input_pattern)
        
        # Repartition
        df = df.repartition(npartitions=self.n_partitions)
        
        # Transformations
        df['amount'] = df['amount'].fillna(0)
        df['is_high_value'] = df['amount'] > 1000
        
        # GroupBy (Aggregations)
        result = df.groupby('category').amount.mean()
        
        # Compute/Write
        print(f"Dask: Writing to {output_dir}")
        result.to_csv(f"{output_dir}/means-*.csv") # Computes here
