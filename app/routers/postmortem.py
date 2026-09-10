import httpx
import time
from fastapi import APIRouter
from app.logger import log
from google import genai
from dotenv import load_dotenv
load_dotenv()
import os


router = APIRouter(
    prefix="/postmortem",
    tags=["Postmortem"]
)

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")


async def fetch_logs():
    end = int(time.time() * 1e9)
    start = int((time.time() - 1800) * 1e9)  # last 30 min

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://loki:3100/loki/api/v1/query_range",
            params={
                "query": '{job="fastapi-app"}',
                "start": start,
                "end": end,
                "limit": 100
            }
        )
        data = response.json()
        logs = []
        for stream in data.get("data", {}).get("result", []):
            for entry in stream.get("values", []):
                logs.append(entry[1])
        return logs


async def fetch_metrics():
    async with httpx.AsyncClient() as client:
        error_rate = await client.get(
            "http://prometheus:9090/api/v1/query",
            params={"query": "rate(api_errors_total[5m])"}
        )
        latency = await client.get(
            "http://prometheus:9090/api/v1/query",
            params={"query": "histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))"}
        )
        return {
            "error_rate": error_rate.json(),
            "latency_p95": latency.json()
        }


async def fetch_traces():
    end_ns = int(time.time() * 1e9)
    start_ns = int((time.time() - 1800) * 1e9)

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://tempo:3200/api/search",
            params={
                "start": int(start_ns / 1e9),
                "end": int(end_ns / 1e9),
                "limit": 10
            }
        )
        return response.json()


@router.post("/generate")
async def generate_postmortem():
    log.info("postmortem generation started")

    logs = await fetch_logs()
    metrics = await fetch_metrics()
    traces = await fetch_traces()

    prompt = f"""
You are an SRE engineer. Generate a blameless postmortem report based on the following observability data.

## Logs (last 30 minutes):
{chr(10).join(logs[:50])}

## Metrics:
- Error Rate: {metrics['error_rate']}
- P95 Latency: {metrics['latency_p95']}

## Traces:
{traces}

Generate a structured postmortem with:
1. Incident Summary
2. Timeline (when issue started, when detected, when resolved)
3. Root Cause
4. Impact
5. Bottleneck Service (from traces)
6. Fix Applied
7. MTTR
8. Action Items to prevent recurrence

IMPORTANT RULES:
- Only use the data provided above. Do not assume or fabricate any information.
- If logs are empty, say "No logs available for this period."
- If metrics show no data, say "Metrics unavailable."
- If traces are empty, say "No traces captured."
- Do not guess the root cause if data is insufficient — say "Root cause undetermined due to insufficient data."


"""

    # response = model.generate_content(prompt)

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )
    




    log.info("postmortem generation complete")

    return {
        "postmortem": response.text,
        "sources": {
            "logs_fetched": len(logs),
            "traces_fetched": len(traces.get("traces", []))
        }
    }