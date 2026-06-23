from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "CareerPilot API"}

def test_me_requires_authentication():
    response = client.get("/me")

    assert response.status_code  == 401