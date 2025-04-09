
from flask import Flask, request, jsonify
import sqlite3
import os
import requests

app = Flask(__name__)
DATABASE = "data.db"
CLOUDFLARE_ROUTER_URL = "https://apexsecurityint.com/dry-truth-1f56"

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp REAL,
                        temperature REAL,
                        humidity REAL,
                        air_quality REAL
                      )''')
    conn.commit()
    conn.close()

@app.route('/ingest', methods=['POST'])
def ingest_data():
    """Endpoint to ingest IoT sensor data"""
    data = request.json
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO sensor_data (timestamp, temperature, humidity, air_quality)
                          VALUES (?, ?, ?, ?)''', 
                       (data['timestamp'], data['temperature'], data['humidity'], data['air_quality']))
        conn.commit()
        conn.close()

        # Forward data to Cloudflare worker
        response = requests.post(CLOUDFLARE_ROUTER_URL, json=data)
        if response.status_code != 200:
            return jsonify({"status": "success", "message": "Data ingested locally, but Cloudflare forwarding failed"}), 206

        return jsonify({"status": "success", "message": "Data ingested and forwarded to Cloudflare"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/data', methods=['GET'])
def get_data():
    """Endpoint to fetch sensor data"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True, port=5001)  # Updated port
