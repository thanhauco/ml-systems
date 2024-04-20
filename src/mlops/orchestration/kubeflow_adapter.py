from typing import Callable

class KubeflowAdapter:
    """
    Mock adapter for creating KFP components.
    """
    
    @staticmethod
    def component(base_image: str = "python:3.9"):
        def decorator(func: Callable):
            def wrapper(*args, **kwargs):
                print(f"Running KFP Component: {func.__name__} in {base_image}")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def pipeline(name: str):
        def decorator(func: Callable):
            def wrapper(*args, **kwargs):
                print(f"Compiling Pipeline: {name}")
                return func(*args, **kwargs)
            return wrapper
        return decorator

# Usage:
# @KubeflowAdapter.component()
# def preprocess(data_path: str): ...
