from functools import wraps
import time
from .experiment_manager import ExperimentManager

def auto_log(exp_manager: ExperimentManager):
    """
    Decorator to automatically log function arguments and execution time.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log params
            for k, v in kwargs.items():
                if isinstance(v, (int, float, str, bool)):
                    try:
                        exp_manager.log_param(k, v)
                    except Exception:
                        pass
            
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                duration = time.perf_counter() - start
                try:
                    exp_manager.log_metric(f"{func.__name__}_duration", duration)
                except Exception:
                    pass
        return wrapper
    return decorator
