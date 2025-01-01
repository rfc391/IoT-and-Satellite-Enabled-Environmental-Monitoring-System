# IoT and Satellite-Enabled Environmental Monitoring System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Flask Backend](#running-the-flask-backend)
  - [Running the FastAPI Backend](#running-the-fastapi-backend)
- [Endpoints](#endpoints)
  - [Flask Endpoints](#flask-endpoints)
  - [FastAPI Endpoints](#fastapi-endpoints)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview
This IoT and satellite-enabled system simplifies environmental monitoring by integrating modern sensor technologies with predictive analytics. The project focuses on usability, flexibility, and seamless deployment, making it ideal for research, industrial applications, and personal projects.

## Features
- **Comprehensive Data Management**: Efficient ingestion and storage of sensor data.
- **Machine Learning Analytics**: Use advanced models to predict environmental trends.
- **Flexible API**: RESTful endpoints for easy integration with external systems.
- **Cloudflare Worker Integration**: Forward data to Cloudflare workers for additional processing (mocked in local tests).
- **User-Friendly Deployment**: Includes Docker support for quick setup.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- SQLite (bundled with Python)
- Optional: Docker and Docker Compose

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/environmental-monitoring-system.git
   cd environmental-monitoring-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python src/backend/main.py
   ```

## Usage

### Running the Flask Backend
1. Navigate to the `src/backend` folder:
   ```bash
   cd src/backend
   ```

2. Start the Flask server:
   ```bash
   python main.py
   ```
   By default, it runs on `http://127.0.0.1:5000`.

### Running the FastAPI Backend
1. Navigate to the `src/backend` folder:
   ```bash
   cd src/backend
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn api:app --host 0.0.0.0 --port 8000
   ```
   By default, it runs on `http://127.0.0.1:8000`.

## Endpoints

### Flask Endpoints
#### **POST /ingest**
Ingest sensor data into the system.
- **Request Body**:
  ```json
  {
      "timestamp": 1735718918.0184543,
      "temperature": 22.5,
      "humidity": 45.3,
      "pressure": 1012.5,
      "air_quality": 78.2
  }
  ```
- **Response**:
  ```json
  {
      "status": "success",
      "worker_response": {
          "status": "success",
          "message": "Data forwarded to Cloudflare worker (mocked)."
      }
  }
  ```

#### **GET /data**
Retrieve all ingested data for analysis.
- **Response**:
  ```json
  [
      [1, 1735718918.0184543, 22.5, 45.3, 78.2]
  ]
  ```

### FastAPI Endpoints
#### **POST /api/analytics/predict**
Predict environmental trends using real-time or historical sensor data.
- **Request Body**:
  ```json
  [
      {
          "timestamp": 1735718918.0184543,
          "temperature": 22.5,
          "humidity": 45.3,
          "pressure": 1012.5,
          "air_quality": 78.2
      }
  ]
  ```
- **Response**:
  ```json
  {
      "status": "success",
      "processed_data": {
          "temperature_avg": 23.25,
          "humidity_avg": 42.7,
          "pressure_avg": 1011.4,
          "air_quality_avg": 79.85
      }
  }
  ```

## Development
### Running Tests
1. Install test dependencies:
   ```bash
   pip install pytest
   ```
2. Run tests:
   ```bash
   pytest tests
   ```

### Docker Setup
1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```
2. Access the Flask and FastAPI services as per the configurations in `docker-compose.yml`.

## Contributing
We value contributions that enhance usability and functionality. To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Create a pull request and describe your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
