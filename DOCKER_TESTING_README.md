
# Docker-Based Testing Environment for IoT Project

## Prerequisites
- Docker installed on your machine.

## Steps to Run the Tests
1. **Build the Docker Image**:
    ```bash
    docker build -t iot_test_env -f Dockerfile.test .
    ```

2. **Run the Tests**:
    ```bash
    docker run --rm iot_test_env
    ```

3. **View the Results**:
   The test results will be displayed in the terminal after the container execution.

---

## Notes
- Ensure the `requirements.txt` file includes all dependencies.
- The `PYTHONPATH` is set to include the `src` directory automatically in the container.
