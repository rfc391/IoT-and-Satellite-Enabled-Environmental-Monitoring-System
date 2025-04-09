
# API Reference

## Endpoints

### `/ingest` [POST]
- **Description**: Ingest sensor data into the system.
- **Payload**:
  ```json
  {
    "timestamp": 1634552400,
    "temperature": 25.5,
    "humidity": 60.2,
    "air_quality": 42.8
  }
  ```

### `/data` [GET]
- **Description**: Retrieve all sensor data.
- **Response**:
  ```json
  [
    {"id": 1, "timestamp": 1634552400, "temperature": 25.5, "humidity": 60.2, "air_quality": 42.8}
  ]
  ```
