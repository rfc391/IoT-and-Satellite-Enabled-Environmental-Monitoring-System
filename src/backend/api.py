
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import List
import pandas as pd
import logging
import requests

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define the Cloudflare worker URL
CLOUDFLARE_ROUTER_URL = "https://apexsecurityint.com/dry-truth-1f56"

class SensorData(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    air_quality: float

@app.post("/api/analytics/predict")
async def predict_trend(sensor_data: List[SensorData]):
    logger.debug("Received payload: %s", sensor_data)
    try:
        # Convert list of Pydantic objects to DataFrame
        df = pd.DataFrame([data.dict() for data in sensor_data])
        logger.debug("DataFrame created: %s", df)

        # Forward data to the Cloudflare worker for processing
        response = requests.post(CLOUDFLARE_ROUTER_URL, json={"sensor_data": df.to_dict(orient="records")})
        if response.status_code != 200:
            logger.error("Cloudflare worker error: %s", response.text)
            raise HTTPException(status_code=500, detail="Error in Cloudflare worker")

        # Return the worker's response
        return {"status": "success", "worker_response": response.json()}
    except ValidationError as ve:
        logger.error("Validation Error: %s", ve)
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        logger.error("Unhandled Error: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
