import requests
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000/artifacts"  # ✅ Correct endpoint

for i in range(5):
    payload = {
        "test_name": "test_login_with_valid_credentials",
        "status": "fail",
        "failure_reason": "TimeoutError on button click",
        "run_id": f"run_20250709_00{i}",
        "timestamp": (datetime.now() - timedelta(days=i)).isoformat(),
    }

    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 200:
        print(f"[✓] - {payload['run_id']}")
    else:
        print(f"[{response.status_code}] - {payload['run_id']}")
