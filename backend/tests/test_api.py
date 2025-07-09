import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from backend.main import app
from datetime import datetime

client = TestClient(app)

def test_add_artifact():
    payload = {
        "test_name": "login_test",
        "status": "fail",
        "failure_reason": "Element not found",
        "run_id": "run_101",
        "timestamp": datetime.utcnow().isoformat()
    }
    response = client.post("/api/artifacts/", json=payload)
    assert response.status_code == 200
    assert response.json()["artifact"]["test_name"] == "login_test"

def test_get_artifacts():
    response = client.get("/api/artifacts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_suggestion_api(monkeypatch):
    def mock_openai_call(*args, **kwargs):
        class Dummy:
            def __init__(self):
                self.choices = [
                    type("obj", (object,), {
                        "message": type("msg", (object,), {"content": "Test login with invalid characters"})()
                    })
                ]

        return Dummy()

    monkeypatch.setattr("openai.ChatCompletion.create", mock_openai_call)

    payload = {
        "pr_description": "Added password validation",
        "bug_summary": "Special chars breaking login"
    }
    response = client.post("/api/suggest/", json=payload)
    assert response.status_code == 200
    assert "Test login with invalid characters" in response.json()["suggestions"]
