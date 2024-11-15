# API module for all endpoints
from fastapi import APIRouter
from ..endpoints.emotion import Emotion
from ..endpoints.emotion_batch import EmotionBatch
from ..schema.doc import Doc
from ..schema.docs import Docs

router = APIRouter(
    prefix='/api',
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/emotion-detection')
async def emotion(doc: Doc):
    emotion = Emotion(doc.id, doc.text)
    result = emotion.get_inference()

    return result

@router.post('/emotion-detection-batch')
async def emotion_batch(docs: Docs):
    emotions = EmotionBatch(docs.data)
    result = emotions.get_inference()

    return result