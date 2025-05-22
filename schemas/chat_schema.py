# app/schemas/chat_schema.py
from typing import List

from pydantic import BaseModel


class AddMessageRequest(BaseModel):
    chat_id: str
    branch_id: str
    question: str
    answer: str


class QAPair(BaseModel):
    question: str
    answer: str

class QAPairsResponse(BaseModel):
    chat_id: str
    branch_id: str
    qa_pairs: List[QAPair]

# app/schemas/chat_schema.py

from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class CreateChatRequest(BaseModel):
    title: str


class CreateConversationRequest(BaseModel):
    chat_id: UUID
    branch_id: str
    parent_id: Optional[str] = None


class ChatResponse(BaseModel):
    id: UUID
    user_id: str
    title: str
    created_at: datetime

    class Config:
        orm_mode = True
