from fastapi import APIRouter
from pydantic import BaseModel
from backend.utils import generate_suggestions

class SuggestionRequest(BaseModel):
    pr_description: str
    bug_summary: str = ""

router = APIRouter()

@router.post("/suggest", tags=["AI Suggestions"])
def suggest_tests(req: SuggestionRequest):
    suggestions = generate_suggestions(req.pr_description, req.bug_summary)
    return {"suggestions": suggestions}
