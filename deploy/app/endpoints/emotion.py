from ..services.emotion_inference import EmotionInference
from config.logging import logger

class Emotion:
  def __init__(self, id, text):
    self._id = id
    self._input = text

  def get_inference(self):
    logger.info("Emotion inference is in progress..")

    emotion_inference = EmotionInference()
    label, confidence = emotion_inference.get_inference(self._input)

    logger.info("Emotion inference finished!")

    return {"result": {"id": self._id,
                       "label": label, 
                       "confidence": confidence},
            "status": 1}