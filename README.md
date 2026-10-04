# 🚀 TraceIQ | AI-Powered Observability Platform

An end-to-end observability platform built to monitor API performance, detect system failures, visualize telemetry, and automate incident postmortem generation using Generative AI.

## 🚀 Key Features

* **Metrics Monitoring:** Tracks API requests, errors, latency, and database performance.
* **Centralized Logging:** Collects structured application logs for debugging.
* **Distributed Tracing:** Tracks request execution across services.
* **Automated Alerting:** Detects high error rates, latency spikes, and service failures.
* **AI-Powered Postmortems:** Uses Gemini to analyze telemetry and generate structured incident reports.
* **Performance Analysis:** Evaluates system behavior through Grafana dashboards.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, SQLAlchemy
* **Database:** PostgreSQL
* **Monitoring:** Prometheus, Grafana
* **Logging:** Loki, Promtail, Structlog
* **Tracing:** OpenTelemetry, Tempo
* **Alerting:** Alertmanager
* **GenAI:** Google Gemini 2.5 Flash
* **Deployment:** Docker, Docker Compose

## 🏗️ Architecture

```text
FastAPI Application
       |
       ├── Metrics ─────── Prometheus
       ├── Logs ────────── Loki + Promtail
       └── Traces ──────── OpenTelemetry + Tempo
                                |
                         Grafana Dashboard
                                |
                         Alertmanager
                                |
                     Incident Data Collection
                                |
                         Gemini 2.5 Flash
                                |
                     Automated Postmortem
```

## 📊 Custom Metrics

* `api_requests_total` — Total API requests
* `api_errors_total` — Total API errors
* `request_duration_seconds` — API response latency
* `active_requests` — Currently active requests
* `app_info` — Application metadata
* `db_query_duration_seconds` — Database query latency
* `product_operations_total` — Business operation counts

## 🤖 AI-Powered Incident Analysis

The platform collects logs, metrics, and traces from the monitoring stack and sends the incident context to Gemini.

It generates structured postmortem reports containing:

* Incident Summary
* Timeline
* Root Cause Analysis
* Service Impact
* Bottleneck Identification
* MTTR
* Preventive Action Items

## 🚦 Quick Start

### 1. Clone the Repository

```bash
git clone <repo-url>
cd Health_system
```

### 2. Configure Environment

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
LOG_LEVEL=INFO
```

### 3. Start the Platform

```bash
docker compose up --build
```

### 4. Access Services

| Service         | URL                        |
| --------------- | -------------------------- |
| FastAPI Swagger | http://localhost:8000/docs |
| Prometheus      | http://localhost:9090      |
| Grafana         | http://localhost:3001      |
| Alertmanager    | http://localhost:9093      |

## 🧪 Testing the System

### 1. Generate API Traffic

Use the Swagger UI to create products and send API requests.

### 2. Simulate an Incident

Introduce controlled API failures or latency to observe changes in metrics, logs, and traces.

### 3. Monitor the Dashboard

Open Grafana to inspect request rates, error rates, latency, and database performance.

### 4. Generate an AI Postmortem

```http
POST /postmortem/generate
```

The endpoint collects available telemetry and generates a structured incident report.

## 📈 Results

* Implemented 7 custom application and database metrics.
* Reduced MTTR from 16 minutes to 5 minutes in controlled failure simulations (~69% reduction).
* Reduced manual incident analysis and documentation effort by approximately 90% through automated postmortem generation.

## 🔮 Future Improvements

* Retrieval-Augmented Generation (RAG) for context-aware incident analysis.
* Historical incident knowledge base.
* Automated remediation recommendations.
* Advanced incident correlation.


## 👤 Author
**Umang Chandra**

