# IoT and Satellite-Enabled Environmental Monitoring System

## Overview
The **IoT and Satellite-Enabled Environmental Monitoring System** is a scalable and modular solution for real-time environmental monitoring. Leveraging IoT devices, satellite communication, and cloud-based infrastructure, this system enables seamless data collection, visualization, and predictive analytics. It includes a user-friendly dashboard, public API endpoints, automated deployment pipelines, and workflow integrations for ease of use and adaptability.

---

## Features

### Core Functionalities
1. **Real-Time IoT Data Collection**
   - Monitor environmental factors such as temperature, humidity, pressure, and air quality.
   - Support for both real-time and batch data collection from IoT devices.

2. **Advanced Predictive Analytics**
   - Machine learning models (Linear Regression, Random Forest) for forecasting trends.
   - Metrics like Mean Squared Error (MSE) and R² for model evaluation.

3. **Interactive Dashboard**
   - Visualize real-time and historical data.
   - Manage IoT devices with a responsive, multi-browser-compatible interface.

4. **Public API Access**
   - RESTful APIs for real-time sensor data, batch processing, and analytics.
   - Built-in support for Cloudflare Workers to optimize API delivery.

### Workflow Integrations
1. **Cloudflare Workflows**
   - Automate multi-step tasks with error handling and state persistence.
   - Define modular workflows for robust data processing.

2. **GitHub Actions CI/CD**
   - Automated testing, building, and deployment pipelines.

3. **Docker Support**
   - Containerized deployment for seamless scalability.

---

## Installation and Setup

### Prerequisites
- **Python 3.8+**
- **Docker and Docker Compose** (Optional but recommended for production)
- **Cloudflare Account** (For serverless deployment)
- **GitHub Repository** (For CI/CD integration)

### Quick Start
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rfc391/IoT-and-Satellite-Enabled-Environmental-Monitoring-System.git
   cd IoT-and-Satellite-Enabled-Environmental-Monitoring-System
   ```

2. **Run with Docker**:
   ```bash
   docker-compose up --build
   ```
   - Access the dashboard at `http://localhost:8000/dashboard`.
   - API documentation available at `http://localhost:8000/docs`.

3. **Manual Setup**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the server:
     ```bash
     uvicorn src.backend.api:app --reload
     ```

4. **Deploy to Cloudflare**:
   - Upload the provided Cloudflare Worker script.
   - Configure Cloudflare Workers to proxy API and dashboard requests.

5. **GitHub Pages Deployment**:
   - Hosted at: [https://rfc391.github.io/IoT-and-Satellite-Enabled-Environmental-Monitoring-System](https://rfc391.github.io/IoT-and-Satellite-Enabled-Environmental-Monitoring-System)

6. **Cloudflare Workflow Integration**:
   - Use the following example to define and deploy Cloudflare Workflows.

---

## Cloudflare Workflow Example

### Define Workflow
Create a Workflow using the `npm create cloudflare@latest` command:
```bash
npm create cloudflare@latest workflows-starter -- --template "cloudflare/workflows-starter"
```

### Example Workflow Steps
```typescript
import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from 'cloudflare:workers';

type Env = {
    MY_KV_NAMESPACE: KVNamespace;
};

type Params = {
    email: string;
};

export class MyWorkflow extends WorkflowEntrypoint<Env, Params> {
    async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
        const my_value = await step.do('My First Step', async () => {
            return "a".repeat(25000);
        });

        await step.sleep("sleep", "2 minutes");

        await step.do(
            'My Second Step',
            {
                retries: {
                    limit: 5,
                    delay: '1 second',
                    backoff: 'constant',
                },
                timeout: '15 minutes',
            },
            async () => {
                if (Math.random() > 0.5) {
                    throw new Error('Oh no!');
                }
            },
        );
    }
}
```

### Deploy Workflow
1. Replace bindings (`MY_KV_NAMESPACE`) with your specific Cloudflare resources.
2. Deploy using the Cloudflare CLI.

---

## Usage Guide

### Dashboard
- **Device Management**:
  - Add, update, or remove IoT devices.
- **Data Visualization**:
  - Interactive graphs for real-time and historical data.
- **Cross-Browser Compatibility**:
  - Works seamlessly on Chrome, Firefox, Safari, and Edge.

### API Endpoints
1. **Real-Time Data**: `GET /api/sensor/realtime`
2. **Batch Data**: `GET /api/sensor/batch?batch_size=10`
3. **Predictive Analytics**: `POST /api/analytics/predict`
   - Payload example:
     ```json
     [
       {"temperature": 25.5, "humidity": 55.0, "pressure": 1012.0, "air_quality": 75.0},
       {"temperature": 22.0, "humidity": 60.0, "pressure": 1015.0, "air_quality": 70.0}
     ]
     ```

---

## Developer Documentation

### Project Structure
```
IoT-and-Satellite-Enabled-Environmental-Monitoring-System/
|-- src/
|   |-- backend/       # FastAPI-based API services
|   |-- ai_ml/         # Predictive analytics models
|   |-- iot_sensors/   # IoT data collection logic
|   |-- utils/         # Helper functions and utilities
|-- dashboard/         # Frontend dashboard files
|-- tests/             # Unit, integration, and E2E tests
|-- docs/              # Project documentation
|-- .github/workflows/ # CI/CD workflows for GitHub Actions
```

### Extending the System
- **Add New Sensors**: Extend `src/iot_sensors/sensors.py`.
- **Integrate More Models**: Add algorithms in `src/ai_ml/models.py`.
- **Expand APIs**: Modify `src/backend/api.py`.

---

## CI/CD Pipeline

### GitHub Actions Workflow
1. Automatically triggered on every push to the `main` branch.
2. Steps include:
   - Install dependencies.
   - Run the test suite.
   - Deploy the FastAPI server.
3. Configuration file: `.github/workflows/ci_cd_pipeline.yml`.

---

## Contributing
We welcome contributions to improve the system. To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed descriptions of changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## Acknowledgements
Special thanks to the open-source community for tools and libraries that made this project possible:
- FastAPI
- Docker
- Cloudflare Workers
- GitHub Actions
