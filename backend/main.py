from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.test_artifact import router as artifact_router
from backend.routes.suggest import router as suggest_router

app = FastAPI()

# Allow frontend CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers with simplified paths
app.include_router(artifact_router, prefix="")  # Now uses /artifacts
app.include_router(suggest_router, prefix="")   # Now uses /suggest
