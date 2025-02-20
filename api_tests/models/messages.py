import time
import uuid

from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    id: str = str(uuid.uuid4())
    ts: str = str(int(time.time() * 1000))
    text: str


class SendMessageResponse(BaseModel):
    id: str
    ts: int
    sessionId: str
    text: str
    sender: str
