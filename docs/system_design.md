
# System Design

## Overview
This system integrates IoT sensors and satellite communication to monitor environmental conditions in real time.

## Architecture
- **IoT Sensors**: Collect temperature, humidity, and air quality data.
- **Satellite Communication**: Relays data from remote areas.
- **Backend**: Flask-based API for data ingestion and retrieval.
- **Visualization**: Generates dashboards and heatmaps.
- **AI/ML**: Predicts trends using machine learning models.

### Diagram
[Placeholder for architecture diagram]

## Module Interaction
- IoT sensors feed data to the backend via REST APIs.
- Satellite communication acts as a relay for remote IoT sensors.
- The backend stores data in a database and exposes it for visualization and ML models.
