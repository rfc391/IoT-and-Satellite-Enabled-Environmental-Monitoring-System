
# IoT and Satellite-Enabled Environmental Monitoring System

## Overview
The **IoT and Satellite-Enabled Environmental Monitoring System** is a scalable, modular platform for real-time environmental monitoring. It leverages IoT devices, satellite communication, and cloud infrastructure for seamless data collection, analysis, and visualization.

This system provides:
- Real-time monitoring of environmental parameters like temperature, humidity, pressure, and air quality.
- Predictive analytics using advanced machine learning models.
- A responsive dashboard and RESTful API for data interaction.

---

## Features

### Core Functionalities
- **IoT Data Collection**: Real-time and batch data collection from IoT sensors.
- **Predictive Analytics**: Machine learning models for forecasting trends with evaluation metrics like MSE and R².
- **Interactive Dashboard**: Visualizes data and allows device management.
- **Public API**: RESTful endpoints for data retrieval and analytics.

### Integrations
- **Cloudflare Workers**: Optimize API delivery and automate workflows.
- **GitHub Actions**: CI/CD pipelines for automated testing and deployment.
- **Docker Support**: Simplified deployment in any environment.

---

## Quick Start

### Prerequisites
- **Python 3.8+**
- **Docker and Docker Compose** (optional for local testing)
- **Cloudflare Account** (optional for deployment)

### Installation

#### Local Environment
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/IoT-and-Satellite-Enabled-Environmental-Monitoring-System.git
    cd IoT-and-Satellite-Enabled-Environmental-Monitoring-System
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:
    ```bash
    uvicorn src.backend.api:app --reload
    ```
    Access the dashboard at `http://localhost:8000/dashboard` and API docs at `http://localhost:8000/docs`.

#### Docker Environment
1. Build and start the container:
    ```bash
    docker-compose up --build
    ```

2. Access the dashboard at `http://localhost:8000/dashboard`.

---

## Usage Guide

### Dashboard
- Add, update, and manage IoT devices.
- View interactive graphs for historical and real-time data.

### API Endpoints
1. **Retrieve Real-Time Data**: `GET /api/sensor/realtime`
2. **Batch Data Retrieval**: `GET /api/sensor/batch?batch_size=10`
3. **Predictive Analytics**: `POST /api/analytics/predict`
   - Example payload:
     ```json
     [
       {"temperature": 25.5, "humidity": 55.0, "pressure": 1012.0, "air_quality": 75.0},
       {"temperature": 22.0, "humidity": 60.0, "pressure": 1015.0, "air_quality": 70.0}
     ]
     ```

---

## Development and Testing

### Project Structure
```
IoT-and-Satellite-Enabled-Environmental-Monitoring-System/
|-- src/
|   |-- backend/       # API and server code
|   |-- ai_ml/         # Predictive analytics models
|   |-- iot_sensors/   # IoT data collection logic
|   |-- utils/         # Utility modules
|-- dashboard/         # Frontend dashboard files
|-- tests/             # Unit and integration tests
```

### Running Tests
1. Install `pytest`:
    ```bash
    pip install pytest
    ```

2. Run all tests:
    ```bash
    pytest tests/
    ```

### Docker-Based Testing
Refer to the `DOCKER_TESTING_README.md` file for detailed instructions on setting up and running tests in Docker.

---

## Deployment

### Cloudflare Workers
1. Install the Cloudflare CLI:
    ```bash
    npm install -g wrangler
    ```

2. Authenticate with your Cloudflare account:
    ```bash
    wrangler login
    ```

3. Deploy the Worker:
    ```bash
    wrangler publish
    ```

---

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
