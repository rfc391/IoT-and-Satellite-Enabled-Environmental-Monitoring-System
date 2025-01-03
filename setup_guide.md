
# Setup Guide

## Prerequisites
- Python 3.8 or higher
- Docker (optional for containerized deployment)

## Installation
1. Clone the repository.
2. Navigate to the project directory: `cd IoT_Satellite_Environmental_System`.
3. Install dependencies: `pip install -r requirements.txt`.

## Running the Application
1. Start the backend: `python src/backend/main.py`.
2. Test ingestion: Send POST requests to `/ingest` with sensor data.

## Docker Deployment
1. Build the image: `docker-compose build`.
2. Start the services: `docker-compose up`.
