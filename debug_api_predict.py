
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import List
from src.ai_ml.analytics import train_linear_model, evaluate_model, preprocess_data
import pandas as pd
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SensorData(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    air_quality: float

@app.post("/api/analytics/predict")
async def predict_trend(sensor_data: List[SensorData]):
    logger.debug("Received payload: %s", sensor_data)
    try:
        # Validate payload explicitly
        validated_data = [SensorData(**data.dict()) for data in sensor_data]
        logger.debug("Validated payload: %s", validated_data)

        # Convert to DataFrame for model processing
        df = pd.DataFrame([data.dict() for data in validated_data])
        logger.debug("DataFrame created: %s", df)

        # Extract features and target
        X = df[["temperature", "humidity", "pressure"]]
        y = df["air_quality"]
        X_scaled, _ = preprocess_data(X)

        # Train and evaluate model
        model = train_linear_model(X_scaled, y)
        metrics = evaluate_model(model, X_scaled, y)
        logger.debug("Model metrics: %s", metrics)

        return {"status": "success", "metrics": metrics}
    except ValidationError as ve:
        logger.error("Validation Error: %s", ve)
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        logger.error("Unhandled Error: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
