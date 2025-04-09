
# Simulated Sensor Feed for Offline Mode

import random
import time

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(10.0, 40.0), 2),
        "humidity": round(random.uniform(20.0, 80.0), 2),
        "radiation": round(random.uniform(0.01, 0.2), 4),
        "air_quality_index": random.randint(10, 150)
    }

def run_simulation(interval=2):
    while True:
        data = generate_sensor_data()
        print(f"[SIM] Sensor Data: {data}")
        time.sleep(interval)
