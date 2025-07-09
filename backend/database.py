from typing import List
from backend.models import TestArtifact


test_db: List[TestArtifact] = []

def add_artifact(artifact: TestArtifact):
    test_db.append(artifact)

def get_all_artifacts():
    return test_db