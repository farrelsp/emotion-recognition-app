from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from app.routes.router import router
from app.endpoints.emotion import Emotion
import logging

API_VERSION = "1.0.0"
app = FastAPI()
app.include_router(router)
logging.basicConfig(level=logging.INFO)

class TextRequest(BaseModel):
  text: str

class PredictionResponse(BaseModel):
  emotion: str
  confidence: float

# Default root path
@app.get('/')
async def root():
  message = {
    "message": "Welcome to Emotion Detection API"
    }
  
  return message

@app.post('/predict', response_model=PredictionResponse)
async def predict_emotion(request: TextRequest):
  logging.info(f"Received text: {request.text}")

  try:
    emotion_instance = Emotion(id=1, text=request.text)
    result = emotion_instance.get_inference()
    logging.info(f"Prediction result: {result}")

    if result['status'] == 1:
      logging.info(f"Result structure: {result}")
      label = result['result']['label']
      confidence = result['result']['confidence']
      return PredictionResponse(emotion=label, confidence=confidence)
    else:
      return HTTPException(status_code=400, detail="Inference failed!")
    
  except Exception as e:
    logging.error(f"Error: {str(e)}")
    return HTTPException(status_code=500, detail=f"{str(e)}")