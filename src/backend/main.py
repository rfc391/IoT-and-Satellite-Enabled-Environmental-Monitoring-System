
"""Backend Module - Main Application"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = "data.db"

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
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO sensor_data (timestamp, temperature, humidity, air_quality)
                      VALUES (?, ?, ?, ?)''', 
                   (data['timestamp'], data['temperature'], data['humidity'], data['air_quality']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Data ingested"}), 200

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
    app.run(debug=True, port=8000)
