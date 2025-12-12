import concurrent.futures
import uuid
from typing import Any, Callable

class ObjectRef:
    def __init__(self, obj_id: str, value: Any = None):
        self.obj_id = obj_id
        self._value = value
        self._future = None

    def set_future(self, future):
        self._future = future

    def get(self):
        if self._future:
            return self._future.result()
        return self._value

class RayMock:
    """
    Simulates Ray's API: init, remote, get, wait.
    """
    _executor = None

    @classmethod
    def init(cls):
        print("Initializing Ray Cluster (Simulation)...")
        cls._executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    @classmethod
    def get(cls, refs):
        if isinstance(refs, list):
            return [r.get() for r in refs]
        return refs.get()

    @classmethod
    def remote(cls, func_or_class):
        # Decorator logic
        class RemoteWrapper:
            def __init__(self, *args, **kwargs):
                self._obj = func_or_class(*args, **kwargs) if isinstance(func_or_class, type) else None
                self._func = func_or_class
            
            def remote(self, *args, **kwargs):
                obj_id = str(uuid.uuid4())
                ref = ObjectRef(obj_id)
                
                # Execute in thread pool
                if RayMock._executor is None:
                    raise RuntimeError("Call RayMock.init() first")
                
                def task():
                    if isinstance(func_or_class, type):
                        # Method call on actor logic is complex to mock purely with decorators
                        # verifying this later
                        # For simulation, we assume logic is handled by the proxy or we invoke directly if possible
                        # But since 'func_or_class' is the class type here, and we don't have the instance easily in this scope 
                        # without more complex state management.
                        # We will log a warning and return DUMMY.
                        print(f"Warning: Mock Actor task execution not fully simulated for {func_or_class}")
                        return "MOCK_ACTOR_RESULT"
                    return self._func(*args, **kwargs)

                future = RayMock._executor.submit(task)
                ref.set_future(future)
                return ref

        if isinstance(func_or_class, type):
            # Actor simulation: return a class that builds proxies
            class ActorProxy:
                def __init__(self, *args, **kwargs):
                    self.instance = func_or_class(*args, **kwargs)
                
                def __getattr__(self, name):
                    method = getattr(self.instance, name)
                    def remote_method(*m_args, **m_kwargs):
                        obj_id = str(uuid.uuid4())
                        ref = ObjectRef(obj_id)
                        future = RayMock._executor.submit(method, *m_args, **m_kwargs)
                        ref.set_future(future)
                        return ref
                    # Helper to allow .remote() call
                    class MethodProxy:
                        def remote(self, *a, **k): return remote_method(*a, **k)
                    return MethodProxy()
            
            # Add .remote() to the original class
            func_or_class.remote = lambda *a, **k: ActorProxy(*a, **k)
            return func_or_class
        else:
            # Task simulation
            func_or_class.remote = RemoteWrapper(func_or_class).remote
            return func_or_class

# Usage alias
ray = RayMock
