import json
import httpx
from pathlib import Path

BASE = "http://127.0.0.1:8001"

# 1. Enable rag_slow
r = httpx.post(f"{BASE}/incidents/rag_slow/enable")
print("Enable rag_slow:", r.json())

# 2. Send 3 requests during incident
lines = [l for l in Path("data/sample_queries.jsonl").read_text().splitlines() if l.strip()][:3]
print("\nRequests during incident (expect high latency):")
for line in lines:
    r = httpx.post(f"{BASE}/chat", json=json.loads(line), timeout=30)
    d = r.json()
    cid = d.get("correlation_id")
    lat = d.get("latency_ms")
    print(f"  [{r.status_code}] {cid} | latency={lat}ms")

# 3. Disable incident
r = httpx.post(f"{BASE}/incidents/rag_slow/disable")
print("\nDisable rag_slow:", r.json())
print("\nDone! Check logs and Langfuse for high latency traces.")
