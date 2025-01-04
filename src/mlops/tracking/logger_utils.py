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
                    except Exception as e:
                        # Avoid crashing app due to logging failure
                        print(f"Failed to log param {k}: {e}")
            
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                duration = time.perf_counter() - start
                try:
                    exp_manager.log_metric(f"{func.__name__}_duration", duration)
                except Exception as e:
                    print(f"Failed to log duration: {e}")
        return wrapper
    return decorator
