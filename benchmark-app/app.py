from flask import Flask
import time
import os
from prometheus_client import start_http_server, Summary, Counter, Gauge

app = Flask(__name__)

# Prometheus Metrics
REQUEST_LATENCY = Summary("request_latency_seconds", "Request latency")
REQUEST_COUNT = Counter("http_requests_total", "Total request count")
CPU_OPERATIONS = Counter("cpu_operations", "Number of CPU-intensive operations")

@app.route("/")
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.inc()
    app_type = os.getenv("APP_TYPE", "default")

    if app_type == "latency-sensitive":
        pass  # 快速回應
    elif app_type == "energy-limit":
        for _ in range(1000000):  # 模擬 CPU 密集計算
            _ = _ * 2
        CPU_OPERATIONS.inc()
    elif app_type == "resource-limit":
        time.sleep(0.2)  # 模擬延遲

    return f"Hello from {app_type} app!"

if __name__ == "__main__":
    start_http_server(8000)  # 暴露 metrics 端點
    app.run(host="0.0.0.0", port=8080)
