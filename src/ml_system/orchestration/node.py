from typing import Dict, Any, List
from ..core.base_component import BaseComponent

class PipelineNode:
    """
    Wraps a BaseComponent to be executable within a Pipeline.
    """
    def __init__(self, component: BaseComponent, name: str = None):
        self.component = component
        self.name = name or component.name
        self.upstreams: List[str] = []
        
    def execute(self, context: Dict[str, Any]):
        """
        Executes the wrapped component.
        """
        print(f"--- Running Node: {self.name} ---")
        try:
            self.component.initialize()
            result = self.component.execute(context)
            self.component.shutdown()
            return result
        except Exception as e:
            print(f"Node {self.name} Failed: {e}")
            raise e
