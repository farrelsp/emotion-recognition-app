from pydantic import BaseModel

class Doc(BaseModel):
  id: str
  text: str