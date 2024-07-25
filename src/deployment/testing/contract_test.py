import pytest
import requests
from pydantic import BaseModel, ValidationError

class ResponseSchema(BaseModel):
    id: str
    prediction: float
    latency_ms: float

def test_api_contract():
    url = "http://localhost:8000/predict"
    payload = {"id": "test", "features": [0.0]}
    
    try:
        resp = requests.post(url, json=payload)
    except requests.exceptions.ConnectionError:
        pytest.skip("API not running")

    assert resp.status_code == 200
    
    # Validation
    try:
        data = ResponseSchema(**resp.json())
        assert isinstance(data.prediction, float)
    except ValidationError as e:
        pytest.fail(f"Schema mismatch: {e}")

if __name__ == "__main__":
    test_api_contract()

