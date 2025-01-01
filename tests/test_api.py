
import sys
sys.path.append(r"/mnt/data/IoT-and-Satellite-Enabled-Environmental-Monitoring-System-main/IoT-and-Satellite-Enabled-Environmental-Monitoring-System-main/src")

from fastapi.testclient import TestClient
from src.backend.api import app

client = TestClient(app)


def test_predict_trend():
    # Test payload
    sensor_data = [
        {"temperature": 25.5, "humidity": 55.0, "pressure": 1012.0, "air_quality": 75.0},
        {"temperature": 22.0, "humidity": 60.0, "pressure": 1015.0, "air_quality": 70.0},
    ]

    print("Sending Payload:", sensor_data)
    response = client.post("/api/analytics/predict", json=sensor_data)

    # Debugging information
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content.decode())

    # Assertions
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json()["status"] == "success", f"Unexpected response: {response.json()}"
