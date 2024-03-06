from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Request, Response
import time

REQUEST_COUNT = Counter("http_requests_total", "Total Requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["endpoint"])

async def prometheus_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    endpoint = request.url.path
    status = str(response.status_code)
    
    REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status=status).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
    
    return response

# Helper to expose /metrics
async def metrics_endpoint():
    return Response(generate_latest(), media_type="text/plain")

