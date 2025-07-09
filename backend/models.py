from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TestArtifact(BaseModel):
    test_name: str
    status: str
    failure_reason: Optional[str] = None
    run_id: str
    timestamp: datetime

class SuggestionRequest(BaseModel):
    pr_description: str
    bug_summary: Optional[str] = None
