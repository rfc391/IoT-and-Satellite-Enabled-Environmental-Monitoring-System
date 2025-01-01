
"""IoT Sensors Module - Simulated Data Collection"""

import random
import time

def collect_sensor_data():
    """Simulates data collection from IoT sensors"""
    return {
        "timestamp": time.time(),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "air_quality": round(random.uniform(0.0, 100.0), 2)
    }
