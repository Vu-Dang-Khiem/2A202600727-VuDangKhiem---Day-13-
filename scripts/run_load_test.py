import json
import time
import httpx
from pathlib import Path

QUERIES = Path("data/sample_queries.jsonl")
lines = [line for line in QUERIES.read_text(encoding="utf-8").splitlines() if line.strip()]

print(f"Sending {len(lines)} requests to port 8001...")
with httpx.Client(timeout=30.0) as client:
    for i, line in enumerate(lines):
        payload = json.loads(line)
        r = client.post("http://127.0.0.1:8001/chat", json=payload)
        data = r.json()
        cid = data.get("correlation_id", "?")
        lat = data.get("latency_ms", "?")
        feat = payload.get("feature", "?")
        print(f"[{i+1}/{len(lines)}] {r.status_code} | {cid} | {feat} | {lat}ms")
        time.sleep(0.1)

print("Done!")
