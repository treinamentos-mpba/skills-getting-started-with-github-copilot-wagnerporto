from src.app import activities


def test_signup_participant(client):
    email = "new.student@mergington.edu"

    response = client.post("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_existing_participant(client):
    email = "michael@mergington.edu"
    original_participants = activities["Chess Club"]["participants"][:]

    response = client.post("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
    assert activities["Chess Club"]["participants"] == original_participants


def test_signup_for_unknown_activity(client):
    email = "new.student@mergington.edu"

    response = client.post("/activities/Unknown/signup", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_without_email(client):
    original_participants = activities["Chess Club"]["participants"][:]

    response = client.post("/activities/Chess Club/signup")

    assert response.status_code == 422
    assert activities["Chess Club"]["participants"] == original_participants


def test_signup_after_unregistering(client):
    email = "michael@mergington.edu"
    unregister_response = client.delete(
        "/activities/Chess Club/signup", params={"email": email}
    )
    assert unregister_response.status_code == 200

    response = client.post("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert activities["Chess Club"]["participants"].count(email) == 1