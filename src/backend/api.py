
"""Backend Module - API with Manual Validation for Debugging"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import List
from src.iot_sensors.sensors import collect_sensor_data, batch_collect_sensor_data
from src.ai_ml.analytics import train_linear_model, evaluate_model, preprocess_data
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

class SensorData(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    air_quality: float

@app.get("/api/sensor/realtime")
async def get_realtime_sensor_data():
    data = collect_sensor_data()
    return {"status": "success", "data": data}

@app.get("/api/sensor/batch")
async def get_batch_sensor_data(batch_size: int = 5):
    data_batch = batch_collect_sensor_data(batch_size=batch_size)
    return {"status": "success", "data": data_batch}

@app.post("/api/analytics/predict")
async def predict_trend(sensor_data: List[SensorData]):
    logger.debug("Received raw payload: %s", sensor_data)
    try:
        # Validate payload explicitly using Pydantic
        validated_data = [SensorData(**data.dict()) for data in sensor_data]
        logger.debug("Validated data: %s", validated_data)

        # Convert validated data to DataFrame
        df = pd.DataFrame([data.dict() for data in validated_data])
        logger.debug("Converted DataFrame: %s", df)

        X = df[["temperature", "humidity", "pressure"]]
        y = df["air_quality"]
        X_scaled, _ = preprocess_data(X)
        model = train_linear_model(X_scaled, y)
        metrics = evaluate_model(model, X_scaled, y)
        return {"status": "success", "metrics": metrics}
    except ValidationError as ve:
        logger.error("Validation Error: %s", ve)
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        logger.error("Error processing request: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
