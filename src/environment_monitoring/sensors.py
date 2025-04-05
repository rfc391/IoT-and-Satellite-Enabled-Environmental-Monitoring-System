
"""IoT Sensors Module - Enhanced Data Collection and Processing"""

import random
import time
import json

def collect_sensor_data():
    """Simulates data collection from IoT sensors"""
    return {
        "timestamp": time.time(),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "air_quality": round(random.uniform(0.0, 100.0), 2),
        "pressure": round(random.uniform(950.0, 1050.0), 2),
        "motion_detected": random.choice([True, False])
    }

def stream_sensor_data(interval=1, iterations=10):
    """Streams real-time sensor data at given intervals"""
    for _ in range(iterations):
        data = collect_sensor_data()
        print(json.dumps(data))  # Simulate streaming by printing as JSON
        time.sleep(interval)

def batch_collect_sensor_data(batch_size=5):
    """Collects sensor data in batches"""
    data_batch = [collect_sensor_data() for _ in range(batch_size)]
    return data_batch

def save_sensor_data(data, filepath):
    """Save collected sensor data to a JSON file"""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
