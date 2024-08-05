import pickle
import joblib
from typing import Any
import os

class Serializer:
    @staticmethod
    def save_pickle(obj: Any, path: str):
        # SECURITY WARNING: Pickle is unsafe. Only use in trusted envs.
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def load_pickle(path: str) -> Any:
        with open(path, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def save_joblib(obj: Any, path: str):
        # Better for numpy arrays
        joblib.dump(obj, path)

    @staticmethod
    def load_joblib(path: str) -> Any:
        return joblib.load(path)
