from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_health_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_system_status() -> None:
    response = client.get("/api/v1/system/status")
    assert response.status_code == 200
    assert response.json()["architecture"] == "platform-neutral-plugin-based"


def test_plugins_list_placeholders() -> None:
    response = client.get("/api/v1/plugins")
    assert response.status_code == 200
    publishers = response.json()["publishers"]
    assert {publisher["name"] for publisher in publishers} == {"youtube", "tiktok", "instagram"}


def test_human_control_safety_defaults() -> None:
    response = client.get("/api/v1/human-control/safety")
    assert response.status_code == 200
    assert response.json()["public_publishing"] == "disabled"
