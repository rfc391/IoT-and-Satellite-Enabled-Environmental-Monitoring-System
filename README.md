# IoT and Satellite-Enabled Environmental Monitoring System

## Overview
This project combines IoT devices with satellite communication to enable real-time environmental monitoring. Its modular architecture supports diverse applications, from climate research to disaster response.

## Features
- **IoT Sensor Data Ingestion**: Accepts temperature, humidity, and air quality readings.
- **Database Management**: Stores data in an SQLite database with automated initialization.
- **Image Processing**: Processes uploaded images using OpenCV.
- **API Endpoints**:
  - `/ingest`: Ingest sensor data.
  - `/data`: Retrieve stored data.
  - `/process-image`: Process images with AI.
- **Automated Testing and Deployment**: Utilizes GitHub Actions for CI/CD and Docker for containerized deployment.

## Prerequisites
- Python 3.9+
- Docker and Docker Compose

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rfc391/IoT-and-Satellite-Enabled-Environmental-Monitoring-System.git
cd IoT-and-Satellite-Enabled-Environmental-Monitoring-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application Locally
```bash
python main.py
```
Access the application at `http://localhost:5000`

### 4. Run with Docker
```bash
docker-compose up --build
```

### 5. Run Tests
```bash
pytest
```

## API Reference

### `/ingest`
- **Method**: POST
- **Description**: Ingests IoT sensor data.
- **Payload**:
  ```json
  {
    "timestamp": 1672531200,
    "temperature": 22.5,
    "humidity": 45.0,
    "air_quality": 85.0
  }
  ```

### `/data`
- **Method**: GET
- **Description**: Fetches stored sensor data.

### `/process-image`
- **Method**: POST
- **Description**: Processes an uploaded image.
- **Payload**: Multipart/form-data with an `image` file.

## CI/CD Workflow
The pipeline automates:
- Dependency installation.
- Running tests with `pytest`.
- Building and deploying Docker containers.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

