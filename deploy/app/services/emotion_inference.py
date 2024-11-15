import torch
import torch.nn.functional as F
from ..load_models import models
from utils.preprocessing import Preprocessing
from config.logging import logger

class EmotionInference:
  def __init__(self):
    self.preprocessor = Preprocessing()

  def get_inference(self, text):
    try:
      cleaned_text = self.preprocessor.clean_text(text)
      subwords = models.tokenizer.encode(cleaned_text)
      subwords = torch.LongTensor(subwords).view(1, -1).to(models.model.device)

      logits = models.model(subwords)[0]
      prediction = torch.topk(logits, k=1, dim=-1)[1].squeeze().item()
      confidence_score = F.softmax(logits, dim=-1).squeeze()[prediction] * 100

      return models.i2w[prediction], float(confidence_score.item())
    
    except Exception as e:
      logger.error("Error during inference: {e}, text: {text}")

      return "", 0
