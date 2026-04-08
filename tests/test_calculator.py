from fastapi.testclient import TestClient
from calculator import app

client = TestClient(app)

def test_TC_001():
    response = client.post("/api/v1/add", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "result": 15}

def test_TC_002():
    payload = {"a": 5, "b": 10}
    response = client.post("/api/v1/subtract", json=payload)
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "result": -5}

def test_TC_003():
    response = client.post("/api/v1/multiply", json={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "result": 0}

def test_TC_004():
    payload = {"a": 20, "b": 4}
    response = client.post("/api/v1/divide", json=payload)
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "result": 5}

def test_TC_005():
    payload = {"a": 10, "b": 0}
    response = client.post("/api/v1/divide", json=payload)
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}

