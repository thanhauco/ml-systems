import importlib
import time
from functools import wraps
from typing import Callable, Any

def dynamic_import(class_path: str) -> Any:
    """
    Dynamically imports a class from a string path.
    e.g., 'sklearn.linear_model.LogisticRegression'
    """
    module_path, class_name = class_path.rsplit('.', 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)

def timey(logger=None):
    """Decorator to measure execution time."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            msg = f"{func.__name__} took {duration:.4f}s"
            if logger:
                logger.info(msg)
            else:
                print(msg)
            return result
        return wrapper
    return decorator

def retry(retries: int = 3, delay: float = 1.0):
    """Simple retry decorator with exponential backoff."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(current_delay)
                    current_delay *= 2
            raise last_exception
        return wrapper
    return decorator
