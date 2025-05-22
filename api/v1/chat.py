# app/api/v1/chat.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

from auth.security import token_verification
from core.db import get_db
from models.models import Chat, Conversation
from schemas.chat_schema import CreateChatRequest, CreateConversationRequest, ChatResponse

router = APIRouter()

@router.post("/create-chat", response_model=ChatResponse)
async def create_chat(
    request: CreateChatRequest,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(token_verification)
):
    try:
        new_chat = Chat(
            id=uuid4(),
            title=request.title,
            user_id=user["user_id"]
        )
        db.add(new_chat)
        await db.commit()
        await db.refresh(new_chat)
        return new_chat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-conversation")
async def create_conversation(
    request: CreateConversationRequest,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(token_verification)
):
    try:
        new_convo = Conversation(
            id=uuid4(),
            chat_id=request.chat_id,
            branch_id=request.branch_id,
            parent_id=request.parent_id
        )
        db.add(new_convo)
        await db.commit()
        return {"success": True, "message": "Conversation entry added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
