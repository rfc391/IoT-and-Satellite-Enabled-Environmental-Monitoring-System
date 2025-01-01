
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/backend')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


import pytest
from fastapi.testclient import TestClient
from src.backend.api import app

client = TestClient(app)

def test_get_realtime_sensor_data():
    response = client.get("/api/sensor/realtime")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "data" in response.json()

def test_get_batch_sensor_data():
    response = client.get("/api/sensor/batch?batch_size=3")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 3


    sensor_data = [
        {"temperature": 25.5, "humidity": 55.0, "pressure": 1012.0, "air_quality": 75.0},
        {"temperature": 22.0, "humidity": 60.0, "pressure": 1015.0, "air_quality": 70.0},
    ]
    response = client.post("/api/analytics/predict", json=sensor_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "metrics" in response.json()

