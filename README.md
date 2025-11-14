README.md — Complete Observability System Using Prometheus, Grafana, Loki & Jaeger
Project Title

Complete Observability System: Metrics, Logs & Traces

 Objective

Build a fully integrated observability stack that monitors a sample application using:

Prometheus → Metrics

Loki + Promtail → Logs

Jaeger → Traces

Grafana → Dashboards

Docker Compose → To run everything easily

This project helps you understand how real-world monitoring systems work.

<<<<<<<< Project Architecture >>>>>>
            ┌──────────┐
            │   App    │
            │ Flask/Node│
            └─────┬────┘
                  │
         ┌────────┼──────────────┐
         │        │              │
         ▼        ▼              ▼
   Prometheus   Promtail       Jaeger
   (Metrics)     │           (Traces)
                 ▼
                Loki
               (Logs)
         └────────┬────────┘
                  ▼
               Grafana
          (Dashboards UI)

 Project Structure

observability/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── docker-compose.yml
├── prometheus.yml
├── loki-config.yml
├── promtail-config.yml
│
└── README.md

 
 ********** Tools Used **************
Tool	Purpose
Prometheus	Scrapes metrics from the application
Grafana	Visualizes logs, metrics, traces
Loki	Stores logs
Promtail	Sends Docker logs → Loki
Jaeger	Shows request traces
Docker Compose	Runs all services together

How to Run This Project
1. Install Docker & Docker Compose

Download from:
https://www.docker.com/products/docker-desktop

2. Run the Entire Stack

Open terminal in this project folder:

docker-compose up --build

🌐 Service URLs
Service	URL
Application	http://localhost:8080

Prometheus	http://localhost:9090

Grafana	http://localhost:3000

Jaeger (Traces)	http://localhost:16686

Loki	Integrated in Grafana
 Sample Application Explanation

The sample Flask application does:

✔ Logs: "Home endpoint called"
✔ Metrics:

total requests

request latency
✔ Dummy delay (to see graphs)
✔ /metrics endpoint for Prometheus

 Configuration Files
 1. Prometheus (prometheus.yml)

Prometheus scrapes metrics from:

app:8080

⭐ 2. Loki (loki-config.yml)

Stores logs locally.

⭐ 3. Promtail (promtail-config.yml)

Reads Docker logs:

/var/lib/docker/containers/*/*.log

⭐ 4. docker-compose.yml

Runs:

app

prometheus

loki

promtail

grafana

jaeger

Everything starts with one command.

Grafana Dashboards

After opening Grafana (http://localhost:3000):

Login →

admin / admin


Add datasources:

Prometheus → http://prometheus:9090

Loki → http://loki:3100

Jaeger → http://jaeger:16686

Create dashboards:

Request count graph

Latency graph

Logs panel

Tracing panel

Export dashboards as JSON and include in your submission.

 Testing the App

Open terminal:

curl localhost:8080
curl localhost:8080/metrics

<img width="1919" height="1044" alt="Screenshot 2025-11-14 121554" src="https://github.com/user-attachments/assets/63b64d45-0817-4d17-969c-684f55e63625" />

<img width="1919" height="1040" alt="Screenshot 2025-11-14 121622" src="https://github.com/user-attachments/assets/630e4883-30c6-4e3e-b3ee-eb04a5bf38a8" />

<img width="1913" height="1033" alt="Screenshot 2025-11-14 121705" src="https://github.com/user-attachments/assets/fac9d06a-12fc-4a26-93f2-7b0b2b186158" />

<img width="1913" height="1036" alt="Screenshot 2025-11-14 121731" src="https://github.com/user-attachments/assets/7cc0ae52-2a35-47e3-8c55-9c7c5e40c21f" />

<img width="1911" height="1040" alt="Screenshot 2025-11-14 123354" src="https://github.com/user-attachments/assets/d6cce7d0-459e-4d25-8486-8118023f175d" />

<img width="1916" height="1037" alt="Screenshot 2025-11-14 121945" src="https://github.com/user-attachments/assets/cf5058c1-28fb-476e-a53c-e12980c88194" />


Generate traffic:

while true; do curl localhost:8080; sleep 1; done

>> What You Will Observe
Metrics (Prometheus/Grafana)

Request count increasing

Latency histogram

Traffic spikes

 Logs (Loki/Grafana)

Log lines from the app

Ability to filter logs

View error logs if any

 Traces (Jaeger)

Each request trace

Timeline view

Latency breakdown

Report Summary (For Submission)

You can include:

1. Introduction

Explain metrics, logs, traces.

2. Architecture

Insert the diagram provided above.

3. Tools Used

Prometheus, Grafana, Loki, Promtail, Jaeger.

4. Observations

Metrics show request trends

Logs show call patterns

Jaeger shows full trace

Delay demonstrates latency graphs

5. Conclusion

Observability provides full visibility and helps debugging.
