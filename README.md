
# IoT and Satellite-Enabled Environmental Monitoring System

## Overview
This project enables IoT and satellite-based environmental monitoring, providing real-time data collection, predictive analytics, and public API access via GitHub Pages.

## Features
1. **IoT Data Collection**:
   - Simulated real-time and batch IoT sensor data.
   - Supports temperature, humidity, pressure, and air quality readings.

2. **Predictive Analytics**:
   - Utilizes machine learning for environmental trend predictions.
   - Supports linear regression and random forest models.

3. **Public API via GitHub Pages**:
   - Publishes IoT data and analytics results to GitHub Pages.
   - Publicly accessible data served directly from a GitHub repository.

## Setup Instructions
1. **Install Dependencies**:
   - Run `pip install -r requirements.txt` to install required Python libraries.

2. **Run the Application**:
   - Start the FastAPI server: `uvicorn src.backend.api:app --reload`.
   - Access API documentation at `http://127.0.0.1:8000/docs`.

3. **Testing**:
   - Execute `pytest tests` to run all test cases.

4. **Publish Data to GitHub Pages**:
   - Use the script `publish_to_github_pages.py`:
     ```bash
     python publish_to_github_pages.py
     ```
   - Replace `https://rfc391.github.io/IoT-and-Satellite-Enabled-Environmental-Monitoring-System/` in the script with your repository URL.

## Example API Endpoints
1. **Real-time Sensor Data**:
   - URL: `GET /api/sensor/realtime`
2. **Batch Sensor Data**:
   - URL: `GET /api/sensor/batch?batch_size=5`
3. **Predict Trends**:
   - URL: `POST /api/analytics/predict`

## GitHub Pages
- Once published, data is available at `https://rfc391.github.io/IoT-and-Satellite-Enabled-Environmental-Monitoring-System/iot_data.json`.

---

### License
This project is licensed under the MIT License.
