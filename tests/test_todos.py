from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

import json

# Assume client = TestClient(app) is defined globally

def test_TC_001_get_all_existing_tasks():
    response = client.get("/todos")
    assert response.status_code == 200
    expected_response_data = json.loads("{\"todos\": [{\"id\": 1, \"title\": \"Learn FastAPI routing\", \"completed\": false}]}")
    assert response.json() == expected_response_data

def test_TC_002_get_a_single_task_by_valid_id():
    response = client.get("/todos/1")
    assert response.status_code == 200
    expected_response_data = json.loads("{\"id\": 1, \"title\": \"Learn FastAPI routing\", \"completed\": false}")
    assert response.json() == expected_response_data

def test_TC_003_get_a_task_with_an_id_that_does_not_exist():
    response = client.get("/todos/999")
    assert response.status_code == 404
    expected_response_data = json.loads("{\"detail\": \"Task not found\"}")
    assert response.json() == expected_response_data

def test_TC_004_create_a_new_task():
    request_body = json.loads("{\"title\": \"Write tests\", \"completed\": false}")
    response = client.post("/todos", json=request_body)
    assert response.status_code == 201
    expected_response_data = json.loads("{\"id\": 2, \"title\": \"Write tests\", \"completed\": false}")
    assert response.json() == expected_response_data

def test_TC_005_create_a_task_missing_the_required_title_field():
    request_body = json.loads("{\"completed\": false}")
    response = client.post("/todos", json=request_body)
    assert response.status_code == 422
    # The 'Expected Response' for this test case is a placeholder string "(FastAPI Validation Error Response Details)",
    # which is not valid JSON. Therefore, an exact JSON response assertion is not possible.
    # A real test would parse the actual error response and assert specific error details,
    # for example, checking for the presence of a 'detail' key and specific error messages.

def test_TC_006_update_an_existing_task_successfully():
    request_body = json.loads("{\"title\": \"Master FastAPI\", \"completed\": true}")
    response = client.put("/todos/1", json=request_body)
    assert response.status_code == 200
    expected_response_data = json.loads("{\"id\": 1, \"title\": \"Master FastAPI\", \"completed\": true}")
    assert response.json() == expected_response_data

def test_TC_007_update_a_task_with_an_id_that_does_not_exist():
    request_body = json.loads("{\"title\": \"Ghost Task\", \"completed\": true}")
    response = client.put("/todos/999", json=request_body)
    assert response.status_code == 404
    expected_response_data = json.loads("{\"detail\": \"Task not found\"}")
    assert response.json() == expected_response_data

def test_TC_008_update_a_task_with_invalid_missing_data():
    request_body = json.loads("{\"completed\": true}")
    response = client.put("/todos/1", json=request_body)
    assert response.status_code == 422
    # The 'Expected Response' for this test case is a placeholder string "(FastAPI Validation Error Response Details)",
    # which is not valid JSON. Therefore, an exact JSON response assertion is not possible.
    # A real test would parse the actual error response and assert specific error details,
    # for example, checking for the presence of a 'detail' key and specific error messages.

