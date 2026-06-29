from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_sdk_status_route() -> None:
    response = client.get("/api/v1/sdk/status")
    assert response.status_code == 200
    assert response.json()["version"] == "0.3.0"


def test_sdk_plugins_route() -> None:
    response = client.get("/api/v1/sdk/plugins")
    assert response.status_code == 200
    assert len(response.json()["plugins"]) >= 3
