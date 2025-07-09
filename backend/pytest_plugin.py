# backend/pytest_plugin.py
import requests
from datetime import datetime

def pytest_runtest_logreport(report):
    if report.when == "call":
        payload = {
            "test_name": report.nodeid,
            "status": "fail" if report.failed else "pass",
            "failure_reason": str(report.longrepr) if report.failed else None,
            "run_id": "run_20250709_auto",
            "timestamp": datetime.utcnow().isoformat()
        }
        try:
            res = requests.post("http://localhost:8000/artifacts", json=payload)
            print(f"[{res.status_code}] - {payload['test_name']}")
        except Exception as e:
            print("❌ Failed to post artifact:", e)
