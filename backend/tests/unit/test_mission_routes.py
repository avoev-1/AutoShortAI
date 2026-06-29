from fastapi.testclient import TestClient
from app.main import create_app
client=TestClient(create_app())

def test_list_mission_templates() -> None:
    response=client.get("/api/v1/missions/templates")
    assert response.status_code==200
    assert len(response.json()["templates"])>=2

def test_plan_mission_route() -> None:
    response=client.post("/api/v1/missions/plan", json={"title":"Demo","platforms":["youtube"],"creation_mode":"assisted"})
    assert response.status_code==200
    data=response.json()
    assert data["template_id"]=="standard_short_form"
    assert data["steps"][0]["step_id"]=="topic"
