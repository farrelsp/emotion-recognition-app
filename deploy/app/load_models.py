import os
import torch
from transformers import BertForSequenceClassification, BertTokenizer 
from config.logging import logger

CWD = os.getcwd()

class Models:
  def __init__(self):
    self.model, self.tokenizer, self.w2i, self.i2w = self.load_models()

  def load_models(self):
    model_path = f"{CWD}/ml-models"

    w2i = {'sadness': 0, 'anger': 1, 'surprise': 2, 'fear': 3, 'joy': 4, 'disgust': 5, 'trust': 6, 'anticipation': 7}
    i2w = {0: 'sadness', 1: 'anger', 2: 'surprise', 3: 'fear', 4: 'joy', 5: 'disgust', 6: 'trust', 7: 'anticipation'}

    model = BertForSequenceClassification.from_pretrained(model_path)
    tokenizer = BertTokenizer.from_pretrained(model_path)

    if torch.cuda.is_available():
        model.cuda()
        logger.info('CUDA Enabled')
    else:
        logger.info('CUDA Disabled')

    return model, tokenizer, w2i, i2w
  
logger.info('Load model is on progress...')
models = Models()
logger.info('Load model is finished!')