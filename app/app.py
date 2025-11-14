from flask import Flask
import time
import logging
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Metrics
REQUEST_COUNTER = Counter("requests_total", "Total HTTP Requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency")

@app.route("/")
def home():
    logging.info("Home endpoint called")

    start = time.time()

    REQUEST_COUNTER.inc()
    time.sleep(0.5)  # dummy delay

    REQUEST_LATENCY.observe(time.time() - start)

    return "Hello! Observability is working!"

@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0", port=8080)

