from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_missing_fields():
    response = client.post(
        "/register",
        json={}
    )

    assert response.status_code == 422

def test_login_missing_fields():
    response = client.post(
        "/register",
        json={}
    )

    assert response.status_code == 422

def test_register_login_and_get_me():
    email = "test_user@abc.com"
    password = "testpassword123"

    # Register
    register_response = client.post(
        "/register",
        json={
            "email": email,
            "password": password
        }
    )

    assert register_response.status_code == 200

    # Login
    login_response = client.post(
        "/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # Access protected endpoint
    me_response = client.get(
        "/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert me_response.status_code == 200
    assert me_response.json()["email"] == email