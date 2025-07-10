from fastapi import APIRouter
from pydantic import BaseModel
from backend.utils import generate_suggestions  # Make sure this file exists

router = APIRouter()

class SuggestionRequest(BaseModel):
    pr_description: str
    bug_summary: str = ""

@router.post("/suggest", tags=["AI Suggestions"])
def suggest_tests(payload: SuggestionRequest):
    prompt = f"""
You are a senior QA engineer. Based on the following pull request description and a recent bug fix, suggest 3 diverse test scenarios: one functional, one edge case, and one regression.

Pull Request Description: "{payload.pr_description}"
Bug Summary: "{payload.bug_summary}"

Return only the test suggestions in a numbered list.
"""
    suggestions = generate_suggestions(prompt)
    return {"suggestions": suggestions}
