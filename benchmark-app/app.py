import os
import time
from flask import Flask, Response
# prometheus_client 提供了幫你暴露 metrics 的功能
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Summary, Counter

app = Flask(__name__)

# 定義指標
REQUEST_LATENCY = Summary('http_request_latency_seconds', 'Request latency')
REQUEST_COUNT = Counter('http_requests_total', 'Total number of http requests')
CPU_INTENSIVE_COUNT = Counter('cpu_intensive_operations', 'CPU intensive ops count')

@app.route('/')
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.inc()

    app_type = os.environ.get('APP_TYPE', 'default')
    if app_type == 'latency-sensitive':
        # 模擬延遲敏感 => 盡量不做額外延遲
        pass

    elif app_type == 'energy-limit':
        # 模擬需要CPU計算 => 累積計算量
        CPU_INTENSIVE_COUNT.inc()
        x = 0
        for i in range(1000000):
            x += i

    elif app_type == 'resource-limit':
        # 模擬做一些IO等待 => sleep 0.2秒
        time.sleep(0.2)

    return f"Hello from {app_type} app!"

# /metrics 路徑：暴露 Prometheus 格式指標
@app.route('/metrics')
def metrics():
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
