from ..services.emotion_inference import EmotionInference
from config.logging import logger

class EmotionBatch:
  def __init__(self, id, texts):
    self._input = texts

  def get_inference(self):
    logger.info("Emotion inference (batch) is in progress..")

    emotion_inference = EmotionInference()
    result = []
    for text in self._input:
      label, confidence = emotion_inference.get_inference(text['content'])
      result.append({
        "id": text["id"],
        "label": label,
        "confidence": confidence
      })

    logger.info("Emotion inference (batch) finished!")

    return {"result": result,
            "status": 1}