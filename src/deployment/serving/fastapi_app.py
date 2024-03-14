from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
import time

app = FastAPI(title="ML Inference Service")

class PredictionRequest(BaseModel):
    id: str
    features: List[float]

class PredictionResponse(BaseModel):
    id: str
    prediction: float
    latency_ms: float

# Mock model loading
model = None

@app.on_event("startup")
async def load_model():
    global model
    # Simulate loading
    time.sleep(2)
    model = lambda x: sum(x) / len(x) if x else 0.0
    print("Model loaded successfully")

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not ready")
    
    start = time.perf_counter()
    try:
        result = model(request.features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    duration = (time.perf_counter() - start) * 1000
    
    return PredictionResponse(
        id=request.id,
        prediction=result,
        latency_ms=duration
    )

@app.get("/health")
async def health():
    return {"status": "healthy" if model else "unhealthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
