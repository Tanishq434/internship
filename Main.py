from fastapi import FastAPI
from prometheus_client import start_http_server, Summary, Counter
import time
import random

app = FastAPI()

# Metrics
REQUEST_TIME = Summary('request_duration_seconds', 'Time spent on requests')
REQUEST_COUNT = Counter('total_requests', 'Number of requests')

@app.get("/")
@REQUEST_TIME.time()
def read_root():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.2, 1.0))  # Simulate delay
    return {"message": "Hello from monitored FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    start_http_server(8001)  # Prometheus metrics endpoint
    uvicorn.run(app, host="0.0.0.0", port=8000)
