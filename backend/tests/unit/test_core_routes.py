from fastapi.testclient import TestClient
from app.main import create_app

client = TestClient(create_app())


def test_default_workflow_route() -> None:
    response = client.get("/api/v1/core/workflow/default")
    assert response.status_code == 200
    assert response.json()["workflow"] == "default_short_form_content"


def test_plan_demo_route() -> None:
    response = client.get("/api/v1/core/plan/demo")
    assert response.status_code == 200
    assert response.json()["planned_steps"][0] == "research"
