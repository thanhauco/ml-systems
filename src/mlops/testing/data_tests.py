from typing import List, Dict, Any, Callable
import math

class DataValidator:
    """
    Lightweight GreatExpectations-style validator.
    """
    
    def __init__(self, df: List[Dict[str, Any]]):
        self.df = df
        self.errors = []

    def expect_column_to_exist(self, column: str) -> 'DataValidator':
        if not self.df: return self
        if column not in self.df[0]:
            self.errors.append(f"Column {column} missing")
        return self

    def expect_column_values_to_be_between(self, column: str, min_val: float, max_val: float) -> 'DataValidator':
        for i, row in enumerate(self.df):
            val = row.get(column)
            if not isinstance(val, (int, float)): continue
            if not (min_val <= val <= max_val):
                self.errors.append(f"Row {i} {column}={val} out of range [{min_val}, {max_val}]")
        return self

    def validate(self) -> bool:
        if self.errors:
            print("Validation Failed:")
            for e in self.errors:
                print(f" - {e}")
            return False
        print("Validation Passed")
        return True
