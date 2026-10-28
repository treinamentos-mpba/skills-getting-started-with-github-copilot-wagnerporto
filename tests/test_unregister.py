import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    original_participants = activities["Chess Club"]["participants"][:]
    with TestClient(app) as test_client:
        yield test_client
    activities["Chess Club"]["participants"][:] = original_participants


def test_unregister_participant(client):
    email = "michael@mergington.edu"
    response = client.delete("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert email not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_unknown_participant(client):
    original_participants = activities["Chess Club"]["participants"][:]
    response = client.delete(
        "/activities/Chess Club/signup", params={"email": "unknown@mergington.edu"}
    )

    assert response.status_code == 404
    assert activities["Chess Club"]["participants"] == original_participants


def test_unregister_from_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown/signup", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 404