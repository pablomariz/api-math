from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_sum_route():
    response = client.post("/sum", json=[1, 2, 3, 4, 5])
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_average_route():
    response = client.post("/average", json=[1, 2, 3, 4, 5])
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_average_route_empty_list():
    response = client.post("/average", json=[])
    assert response.status_code == 400
    assert response.json() == {"detail": "Não é possível calcular a média de uma lista vazia"}
