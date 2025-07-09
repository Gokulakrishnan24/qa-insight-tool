from fastapi import APIRouter, Query
from backend.models import TestArtifact
from backend.database import add_artifact, get_all_artifacts

router = APIRouter()

@router.post("/artifacts", tags=["Test Artifacts"])
def add_test_artifact(artifact: TestArtifact):
    add_artifact(artifact)
    return {"msg": "Artifact added", "artifact": artifact}

@router.get("/artifacts", tags=["Test Artifacts"])
def list_artifacts(run_id: str = Query(None), date: str = Query(None)):
    data = get_all_artifacts()

    if run_id:
        data = [a for a in data if a.run_id == run_id]

    if date:
        # This assumes `timestamp` is an ISO string like "2025-07-09T..."
        data = [a for a in data if a.timestamp.startswith(date)]

    return data

