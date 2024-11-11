from typing import List, Dict

class LineageGraph:
    """
    Tracks dependencies between Data, Code, and Models.
    """
    def __init__(self):
        self.adjacency = {} # artifact_id -> [downstream_artifact_ids]

    def add_event(self, source_id: str, target_id: str, operation: str):
        if source_id not in self.adjacency:
            self.adjacency[source_id] = []
        self.adjacency[source_id].append({"target": target_id, "op": operation})

    def get_downstream(self, artifact_id: str) -> List[Dict]:
        return self.adjacency.get(artifact_id, [])
