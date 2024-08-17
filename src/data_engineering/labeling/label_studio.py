from typing import Dict, Any, List

class LabelStudioClient:
    """
    Mock client for Label Studio API.
    """
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    def create_project(self, title: str):
        print(f"Creating project '{title}' in Label Studio")
        return {"id": 1, "title": title}

    def import_tasks(self, project_id: int, tasks: List[Dict[str, Any]]):
        print(f"Importing {len(tasks)} tasks into project {project_id}")

    def export_annotations(self, project_id: int) -> List[Dict[str, Any]]:
        print(f"Exporting annotations from project {project_id}")
        return [
            {"id": 100, "result": [{"value": {"choices": ["Positive"]}}]}
        ]
